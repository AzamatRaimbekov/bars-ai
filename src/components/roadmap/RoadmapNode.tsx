import { memo } from "react";
import { motion } from "framer-motion";
import { Check, Lock, Star, Crown } from "lucide-react";
import type { NodeStatus } from "@/types";

export interface PathNodeProps {
  id: string;
  title: string;
  status: NodeStatus;
  color: string;
  index: number;
  isCurrentNode?: boolean;
  compact?: boolean;
  onClick: () => void;
}

export const PathNode = memo(function PathNode({
  title,
  status,
  color,
  index,
  isCurrentNode,
  compact,
  onClick,
}: PathNodeProps) {
  const isCompleted = status === "completed";
  const isAvailable = status === "available";
  const isLocked = status === "locked";

  const size = compact
    ? (isAvailable ? 58 : 50)
    : (isAvailable ? 76 : 66);

  const bgColor = isCompleted
    ? "#4ADE80"
    : isAvailable
    ? color
    : "rgba(255,255,255,0.1)";

  const borderColor = isCompleted
    ? "#22C55E"
    : isAvailable
    ? "rgba(255,255,255,0.3)"
    : "rgba(255,255,255,0.08)";

  return (
    <div className="flex flex-col items-center gap-2.5">
      <motion.button
        onClick={isLocked ? undefined : onClick}
        disabled={isLocked}
        aria-label={`${title} — ${status}`}
        style={{ width: size, height: size }}
        whileHover={!isLocked ? { scale: 1.15, y: -4 } : undefined}
        whileTap={!isLocked ? { scale: 0.92 } : undefined}
        className="relative flex items-center justify-center rounded-full focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/50 cursor-pointer"
      >
        {/* Multiple pulsing rings for available node */}
        {isAvailable && (
          <>
            <motion.span
              className="absolute inset-0 rounded-full"
              style={{ border: `3px solid ${color}` }}
              animate={{ scale: [1, 1.5, 1], opacity: [0.5, 0, 0.5] }}
              transition={{ repeat: Infinity, duration: 2, ease: "easeOut" }}
            />
            <motion.span
              className="absolute inset-0 rounded-full"
              style={{ border: `2px solid ${color}` }}
              animate={{ scale: [1, 1.8, 1], opacity: [0.3, 0, 0.3] }}
              transition={{ repeat: Infinity, duration: 2, delay: 0.3, ease: "easeOut" }}
            />
            <motion.span
              className="absolute inset-0 rounded-full"
              style={{ border: `1px solid ${color}` }}
              animate={{ scale: [1, 2.2, 1], opacity: [0.15, 0, 0.15] }}
              transition={{ repeat: Infinity, duration: 2, delay: 0.6, ease: "easeOut" }}
            />
          </>
        )}

        {/* Completed sparkle effect */}
        {isCompleted && (
          <motion.span
            className="absolute inset-0 rounded-full"
            style={{ border: "2px solid #4ADE80" }}
            animate={{ scale: [1, 1.3, 1], opacity: [0.4, 0, 0.4] }}
            transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
          />
        )}

        {/* Main circle */}
        <motion.div
          className="relative flex items-center justify-center rounded-full border-4"
          style={{
            width: size,
            height: size,
            background: isAvailable
              ? `linear-gradient(145deg, ${color}, ${color}cc)`
              : isCompleted
              ? "linear-gradient(145deg, #4ADE80, #22C55E)"
              : "linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04))",
            borderColor,
            opacity: isLocked ? 0.4 : 1,
            boxShadow: isAvailable
              ? `0 0 30px ${color}90, 0 0 60px ${color}40, 0 8px 24px rgba(0,0,0,0.4), inset 0 2px 4px rgba(255,255,255,0.2)`
              : isCompleted
              ? "0 0 20px rgba(74,222,128,0.5), 0 0 40px rgba(74,222,128,0.2), 0 8px 20px rgba(0,0,0,0.35), inset 0 2px 4px rgba(255,255,255,0.15)"
              : "0 4px 12px rgba(0,0,0,0.4), inset 0 1px 2px rgba(255,255,255,0.05)",
          }}
          animate={isAvailable ? {
            boxShadow: [
              `0 0 30px ${color}90, 0 0 60px ${color}40, 0 8px 24px rgba(0,0,0,0.4), inset 0 2px 4px rgba(255,255,255,0.2)`,
              `0 0 40px ${color}b0, 0 0 80px ${color}50, 0 8px 24px rgba(0,0,0,0.4), inset 0 2px 4px rgba(255,255,255,0.2)`,
              `0 0 30px ${color}90, 0 0 60px ${color}40, 0 8px 24px rgba(0,0,0,0.4), inset 0 2px 4px rgba(255,255,255,0.2)`,
            ],
          } : {}}
          transition={{ repeat: Infinity, duration: 2.5, ease: "easeInOut" }}
        >
          {/* Planet atmosphere glow */}
          <div
            className="absolute rounded-full"
            style={{
              top: 2,
              left: "15%",
              width: "70%",
              height: "40%",
              background: "linear-gradient(180deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0) 100%)",
              borderRadius: "50%",
            }}
          />

          {/* Inner crater ring */}
          <div
            className="absolute inset-2 rounded-full"
            style={{
              border: `1.5px solid rgba(255,255,255,${isLocked ? "0.04" : "0.12"})`,
            }}
          />

          {/* Planet ring (Saturn-style) for available nodes */}
          {isAvailable && (
            <motion.div
              className="absolute pointer-events-none"
              style={{
                width: size * 1.6,
                height: size * 0.35,
                left: "50%",
                top: "50%",
                transform: "translate(-50%, -50%) rotateX(65deg)",
                border: `2px solid ${color}60`,
                borderRadius: "50%",
              }}
              animate={{ opacity: [0.4, 0.7, 0.4] }}
              transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
            />
          )}

          {/* Icon */}
          {isCompleted && (
            <Check
              size={size * 0.38}
              strokeWidth={3.5}
              className="text-white relative z-10 drop-shadow-lg"
            />
          )}
          {isAvailable && (
            <motion.div
              animate={{ rotate: [0, 10, -10, 0] }}
              transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
            >
              {isCurrentNode && index === 0 ? (
                <Crown
                  size={size * 0.4}
                  strokeWidth={2}
                  fill="rgba(255,255,255,0.9)"
                  className="text-white relative z-10 drop-shadow-lg"
                />
              ) : (
                <Star
                  size={size * 0.4}
                  strokeWidth={0}
                  fill="rgba(255,255,255,0.95)"
                  className="text-white relative z-10 drop-shadow-lg"
                />
              )}
            </motion.div>
          )}
          {isLocked && (
            <Lock
              size={size * 0.34}
              strokeWidth={2.5}
              className="text-gray-400 relative z-10"
            />
          )}

          {/* Step number badge */}
          <span
            className="absolute -bottom-1.5 -right-1.5 rounded-full flex items-center justify-center font-bold shadow-lg"
            style={{
              minWidth: compact ? 18 : 22,
              height: compact ? 18 : 22,
              fontSize: compact ? 8 : 10,
              backgroundColor: isCompleted
                ? "#166534"
                : isAvailable
                ? "#0a0a0a"
                : "rgba(255,255,255,0.06)",
              color: isCompleted ? "#BBF7D0" : isAvailable ? "white" : "rgba(255,255,255,0.3)",
              border: isCompleted
                ? "2px solid #4ADE80"
                : isAvailable
                ? `2px solid ${color}`
                : "2px solid rgba(255,255,255,0.08)",
              boxShadow: isAvailable ? `0 0 8px ${color}60` : undefined,
            }}
          >
            {index + 1}
          </span>
        </motion.div>
      </motion.button>

      {/* Label below */}
      <span
        className="text-center font-medium leading-snug select-none"
        style={{
          maxWidth: compact ? 100 : 130,
          fontSize: compact ? 10 : 11,
          color: isLocked ? "rgba(255,255,255,0.25)" : isAvailable ? "rgba(255,255,255,0.95)" : "rgba(255,255,255,0.6)",
          textShadow: "0 1px 4px rgba(0,0,0,0.8)",
          display: "-webkit-box",
          WebkitLineClamp: 2,
          WebkitBoxOrient: "vertical" as const,
          overflow: "hidden",
          wordBreak: "break-word" as const,
        }}
      >
        {title}
      </span>
    </div>
  );
});
