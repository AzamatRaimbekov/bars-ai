import { NavLink } from "react-router-dom";
import { cn } from "@/lib/cn";
import { useTranslation } from "@/hooks/useTranslation";
import {
  LayoutDashboard,
  MessageCircle,
  Mic,
  Trophy,
  Medal,
  Shield,
  User,
  BookOpen,
} from "lucide-react";

export function Sidebar() {
  const { t } = useTranslation();

  const navItems = [
    { to: "/dashboard", icon: LayoutDashboard, label: t("nav.dashboard") },
    { to: "/courses", icon: BookOpen, label: t("nav.courses") },
    { to: "/mentor", icon: MessageCircle, label: t("nav.mentor") },
    { to: "/simulator", icon: Mic, label: t("nav.simulator") },
    { to: "/achievements", icon: Trophy, label: t("nav.achievements") },
    { to: "/leaderboard", icon: Medal, label: t("nav.leaderboard") },
    { to: "/leagues", icon: Shield, label: t("nav.leagues") },
    { to: "/profile", icon: User, label: t("nav.profile") },
  ];

  return (
    <aside className="hidden lg:flex fixed left-0 top-0 h-full w-64 border-r border-white/[0.06] bg-[#0A0A0A] z-40 flex-col">
      {/* Logo */}
      <div className="p-6 flex items-center gap-3">
        <h1 className="text-xl font-bold text-white">Bars AI</h1>
      </div>

      {/* Nav */}
      <nav className="flex-1 px-3 space-y-0.5">
        {navItems.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              cn(
                "relative flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium transition-all",
                isActive
                  ? "text-[#FB923C] bg-[#F97316]/[0.08]"
                  : "text-white/40 hover:text-white hover:bg-white/[0.04]"
              )
            }
          >
            {({ isActive }) => (
              <>
                {/* Active left indicator bar */}
                {isActive && (
                  <span className="absolute left-0 top-1/2 -translate-y-1/2 w-[2px] h-5 bg-[#F97316] rounded-full" />
                )}
                <Icon size={18} strokeWidth={isActive ? 2.2 : 1.8} />
                {label}
              </>
            )}
          </NavLink>
        ))}
      </nav>

      {/* Footer */}
      <div className="px-6 pb-5">
        <p className="text-xs text-white/20">{t("app.version")}</p>
      </div>
    </aside>
  );
}
