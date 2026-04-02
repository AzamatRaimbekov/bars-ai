import { NavLink } from "react-router-dom";
import { cn } from "@/lib/cn";
import {
  LayoutDashboard,
  Map,
  MessageCircle,
  Mic,
  Trophy,
  User,
} from "lucide-react";

const navItems = [
  { to: "/dashboard", icon: LayoutDashboard, label: "Dashboard" },
  { to: "/roadmap", icon: Map, label: "Roadmap" },
  { to: "/mentor", icon: MessageCircle, label: "AI Mentor" },
  { to: "/simulator", icon: Mic, label: "Simulator" },
  { to: "/achievements", icon: Trophy, label: "Achievements" },
  { to: "/profile", icon: User, label: "Profile" },
];

export function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-full w-64 border-r border-border bg-surface/50 backdrop-blur-xl z-40 flex flex-col">
      <div className="p-6">
        <h1 className="text-xl font-bold">
          <span className="text-primary">Path</span>
          <span className="text-accent">Mind</span>
        </h1>
      </div>

      <nav className="flex-1 px-3 space-y-1">
        {navItems.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium transition-all",
                isActive
                  ? "bg-primary/10 text-primary"
                  : "text-text-secondary hover:text-text hover:bg-surface"
              )
            }
          >
            <Icon size={18} />
            {label}
          </NavLink>
        ))}
      </nav>

      <div className="p-4 mx-3 mb-4 rounded-xl bg-bg border border-border">
        <p className="text-xs text-text-secondary">AI-Powered Learning</p>
        <p className="text-xs text-primary mt-1">PathMind v1.0</p>
      </div>
    </aside>
  );
}
