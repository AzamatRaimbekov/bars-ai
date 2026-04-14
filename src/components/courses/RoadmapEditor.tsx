import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import { motion, AnimatePresence } from "framer-motion";
import { LayoutGrid, Save, Zap, BookOpen } from "lucide-react";
import { Button } from "@/components/ui/Button";
import type { CourseSection } from "@/services/courseApi";

// ─── Public types ───────────────────────────────────────────────────────────

export interface NodePosition {
  id: string;
  x: number;
  y: number;
}

export interface RoadmapEdge {
  id: string;
  source: string;
  target: string;
}

interface RoadmapEditorProps {
  sections: CourseSection[];
  initialPositions?: NodePosition[];
  initialEdges?: RoadmapEdge[];
  onSave?: (positions: NodePosition[], edges: RoadmapEdge[]) => void;
}

// ─── Internal flat node ──────────────────────────────────────────────────────

interface FlatNode {
  id: string;
  lessonTitle: string;
  sectionTitle: string;
  sectionColor: string;
  sectionIndex: number;
  globalIndex: number;
  xp: number;
}

// ─── Constants ───────────────────────────────────────────────────────────────

const SECTION_COLORS = [
  "#F97316",
  "#FFB800",
  "#4ADE80",
  "#22C55E",
  "#FF6B6B",
  "#FB923C",
  "#34D399",
  "#EC4899",
];

// Snake layout fractions — the path weaves left-center-right like RoadmapCanvas
const SNAKE_X_FRACS = [0.50, 0.75, 0.50, 0.25, 0.50];
const CANVAS_W = 500;
const ROW_HEIGHT = 148;
const V_PADDING = 90;

// Node circle sizes
const NODE_SIZE = 72;

// ─── Helpers ─────────────────────────────────────────────────────────────────

function snakeX(index: number): number {
  return SNAKE_X_FRACS[index % SNAKE_X_FRACS.length] * CANVAS_W;
}

function computeSnakePositions(nodes: FlatNode[]): NodePosition[] {
  return nodes.map((n, i) => ({
    id: n.id,
    x: snakeX(i),
    y: V_PADDING + i * ROW_HEIGHT,
  }));
}

function canvasHeight(nodeCount: number): number {
  if (nodeCount === 0) return 400;
  return V_PADDING * 2 + (nodeCount - 1) * ROW_HEIGHT + 160;
}

/** Quadratic bezier segment string (same algorithm as RoadmapCanvas) */
function bezierSegment(
  x1: number,
  y1: number,
  x2: number,
  y2: number
): string {
  const cx = (x1 + x2) / 2;
  const cy = (y1 + y2) / 2;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.sqrt(dx * dx + dy * dy);
  if (len === 0) return `Q ${cx} ${cy} ${x2} ${y2}`;
  const nx = -dy / len;
  const ny = dx / len;
  const bow = Math.min(Math.abs(dx) * 0.4, 50);
  return `Q ${cx + nx * bow} ${cy + ny * bow} ${x2} ${y2}`;
}

function buildPathD(positions: Map<string, { x: number; y: number }>, orderedIds: string[]): string {
  if (orderedIds.length === 0) return "";
  const first = positions.get(orderedIds[0]);
  if (!first) return "";
  let d = `M ${first.x} ${first.y}`;
  for (let i = 1; i < orderedIds.length; i++) {
    const prev = positions.get(orderedIds[i - 1]);
    const cur = positions.get(orderedIds[i]);
    if (!prev || !cur) continue;
    d += ` ${bezierSegment(prev.x, prev.y, cur.x, cur.y)}`;
  }
  return d;
}

function generateStars(count: number, height: number) {
  const out = [];
  for (let i = 0; i < count; i++) {
    out.push({
      x: Math.random() * 100,
      y: Math.random() * height,
      size: 1 + Math.random() * 2.5,
      delay: Math.random() * 4,
      duration: 2 + Math.random() * 3,
    });
  }
  return out;
}

// ─── Editor node circle ───────────────────────────────────────────────────────

interface EditorNodeCircleProps {
  node: FlatNode;
  x: number;
  y: number;
  isDragging: boolean;
  isSelected: boolean;
  onMouseDown: (e: React.MouseEvent) => void;
}

function EditorNodeCircle({
  node,
  x,
  y,
  isDragging,
  isSelected,
  onMouseDown,
}: EditorNodeCircleProps) {
  const color = node.sectionColor;
  const size = NODE_SIZE;

  return (
    <motion.div
      className="absolute select-none"
      style={{
        left: x,
        top: y,
        transform: "translate(-50%, -50%)",
        zIndex: isDragging ? 50 : isSelected ? 30 : 10,
        cursor: isDragging ? "grabbing" : "grab",
      }}
      initial={{ opacity: 0, scale: 0.4, y: 16 }}
      animate={{ opacity: 1, scale: 1, y: 0 }}
      transition={{
        delay: node.globalIndex * 0.035,
        type: "spring",
        stiffness: 260,
        damping: 20,
      }}
      onMouseDown={onMouseDown}
    >
      <div className="flex flex-col items-center gap-2">
        {/* ── Outer glow rings (selected state) ── */}
        {isSelected && (
          <>
            <motion.span
              className="absolute rounded-full pointer-events-none"
              style={{
                width: size,
                height: size,
                top: 0,
                left: "50%",
                transform: "translate(-50%, 0)",
                border: `3px solid ${color}`,
              }}
              animate={{ scale: [1, 1.55, 1], opacity: [0.6, 0, 0.6] }}
              transition={{ repeat: Infinity, duration: 1.8, ease: "easeOut" }}
            />
            <motion.span
              className="absolute rounded-full pointer-events-none"
              style={{
                width: size,
                height: size,
                top: 0,
                left: "50%",
                transform: "translate(-50%, 0)",
                border: `2px solid ${color}`,
              }}
              animate={{ scale: [1, 1.9, 1], opacity: [0.3, 0, 0.3] }}
              transition={{ repeat: Infinity, duration: 1.8, delay: 0.3, ease: "easeOut" }}
            />
          </>
        )}

        {/* ── Main circle ── */}
        <motion.div
          className="relative flex items-center justify-center rounded-full border-4 flex-shrink-0"
          style={{
            width: size,
            height: size,
            background: `linear-gradient(145deg, ${color}, ${color}bb)`,
            borderColor: isSelected ? color : "rgba(255,255,255,0.25)",
            boxShadow: isDragging
              ? `0 0 40px ${color}90, 0 0 80px ${color}40, 0 16px 40px rgba(0,0,0,0.6), inset 0 2px 4px rgba(255,255,255,0.2)`
              : isSelected
              ? `0 0 32px ${color}80, 0 0 64px ${color}35, 0 8px 24px rgba(0,0,0,0.45), inset 0 2px 4px rgba(255,255,255,0.2)`
              : `0 0 20px ${color}50, 0 0 40px ${color}20, 0 6px 18px rgba(0,0,0,0.4), inset 0 2px 4px rgba(255,255,255,0.15)`,
          }}
          animate={
            isSelected
              ? {
                  boxShadow: [
                    `0 0 32px ${color}80, 0 0 64px ${color}35, 0 8px 24px rgba(0,0,0,0.45), inset 0 2px 4px rgba(255,255,255,0.2)`,
                    `0 0 44px ${color}a0, 0 0 88px ${color}50, 0 8px 24px rgba(0,0,0,0.45), inset 0 2px 4px rgba(255,255,255,0.2)`,
                    `0 0 32px ${color}80, 0 0 64px ${color}35, 0 8px 24px rgba(0,0,0,0.45), inset 0 2px 4px rgba(255,255,255,0.2)`,
                  ],
                }
              : {}
          }
          transition={{ repeat: Infinity, duration: 2.5, ease: "easeInOut" }}
        >
          {/* Glass highlight */}
          <div
            className="absolute rounded-full pointer-events-none"
            style={{
              top: 5,
              left: "18%",
              width: "64%",
              height: "36%",
              background:
                "linear-gradient(180deg, rgba(255,255,255,0.32) 0%, rgba(255,255,255,0) 100%)",
              borderRadius: "50%",
            }}
          />

          {/* Inner ring */}
          <div
            className="absolute inset-2 rounded-full pointer-events-none"
            style={{ border: "2px solid rgba(255,255,255,0.15)" }}
          />

          {/* Icon */}
          <motion.div
            animate={{ rotate: isSelected ? [0, 8, -8, 0] : 0 }}
            transition={{ repeat: isSelected ? Infinity : 0, duration: 3, ease: "easeInOut" }}
          >
            <BookOpen
              size={size * 0.36}
              strokeWidth={1.8}
              fill="rgba(255,255,255,0.15)"
              className="text-white relative z-10 drop-shadow-lg"
            />
          </motion.div>

          {/* Step badge */}
          <span
            className="absolute -bottom-1.5 -right-1.5 rounded-full flex items-center justify-center font-bold shadow-lg"
            style={{
              minWidth: 22,
              height: 22,
              fontSize: 9,
              backgroundColor: "#000000",
              color: "white",
              border: `2px solid ${color}`,
              boxShadow: `0 0 8px ${color}50`,
            }}
          >
            {node.globalIndex + 1}
          </span>
        </motion.div>

        {/* ── Labels ── */}
        <div className="flex flex-col items-center gap-0.5 pointer-events-none">
          {/* Section badge */}
          <span
            className="px-2 py-0.5 rounded-full text-[8px] font-bold uppercase tracking-wider"
            style={{
              backgroundColor: `${color}25`,
              color,
              border: `1px solid ${color}40`,
            }}
          >
            {node.sectionTitle.length > 16
              ? node.sectionTitle.slice(0, 14) + "…"
              : node.sectionTitle}
          </span>

          {/* Lesson title */}
          <span
            className="text-center font-semibold leading-tight"
            style={{
              maxWidth: 110,
              fontSize: 11,
              color: "rgba(255,255,255,0.92)",
              textShadow: "0 2px 6px rgba(0,0,0,0.8)",
            }}
          >
            {node.lessonTitle}
          </span>

          {/* XP pill */}
          {node.xp > 0 && (
            <span
              className="flex items-center gap-0.5 px-1.5 py-0.5 rounded-full"
              style={{
                fontSize: 9,
                color: "#FCD34D",
                backgroundColor: "rgba(252,211,77,0.12)",
                border: "1px solid rgba(252,211,77,0.25)",
              }}
            >
              <Zap size={8} strokeWidth={2.5} className="text-yellow-400" />
              +{node.xp} XP
            </span>
          )}
        </div>
      </div>
    </motion.div>
  );
}

// ─── Main Component ───────────────────────────────────────────────────────────

export function RoadmapEditor({
  sections,
  initialPositions = [],
  initialEdges = [],
  onSave,
}: RoadmapEditorProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [saving, setSaving] = useState(false);
  const [selectedId, setSelectedId] = useState<string | null>(null);

  // ── Build a flat ordered list of nodes from sections ──────────────────────
  const flatNodes = useMemo<FlatNode[]>(() => {
    const result: FlatNode[] = [];
    sections.forEach((section, sectionIdx) => {
      const color = SECTION_COLORS[sectionIdx % SECTION_COLORS.length];
      const sorted = [...section.lessons].sort((a, b) => a.position - b.position);
      sorted.forEach((lesson) => {
        result.push({
          id: lesson.id,
          lessonTitle: lesson.title,
          sectionTitle: section.title,
          sectionColor: color,
          sectionIndex: sectionIdx,
          globalIndex: result.length,
          xp: lesson.xp_reward,
        });
      });
    });
    return result;
  }, [sections]);

  const orderedIds = useMemo(() => flatNodes.map((n) => n.id), [flatNodes]);

  // ── Positions map (id → {x, y}) ───────────────────────────────────────────
  const [positions, setPositions] = useState<Map<string, { x: number; y: number }>>(() => {
    const posMap = new Map(initialPositions.map((p) => [p.id, { x: p.x, y: p.y }]));
    const snakeDefaults = computeSnakePositions(
      flatNodes
    );
    const map = new Map<string, { x: number; y: number }>();
    snakeDefaults.forEach((p) => {
      map.set(p.id, posMap.get(p.id) ?? { x: p.x, y: p.y });
    });
    return map;
  });

  // Sync when flatNodes changes (new sections/lessons added)
  useEffect(() => {
    setPositions((prev) => {
      const snakeDefaults = computeSnakePositions(flatNodes);
      const next = new Map(prev);
      snakeDefaults.forEach((p) => {
        if (!next.has(p.id)) {
          next.set(p.id, { x: p.x, y: p.y });
        }
      });
      // Remove stale ids
      const validIds = new Set(flatNodes.map((n) => n.id));
      for (const key of next.keys()) {
        if (!validIds.has(key)) next.delete(key);
      }
      return next;
    });
  }, [flatNodes]);

  // ── Edges ─────────────────────────────────────────────────────────────────
  // We keep user-supplied edges, but always draw a default sequential chain
  // when no edges are provided.
  const edges = useMemo<RoadmapEdge[]>(() => {
    if (initialEdges.length > 0) return initialEdges;
    return orderedIds.slice(1).map((id, i) => ({
      id: `auto-${orderedIds[i]}-${id}`,
      source: orderedIds[i],
      target: id,
    }));
  }, [initialEdges, orderedIds]);

  // ── Canvas dimensions ─────────────────────────────────────────────────────
  const cHeight = useMemo(() => canvasHeight(flatNodes.length), [flatNodes.length]);

  // ── Starfield ─────────────────────────────────────────────────────────────
  const stars = useMemo(() => generateStars(55, cHeight), [cHeight]);

  // ── Section header positions ───────────────────────────────────────────────
  const sectionHeaders = useMemo(() => {
    const headers: Array<{
      sectionIndex: number;
      label: string;
      color: string;
      y: number;
    }> = [];
    let prevSection = -1;
    flatNodes.forEach((node, i) => {
      if (node.sectionIndex !== prevSection) {
        prevSection = node.sectionIndex;
        const pos = positions.get(node.id);
        const y = pos ? pos.y - 52 : V_PADDING + i * ROW_HEIGHT - 52;
        if (y >= 0) {
          headers.push({
            sectionIndex: node.sectionIndex,
            label: node.sectionTitle,
            color: node.sectionColor,
            y,
          });
        }
      }
    });
    return headers;
  }, [flatNodes, positions]);

  // ── SVG path ─────────────────────────────────────────────────────────────
  const pathD = useMemo(
    () => buildPathD(positions, orderedIds),
    [positions, orderedIds]
  );

  // Individual segment paths (for per-edge coloring based on sections)
  const segmentPaths = useMemo(() => {
    return edges.map((edge) => {
      const from = positions.get(edge.source);
      const to = positions.get(edge.target);
      if (!from || !to) return null;
      const fromNode = flatNodes.find((n) => n.id === edge.source);
      const color = fromNode?.sectionColor ?? "#F97316";
      const d = `M ${from.x} ${from.y} ${bezierSegment(from.x, from.y, to.x, to.y)}`;
      return { id: edge.id, d, color };
    });
  }, [edges, positions, flatNodes]);

  // ── Dragging ──────────────────────────────────────────────────────────────
  const dragState = useRef<{
    id: string;
    startMouseX: number;
    startMouseY: number;
    startNodeX: number;
    startNodeY: number;
  } | null>(null);

  const [draggingId, setDraggingId] = useState<string | null>(null);

  const handleNodeMouseDown = useCallback(
    (id: string, e: React.MouseEvent) => {
      e.preventDefault();
      e.stopPropagation();
      const pos = positions.get(id);
      if (!pos) return;
      dragState.current = {
        id,
        startMouseX: e.clientX,
        startMouseY: e.clientY,
        startNodeX: pos.x,
        startNodeY: pos.y,
      };
      setDraggingId(id);
      setSelectedId(id);
    },
    [positions]
  );

  useEffect(() => {
    const onMouseMove = (e: MouseEvent) => {
      const ds = dragState.current;
      if (!ds) return;
      const dx = e.clientX - ds.startMouseX;
      const dy = e.clientY - ds.startMouseY;
      setPositions((prev) => {
        const next = new Map(prev);
        next.set(ds.id, {
          x: Math.max(NODE_SIZE / 2, Math.min(CANVAS_W - NODE_SIZE / 2, ds.startNodeX + dx)),
          y: Math.max(NODE_SIZE / 2, ds.startNodeY + dy),
        });
        return next;
      });
    };

    const onMouseUp = () => {
      dragState.current = null;
      setDraggingId(null);
    };

    window.addEventListener("mousemove", onMouseMove);
    window.addEventListener("mouseup", onMouseUp);
    return () => {
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("mouseup", onMouseUp);
    };
  }, []);

  // Clear selection when clicking canvas background
  const handleCanvasClick = useCallback(() => {
    setSelectedId(null);
  }, []);

  // ── Auto-layout ───────────────────────────────────────────────────────────
  const handleAutoLayout = useCallback(() => {
    const snake = computeSnakePositions(flatNodes);
    // Animate by updating positions — framer-motion on the node handles the
    // visual spring; we just flip the data.
    setPositions(() => {
      const next = new Map<string, { x: number; y: number }>();
      snake.forEach((p) => next.set(p.id, { x: p.x, y: p.y }));
      return next;
    });
    setSelectedId(null);
  }, [flatNodes]);

  // ── Save ──────────────────────────────────────────────────────────────────
  const handleSave = useCallback(async () => {
    setSaving(true);
    try {
      const posArr: NodePosition[] = [];
      positions.forEach((pos, id) => posArr.push({ id, x: pos.x, y: pos.y }));
      onSave?.(posArr, edges);
    } finally {
      setSaving(false);
    }
  }, [positions, edges, onSave]);

  // ── Dynamic canvas height (account for dragged nodes going below) ─────────
  const dynamicHeight = useMemo(() => {
    let maxY = cHeight;
    positions.forEach((p) => {
      maxY = Math.max(maxY, p.y + NODE_SIZE + 80);
    });
    return maxY;
  }, [positions, cHeight]);

  // ── Render ────────────────────────────────────────────────────────────────
  const bgGradient =
    "linear-gradient(175deg, #F9731610 0%, #F9731608 30%, #00000005 60%, #000000 100%)";

  return (
    <div className="flex flex-col h-full">
      {/* ── Toolbar ── */}
      <div className="flex items-center justify-between px-4 py-2.5 border-b border-white/6 bg-[#0A0A0A] flex-shrink-0 gap-3">
        <div className="flex items-center gap-2 min-w-0">
          <Button variant="secondary" size="sm" onClick={handleAutoLayout}>
            <LayoutGrid size={14} />
            Авто-раскладка
          </Button>
          <p className="text-[11px] text-white/40 hidden sm:block truncate">
            Перетаскивайте узлы. «Авто-раскладка» вернёт змейку.
          </p>
        </div>
        <Button size="sm" onClick={handleSave} disabled={saving}>
          <Save size={14} />
          {saving ? "Сохранение..." : "Сохранить"}
        </Button>
      </div>

      {/* ── Scrollable canvas ── */}
      <div
        ref={containerRef}
        className="flex-1 min-h-0 relative overflow-y-auto overflow-x-hidden"
        style={{
          background: bgGradient,
          scrollbarWidth: "thin",
          scrollbarColor: "#F9731640 transparent",
          WebkitOverflowScrolling: "touch",
        }}
        onClick={handleCanvasClick}
      >
        {/* Starfield */}
        <div
          className="absolute inset-0 pointer-events-none"
          style={{ height: dynamicHeight }}
        >
          {stars.map((star, i) => (
            <motion.div
              key={i}
              className="absolute rounded-full"
              style={{
                left: `${star.x}%`,
                top: star.y,
                width: star.size,
                height: star.size,
                backgroundColor: "white",
              }}
              animate={{ opacity: [0.08, 0.55, 0.08] }}
              transition={{
                repeat: Infinity,
                duration: star.duration,
                delay: star.delay,
                ease: "easeInOut",
              }}
            />
          ))}
        </div>

        {/* Dot pattern overlay */}
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            backgroundImage:
              "radial-gradient(circle, rgba(249,115,22,0.08) 1px, transparent 1px)",
            backgroundSize: "32px 32px",
            height: dynamicHeight,
          }}
        />

        {/* Main canvas column */}
        <div
          className="relative mx-auto"
          style={{
            width: CANVAS_W,
            height: dynamicHeight,
            minHeight: "100%",
            zIndex: 5,
          }}
        >
          {/* ── SVG paths ── */}
          <svg
            className="absolute inset-0 pointer-events-none"
            width={CANVAS_W}
            height={dynamicHeight}
            style={{ overflow: "visible" }}
          >
            <defs>
              <filter id="re-road-glow" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="6" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
              <filter id="re-path-shadow" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow
                  dx="0"
                  dy="3"
                  stdDeviation="5"
                  floodColor="rgba(0,0,0,0.4)"
                />
              </filter>
            </defs>

            {/* Road glow */}
            <path
              d={pathD}
              fill="none"
              stroke="rgba(249,115,22,0.15)"
              strokeWidth={32}
              strokeLinecap="round"
              strokeLinejoin="round"
              filter="url(#re-road-glow)"
            />

            {/* Base road (frosted glass) */}
            <path
              d={pathD}
              fill="none"
              stroke="rgba(255,255,255,0.18)"
              strokeWidth={22}
              strokeLinecap="round"
              strokeLinejoin="round"
              filter="url(#re-path-shadow)"
            />

            {/* Edge highlight */}
            <path
              d={pathD}
              fill="none"
              stroke="rgba(255,255,255,0.05)"
              strokeWidth={28}
              strokeLinecap="round"
              strokeLinejoin="round"
            />

            {/* Center dashes */}
            <path
              d={pathD}
              fill="none"
              stroke="rgba(255,255,255,0.09)"
              strokeWidth={3}
              strokeLinecap="round"
              strokeDasharray="10 16"
            />

            {/* Colored per-segment paths */}
            {segmentPaths.map((seg) => {
              if (!seg) return null;
              return (
                <g key={seg.id}>
                  <path
                    d={seg.d}
                    fill="none"
                    stroke={seg.color}
                    strokeWidth={32}
                    strokeLinecap="round"
                    opacity={0.07}
                    filter="url(#re-road-glow)"
                  />
                  <path
                    d={seg.d}
                    fill="none"
                    stroke={seg.color}
                    strokeWidth={14}
                    strokeLinecap="round"
                    opacity={0.55}
                  />
                  <path
                    d={seg.d}
                    fill="none"
                    stroke="rgba(255,255,255,0.12)"
                    strokeWidth={4}
                    strokeLinecap="round"
                  />
                </g>
              );
            })}
          </svg>

          {/* ── Section header labels ── */}
          <AnimatePresence>
            {sectionHeaders.map((hdr) => (
              <div
                key={`sec-hdr-${hdr.sectionIndex}`}
                className="absolute left-0 right-0 flex items-center justify-center pointer-events-none"
                style={{ top: hdr.y, zIndex: 8 }}
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.8, y: 8 }}
                  animate={{ opacity: 1, scale: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.8 }}
                  transition={{
                    delay: hdr.sectionIndex * 0.08,
                    type: "spring",
                    stiffness: 220,
                  }}
                  className="flex items-center gap-2 px-4 py-1.5 rounded-full text-[11px] font-bold uppercase tracking-widest"
                  style={{
                    background: `linear-gradient(135deg, ${hdr.color}30, ${hdr.color}18)`,
                    color: "rgba(255,255,255,0.92)",
                    border: `2px solid ${hdr.color}55`,
                    backdropFilter: "blur(12px)",
                    textShadow: "0 1px 4px rgba(0,0,0,0.7)",
                    boxShadow: `0 4px 16px ${hdr.color}25, 0 0 0 1px ${hdr.color}15`,
                  }}
                >
                  <span style={{ fontSize: 15 }}>📖</span>
                  <span>{hdr.label}</span>
                </motion.div>
              </div>
            ))}
          </AnimatePresence>

          {/* ── Nodes ── */}
          {flatNodes.map((node) => {
            const pos = positions.get(node.id);
            if (!pos) return null;
            return (
              <EditorNodeCircle
                key={node.id}
                node={node}
                x={pos.x}
                y={pos.y}
                isDragging={draggingId === node.id}
                isSelected={selectedId === node.id}
                onMouseDown={(e) => handleNodeMouseDown(node.id, e)}
              />
            );
          })}

          {/* ── START marker ── */}
          {flatNodes.length > 0 && (() => {
            const firstPos = positions.get(flatNodes[0].id);
            if (!firstPos) return null;
            return (
              <motion.div
                className="absolute flex flex-col items-center gap-1 pointer-events-none"
                style={{
                  left: firstPos.x,
                  top: firstPos.y + NODE_SIZE / 2 + 16,
                  transform: "translateX(-50%)",
                  zIndex: 6,
                }}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.5 }}
              >
                <span
                  className="text-[9px] font-bold uppercase tracking-widest px-2.5 py-1 rounded-full"
                  style={{
                    color: "rgba(255,255,255,0.6)",
                    background: "rgba(108,99,255,0.18)",
                    border: "1px solid rgba(108,99,255,0.35)",
                    textShadow: "0 1px 3px rgba(0,0,0,0.5)",
                  }}
                >
                  НАЧАЛО 🚩
                </span>
              </motion.div>
            );
          })()}

          {/* ── FINISH marker ── */}
          {flatNodes.length > 0 && (() => {
            const lastNode = flatNodes[flatNodes.length - 1];
            const lastPos = positions.get(lastNode.id);
            if (!lastPos) return null;
            return (
              <motion.div
                className="absolute flex flex-col items-center gap-1 pointer-events-none"
                style={{
                  left: lastPos.x,
                  top: lastPos.y - NODE_SIZE / 2 - 44,
                  transform: "translateX(-50%)",
                  zIndex: 6,
                }}
                initial={{ opacity: 0, y: 12 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.8 }}
              >
                <motion.span
                  className="text-2xl drop-shadow-lg"
                  animate={{ scale: [1, 1.12, 1] }}
                  transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
                >
                  🏆
                </motion.span>
                <span
                  className="text-[9px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full"
                  style={{
                    color: "rgba(255,215,0,0.75)",
                    background: "rgba(255,215,0,0.1)",
                    border: "1px solid rgba(255,215,0,0.25)",
                  }}
                >
                  ФИНИШ
                </span>
              </motion.div>
            );
          })()}
        </div>
      </div>

      {/* ── Legend ── */}
      <div className="flex items-center gap-3 px-4 py-2.5 border-t border-white/10 bg-white/[0.03] flex-shrink-0 overflow-x-auto">
        <span className="text-[10px] text-white/40 uppercase tracking-wider flex-shrink-0">
          Секции:
        </span>
        {sections.map((section, i) => (
          <motion.div
            key={section.id}
            initial={{ opacity: 0, scale: 0.88 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: i * 0.04 }}
            className="flex items-center gap-1.5 flex-shrink-0"
          >
            <div
              className="w-2.5 h-2.5 rounded-full flex-shrink-0"
              style={{
                backgroundColor: SECTION_COLORS[i % SECTION_COLORS.length],
                boxShadow: `0 0 6px ${SECTION_COLORS[i % SECTION_COLORS.length]}80`,
              }}
            />
            <span className="text-[10px] text-white/50 whitespace-nowrap">{section.title}</span>
          </motion.div>
        ))}
        <span className="ml-auto text-[10px] text-white/25 flex-shrink-0 hidden sm:block">
          {flatNodes.length} уроков
        </span>
      </div>
    </div>
  );
}
