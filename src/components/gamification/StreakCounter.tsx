import { useUserStore } from "@/store/userStore";
import { Flame } from "lucide-react";
import { motion } from "framer-motion";

export function StreakCounter() {
  const streak = useUserStore((s) => s.profile?.streak ?? 0);

  return (
    <div className="flex items-center gap-2">
      <motion.div
        animate={streak > 0 ? { scale: [1, 1.2, 1] } : undefined}
        transition={{ repeat: Infinity, duration: 1.5 }}
      >
        <Flame
          size={18}
          className={streak > 0 ? "text-warning" : "text-text-secondary"}
          fill={streak > 0 ? "#FFB800" : "none"}
        />
      </motion.div>
      <span className="text-sm font-semibold">
        {streak} <span className="text-text-secondary font-normal">day{streak !== 1 ? "s" : ""}</span>
      </span>
    </div>
  );
}
