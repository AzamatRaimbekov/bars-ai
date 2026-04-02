import { cn } from "@/lib/cn";
import { motion } from "framer-motion";
import type { HTMLAttributes, ReactNode } from "react";

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  glow?: string;
  hover?: boolean;
}

export function Card({ children, className, glow, hover = false, ...props }: CardProps) {
  return (
    <motion.div
      whileHover={hover ? { y: -2, scale: 1.01 } : undefined}
      className={cn(
        "rounded-2xl border border-border bg-surface/80 backdrop-blur-xl p-6 relative overflow-hidden",
        hover && "cursor-pointer transition-colors hover:border-primary/30",
        className
      )}
      style={
        glow
          ? {
              boxShadow: `0 0 40px ${glow}15, inset 0 1px 0 ${glow}10`,
            }
          : undefined
      }
      {...(props as any)}
    >
      {children}
    </motion.div>
  );
}
