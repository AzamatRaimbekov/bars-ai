import { cn } from "@/lib/cn";
import type { BadgeRarity } from "@/types";

const rarityStyles: Record<BadgeRarity, string> = {
  Common: "border-text-secondary/30 text-text-secondary",
  Rare: "border-primary/50 text-primary",
  Epic: "border-accent/50 text-accent",
  Legendary: "border-primary/50 text-primary",
};

interface BadgeProps {
  icon: string;
  name: string;
  rarity: BadgeRarity;
  locked?: boolean;
  className?: string;
}

export function Badge({ icon, name, rarity, locked, className }: BadgeProps) {
  return (
    <div
      className={cn(
        "flex flex-col items-center gap-2 p-4 rounded-2xl border bg-surface/50 transition-all",
        locked ? "opacity-40 grayscale" : rarityStyles[rarity],
        className
      )}
    >
      <span className="text-3xl">{icon}</span>
      <span className="text-xs font-medium text-center">{name}</span>
      <span
        className={cn(
          "text-[10px] uppercase tracking-wider font-semibold",
          locked ? "text-text-secondary/50" : rarityStyles[rarity]
        )}
      >
        {rarity}
      </span>
    </div>
  );
}
