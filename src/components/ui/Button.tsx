import { cn } from "@/lib/cn";
import { motion } from "framer-motion";
import type { ButtonHTMLAttributes, ReactNode } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "ghost";
  size?: "sm" | "md" | "lg";
  children: ReactNode;
}

export function Button({
  variant = "primary",
  size = "md",
  className,
  children,
  ...props
}: ButtonProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      className={cn(
        "inline-flex items-center justify-center gap-2 rounded-xl font-medium transition-all duration-200 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed",
        {
          "bg-primary text-white":
            variant === "primary",
          "bg-surface border border-border text-text hover:border-primary/50":
            variant === "secondary",
          "bg-transparent text-text-secondary hover:text-text hover:bg-surface":
            variant === "ghost",
        },
        {
          "px-3 py-1.5 text-sm": size === "sm",
          "px-5 py-2.5 text-sm": size === "md",
          "px-7 py-3.5 text-base": size === "lg",
        },
        className
      )}
      {...(props as any)}
    >
      {children}
    </motion.button>
  );
}
