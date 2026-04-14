import { cn } from "@/lib/cn";
import type { InputHTMLAttributes } from "react";

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
}

export function Input({ label, className, ...props }: InputProps) {
  return (
    <div className="w-full">
      {label && <label className="block text-xs text-text-secondary mb-1.5 uppercase tracking-wider">{label}</label>}
      <input
        className={cn(
          "w-full rounded-xl border border-border bg-transparent px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50",
          className
        )}
        {...props}
      />
    </div>
  );
}
