import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { motion } from "framer-motion";
import { PathNode } from "./RoadmapNode";
import { useTranslation } from "@/hooks/useTranslation";
import type { RoadmapNodeData, NodeStatus } from "@/types";

interface RoadmapCanvasProps {
  roadmapData: RoadmapNodeData[];
  completedNodes: string[];
  color: string;
  onNodeClick: (nodeId: string) => void;
}

// ─── Mascot images cycle ─────────────────────────────────────

const MASCOT_IMAGES = [
  "/images/mascot-thinking.png",
  "/images/mascot-reading.png",
  "/images/mascot-happy.png",
  "/images/mascot-confused.png",
  "/images/mascot-study.png",
  "/images/mascot-sad.png",
];

// ─── Layout ────────────────────────────────────────────────────────────────

const SNAKE_X_FRACS_DESKTOP = [0.50, 0.75, 0.50, 0.25, 0.50];
const SNAKE_X_FRACS_MOBILE = [0.35, 0.65, 0.35, 0.65, 0.50];
const ROW_HEIGHT_DESKTOP = 140;
const ROW_HEIGHT_MOBILE = 110;
const V_PADDING = 80;
const CANVAS_W_DESKTOP = 460;

function bezierSegment(x1: number, y1: number, x2: number, y2: number): string {
  const cx = (x1 + x2) / 2;
  const cy = (y1 + y2) / 2;
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.sqrt(dx * dx + dy * dy);
  const nx = -dy / len;
  const ny = dx / len;
  const bow = Math.min(Math.abs(dx) * 0.4, 50);
  const cpx = cx + nx * bow;
  const cpy = cy + ny * bow;
  return `Q ${cpx} ${cpy} ${x2} ${y2}`;
}

function generateStars(count: number, canvasH: number) {
  const stars = [];
  for (let i = 0; i < count; i++) {
    stars.push({
      x: Math.random() * 100,
      y: Math.random() * canvasH,
      size: 1 + Math.random() * 2.5,
      delay: Math.random() * 4,
      duration: 2 + Math.random() * 3,
    });
  }
  return stars;
}

function useIsMobile() {
  const [mobile, setMobile] = useState(false);
  useEffect(() => {
    const check = () => setMobile(window.innerWidth < 768);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);
  return mobile;
}

// ─── Component ─────────────────────────────────────────────────────────────

export function RoadmapCanvas({
  roadmapData,
  completedNodes,
  color,
  onNodeClick,
}: RoadmapCanvasProps) {
  const { lang } = useTranslation();
  const scrollRef = useRef<HTMLDivElement>(null);
  const isMobile = useIsMobile();

  const canvasW = isMobile ? Math.min(window.innerWidth - 32, 360) : CANVAS_W_DESKTOP;
  const rowHeight = isMobile ? ROW_HEIGHT_MOBILE : ROW_HEIGHT_DESKTOP;
  const snakeXFracs = isMobile ? SNAKE_X_FRACS_MOBILE : SNAKE_X_FRACS_DESKTOP;

  const getStatus = useCallback(
    (nodeId: string, index: number): NodeStatus => {
      if (completedNodes.includes(nodeId)) return "completed";
      if (index === 0) return "available";
      return completedNodes.includes(roadmapData[index - 1].id) ? "available" : "locked";
    },
    [completedNodes, roadmapData]
  );

  const canvasHeight = useMemo(
    () => V_PADDING * 2 + (roadmapData.length - 1) * rowHeight + 120,
    [roadmapData.length, rowHeight]
  );

  const nodePositions = useMemo(
    () =>
      roadmapData.map((_, i) => ({
        x: snakeXFracs[i % snakeXFracs.length] * canvasW,
        y: V_PADDING + i * rowHeight,
      })),
    [roadmapData, canvasW, rowHeight, snakeXFracs]
  );

  const pathD = useMemo(() => {
    if (nodePositions.length === 0) return "";
    let d = `M ${nodePositions[0].x} ${nodePositions[0].y}`;
    for (let i = 1; i < nodePositions.length; i++) {
      const { x: x1, y: y1 } = nodePositions[i - 1];
      const { x: x2, y: y2 } = nodePositions[i];
      d += ` ${bezierSegment(x1, y1, x2, y2)}`;
    }
    return d;
  }, [nodePositions]);

  const sections = useMemo(() => {
    const result: Array<{
      sectionIndex: number;
      label: string;
      startNodeIdx: number;
      endNodeIdx: number;
    }> = [];
    let current = -1;
    roadmapData.forEach((node, i) => {
      if (node.sectionIndex !== current) {
        current = node.sectionIndex;
        result.push({
          sectionIndex: node.sectionIndex,
          label: node.section[lang],
          startNodeIdx: i,
          endNodeIdx: i,
        });
      } else {
        result[result.length - 1].endNodeIdx = i;
      }
    });
    return result;
  }, [roadmapData, lang]);

  const stars = useMemo(() => generateStars(isMobile ? 30 : 60, canvasHeight), [canvasHeight, isMobile]);

  // Auto-scroll to current node
  useEffect(() => {
    const firstAvailableIdx = roadmapData.findIndex(
      (n, i) => getStatus(n.id, i) === "available"
    );
    if (firstAvailableIdx === -1 || !scrollRef.current) return;

    const targetY = nodePositions[firstAvailableIdx]?.y ?? 0;
    const containerH = scrollRef.current.clientHeight;
    const scrollTop = targetY - containerH / 2 + 40;

    const timer = setTimeout(() => {
      scrollRef.current?.scrollTo({ top: Math.max(0, scrollTop), behavior: "smooth" });
    }, 300);
    return () => clearTimeout(timer);
  }, [roadmapData, nodePositions, getStatus]);

  const bgGradient = `linear-gradient(175deg, ${color}30 0%, ${color}14 30%, ${color}06 60%, #000000 100%)`;

  const roadW = isMobile ? 16 : 22;
  const roadGlowW = isMobile ? 24 : 32;

  return (
    <div
      ref={scrollRef}
      className="relative w-full overflow-y-auto overflow-x-hidden"
      style={{
        height: isMobile ? "calc(100dvh - 11rem)" : "calc(100vh - 8rem)",
        background: bgGradient,
        borderRadius: isMobile ? "1rem" : "1.25rem",
        scrollbarWidth: "thin",
        scrollbarColor: `${color}40 transparent`,
        WebkitOverflowScrolling: "touch",
      }}
    >
      {/* ── Starfield background ── */}
      <div className="absolute inset-0 pointer-events-none" style={{ height: canvasHeight }}>
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
            animate={{ opacity: [0.1, 0.6, 0.1] }}
            transition={{
              repeat: Infinity,
              duration: star.duration,
              delay: star.delay,
              ease: "easeInOut",
            }}
          />
        ))}
      </div>

      {/* ── Subtle pattern overlay ── */}
      <div
        className="pointer-events-none absolute inset-0"
        style={{
          backgroundImage: `radial-gradient(circle, ${color}12 1px, transparent 1px)`,
          backgroundSize: "32px 32px",
          height: canvasHeight,
        }}
      />

      {/* ── Mascots placed at each section midpoint, alternating sides ── */}
      {sections.map((sec, i) => {
        const startY = nodePositions[sec.startNodeIdx]?.y ?? 0;
        const endY = nodePositions[sec.endNodeIdx]?.y ?? 0;
        const midY = (startY + endY) / 2;
        const midNodeIdx = Math.floor((sec.startNodeIdx + sec.endNodeIdx) / 2);
        const midNodeX = nodePositions[midNodeIdx]?.x ?? canvasW / 2;

        // Place mascot on opposite side from the mid-section node
        const isNodeOnRight = midNodeX > canvasW / 2;
        const mascotSize = isMobile ? 60 : 90;
        const offsetX = isMobile ? 12 : 20;
        const mascotLeft = isNodeOnRight
          ? offsetX
          : canvasW - mascotSize - offsetX;

        return (
          <motion.img
            key={`mascot-sec-${i}`}
            src={MASCOT_IMAGES[i % MASCOT_IMAGES.length]}
            alt="Panda mascot"
            className="absolute pointer-events-none select-none"
            style={{
              left: mascotLeft,
              top: midY - mascotSize / 2,
              width: mascotSize,
              height: mascotSize,
              objectFit: "contain",
              zIndex: 3,
              filter: "drop-shadow(0 4px 12px rgba(0,0,0,0.4))",
              transform: isNodeOnRight ? undefined : "scaleX(-1)",
            }}
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{
              opacity: isMobile ? 0.7 : 0.85,
              scale: 1,
              y: [0, -6, 0],
            }}
            transition={{
              opacity: { delay: 0.3 + i * 0.15, duration: 0.4 },
              scale: { delay: 0.3 + i * 0.15, type: "spring", stiffness: 200 },
              y: { repeat: Infinity, duration: 3.5 + i * 0.4, ease: "easeInOut" },
            }}
          />
        );
      })}

      {/* ── Main canvas ── */}
      <div
        className="relative mx-auto"
        style={{
          width: canvasW,
          height: canvasHeight,
          minHeight: "100%",
          zIndex: 5,
        }}
      >
        {/* ── SVG winding path ── */}
        <svg
          className="absolute inset-0 pointer-events-none"
          width={canvasW}
          height={canvasHeight}
          style={{ overflow: "visible" }}
        >
          <defs>
            <filter id="road-glow" x="-30%" y="-30%" width="160%" height="160%">
              <feGaussianBlur stdDeviation="6" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="path-shadow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="3" stdDeviation="5" floodColor="rgba(0,0,0,0.4)" />
            </filter>
          </defs>

          {/* Road glow underneath */}
          <path
            d={pathD}
            fill="none"
            stroke={`${color}30`}
            strokeWidth={roadGlowW}
            strokeLinecap="round"
            strokeLinejoin="round"
            filter="url(#road-glow)"
          />

          {/* Base road */}
          <path
            d={pathD}
            fill="none"
            stroke="rgba(255,255,255,0.10)"
            strokeWidth={roadW}
            strokeLinecap="round"
            strokeLinejoin="round"
            filter="url(#path-shadow)"
          />

          {/* Road edge highlights */}
          <path
            d={pathD}
            fill="none"
            stroke="rgba(255,255,255,0.06)"
            strokeWidth={roadW + 6}
            strokeLinecap="round"
            strokeLinejoin="round"
          />

          {/* Center dashes */}
          <path
            d={pathD}
            fill="none"
            stroke="rgba(255,255,255,0.1)"
            strokeWidth={isMobile ? 2 : 3}
            strokeLinecap="round"
            strokeDasharray="10 16"
          />

          {/* Colored segments for completed/active */}
          {roadmapData.slice(1).map((node, i) => {
            const fromStatus = getStatus(roadmapData[i].id, i);
            const toStatus = getStatus(node.id, i + 1);
            const isSegCompleted = toStatus === "completed" || fromStatus === "completed";
            const isSegActive = toStatus === "available" && fromStatus !== "locked";

            if (!isSegCompleted && !isSegActive) return null;

            const { x: x1, y: y1 } = nodePositions[i];
            const { x: x2, y: y2 } = nodePositions[i + 1];
            const segD = `M ${x1} ${y1} ${bezierSegment(x1, y1, x2, y2)}`;
            const activeW = isMobile ? 12 : 16;
            const completedW = isMobile ? 10 : 14;

            return (
              <g key={node.id}>
                {isSegActive && (
                  <path
                    d={segD}
                    fill="none"
                    stroke={color}
                    strokeWidth={roadGlowW}
                    strokeLinecap="round"
                    opacity={0.15}
                    filter="url(#road-glow)"
                  />
                )}
                <path
                  d={segD}
                  fill="none"
                  stroke={isSegCompleted ? "#4ADE80" : color}
                  strokeWidth={isSegActive ? activeW : completedW}
                  strokeLinecap="round"
                  opacity={isSegActive ? 0.8 : 0.9}
                />
                <path
                  d={segD}
                  fill="none"
                  stroke="rgba(255,255,255,0.15)"
                  strokeWidth={isMobile ? 3 : 4}
                  strokeLinecap="round"
                />
              </g>
            );
          })}
        </svg>

        {/* ── Section header labels ── */}
        {sections.map((sec) => {
          const topY = nodePositions[sec.startNodeIdx]?.y ?? 0;
          const labelY = topY - (isMobile ? 44 : 52);
          if (labelY < 0) return null;

          const headerEmoji = "📖";

          return (
            <div
              key={`sec-label-${sec.sectionIndex}`}
              className="absolute left-0 right-0 flex items-center justify-center pointer-events-none"
              style={{ top: labelY, zIndex: 10 }}
            >
              <motion.div
                initial={{ opacity: 0, scale: 0.8, y: 10 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                transition={{ delay: sec.sectionIndex * 0.12, type: "spring", stiffness: 200 }}
                className="flex items-center gap-1.5 lg:gap-2 px-3 lg:px-5 py-1 lg:py-1.5 rounded-full text-[10px] lg:text-[12px] font-bold uppercase tracking-widest"
                style={{
                  background: `linear-gradient(135deg, ${color}30, ${color}15)`,
                  color: "rgba(255,255,255,0.9)",
                  border: `2px solid ${color}50`,
                  backdropFilter: "blur(12px)",
                  textShadow: "0 1px 4px rgba(0,0,0,0.6)",
                  boxShadow: `0 4px 16px ${color}25, 0 0 0 1px ${color}15`,
                  maxWidth: isMobile ? "85%" : undefined,
                }}
              >
                <span style={{ fontSize: isMobile ? 13 : 16 }}>{headerEmoji}</span>
                <span className="truncate">{sec.label}</span>
              </motion.div>
            </div>
          );
        })}

        {/* ── Nodes ── */}
        {roadmapData.map((node, i) => {
          const { x, y } = nodePositions[i];
          const status = getStatus(node.id, i);

          return (
            <motion.div
              key={node.id}
              className="absolute"
              style={{
                left: x,
                top: y,
                transform: "translate(-50%, -50%)",
                zIndex: 10,
              }}
              initial={{ opacity: 0, scale: 0.5, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              transition={{
                delay: i * 0.04,
                type: "spring",
                stiffness: 250,
                damping: 18,
              }}
            >
              <PathNode
                id={node.id}
                title={node.title[lang]}
                status={status}
                color={color}
                index={i}
                isCurrentNode={status === "available"}
                onClick={() => onNodeClick(node.id)}
                compact={isMobile}
              />
            </motion.div>
          );
        })}

        {/* ── Start flag with mascot at bottom ── */}
        {roadmapData.length > 0 && (
          <motion.div
            className="absolute flex flex-col items-center gap-1 pointer-events-none"
            style={{
              left: nodePositions[0].x,
              top: nodePositions[0].y + (isMobile ? 48 : 60),
              transform: "translateX(-50%)",
              zIndex: 6,
            }}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
          >
            <motion.img
              src="/images/mascot-happy.png"
              alt="Start!"
              className="object-contain drop-shadow-2xl"
              style={{ width: isMobile ? 80 : 112, height: isMobile ? 80 : 112 }}
              animate={{ y: [0, -8, 0] }}
              transition={{ repeat: Infinity, duration: 2.5, ease: "easeInOut" }}
            />
            <span
              className="text-[9px] lg:text-[10px] font-bold uppercase tracking-widest px-3 py-1 rounded-full"
              style={{
                color: "rgba(255,255,255,0.7)",
                background: `${color}20`,
                border: `1px solid ${color}30`,
                textShadow: "0 1px 3px rgba(0,0,0,0.5)",
              }}
            >
              START 🚩
            </span>
          </motion.div>
        )}

        {/* ── Trophy at the end ── */}
        {roadmapData.length > 0 && (() => {
          const lastPos = nodePositions[nodePositions.length - 1];
          const lastStatus = getStatus(
            roadmapData[roadmapData.length - 1].id,
            roadmapData.length - 1
          );

          return (
            <motion.div
              className="absolute flex flex-col items-center gap-2 pointer-events-none"
              style={{
                left: lastPos.x,
                top: lastPos.y - (isMobile ? 100 : 140),
                transform: "translateX(-50%)",
                zIndex: 6,
              }}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 1 }}
            >
              <motion.img
                src={lastStatus === "completed" ? "/images/mascot-study.png" : "/images/mascot-reading.png"}
                alt="Finish"
                className="object-contain drop-shadow-2xl"
                style={{ width: isMobile ? 64 : 96, height: isMobile ? 64 : 96 }}
                animate={lastStatus === "completed" ? {
                  scale: [1, 1.1, 1],
                  rotate: [0, 5, -5, 0],
                } : { y: [0, -6, 0] }}
                transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
              />
              <motion.span
                className="text-2xl lg:text-3xl drop-shadow-lg"
                animate={lastStatus === "completed" ? {
                  scale: [1, 1.15, 1],
                  rotate: [0, 5, -5, 0],
                } : {}}
                transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
              >
                🏆
              </motion.span>
              <span
                className="text-[10px] lg:text-[11px] font-bold uppercase tracking-wider px-3 py-1 rounded-full"
                style={{
                  color: lastStatus === "completed" ? "#FFD700" : "rgba(255,255,255,0.4)",
                  background: lastStatus === "completed" ? "rgba(255,215,0,0.15)" : "rgba(255,255,255,0.05)",
                  border: `1px solid ${lastStatus === "completed" ? "rgba(255,215,0,0.4)" : "rgba(255,255,255,0.1)"}`,
                  textShadow: "0 1px 4px rgba(0,0,0,0.6)",
                }}
              >
                {lastStatus === "completed" ? "COMPLETE! 🎉" : "FINISH"}
              </span>
            </motion.div>
          );
        })()}
      </div>
    </div>
  );
}
