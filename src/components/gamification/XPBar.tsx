import { useUserStore } from "@/store/userStore";
import { useTranslation } from "@/hooks/useTranslation";
import { LEVELS_ORDERED, LEVEL_THRESHOLDS } from "@/lib/constants";
import { ProgressBar } from "@/components/ui/ProgressBar";

export function XPBar() {
  const profile = useUserStore((s) => s.profile);
  const { t } = useTranslation();
  if (!profile) return null;

  const currentIdx = LEVELS_ORDERED.indexOf(profile.level);
  const nextLevel = LEVELS_ORDERED[currentIdx + 1];
  const currentThreshold = LEVEL_THRESHOLDS[profile.level];
  const nextThreshold = nextLevel ? LEVEL_THRESHOLDS[nextLevel] : currentThreshold;
  const progress = profile.xp - currentThreshold;
  const needed = nextThreshold - currentThreshold;

  return (
    <div className="flex items-center gap-3">
      <span className="text-xs font-semibold text-[#FB923C]">{t(`level.${profile.level}` as any)}</span>
      <div className="w-32">
        <ProgressBar value={progress} max={needed || 1} color="#F97316" />
      </div>
      <span className="text-xs text-white/40">{profile.xp} XP</span>
    </div>
  );
}
