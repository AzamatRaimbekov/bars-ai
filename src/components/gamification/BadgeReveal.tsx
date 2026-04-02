import { motion, AnimatePresence } from "framer-motion";
import type { Badge as BadgeType } from "@/types";

interface BadgeRevealProps {
  badge: BadgeType | null;
  onClose: () => void;
}

export function BadgeReveal({ badge, onClose }: BadgeRevealProps) {
  return (
    <AnimatePresence>
      {badge && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
          onClick={onClose}
        >
          <motion.div
            initial={{ scale: 0, rotate: -180 }}
            animate={{ scale: 1, rotate: 0 }}
            exit={{ scale: 0, rotate: 180 }}
            transition={{ type: "spring", damping: 15 }}
            className="flex flex-col items-center gap-4 p-8 rounded-3xl border border-primary/30 bg-surface"
          >
            <motion.span
              className="text-7xl"
              animate={{ scale: [1, 1.3, 1] }}
              transition={{ repeat: 3, duration: 0.6 }}
            >
              {badge.icon}
            </motion.span>
            <h3 className="text-xl font-bold text-primary">Badge Unlocked!</h3>
            <p className="text-lg font-semibold">{badge.name}</p>
            <p className="text-sm text-text-secondary text-center max-w-xs">
              {badge.description}
            </p>
            <span className="text-xs uppercase tracking-wider text-warning font-bold">
              {badge.rarity}
            </span>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
