import { useEffect, useState } from "react";
import { CreditCard, Check, X, Eye } from "lucide-react";
import { apiFetch } from "../lib/api";
import PageTransition from "../components/PageTransition";
import StatusBadge from "../components/StatusBadge";

interface Payment {
  id: string;
  course_id: string;
  course_title: string;
  user_name: string;
  user_email: string;
  amount: number;
  currency: string;
  screenshot_url: string;
  status: string;
  created_at: string;
}

export default function PaymentsPage() {
  const [payments, setPayments] = useState<Payment[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState("all");
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [actionLoading, setActionLoading] = useState<string | null>(null);

  useEffect(() => {
    apiFetch<Payment[]>("/api/admin/payments")
      .then(setPayments)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const pendingCount = payments.filter((p) => p.status === "pending").length;

  const filtered =
    filter === "all"
      ? payments
      : payments.filter((p) => p.status === filter);

  async function handleReview(id: string, action: "approve" | "reject") {
    const label = action === "approve" ? "одобрить" : "отклонить";
    if (!confirm(`Вы уверены, что хотите ${label} этот платёж?`)) return;

    setActionLoading(id);
    try {
      await apiFetch(`/api/admin/payments/${id}/review`, {
        method: "POST",
        body: JSON.stringify({ action }),
      });
      setPayments((prev) =>
        prev.map((p) =>
          p.id === id
            ? { ...p, status: action === "approve" ? "approved" : "rejected" }
            : p
        )
      );
    } catch {
      alert("Ошибка при обработке платежа");
    } finally {
      setActionLoading(null);
    }
  }

  const statusLabel: Record<string, string> = {
    approved: "Одобрен",
    pending: "Ожидает",
    rejected: "Отклонён",
  };

  const statusVariant = (s: string) => {
    if (s === "approved") return "green" as const;
    if (s === "pending") return "yellow" as const;
    return "red" as const;
  };

  return (
    <PageTransition>
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <CreditCard size={20} className="text-purple-400" />
          <h1 className="text-xl font-bold text-white">
            Платежи{" "}
            {pendingCount > 0 && (
              <span className="text-yellow-400 font-normal text-base">
                ({pendingCount} ожидают)
              </span>
            )}
          </h1>
        </div>

        <div className="flex items-center gap-2">
          {["all", "pending", "approved", "rejected"].map((s) => (
            <button
              key={s}
              onClick={() => setFilter(s)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-colors cursor-pointer ${
                filter === s
                  ? "bg-[var(--accent)] text-white"
                  : "bg-white/5 text-zinc-400 hover:text-white hover:bg-white/10"
              }`}
            >
              {s === "all"
                ? "Все"
                : s === "pending"
                  ? "Ожидают"
                  : s === "approved"
                    ? "Одобрены"
                    : "Отклонены"}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="flex items-center justify-center h-64 text-zinc-500">
          Загрузка...
        </div>
      ) : (
        <div className="bg-[var(--surface)] border border-white/8 rounded-xl overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-zinc-500 text-left border-b border-white/8">
                  <th className="px-5 py-3 font-medium">Пользователь</th>
                  <th className="px-5 py-3 font-medium">Курс</th>
                  <th className="px-5 py-3 font-medium">Сумма</th>
                  <th className="px-5 py-3 font-medium">Дата</th>
                  <th className="px-5 py-3 font-medium">Статус</th>
                  <th className="px-5 py-3 font-medium">Скриншот</th>
                  <th className="px-5 py-3 font-medium">Действия</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((p) => (
                  <tr
                    key={p.id}
                    className="border-t border-white/5 hover:bg-white/3 transition-colors"
                  >
                    <td className="px-5 py-3">
                      <div className="text-white font-medium">{p.user_name}</div>
                      <div className="text-xs text-zinc-500">{p.user_email}</div>
                    </td>
                    <td className="px-5 py-3 text-zinc-300 max-w-xs truncate">
                      {p.course_title}
                    </td>
                    <td className="px-5 py-3 text-white font-medium">
                      {p.amount} {p.currency}
                    </td>
                    <td className="px-5 py-3 text-zinc-400">
                      {new Date(p.created_at).toLocaleDateString("ru-RU")}
                    </td>
                    <td className="px-5 py-3">
                      <StatusBadge variant={statusVariant(p.status)}>
                        {statusLabel[p.status] ?? p.status}
                      </StatusBadge>
                    </td>
                    <td className="px-5 py-3">
                      {p.screenshot_url ? (
                        <button
                          onClick={() => setPreviewUrl(p.screenshot_url)}
                          className="flex items-center gap-1 text-xs text-[var(--accent)] hover:underline cursor-pointer"
                        >
                          <Eye size={14} />
                          Открыть
                        </button>
                      ) : (
                        <span className="text-zinc-600 text-xs">Нет</span>
                      )}
                    </td>
                    <td className="px-5 py-3">
                      {p.status === "pending" ? (
                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => handleReview(p.id, "approve")}
                            disabled={actionLoading === p.id}
                            className="flex items-center gap-1 px-2.5 py-1.5 bg-emerald-500/15 text-emerald-400 hover:bg-emerald-500/25 rounded-lg text-xs font-medium transition-colors cursor-pointer disabled:opacity-50"
                          >
                            <Check size={13} />
                            Одобрить
                          </button>
                          <button
                            onClick={() => handleReview(p.id, "reject")}
                            disabled={actionLoading === p.id}
                            className="flex items-center gap-1 px-2.5 py-1.5 bg-red-500/15 text-red-400 hover:bg-red-500/25 rounded-lg text-xs font-medium transition-colors cursor-pointer disabled:opacity-50"
                          >
                            <X size={13} />
                            Отклонить
                          </button>
                        </div>
                      ) : (
                        <span className="text-zinc-600 text-xs">—</span>
                      )}
                    </td>
                  </tr>
                ))}
                {filtered.length === 0 && (
                  <tr>
                    <td
                      colSpan={7}
                      className="px-5 py-8 text-center text-zinc-500"
                    >
                      Платежей не найдено
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Screenshot preview modal */}
      {previewUrl && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/70"
          onClick={() => setPreviewUrl(null)}
        >
          <div
            className="relative max-w-2xl max-h-[80vh]"
            onClick={(e) => e.stopPropagation()}
          >
            <button
              onClick={() => setPreviewUrl(null)}
              className="absolute -top-3 -right-3 p-1.5 bg-zinc-800 rounded-full text-zinc-400 hover:text-white transition-colors cursor-pointer"
            >
              <X size={16} />
            </button>
            <img
              src={previewUrl}
              alt="Скриншот оплаты"
              className="max-w-full max-h-[80vh] rounded-xl border border-white/8 object-contain"
            />
          </div>
        </div>
      )}
    </PageTransition>
  );
}
