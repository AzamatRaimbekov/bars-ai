import { cn } from "@/lib/cn";
import { motion } from "framer-motion";

interface ProgressBarProps {
  value: number;
  max?: number;
  color?: string;
  className?: string;
  showLabel?: boolean;
}

export function ProgressBar({
  value,
  max = 100,
  color = "#F97316",
  className,
  showLabel = false,
}: ProgressBarProps) {
  const percent = Math.min((value / max) * 100, 100);

  return (
    <div className={cn("w-full", className)}>
      {showLabel && (
        <div className="flex justify-between text-xs text-text-secondary mb-1">
          <span>{value}</span>
          <span>{max}</span>
        </div>
      )}
      <div className="h-1.5 rounded-full bg-border overflow-hidden">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${percent}%` }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="h-full rounded-full"
          style={{
            background: `linear-gradient(90deg, ${color}, ${color}99)`,
          }}
        />
      </div>
    </div>
  );
}
