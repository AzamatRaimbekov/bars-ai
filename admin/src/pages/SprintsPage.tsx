import { useEffect, useState, type FormEvent } from "react";
import { Zap, Plus, StopCircle, Ban } from "lucide-react";
import { apiFetch } from "../lib/api";
import PageTransition from "../components/PageTransition";
import StatusBadge from "../components/StatusBadge";

interface Sprint {
  id: string;
  title: string;
  start_date: string;
  end_date: string;
  status: string;
  prizes: unknown;
}

export default function SprintsPage() {
  const [sprints, setSprints] = useState<Sprint[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formTitle, setFormTitle] = useState("");
  const [formStart, setFormStart] = useState("");
  const [formEnd, setFormEnd] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [actionLoading, setActionLoading] = useState<string | null>(null);

  useEffect(() => {
    loadSprints();
  }, []);

  async function loadSprints() {
    try {
      const data = await apiFetch<Sprint[]>("/api/admin/sprints");
      setSprints(data);
    } catch {
      /* handled */
    } finally {
      setLoading(false);
    }
  }

  async function handleCreate(e: FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    try {
      await apiFetch("/api/admin/sprints", {
        method: "POST",
        body: JSON.stringify({
          title: formTitle,
          start_date: formStart,
          end_date: formEnd,
        }),
      });
      setFormTitle("");
      setFormStart("");
      setFormEnd("");
      setShowForm(false);
      await loadSprints();
    } catch {
      alert("Ошибка при создании спринта");
    } finally {
      setSubmitting(false);
    }
  }

  async function handleClose(id: string) {
    if (!confirm("Завершить этот спринт?")) return;
    setActionLoading(id);
    try {
      await apiFetch(`/api/admin/sprints/${id}/close`, { method: "POST" });
      setSprints((prev) =>
        prev.map((s) => (s.id === id ? { ...s, status: "closed" } : s))
      );
    } catch {
      alert("Ошибка при завершении спринта");
    } finally {
      setActionLoading(null);
    }
  }

  async function handleCancel(id: string) {
    if (!confirm("Отменить этот спринт?")) return;
    setActionLoading(id);
    try {
      await apiFetch(`/api/admin/sprints/${id}/cancel`, { method: "POST" });
      setSprints((prev) =>
        prev.map((s) => (s.id === id ? { ...s, status: "cancelled" } : s))
      );
    } catch {
      alert("Ошибка при отмене спринта");
    } finally {
      setActionLoading(null);
    }
  }

  const statusVariant = (s: string) => {
    if (s === "active") return "green" as const;
    if (s === "upcoming") return "yellow" as const;
    if (s === "cancelled") return "red" as const;
    return "gray" as const;
  };

  const statusLabel: Record<string, string> = {
    active: "Активный",
    upcoming: "Предстоящий",
    closed: "Завершён",
    cancelled: "Отменён",
  };

  return (
    <PageTransition>
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <Zap size={20} className="text-yellow-400" />
          <h1 className="text-xl font-bold text-white">Спринты</h1>
        </div>

        <button
          onClick={() => setShowForm(!showForm)}
          className="flex items-center gap-2 px-4 py-2 bg-[var(--accent)] hover:bg-[var(--accent)]/90 text-white text-sm font-medium rounded-lg transition-colors cursor-pointer"
        >
          <Plus size={16} />
          Новый спринт
        </button>
      </div>

      {/* Create form */}
      {showForm && (
        <form
          onSubmit={handleCreate}
          className="bg-[var(--surface)] border border-white/8 rounded-xl p-5 mb-6 space-y-4"
        >
          <h2 className="text-sm font-semibold text-white">
            Создать спринт
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-xs text-zinc-400 mb-1.5">
                Название
              </label>
              <input
                type="text"
                value={formTitle}
                onChange={(e) => setFormTitle(e.target.value)}
                required
                placeholder="Весенний спринт"
                className="w-full px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[var(--accent)] transition-colors"
              />
            </div>
            <div>
              <label className="block text-xs text-zinc-400 mb-1.5">
                Начало
              </label>
              <input
                type="date"
                value={formStart}
                onChange={(e) => setFormStart(e.target.value)}
                required
                className="w-full px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white focus:outline-none focus:border-[var(--accent)] transition-colors"
              />
            </div>
            <div>
              <label className="block text-xs text-zinc-400 mb-1.5">
                Конец
              </label>
              <input
                type="date"
                value={formEnd}
                onChange={(e) => setFormEnd(e.target.value)}
                required
                className="w-full px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white focus:outline-none focus:border-[var(--accent)] transition-colors"
              />
            </div>
          </div>
          <div className="flex items-center gap-3">
            <button
              type="submit"
              disabled={submitting}
              className="px-4 py-2 bg-[var(--accent)] hover:bg-[var(--accent)]/90 disabled:opacity-50 text-white text-sm font-medium rounded-lg transition-colors cursor-pointer"
            >
              {submitting ? "Создание..." : "Создать"}
            </button>
            <button
              type="button"
              onClick={() => setShowForm(false)}
              className="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/8 text-zinc-300 text-sm rounded-lg transition-colors cursor-pointer"
            >
              Отмена
            </button>
          </div>
        </form>
      )}

      {loading ? (
        <div className="flex items-center justify-center h-64 text-zinc-500">
          Загрузка...
        </div>
      ) : sprints.length === 0 ? (
        <div className="bg-[var(--surface)] border border-white/8 rounded-xl px-5 py-12 text-center text-zinc-500 text-sm">
          Спринтов пока нет
        </div>
      ) : (
        <div className="space-y-4">
          {sprints.map((s) => (
            <div
              key={s.id}
              className="bg-[var(--surface)] border border-white/8 rounded-xl p-5"
            >
              <div className="flex items-start justify-between">
                <div>
                  <div className="flex items-center gap-3 mb-2">
                    <h3 className="text-white font-semibold">{s.title}</h3>
                    <StatusBadge variant={statusVariant(s.status)}>
                      {statusLabel[s.status] ?? s.status}
                    </StatusBadge>
                  </div>
                  <p className="text-sm text-zinc-400">
                    {new Date(s.start_date).toLocaleDateString("ru-RU")} —{" "}
                    {new Date(s.end_date).toLocaleDateString("ru-RU")}
                  </p>
                </div>

                {(s.status === "active" || s.status === "upcoming") && (
                  <div className="flex items-center gap-2">
                    {s.status === "active" && (
                      <button
                        onClick={() => handleClose(s.id)}
                        disabled={actionLoading === s.id}
                        className="flex items-center gap-1.5 px-3 py-1.5 bg-zinc-500/15 text-zinc-300 hover:bg-zinc-500/25 rounded-lg text-xs font-medium transition-colors cursor-pointer disabled:opacity-50"
                      >
                        <StopCircle size={13} />
                        Завершить
                      </button>
                    )}
                    <button
                      onClick={() => handleCancel(s.id)}
                      disabled={actionLoading === s.id}
                      className="flex items-center gap-1.5 px-3 py-1.5 bg-red-500/15 text-red-400 hover:bg-red-500/25 rounded-lg text-xs font-medium transition-colors cursor-pointer disabled:opacity-50"
                    >
                      <Ban size={13} />
                      Отменить
                    </button>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </PageTransition>
  );
}
