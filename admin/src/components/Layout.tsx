import { NavLink, Outlet } from "react-router-dom";
import {
  LayoutDashboard,
  Users,
  BookOpen,
  CreditCard,
  Zap,
  Shield,
  LogOut,
} from "lucide-react";
import { useAuthStore } from "../store/authStore";
import { cn } from "../lib/cn";

const navItems = [
  { to: "/", icon: LayoutDashboard, label: "Дашборд" },
  { to: "/users", icon: Users, label: "Пользователи" },
  { to: "/courses", icon: BookOpen, label: "Курсы" },
  { to: "/moderation", icon: Shield, label: "Модерация" },
  { to: "/payments", icon: CreditCard, label: "Платежи" },
  { to: "/sprints", icon: Zap, label: "Спринты" },
];

export default function Layout() {
  const { adminName, logout } = useAuthStore();

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar */}
      <aside className="w-60 shrink-0 flex flex-col border-r border-white/8 bg-[var(--surface)]">
        <div className="px-5 py-6">
          <h1 className="text-lg font-bold tracking-tight text-white">
            Bars AI{" "}
            <span className="text-[var(--accent)] font-medium">Admin</span>
          </h1>
        </div>

        <nav className="flex-1 px-3 space-y-1">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.to === "/"}
              className={({ isActive }) =>
                cn(
                  "flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors",
                  isActive
                    ? "bg-[var(--accent)] text-white"
                    : "text-zinc-400 hover:text-zinc-200 hover:bg-white/5"
                )
              }
            >
              <item.icon size={18} />
              {item.label}
            </NavLink>
          ))}
        </nav>

        <div className="p-3 border-t border-white/8">
          <button
            onClick={logout}
            className="flex items-center gap-3 w-full px-3 py-2.5 rounded-lg text-sm text-zinc-400 hover:text-red-400 hover:bg-white/5 transition-colors cursor-pointer"
          >
            <LogOut size={18} />
            Выйти
          </button>
        </div>
      </aside>

      {/* Main area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top bar */}
        <header className="h-14 shrink-0 flex items-center justify-end px-6 border-b border-white/8 bg-[var(--surface)]">
          <span className="text-sm text-zinc-400">{adminName}</span>
        </header>

        {/* Content */}
        <main className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
