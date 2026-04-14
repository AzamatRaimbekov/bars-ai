import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowLeft, X, Clock, BookOpen, ArrowRight, Lock, Zap } from "lucide-react";
import { PathNode } from "@/components/roadmap/RoadmapNode";
import { Button } from "@/components/ui/Button";
import { courseApi, type CourseDetail, type CourseProgress, type CourseLesson } from "@/services/courseApi";
import type { NodeStatus } from "@/types";

// ─── Constants ────────────────────────────────────────────────────────────────

const SNAKE_X_FRACS_DESKTOP = [0.50, 0.80, 0.50, 0.20, 0.50];
const SNAKE_X_FRACS_MOBILE  = [0.30, 0.70, 0.30, 0.70, 0.50];
const ROW_HEIGHT_DESKTOP    = 180;
const ROW_HEIGHT_MOBILE     = 140;
const V_PADDING             = 110;
const CANVAS_W_DESKTOP      = 540;

// Colors assigned per-section, cycling through this palette
const SECTION_COLORS = [
  "#F97316",
  "#EC4899",
  "#4ADE80",
  "#FB923C",
  "#3B82F6",
  "#F59E0B",
  "#EF4444",
  "#14B8A6",
];

// Space emojis for section decorations
const SPACE_ICONS = ["🪐", "🌙", "☄️", "🛸", "🌟", "💫", "🔭", "🚀"];

// ─── Types ────────────────────────────────────────────────────────────────────

interface FlatLesson {
  /** lesson ID from the API */
  lessonId: string;
  title: string;
  sectionTitle: string;
  /** 0-based index of the parent section in the sorted sections array */
  sectionIndex: number;
  /** colour assigned to this section */
  color: string;
}

// ─── Utility helpers ──────────────────────────────────────────────────────────

function bezierSegment(x1: number, y1: number, x2: number, y2: number): string {
  const cx  = (x1 + x2) / 2;
  const cy  = (y1 + y2) / 2;
  const dx  = x2 - x1;
  const dy  = y2 - y1;
  const len = Math.sqrt(dx * dx + dy * dy);
  const nx  = -dy / len;
  const ny  =  dx / len;
  const bow = Math.min(Math.abs(dx) * 0.4, 50);
  const cpx = cx + nx * bow;
  const cpy = cy + ny * bow;
  return `Q ${cpx} ${cpy} ${x2} ${y2}`;
}

function generateStars(count: number, canvasH: number) {
  const stars = [];
  for (let i = 0; i < count; i++) {
    stars.push({
      x:        Math.random() * 100,
      y:        Math.random() * canvasH,
      size:     0.5 + Math.random() * 2.5,
      delay:    Math.random() * 6,
      duration: 1.5 + Math.random() * 4,
      color:    Math.random() > 0.85 ? `hsl(${Math.random() * 60 + 200}, 80%, 80%)` : "white",
    });
  }
  return stars;
}

function generateNebulae(count: number, canvasH: number) {
  const nebulae = [];
  const colors = ["#F97316", "#EC4899", "#3B82F6", "#8B5CF6", "#4ADE80"];
  for (let i = 0; i < count; i++) {
    nebulae.push({
      x:      Math.random() * 100,
      y:      (i / count) * canvasH + Math.random() * 200,
      w:      200 + Math.random() * 300,
      h:      200 + Math.random() * 300,
      color:  colors[i % colors.length],
      rotate: Math.random() * 360,
    });
  }
  return nebulae;
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

// ─── Main page ────────────────────────────────────────────────────────────────

export default function CourseRoadmap() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const isMobile = useIsMobile();

  // ── Data state ──────────────────────────────────────────────────────────────
  const [course,   setCourse]   = useState<CourseDetail | null>(null);
  const [progress, setProgress] = useState<CourseProgress | null>(null);
  const [loading,  setLoading]  = useState(true);

  // ── Scroll ref for auto-scroll to current node ──────────────────────────────
  const scrollRef = useRef<HTMLDivElement>(null);

  // ── Selected node for drawer ──────────────────────────────────────────────
  const [selectedLesson, setSelectedLesson] = useState<{
    lesson: FlatLesson;
    index: number;
    status: NodeStatus;
  } | null>(null);

  // ── Fetch ───────────────────────────────────────────────────────────────────
  useEffect(() => {
    if (!id) return;
    setLoading(true);
    Promise.all([
      courseApi.get(id),
      courseApi.getProgress(id).catch(() => null),
    ])
      .then(([courseData, progressData]) => {
        setCourse(courseData);
        setProgress(progressData);
      })
      .catch(() => navigate(`/courses/${id}`))
      .finally(() => setLoading(false));
  }, [id, navigate]);

  // ── Derive: flatten sections → lessons into linear list ─────────────────────
  const flatLessons: FlatLesson[] = useMemo(() => {
    if (!course) return [];
    const sortedSections = [...course.sections].sort(
      (a, b) => a.position - b.position
    );
    const result: FlatLesson[] = [];
    sortedSections.forEach((section, sIdx) => {
      const color = SECTION_COLORS[sIdx % SECTION_COLORS.length];
      [...section.lessons]
        .sort((a, b) => a.position - b.position)
        .forEach((lesson) => {
          result.push({
            lessonId:     lesson.id,
            title:        lesson.title,
            sectionTitle: section.title,
            sectionIndex: sIdx,
            color,
          });
        });
    });
    return result;
  }, [course]);

  // ── Derive completed set ─────────────────────────────────────────────────────
  const completedSet = useMemo(
    () => new Set(progress?.completed_lesson_ids ?? []),
    [progress]
  );

  // ── Progress percentage ──────────────────────────────────────────────────────
  const progressPercent =
    progress && progress.total_lessons > 0
      ? Math.round((progress.completed_count / progress.total_lessons) * 100)
      : 0;

  // ── Layout ───────────────────────────────────────────────────────────────────
  const canvasW     = isMobile ? Math.min(window.innerWidth - 32, 360) : CANVAS_W_DESKTOP;
  const rowHeight   = isMobile ? ROW_HEIGHT_MOBILE : ROW_HEIGHT_DESKTOP;
  const snakeXFracs = isMobile ? SNAKE_X_FRACS_MOBILE : SNAKE_X_FRACS_DESKTOP;

  const canvasHeight = useMemo(
    () => V_PADDING * 2 + (flatLessons.length - 1) * rowHeight + 220,
    [flatLessons.length, rowHeight]
  );

  const nodePositions = useMemo(
    () =>
      flatLessons.map((_, i) => ({
        x: snakeXFracs[i % snakeXFracs.length] * canvasW,
        y: V_PADDING + i * rowHeight,
      })),
    [flatLessons, canvasW, rowHeight, snakeXFracs]
  );

  // ── Node status ──────────────────────────────────────────────────────────────
  const getStatus = useCallback(
    (lessonId: string, index: number): NodeStatus => {
      if (completedSet.has(lessonId)) return "completed";
      if (index === 0) return "available";
      return completedSet.has(flatLessons[index - 1].lessonId) ? "available" : "locked";
    },
    [completedSet, flatLessons]
  );

  // ── SVG path ─────────────────────────────────────────────────────────────────
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

  // ── Section boundary groups (for labels and mascots) ─────────────────────────
  const sections = useMemo(() => {
    const result: Array<{
      sectionIndex: number;
      label: string;
      color: string;
      startNodeIdx: number;
      endNodeIdx: number;
    }> = [];
    let currentSectionIdx = -1;
    flatLessons.forEach((lesson, i) => {
      if (lesson.sectionIndex !== currentSectionIdx) {
        currentSectionIdx = lesson.sectionIndex;
        result.push({
          sectionIndex:  lesson.sectionIndex,
          label:         lesson.sectionTitle,
          color:         lesson.color,
          startNodeIdx:  i,
          endNodeIdx:    i,
        });
      } else {
        result[result.length - 1].endNodeIdx = i;
      }
    });
    return result;
  }, [flatLessons]);

  // ── Stars for starfield ───────────────────────────────────────────────────────
  const stars = useMemo(
    () => generateStars(isMobile ? 60 : 120, canvasHeight),
    [canvasHeight, isMobile]
  );

  const nebulae = useMemo(
    () => generateNebulae(isMobile ? 3 : 5, canvasHeight),
    [canvasHeight, isMobile]
  );

  // ── Auto-scroll to first available node ──────────────────────────────────────
  useEffect(() => {
    const firstAvailableIdx = flatLessons.findIndex(
      (l, i) => getStatus(l.lessonId, i) === "available"
    );
    if (firstAvailableIdx === -1 || !scrollRef.current) return;

    const targetY     = nodePositions[firstAvailableIdx]?.y ?? 0;
    const containerH  = scrollRef.current.clientHeight;
    const scrollTop   = targetY - containerH / 2 + 40;

    const timer = setTimeout(() => {
      scrollRef.current?.scrollTo({ top: Math.max(0, scrollTop), behavior: "smooth" });
    }, 350);
    return () => clearTimeout(timer);
  }, [flatLessons, nodePositions, getStatus]);

  // ── Road rendering helpers ────────────────────────────────────────────────────
  const roadW     = isMobile ? 6 : 8;
  const roadGlowW = isMobile ? 18 : 24;

  // Primary colour — use the first section's colour or fallback to brand orange
  const primaryColor = sections[0]?.color ?? "#F97316";
  const bgGradient   = `radial-gradient(ellipse at 50% 0%, ${primaryColor}12 0%, transparent 50%), radial-gradient(ellipse at 80% 40%, #3B82F608 0%, transparent 40%), radial-gradient(ellipse at 20% 70%, #8B5CF608 0%, transparent 40%), #000000`;

  // ── Handle node click — open drawer ──────────────────────────────────────────
  const handleNodeClick = useCallback((lessonId: string) => {
    const idx = flatLessons.findIndex((l) => l.lessonId === lessonId);
    if (idx === -1) return;
    const lesson = flatLessons[idx];
    const status = getStatus(lessonId, idx);
    setSelectedLesson({ lesson, index: idx, status });
  }, [flatLessons, getStatus]);

  // Find the section's lessons for the selected node
  const selectedSectionLessons = useMemo(() => {
    if (!selectedLesson || !course) return [];
    const section = course.sections
      .sort((a, b) => a.position - b.position)
      [selectedLesson.lesson.sectionIndex];
    if (!section) return [];
    return [...section.lessons].sort((a, b) => a.position - b.position);
  }, [selectedLesson, course]);

  // ── Loading state ─────────────────────────────────────────────────────────────
  if (loading) {
    return (
      <div
        className="flex items-center justify-center"
        style={{ height: "100dvh", background: "#000000" }}
      >
        <motion.p
          className="text-sm font-medium"
          style={{ color: "rgba(255,255,255,0.5)" }}
          animate={{ opacity: [0.4, 1, 0.4] }}
          transition={{ repeat: Infinity, duration: 1.5 }}
        >
          Загрузка...
        </motion.p>
      </div>
    );
  }

  if (!course) return null;

  // ── Render ────────────────────────────────────────────────────────────────────
  return (
    <div
      className="flex flex-col"
      style={{ height: "100dvh", background: "#000000", overflow: "hidden" }}
    >
      {/* ── Top bar ── */}
      <div
        className="shrink-0 flex items-center gap-3 px-4 py-3 border-b"
        style={{
          borderColor: "rgba(255,255,255,0.06)",
          background:  "rgba(0,0,0,0.95)",
          backdropFilter: "blur(12px)",
          zIndex: 50,
        }}
      >
        {/* Back button */}
        <button
          onClick={() => navigate(`/courses/${id}`)}
          className="flex items-center justify-center rounded-full shrink-0 transition-colors hover:bg-white/10 active:bg-white/20 cursor-pointer"
          style={{
            width:  36,
            height: 36,
            color:  "rgba(255,255,255,0.8)",
            border: "1px solid rgba(255,255,255,0.12)",
          }}
          aria-label="Назад"
        >
          <ArrowLeft size={18} />
        </button>

        {/* Title + progress */}
        <div className="flex-1 min-w-0">
          <p
            className="text-[13px] font-bold truncate"
            style={{ color: "rgba(255,255,255,0.95)" }}
          >
            {course.title}
          </p>

          {/* Progress bar */}
          <div className="flex items-center gap-2 mt-1">
            <div
              className="flex-1 h-1.5 rounded-full overflow-hidden"
              style={{ background: "rgba(255,255,255,0.1)" }}
            >
              <motion.div
                className="h-full rounded-full"
                style={{ background: primaryColor }}
                initial={{ width: 0 }}
                animate={{ width: `${progressPercent}%` }}
                transition={{ duration: 0.8, ease: "easeOut" }}
              />
            </div>
            <span
              className="text-[11px] font-semibold shrink-0"
              style={{ color: primaryColor }}
            >
              {progressPercent}%
            </span>
          </div>
        </div>
      </div>

      {/* ── Scrollable roadmap canvas ── */}
      <div
        ref={scrollRef}
        className="relative flex-1 overflow-y-auto overflow-x-hidden"
        style={{
          background:              bgGradient,
          scrollbarWidth:          "thin",
          scrollbarColor:          `${primaryColor}40 transparent`,
          WebkitOverflowScrolling: "touch",
        }}
      >
        {/* Deep space background */}
        <div
          className="absolute inset-0 pointer-events-none"
          style={{ height: canvasHeight }}
        >
          {/* Nebulae — soft glowing clouds */}
          {nebulae.map((n, i) => (
            <motion.div
              key={`neb-${i}`}
              className="absolute rounded-full pointer-events-none"
              style={{
                left:       `${n.x}%`,
                top:        n.y,
                width:      n.w,
                height:     n.h,
                background: `radial-gradient(ellipse, ${n.color}08 0%, ${n.color}04 40%, transparent 70%)`,
                transform:  `translate(-50%, -50%) rotate(${n.rotate}deg)`,
                filter:     "blur(40px)",
              }}
              animate={{ opacity: [0.3, 0.6, 0.3], scale: [1, 1.05, 1] }}
              transition={{ repeat: Infinity, duration: 8 + i * 2, ease: "easeInOut" }}
            />
          ))}

          {/* Stars — twinkling */}
          {stars.map((star, i) => (
            <motion.div
              key={i}
              className="absolute rounded-full"
              style={{
                left:            `${star.x}%`,
                top:             star.y,
                width:           star.size,
                height:          star.size,
                backgroundColor: star.color,
                boxShadow:       star.size > 2 ? `0 0 ${star.size * 3}px ${star.color}` : undefined,
              }}
              animate={{ opacity: [0.05, 0.7, 0.05] }}
              transition={{
                repeat:   Infinity,
                duration: star.duration,
                delay:    star.delay,
                ease:     "easeInOut",
              }}
            />
          ))}

          {/* ── Horizontal starfall — shooting stars flying left to right ── */}
          {Array.from({ length: isMobile ? 5 : 8 }).map((_, i) => {
            const startY = 5 + (i / 8) * 85;
            const len = 50 + Math.random() * 60;
            const dur = 1.2 + Math.random() * 0.8;
            const delay = i * 3 + Math.random() * 5;
            const slight_y = -10 + Math.random() * 20;
            return (
              <motion.div
                key={`fall-${i}`}
                className="absolute pointer-events-none will-change-transform"
                style={{
                  left: -len,
                  top: `${startY}%`,
                  width: len,
                  height: 1.5,
                  borderRadius: 1,
                  background: "linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.15) 60%, rgba(255,255,255,0.6) 100%)",
                }}
                animate={{
                  opacity: [0, 0.7, 0.7, 0],
                  x: [0, window.innerWidth + len],
                  y: [0, slight_y],
                }}
                transition={{
                  repeat: Infinity,
                  duration: dur,
                  delay,
                  ease: "linear",
                  repeatDelay: 10 + Math.random() * 15,
                }}
              />
            );
          })}

          {/* ── Comet — CSS animation for smooth 60fps ── */}
          <div
            className="absolute pointer-events-none will-change-transform"
            style={{
              left: -150,
              top: "12%",
              animation: `comet-fly-1 6s ease-in-out 8s infinite`,
              opacity: 0,
            }}
          >
            <div style={{
              width: 5, height: 5, borderRadius: "50%",
              background: "white",
              boxShadow: "0 0 6px 2px rgba(255,255,255,0.8), 0 0 14px 6px rgba(249,115,22,0.3)",
            }} />
            <div style={{
              position: "absolute", top: 0.5, right: 5, width: 100, height: 2.5,
              borderRadius: 2,
              background: "linear-gradient(270deg, rgba(255,255,255,0.5) 0%, rgba(249,115,22,0.2) 40%, transparent 100%)",
            }} />
            <div style={{
              position: "absolute", top: -1, right: 3, width: 60, height: 1,
              borderRadius: 1,
              background: "linear-gradient(270deg, rgba(255,255,255,0.25) 0%, transparent 100%)",
            }} />
          </div>

          {/* Second comet — opposite direction, rarer */}
          <div
            className="absolute pointer-events-none will-change-transform"
            style={{
              right: -150,
              top: "55%",
              animation: `comet-fly-2 5s ease-in-out 25s infinite`,
              opacity: 0,
            }}
          >
            <div style={{
              width: 4, height: 4, borderRadius: "50%",
              background: "white",
              boxShadow: "0 0 5px 2px rgba(255,255,255,0.7), 0 0 12px 5px rgba(236,72,153,0.25)",
            }} />
            <div style={{
              position: "absolute", top: 0.5, left: 4, width: 80, height: 2,
              borderRadius: 2,
              background: "linear-gradient(90deg, rgba(255,255,255,0.4) 0%, rgba(236,72,153,0.15) 40%, transparent 100%)",
            }} />
          </div>

          {/* CSS keyframes for smooth comet animation */}
          <style>{`
            @keyframes comet-fly-1 {
              0%   { transform: translateX(0) translateY(0); opacity: 0; }
              5%   { opacity: 0.9; }
              80%  { opacity: 0.7; }
              100% { transform: translateX(${(isMobile ? 500 : 900) + 150}px) translateY(60px); opacity: 0; }
            }
            @keyframes comet-fly-2 {
              0%   { transform: translateX(0) translateY(0); opacity: 0; }
              5%   { opacity: 0.7; }
              80%  { opacity: 0.5; }
              100% { transform: translateX(-${(isMobile ? 500 : 900) + 150}px) translateY(40px); opacity: 0; }
            }
          `}</style>
        </div>

        {/* Mascots — rendered inside the main canvas column (below), not here */}

        {/* Main canvas column */}
        <div
          className="relative mx-auto"
          style={{ width: canvasW, height: canvasHeight, minHeight: "100%", zIndex: 5 }}
        >
          {/* SVG winding path */}
          <svg
            className="absolute inset-0 pointer-events-none"
            width={canvasW}
            height={canvasHeight}
            style={{ overflow: "visible" }}
          >
            <defs>
              <filter id="cr-road-glow" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="6" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
              <filter id="cr-path-shadow" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow dx="0" dy="3" stdDeviation="5" floodColor="rgba(0,0,0,0.4)" />
              </filter>
            </defs>

            {/* Stardust glow — wide soft trail */}
            <path
              d={pathD}
              fill="none"
              stroke={`${primaryColor}15`}
              strokeWidth={roadGlowW}
              strokeLinecap="round"
              strokeLinejoin="round"
              filter="url(#cr-road-glow)"
            />

            {/* Star path — thin luminous trail */}
            <path
              d={pathD}
              fill="none"
              stroke="rgba(255,255,255,0.12)"
              strokeWidth={roadW}
              strokeLinecap="round"
              strokeLinejoin="round"
            />

            {/* Sparkle dots along the path */}
            <path
              d={pathD}
              fill="none"
              stroke="rgba(255,255,255,0.25)"
              strokeWidth={2}
              strokeLinecap="round"
              strokeDasharray="2 20"
            />

            {/* Coloured segments for completed / active */}
            {flatLessons.slice(1).map((lesson, i) => {
              const fromStatus    = getStatus(flatLessons[i].lessonId, i);
              const toStatus      = getStatus(lesson.lessonId, i + 1);
              const isCompleted   = toStatus === "completed" || fromStatus === "completed";
              const isActive      = toStatus === "available" && fromStatus !== "locked";
              const segColor      = lesson.color;

              if (!isCompleted && !isActive) return null;

              const { x: x1, y: y1 } = nodePositions[i];
              const { x: x2, y: y2 } = nodePositions[i + 1];
              const segD              = `M ${x1} ${y1} ${bezierSegment(x1, y1, x2, y2)}`;
              const activeW           = isMobile ? 6 : 8;
              const completedW        = isMobile ? 4 : 6;

              return (
                <g key={lesson.lessonId}>
                  {isActive && (
                    <path
                      d={segD}
                      fill="none"
                      stroke={segColor}
                      strokeWidth={roadGlowW}
                      strokeLinecap="round"
                      opacity={0.15}
                      filter="url(#cr-road-glow)"
                    />
                  )}
                  <path
                    d={segD}
                    fill="none"
                    stroke={isCompleted ? "#22C55E" : segColor}
                    strokeWidth={isActive ? activeW : completedW}
                    strokeLinecap="round"
                    opacity={isActive ? 0.8 : 0.9}
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

          {/* Space decorations at section midpoints */}
          {sections.map((sec, i) => {
            const startY     = nodePositions[sec.startNodeIdx]?.y ?? 0;
            const endY       = nodePositions[sec.endNodeIdx]?.y ?? 0;
            const midY       = (startY + endY) / 2;
            const midNodeIdx = Math.floor((sec.startNodeIdx + sec.endNodeIdx) / 2);
            const midNodeX   = nodePositions[midNodeIdx]?.x ?? canvasW / 2;
            const isOnRight  = midNodeX > canvasW / 2;
            const iconSize   = isMobile ? 28 : 36;
            const offsetX    = isMobile ? 8 : 16;
            const iconLeft   = isOnRight ? offsetX : canvasW - iconSize - offsetX;

            return (
              <motion.div
                key={`space-${i}`}
                className="absolute pointer-events-none select-none flex items-center justify-center"
                style={{
                  left:      iconLeft,
                  top:       midY - iconSize / 2,
                  width:     iconSize,
                  height:    iconSize,
                  fontSize:  isMobile ? 20 : 26,
                  zIndex:    3,
                  filter:    "drop-shadow(0 2px 8px rgba(0,0,0,0.5))",
                }}
                initial={{ opacity: 0, scale: 0 }}
                animate={{
                  opacity: 0.6,
                  scale:   1,
                  y:       [0, -4, 0],
                  rotate:  [0, 5, -5, 0],
                }}
                transition={{
                  opacity: { delay: 0.5 + i * 0.1, duration: 0.4 },
                  scale:   { delay: 0.5 + i * 0.1, type: "spring", stiffness: 200 },
                  y:       { repeat: Infinity, duration: 4 + i * 0.5, ease: "easeInOut" },
                  rotate:  { repeat: Infinity, duration: 6 + i * 0.5, ease: "easeInOut" },
                }}
              >
                {SPACE_ICONS[i % SPACE_ICONS.length]}
              </motion.div>
            );
          })}

          {/* Section header labels */}
          {sections.map((sec) => {
            const topY   = nodePositions[sec.startNodeIdx]?.y ?? 0;
            const labelY = topY - (isMobile ? 52 : 64);
            if (labelY < 0) return null;

            return (
              <div
                key={`sec-label-${sec.sectionIndex}`}
                className="absolute left-0 right-0 flex items-center justify-center pointer-events-none"
                style={{ top: labelY, zIndex: 10 }}
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.8, y: 10 }}
                  animate={{ opacity: 1, scale: 1, y: 0 }}
                  transition={{
                    delay:     sec.sectionIndex * 0.12,
                    type:      "spring",
                    stiffness: 200,
                  }}
                  className="flex items-center gap-1.5 px-3 lg:px-5 py-1 lg:py-1.5 rounded-full text-xs uppercase tracking-wider"
                  style={{
                    background:     `linear-gradient(135deg, ${sec.color}20, ${sec.color}10)`,
                    color:          "rgba(255,255,255,0.3)",
                    border:         `1px solid rgba(255,255,255,0.06)`,
                    backdropFilter: "blur(12px)",
                    maxWidth:       isMobile ? "85%" : undefined,
                  }}
                >
                  <span style={{ fontSize: isMobile ? 13 : 16 }}>📖</span>
                  <span className="truncate">{sec.label}</span>
                </motion.div>
              </div>
            );
          })}

          {/* Nodes */}
          {flatLessons.map((lesson, i) => {
            const { x, y } = nodePositions[i];
            const status    = getStatus(lesson.lessonId, i);

            return (
              <motion.div
                key={lesson.lessonId}
                className="absolute"
                style={{
                  left:      x,
                  top:       y,
                  transform: "translate(-50%, -50%)",
                  zIndex:    10,
                }}
                initial={{ opacity: 0, scale: 0.5, y: 20 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                transition={{
                  delay:    i * 0.04,
                  type:     "spring",
                  stiffness: 250,
                  damping:   18,
                }}
              >
                <PathNode
                  id={lesson.lessonId}
                  title={lesson.title}
                  status={status}
                  color={lesson.color}
                  index={i}
                  isCurrentNode={status === "available"}
                  onClick={() => handleNodeClick(lesson.lessonId)}
                  compact={isMobile}
                />
              </motion.div>
            );
          })}

          {/* НАЧАЛО label below first node */}
          {flatLessons.length > 0 && (
            <motion.div
              className="absolute flex items-center justify-center pointer-events-none"
              style={{
                left:      nodePositions[0].x,
                top:       nodePositions[0].y + (isMobile ? 50 : 64),
                transform: "translateX(-50%)",
                zIndex:    6,
              }}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5 }}
            >
              <span
                className="text-[9px] font-bold uppercase tracking-widest px-3 py-1 rounded-full"
                style={{
                  color:      "rgba(255,255,255,0.5)",
                  background: `${primaryColor}15`,
                  border:     `1px solid ${primaryColor}20`,
                }}
              >
                НАЧАЛО
              </span>
            </motion.div>
          )}

          {/* ФИНИШ trophy above last node */}
          {flatLessons.length > 0 && (() => {
            const lastPos    = nodePositions[nodePositions.length - 1];
            const lastLesson = flatLessons[flatLessons.length - 1];
            const lastStatus = getStatus(lastLesson.lessonId, flatLessons.length - 1);

            return (
              <motion.div
                className="absolute flex flex-col items-center gap-2 pointer-events-none"
                style={{
                  left:      lastPos.x,
                  top:       lastPos.y - (isMobile ? 70 : 90),
                  transform: "translateX(-50%)",
                  zIndex:    6,
                }}
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 1 }}
              >
                <motion.div
                  className="flex items-center justify-center"
                  style={{ fontSize: isMobile ? 28 : 36 }}
                  animate={
                    lastStatus === "completed"
                      ? { scale: [1, 1.2, 1], rotate: [0, 10, -10, 0] }
                      : { y: [0, -4, 0] }
                  }
                  transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
                >
                  🚀
                </motion.div>
                <motion.span
                  className="text-2xl lg:text-3xl drop-shadow-lg"
                  animate={
                    lastStatus === "completed"
                      ? { scale: [1, 1.15, 1], rotate: [0, 5, -5, 0] }
                      : {}
                  }
                  transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
                >
                  🏆
                </motion.span>
                <span
                  className="text-[10px] lg:text-[11px] font-bold uppercase tracking-wider px-3 py-1 rounded-full"
                  style={{
                    color:      lastStatus === "completed" ? "#FFD700" : "rgba(255,255,255,0.4)",
                    background: lastStatus === "completed"
                      ? "rgba(255,215,0,0.15)"
                      : "rgba(255,255,255,0.05)",
                    border: `1px solid ${
                      lastStatus === "completed"
                        ? "rgba(255,215,0,0.4)"
                        : "rgba(255,255,255,0.1)"
                    }`,
                    textShadow: "0 1px 4px rgba(0,0,0,0.6)",
                  }}
                >
                  {lastStatus === "completed" ? "ПРОЙДЕНО! 🎉" : "ФИНИШ"}
                </span>
              </motion.div>
            );
          })()}
        </div>
      </div>

      {/* ── Lesson Drawer ── */}
      <AnimatePresence>
        {selectedLesson && (
          <>
            {/* Backdrop */}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setSelectedLesson(null)}
              className="fixed inset-0 bg-black/60 z-[60]"
            />

            {/* Drawer panel — slides up from bottom on mobile, from right on desktop */}
            <motion.div
              initial={{ y: "100%" }}
              animate={{ y: 0 }}
              exit={{ y: "100%" }}
              transition={{ type: "spring", damping: 28, stiffness: 300 }}
              className="fixed bottom-0 left-0 right-0 lg:left-auto lg:top-0 lg:w-96 lg:h-full z-[70] overflow-y-auto"
              style={{
                maxHeight: isMobile ? "85dvh" : "100dvh",
                background: "linear-gradient(180deg, #111111 0%, #000000 100%)",
                borderTop: "1px solid rgba(255,255,255,0.06)",
                borderLeft: isMobile ? "none" : "1px solid rgba(255,255,255,0.06)",
                borderRadius: isMobile ? "1.25rem 1.25rem 0 0" : 0,
              }}
            >
              {/* Handle bar (mobile) */}
              {isMobile && (
                <div className="flex justify-center pt-3 pb-1">
                  <div className="w-10 h-1 rounded-full bg-white/20" />
                </div>
              )}

              <div className="p-5 lg:p-6">
                {/* Header */}
                <div className="flex items-start justify-between mb-4">
                  <div className="flex-1 min-w-0">
                    <div
                      className="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider mb-2"
                      style={{
                        backgroundColor: `${selectedLesson.lesson.color}20`,
                        color: selectedLesson.lesson.color,
                        border: `1px solid ${selectedLesson.lesson.color}40`,
                      }}
                    >
                      {selectedLesson.lesson.sectionTitle}
                    </div>
                    <h3 className="text-lg font-bold text-white">{selectedLesson.lesson.title}</h3>
                  </div>
                  <button
                    onClick={() => setSelectedLesson(null)}
                    className="p-1.5 rounded-lg hover:bg-white/10 text-white/50 hover:text-white transition-colors cursor-pointer shrink-0 ml-3"
                  >
                    <X size={20} />
                  </button>
                </div>

                {/* XP badge */}
                {(() => {
                  const origLesson = selectedSectionLessons.find(l => l.id === selectedLesson.lesson.lessonId);
                  const xp = origLesson?.xp_reward ?? 0;
                  return xp > 0 ? (
                    <div className="flex items-center gap-1.5 mb-4">
                      <Zap size={14} className="text-yellow-400" />
                      <span className="text-sm font-semibold text-yellow-400">+{xp} XP</span>
                    </div>
                  ) : null;
                })()}

                {/* Section lessons list */}
                <div className="mb-5">
                  <p className="text-xs text-white/40 uppercase tracking-wider mb-3 font-medium">
                    Уроки в секции
                  </p>
                  <div className="space-y-1.5">
                    {selectedSectionLessons.map((lesson) => {
                      const isDone = completedSet.has(lesson.id);
                      const isSelected = lesson.id === selectedLesson.lesson.lessonId;
                      return (
                        <button
                          key={lesson.id}
                          onClick={() => {
                            const idx = flatLessons.findIndex(l => l.lessonId === lesson.id);
                            if (idx >= 0) {
                              const fl = flatLessons[idx];
                              setSelectedLesson({ lesson: fl, index: idx, status: getStatus(lesson.id, idx) });
                            }
                          }}
                          className={`w-full text-left px-3.5 py-2.5 rounded-xl text-sm transition-all cursor-pointer border ${
                            isSelected
                              ? `border-[${selectedLesson.lesson.color}] bg-white/10 text-white`
                              : isDone
                              ? "border-green-500/20 bg-green-500/5 text-green-400"
                              : "border-white/5 hover:border-white/15 text-white/70 hover:text-white hover:bg-white/5"
                          }`}
                          style={isSelected ? { borderColor: `${selectedLesson.lesson.color}60` } : undefined}
                        >
                          <span className="flex items-center gap-2">
                            {isDone && <span className="text-green-400">✓</span>}
                            {isSelected && !isDone && <span style={{ color: selectedLesson.lesson.color }}>▸</span>}
                            <span className="flex-1 truncate">{lesson.title}</span>
                            <span className="text-[10px] text-white/30">+{lesson.xp_reward} XP</span>
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Action */}
                {selectedLesson.status === "locked" ? (
                  <div className="flex flex-col items-center gap-3 py-4">
                    <motion.img
                      src="/images/mascot-confused.png"
                      alt="Заблокировано"
                      className="w-24 h-24 object-contain drop-shadow-lg opacity-60"
                      animate={{ y: [0, -4, 0] }}
                      transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
                    />
                    <div className="flex items-center gap-2 text-white/40">
                      <Lock size={14} />
                      <p className="text-sm">Пройдите предыдущие уроки</p>
                    </div>
                  </div>
                ) : (
                  <div className="flex flex-col items-center gap-4">
                    <motion.img
                      src={
                        completedSet.has(selectedLesson.lesson.lessonId)
                          ? "/images/mascot-study.png"
                          : "/images/mascot-thinking.png"
                      }
                      alt="Маскот"
                      className="w-20 h-20 lg:w-24 lg:h-24 object-contain drop-shadow-lg"
                      animate={{ y: [0, -5, 0] }}
                      transition={{ repeat: Infinity, duration: 2.5, ease: "easeInOut" }}
                    />
                    <Button
                      className="w-full"
                      onClick={() => {
                        navigate(`/courses/${id}/learn/${selectedLesson.lesson.lessonId}`);
                      }}
                    >
                      {completedSet.has(selectedLesson.lesson.lessonId)
                        ? "Повторить урок"
                        : "Начать урок"}
                      <ArrowRight size={14} />
                    </Button>
                  </div>
                )}
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}
