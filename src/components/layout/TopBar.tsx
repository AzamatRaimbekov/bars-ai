import { useUserStore } from "@/store/userStore";
import { useTranslation } from "@/hooks/useTranslation";
import { XPBar } from "@/components/gamification/XPBar";
import { StreakCounter } from "@/components/gamification/StreakCounter";
import { TrophyCounter } from "@/components/sprint/TrophyCounter";
import { Flame } from "lucide-react";

export function TopBar() {
  const profile = useUserStore((s) => s.profile);
  const { t } = useTranslation();
  if (!profile) return null;

  const hour = new Date().getHours();
  const greeting =
    hour < 12 ? t("topbar.morning") : hour < 18 ? t("topbar.afternoon") : t("topbar.evening");

  return (
    <header className="h-14 lg:h-16 border-b border-white/[0.06] bg-[#0A0A0A]/80 backdrop-blur-xl flex items-center justify-between px-4 lg:px-6">
      {/* Mobile: logo wordmark + greeting */}
      <div className="flex items-center gap-2.5 lg:hidden">
        <div>
          <span className="text-[13px] font-bold leading-none text-white">PathMind</span>
          <p className="text-[10px] text-white/40 leading-tight mt-0.5">
            {greeting}, {profile.name}
          </p>
        </div>
      </div>

      {/* Desktop: greeting */}
      <h2 className="text-sm font-medium text-white/40 hidden lg:block">
        {greeting},{" "}
        <span className="text-white font-semibold">{profile.name}</span>
      </h2>

      <div className="flex items-center gap-3 lg:gap-6">
        {/* Mobile: compact XP + streak + trophy pills */}
        <div className="flex items-center gap-2 lg:hidden">
          <span className="text-[11px] font-bold text-[#FB923C] bg-white/[0.04] px-2.5 py-1 rounded-full">
            {profile.xp} XP
          </span>
          <div className="flex items-center gap-1 bg-white/[0.04] px-2.5 py-1 rounded-full">
            <Flame size={12} className="text-orange-400" fill="currentColor" />
            <span className="text-[11px] font-bold text-white">{profile.streak}</span>
          </div>
          <TrophyCounter />
        </div>

        {/* Desktop: full XP bar + streak + trophy */}
        <div className="hidden lg:block">
          <XPBar />
        </div>
        <div className="hidden lg:block">
          <StreakCounter />
        </div>
        <div className="hidden lg:block">
          <TrophyCounter />
        </div>
      </div>
    </header>
  );
}
