import { cn } from "../lib/cn";

type Variant = "green" | "yellow" | "red" | "gray" | "purple";

const variants: Record<Variant, string> = {
  green: "bg-emerald-500/15 text-emerald-400 border-emerald-500/20",
  yellow: "bg-yellow-500/15 text-yellow-400 border-yellow-500/20",
  red: "bg-red-500/15 text-red-400 border-red-500/20",
  gray: "bg-zinc-500/15 text-zinc-400 border-zinc-500/20",
  purple: "bg-purple-500/15 text-purple-400 border-purple-500/20",
};

export default function StatusBadge({
  variant,
  children,
}: {
  variant: Variant;
  children: React.ReactNode;
}) {
  return (
    <span
      className={cn(
        "inline-flex items-center px-2 py-0.5 text-xs font-medium rounded-full border",
        variants[variant]
      )}
    >
      {children}
    </span>
  );
}
