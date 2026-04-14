import { useUserStore } from "@/store/userStore";
import { useTranslation } from "@/hooks/useTranslation";
import { Flame } from "lucide-react";
import { motion } from "framer-motion";

export function StreakCounter() {
  const streak = useUserStore((s) => s.profile?.streak ?? 0);
  const { t } = useTranslation();

  return (
    <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#F97316]/8">
      <motion.div
        animate={streak > 0 ? { scale: [1, 1.2, 1] } : undefined}
        transition={{ repeat: Infinity, duration: 1.5 }}
      >
        <Flame
          size={16}
          className={streak > 0 ? "text-[#FB923C]" : "text-white/30"}
          fill={streak > 0 ? "#FB923C" : "none"}
        />
      </motion.div>
      <span className="text-sm font-semibold text-[#FB923C]">
        {streak} <span className="text-[#FB923C]/60 font-normal">{streak !== 1 ? t("common.days") : t("common.day")}</span>
      </span>
    </div>
  );
}
