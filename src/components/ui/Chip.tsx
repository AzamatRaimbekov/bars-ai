import { cn } from "@/lib/cn";
import { motion } from "framer-motion";

interface ChipProps {
  label: string;
  onClick?: () => void;
  active?: boolean;
  className?: string;
}

export function Chip({ label, onClick, active, className }: ChipProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      onClick={onClick}
      className={cn(
        "px-4 py-2 rounded-full text-sm font-medium transition-all cursor-pointer border whitespace-nowrap",
        active
          ? "bg-primary/20 border-primary/50 text-primary"
          : "bg-surface border-border text-text-secondary hover:border-primary/30 hover:text-text",
        className
      )}
    >
      {label}
    </motion.button>
  );
}
