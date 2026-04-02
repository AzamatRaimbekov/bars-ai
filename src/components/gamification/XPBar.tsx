import { useUserStore } from "@/store/userStore";
import { LEVELS_ORDERED, LEVEL_THRESHOLDS } from "@/lib/constants";
import { ProgressBar } from "@/components/ui/ProgressBar";

export function XPBar() {
  const profile = useUserStore((s) => s.profile);
  if (!profile) return null;

  const currentIdx = LEVELS_ORDERED.indexOf(profile.level);
  const nextLevel = LEVELS_ORDERED[currentIdx + 1];
  const currentThreshold = LEVEL_THRESHOLDS[profile.level];
  const nextThreshold = nextLevel ? LEVEL_THRESHOLDS[nextLevel] : currentThreshold;
  const progress = profile.xp - currentThreshold;
  const needed = nextThreshold - currentThreshold;

  return (
    <div className="flex items-center gap-3">
      <span className="text-xs font-semibold text-primary">{profile.level}</span>
      <div className="w-32">
        <ProgressBar value={progress} max={needed || 1} color="#6C63FF" />
      </div>
      <span className="text-xs text-text-secondary">{profile.xp} XP</span>
    </div>
  );
}
