import { useEffect, useState } from "react";
import { Shield, CheckCircle, XCircle, Loader2 } from "lucide-react";
import { apiFetch } from "../lib/api";
import PageTransition from "../components/PageTransition";
import StatusBadge from "../components/StatusBadge";

interface PendingCourse {
  id: string;
  title: string;
  description: string;
  category: string;
  difficulty: string;
  price: number;
  currency: string;
  author_name: string;
  author_email: string;
  author_id: string;
  created_at: string;
}

const difficultyLabel: Record<string, string> = {
  beginner: "Начинающий",
  intermediate: "Средний",
  advanced: "Продвинутый",
  Beginner: "Начинающий",
  Intermediate: "Средний",
  Advanced: "Продвинутый",
};

function difficultyVariant(d: string) {
  const lower = d?.toLowerCase();
  if (lower === "beginner") return "green" as const;
  if (lower === "intermediate") return "yellow" as const;
  if (lower === "advanced") return "red" as const;
  return "gray" as const;
}

export default function ModerationPage() {
  const [courses, setCourses] = useState<PendingCourse[]>([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState<string | null>(null);
  const [rejectingId, setRejectingId] = useState<string | null>(null);
  const [rejectNote, setRejectNote] = useState("");
  const [toast, setToast] = useState<{ message: string; type: "success" | "error" } | null>(null);

  async function loadCourses() {
    try {
      const data = await apiFetch<PendingCourse[]>("/api/admin/courses/pending");
      setCourses(data);
    } catch {
      /* handled by apiFetch */
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadCourses();
  }, []);

  function showToast(message: string, type: "success" | "error" = "success") {
    setToast({ message, type });
    setTimeout(() => setToast(null), 3000);
  }

  async function handleApprove(courseId: string, title: string) {
    if (!confirm(`Одобрить курс «${title}»?`)) return;
    setActionLoading(courseId);
    try {
      await apiFetch(`/api/admin/courses/${courseId}/review`, {
        method: "POST",
        body: JSON.stringify({ action: "approve" }),
      });
      setCourses((prev) => prev.filter((c) => c.id !== courseId));
      showToast(`Курс «${title}» одобрен`);
    } catch {
      showToast("Ошибка при одобрении курса", "error");
    } finally {
      setActionLoading(null);
    }
  }

  async function handleReject(courseId: string, title: string) {
    if (!rejectNote.trim()) return;
    setActionLoading(courseId);
    try {
      await apiFetch(`/api/admin/courses/${courseId}/review`, {
        method: "POST",
        body: JSON.stringify({ action: "reject", note: rejectNote.trim() }),
      });
      setCourses((prev) => prev.filter((c) => c.id !== courseId));
      setRejectingId(null);
      setRejectNote("");
      showToast(`Курс «${title}» отклонён`);
    } catch {
      showToast("Ошибка при отклонении курса", "error");
    } finally {
      setActionLoading(null);
    }
  }

  return (
    <PageTransition>
      <div className="flex items-center gap-3 mb-6">
        <Shield size={20} className="text-orange-400" />
        <h1 className="text-xl font-bold text-white">
          Модерация{" "}
          {courses.length > 0 && (
            <span className="inline-flex items-center justify-center ml-2 px-2.5 py-0.5 text-sm font-medium rounded-full bg-orange-500/15 text-orange-400 border border-orange-500/20">
              {courses.length}
            </span>
          )}
        </h1>
      </div>

      {/* Toast */}
      {toast && (
        <div
          className={`fixed top-4 right-4 z-50 px-4 py-3 rounded-lg text-sm font-medium shadow-lg transition-all ${
            toast.type === "success"
              ? "bg-emerald-500/90 text-white"
              : "bg-red-500/90 text-white"
          }`}
        >
          {toast.message}
        </div>
      )}

      {loading ? (
        <div className="flex items-center justify-center h-64 text-zinc-500">
          Загрузка...
        </div>
      ) : courses.length === 0 ? (
        <div className="bg-[var(--surface)] border border-white/8 rounded-xl p-12 text-center">
          <Shield size={40} className="mx-auto text-zinc-600 mb-3" />
          <p className="text-zinc-400 text-sm">Нет курсов на модерации</p>
        </div>
      ) : (
        <div className="bg-[var(--surface)] border border-orange-500/15 rounded-xl overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="text-zinc-500 text-left border-b border-white/8">
                  <th className="px-5 py-3 font-medium">Название</th>
                  <th className="px-5 py-3 font-medium">Автор</th>
                  <th className="px-5 py-3 font-medium">Категория</th>
                  <th className="px-5 py-3 font-medium">Сложность</th>
                  <th className="px-5 py-3 font-medium">Цена</th>
                  <th className="px-5 py-3 font-medium">Дата</th>
                  <th className="px-5 py-3 font-medium">Действия</th>
                </tr>
              </thead>
              <tbody>
                {courses.map((c) => (
                  <tr
                    key={c.id}
                    className="border-t border-white/5 hover:bg-white/3 transition-colors"
                  >
                    <td className="px-5 py-3">
                      <div className="text-white font-medium max-w-xs truncate">
                        {c.title}
                      </div>
                      {c.description && (
                        <div className="text-zinc-500 text-xs mt-0.5 max-w-xs truncate">
                          {c.description}
                        </div>
                      )}
                    </td>
                    <td className="px-5 py-3">
                      <div className="text-zinc-300">{c.author_name}</div>
                      <div className="text-zinc-500 text-xs">{c.author_email}</div>
                    </td>
                    <td className="px-5 py-3 text-zinc-300">
                      {c.category || "—"}
                    </td>
                    <td className="px-5 py-3">
                      <StatusBadge variant={difficultyVariant(c.difficulty)}>
                        {difficultyLabel[c.difficulty] ?? c.difficulty ?? "—"}
                      </StatusBadge>
                    </td>
                    <td className="px-5 py-3 text-zinc-300">
                      {c.price ? `${c.price} ${c.currency || "KGS"}` : "Бесплатно"}
                    </td>
                    <td className="px-5 py-3 text-zinc-400">
                      {new Date(c.created_at).toLocaleDateString("ru-RU")}
                    </td>
                    <td className="px-5 py-3">
                      {rejectingId === c.id ? (
                        <div className="flex flex-col gap-2 min-w-[200px]">
                          <textarea
                            value={rejectNote}
                            onChange={(e) => setRejectNote(e.target.value)}
                            placeholder="Причина отклонения..."
                            rows={2}
                            className="w-full px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-red-500/50 transition-colors resize-none"
                          />
                          <div className="flex items-center gap-2">
                            <button
                              onClick={() => handleReject(c.id, c.title)}
                              disabled={!rejectNote.trim() || actionLoading === c.id}
                              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-red-500/15 text-red-400 border border-red-500/20 hover:bg-red-500/25 transition-colors cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
                            >
                              {actionLoading === c.id ? (
                                <Loader2 size={13} className="animate-spin" />
                              ) : (
                                <XCircle size={13} />
                              )}
                              Отклонить
                            </button>
                            <button
                              onClick={() => {
                                setRejectingId(null);
                                setRejectNote("");
                              }}
                              className="px-3 py-1.5 rounded-lg text-xs text-zinc-500 hover:text-zinc-300 transition-colors cursor-pointer"
                            >
                              Отмена
                            </button>
                          </div>
                        </div>
                      ) : (
                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => handleApprove(c.id, c.title)}
                            disabled={actionLoading === c.id}
                            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-emerald-500/15 text-emerald-400 border border-emerald-500/20 hover:bg-emerald-500/25 transition-colors cursor-pointer disabled:opacity-50"
                            title="Одобрить"
                          >
                            {actionLoading === c.id ? (
                              <Loader2 size={13} className="animate-spin" />
                            ) : (
                              <CheckCircle size={13} />
                            )}
                            Одобрить
                          </button>
                          <button
                            onClick={() => setRejectingId(c.id)}
                            disabled={actionLoading === c.id}
                            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-red-500/15 text-red-400 border border-red-500/20 hover:bg-red-500/25 transition-colors cursor-pointer disabled:opacity-50"
                            title="Отклонить"
                          >
                            <XCircle size={13} />
                            Отклонить
                          </button>
                        </div>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </PageTransition>
  );
}
