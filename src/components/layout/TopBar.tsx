import { useUserStore } from "@/store/userStore";
import { XPBar } from "@/components/gamification/XPBar";
import { StreakCounter } from "@/components/gamification/StreakCounter";

export function TopBar() {
  const profile = useUserStore((s) => s.profile);
  if (!profile) return null;

  const hour = new Date().getHours();
  const greeting =
    hour < 12 ? "Good morning" : hour < 18 ? "Good afternoon" : "Good evening";

  return (
    <header className="h-16 border-b border-border bg-surface/50 backdrop-blur-xl flex items-center justify-between px-6">
      <div>
        <h2 className="text-sm font-medium">
          {greeting}, <span className="text-primary">{profile.name}</span>
        </h2>
      </div>

      <div className="flex items-center gap-6">
        <XPBar />
        <StreakCounter />
      </div>
    </header>
  );
}
