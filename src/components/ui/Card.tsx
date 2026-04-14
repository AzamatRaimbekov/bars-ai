import { cn } from "@/lib/cn";
import { motion } from "framer-motion";
import type { HTMLAttributes, ReactNode } from "react";

export interface CardProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  hover?: boolean;
  glow?: string;
}

export function Card({ children, className, hover = false, glow, ...props }: CardProps) {
  return (
    <motion.div
      whileHover={hover ? { y: -2, scale: 1.01 } : undefined}
      className={cn(
        "rounded-2xl border border-border bg-surface/80 p-6 relative overflow-hidden",
        hover && "cursor-pointer transition-colors hover:border-primary/30",
        className
      )}
      {...(props as any)}
    >
      {children}
    </motion.div>
  );
}
