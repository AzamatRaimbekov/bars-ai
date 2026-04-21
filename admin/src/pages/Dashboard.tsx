import { useEffect, useState } from "react";
import { Users, BookOpen, Trophy, CreditCard, Zap, Shield } from "lucide-react";
import { apiFetch } from "../lib/api";
import PageTransition from "../components/PageTransition";
import StatusBadge from "../components/StatusBadge";

interface Stats {
  total_users: number;
  total_courses: number;
  total_trophies: number;
  active_sprint: { id: string; title: string; end_date: string } | null;
}

interface PendingCourse {
  id: string;
}

interface Payment {
  id: string;
  course_title: string;
  user_name: string;
  user_email: string;
  amount: number;
  currency: string;
  status: string;
  created_at: string;
}

export default function Dashboard() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [payments, setPayments] = useState<Payment[]>([]);
  const [pendingCount, setPendingCount] = useState(0);
  const [moderationCount, setModerationCount] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const [s, p, pending] = await Promise.all([
          apiFetch<Stats>("/api/admin/stats"),
          apiFetch<Payment[]>("/api/admin/payments"),
          apiFetch<PendingCourse[]>("/api/admin/courses/pending").catch(() => [] as PendingCourse[]),
        ]);
        setStats(s);
        setPayments(p.slice(0, 5));
        setPendingCount(p.filter((x) => x.status === "pending").length);
        setModerationCount(pending.length);
      } catch {
        /* handled by apiFetch */
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64 text-zinc-500">
        Загрузка...
      </div>
    );
  }

  const cards = [
    {
      icon: Users,
      label: "Пользователи",
      value: stats?.total_users ?? 0,
      color: "text-blue-400",
    },
    {
      icon: BookOpen,
      label: "Курсы",
      value: stats?.total_courses ?? 0,
      color: "text-emerald-400",
    },
    {
      icon: Trophy,
      label: "Трофеи",
      value: stats?.total_trophies ?? 0,
      color: "text-yellow-400",
    },
    {
      icon: Shield,
      label: "Курсы на модерации",
      value: moderationCount,
      color: "text-orange-400",
    },
    {
      icon: CreditCard,
      label: "Ожидают оплаты",
      value: pendingCount,
      color: "text-purple-400",
    },
  ];

  return (
    <PageTransition>
      <h1 className="text-xl font-bold text-white mb-6">Дашборд</h1>

      {/* Stats cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-8">
        {cards.map((card) => (
          <div
            key={card.label}
            className="bg-[var(--surface)] border border-white/8 rounded-xl p-5"
          >
            <div className="flex items-center gap-3 mb-3">
              <div className="p-2 rounded-lg bg-white/5">
                <card.icon size={20} className={card.color} />
              </div>
              <span className="text-sm text-zinc-400">{card.label}</span>
            </div>
            <p className="text-2xl font-bold text-white">{card.value}</p>
          </div>
        ))}
      </div>

      {/* Active sprint */}
      {stats?.active_sprint && (
        <div className="bg-[var(--surface)] border border-white/8 rounded-xl p-5 mb-8">
          <div className="flex items-center gap-3 mb-2">
            <Zap size={18} className="text-yellow-400" />
            <h2 className="text-sm font-semibold text-white">
              Активный спринт
            </h2>
          </div>
          <p className="text-white font-medium">
            {stats.active_sprint.title}
          </p>
          <p className="text-sm text-zinc-400 mt-1">
            До{" "}
            {new Date(stats.active_sprint.end_date).toLocaleDateString("ru-RU")}
          </p>
        </div>
      )}

      {/* Recent payments */}
      <div className="bg-[var(--surface)] border border-white/8 rounded-xl">
        <div className="px-5 py-4 border-b border-white/8">
          <h2 className="text-sm font-semibold text-white">
            Последние платежи
          </h2>
        </div>
        {payments.length === 0 ? (
          <div className="px-5 py-8 text-center text-zinc-500 text-sm">
            Платежей пока нет
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-zinc-500 text-left">
                  <th className="px-5 py-3 font-medium">Пользователь</th>
                  <th className="px-5 py-3 font-medium">Курс</th>
                  <th className="px-5 py-3 font-medium">Сумма</th>
                  <th className="px-5 py-3 font-medium">Статус</th>
                  <th className="px-5 py-3 font-medium">Дата</th>
                </tr>
              </thead>
              <tbody>
                {payments.map((p) => (
                  <tr
                    key={p.id}
                    className="border-t border-white/5 hover:bg-white/3 transition-colors"
                  >
                    <td className="px-5 py-3 text-white">{p.user_name}</td>
                    <td className="px-5 py-3 text-zinc-300">
                      {p.course_title}
                    </td>
                    <td className="px-5 py-3 text-zinc-300">
                      {p.amount} {p.currency}
                    </td>
                    <td className="px-5 py-3">
                      <StatusBadge
                        variant={
                          p.status === "approved"
                            ? "green"
                            : p.status === "pending"
                              ? "yellow"
                              : "red"
                        }
                      >
                        {p.status === "approved"
                          ? "Одобрен"
                          : p.status === "pending"
                            ? "Ожидает"
                            : "Отклонён"}
                      </StatusBadge>
                    </td>
                    <td className="px-5 py-3 text-zinc-400">
                      {new Date(p.created_at).toLocaleDateString("ru-RU")}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </PageTransition>
  );
}
