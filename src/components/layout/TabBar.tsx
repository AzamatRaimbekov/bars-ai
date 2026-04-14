import { NavLink, useLocation } from "react-router-dom";
import { cn } from "@/lib/cn";
import {
  LayoutDashboard,
  MessageCircle,
  BookOpen,
  User,
} from "lucide-react";

const tabs = [
  { to: "/dashboard", icon: LayoutDashboard, label: "Главная" },
  { to: "/courses", icon: BookOpen, label: "Курсы" },
  { to: "/mentor", icon: MessageCircle, label: "Ментор" },
  { to: "/profile", icon: User, label: "Профиль" },
] as const;

export function TabBar() {
  const { pathname } = useLocation();

  return (
    <div className="fixed bottom-4 left-4 right-4 z-40 lg:hidden">
      <div
        className="bg-[#1C1C1E]/90 backdrop-blur-2xl rounded-[22px] shadow-lg shadow-black/40"
        style={{ paddingBottom: "env(safe-area-inset-bottom, 0px)" }}
      >
        <div className="grid grid-cols-4 h-[56px]">
          {tabs.map(({ to, icon: Icon, label }) => {
            const active = pathname === to || pathname.startsWith(to + "/");

            return (
              <NavLink
                key={to}
                to={to}
                className="flex items-center justify-center"
              >
                <div className="flex flex-col items-center gap-[2px]">
                  <Icon
                    size={22}
                    strokeWidth={1.8}
                    className={cn(
                      "transition-colors duration-150",
                      active ? "text-[#F97316]" : "text-[#8E8E93]"
                    )}
                  />
                  <span
                    className={cn(
                      "text-[10px] leading-tight font-medium transition-colors duration-150",
                      active ? "text-[#F97316]" : "text-[#8E8E93]"
                    )}
                  >
                    {label}
                  </span>
                </div>
              </NavLink>
            );
          })}
        </div>
      </div>
    </div>
  );
}
