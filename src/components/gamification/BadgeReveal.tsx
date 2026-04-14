import { motion, AnimatePresence } from "framer-motion";
import { useTranslation } from "@/hooks/useTranslation";
import type { Badge as BadgeType } from "@/types";

interface BadgeRevealProps {
  badge: BadgeType | null;
  onClose: () => void;
}

const RARITY_COLORS: Record<string, string> = {
  common: "#6B7280",
  uncommon: "#22C55E",
  rare: "#3B82F6",
  epic: "#A855F7",
  legendary: "#F97316",
};

export function BadgeReveal({ badge, onClose }: BadgeRevealProps) {
  const { t, lang } = useTranslation();

  const rarityColor = badge ? (RARITY_COLORS[badge.rarity] ?? "#F97316") : "#F97316";

  return (
    <AnimatePresence>
      {badge && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm"
          onClick={onClose}
        >
          <motion.div
            initial={{ scale: 0, rotate: -180 }}
            animate={{ scale: 1, rotate: 0 }}
            exit={{ scale: 0, rotate: 180 }}
            transition={{ type: "spring", damping: 15 }}
            className="flex flex-col items-center gap-5 p-8 rounded-3xl bg-[#0A0A0A] text-center"
            style={{ border: `1px solid ${rarityColor}30` }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Badge icon — centered, no mascot */}
            <motion.div
              className="w-24 h-24 rounded-2xl flex items-center justify-center"
              style={{ backgroundColor: `${rarityColor}12` }}
              animate={{ scale: [1, 1.15, 1] }}
              transition={{ repeat: 3, duration: 0.6 }}
            >
              <motion.span
                className="text-5xl"
                animate={{ scale: [1, 1.3, 1] }}
                transition={{ repeat: 3, duration: 0.6, delay: 0.2 }}
              >
                {badge.icon}
              </motion.span>
            </motion.div>

            <div className="space-y-1">
              <h3 className="text-xs uppercase tracking-widest font-semibold" style={{ color: rarityColor }}>
                {t("achievements.badgeUnlocked")}
              </h3>
              <p className="text-xl font-bold text-white">{badge.name[lang]}</p>
            </div>

            <p className="text-sm text-white/40 max-w-xs leading-relaxed">
              {badge.description[lang]}
            </p>

            <span
              className="text-xs uppercase tracking-widest font-bold px-3 py-1 rounded-full"
              style={{ backgroundColor: `${rarityColor}15`, color: rarityColor }}
            >
              {badge.rarity}
            </span>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
