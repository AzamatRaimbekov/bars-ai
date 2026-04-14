import { Modal } from "@/components/ui/Modal";
import { useTranslation } from "@/hooks/useTranslation";
import { motion } from "framer-motion";
import type { Level } from "@/types";

interface LevelUpModalProps {
  open: boolean;
  onClose: () => void;
  level: Level;
}

export function LevelUpModal({ open, onClose, level }: LevelUpModalProps) {
  const { t } = useTranslation();

  return (
    <Modal open={open} onClose={onClose}>
      <div className="flex flex-col items-center gap-5 py-6 text-center">
        {/* Animated ring burst */}
        <motion.div
          className="relative flex items-center justify-center"
          animate={{ rotate: [0, 10, -10, 0], scale: [1, 1.15, 1] }}
          transition={{ repeat: 2, duration: 0.5 }}
        >
          <div className="w-20 h-20 rounded-full bg-[#F97316]/10 flex items-center justify-center">
            <div className="w-14 h-14 rounded-full bg-[#F97316]/20 flex items-center justify-center">
              <span className="text-3xl">🏆</span>
            </div>
          </div>
        </motion.div>

        <div className="space-y-1">
          <h2 className="text-2xl font-bold tracking-tight">{t("gamification.levelUp")}</h2>
          <p className="text-xl font-semibold text-[#FB923C]">{t(`level.${level}` as any)}</p>
        </div>

        <p className="text-sm text-white/40 max-w-xs leading-relaxed">
          {t("gamification.keepGoing")}
        </p>
      </div>
    </Modal>
  );
}
