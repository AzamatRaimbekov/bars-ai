import { useEffect, useState } from "react";
import { Search, BookOpen, Trash2 } from "lucide-react";
import { apiFetch } from "../lib/api";
import PageTransition from "../components/PageTransition";
import StatusBadge from "../components/StatusBadge";

interface Course {
  id: string;
  title: string;
  category: string;
  difficulty: string;
  price: number;
  currency: string;
  enrolled_count: number;
  status: string;
}

interface CoursesResponse {
  items: Course[];
  total: number;
}

export default function CoursesPage() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [search, setSearch] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("");
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editPrice, setEditPrice] = useState("");

  useEffect(() => {
    apiFetch<CoursesResponse>("/api/courses?page=1&page_size=100")
      .then((data) => setCourses(data.items))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const categories = [...new Set(courses.map((c) => c.category).filter(Boolean))];

  const filtered = courses.filter((c) => {
    const matchSearch = c.title
      ?.toLowerCase()
      .includes(search.toLowerCase());
    const matchCategory = !categoryFilter || c.category === categoryFilter;
    return matchSearch && matchCategory;
  });

  async function handleDelete(id: string) {
    if (!confirm("Удалить этот курс?")) return;
    try {
      await apiFetch(`/api/courses/${id}`, { method: "DELETE" });
      setCourses((prev) => prev.filter((c) => c.id !== id));
    } catch {
      alert("Ошибка при удалении курса");
    }
  }

  function startEdit(course: Course) {
    setEditingId(course.id);
    setEditPrice(String(course.price ?? 0));
  }

  async function savePrice(id: string) {
    try {
      await apiFetch(`/api/courses/${id}`, {
        method: "PATCH",
        body: JSON.stringify({ price: Number(editPrice) }),
      });
      setCourses((prev) =>
        prev.map((c) =>
          c.id === id ? { ...c, price: Number(editPrice) } : c
        )
      );
      setEditingId(null);
    } catch {
      alert("Ошибка при обновлении цены");
    }
  }

  function difficultyVariant(d: string) {
    if (d === "beginner") return "green" as const;
    if (d === "intermediate") return "yellow" as const;
    if (d === "advanced") return "red" as const;
    return "gray" as const;
  }

  const difficultyLabel: Record<string, string> = {
    beginner: "Начинающий",
    intermediate: "Средний",
    advanced: "Продвинутый",
  };

  return (
    <PageTransition>
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <BookOpen size={20} className="text-emerald-400" />
          <h1 className="text-xl font-bold text-white">
            Курсы{" "}
            <span className="text-zinc-500 font-normal text-base">
              ({courses.length})
            </span>
          </h1>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={categoryFilter}
            onChange={(e) => setCategoryFilter(e.target.value)}
            className="px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white focus:outline-none focus:border-[var(--accent)] transition-colors"
          >
            <option value="">Все категории</option>
            {categories.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>

          <div className="relative">
            <Search
              size={16}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-zinc-500"
            />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Поиск..."
              className="pl-9 pr-4 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[var(--accent)] transition-colors w-64"
            />
          </div>
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
                  <th className="px-5 py-3 font-medium">Название</th>
                  <th className="px-5 py-3 font-medium">Категория</th>
                  <th className="px-5 py-3 font-medium">Сложность</th>
                  <th className="px-5 py-3 font-medium">Цена</th>
                  <th className="px-5 py-3 font-medium">Записалось</th>
                  <th className="px-5 py-3 font-medium">Статус</th>
                  <th className="px-5 py-3 font-medium">Действия</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((c) => (
                  <tr
                    key={c.id}
                    className="border-t border-white/5 hover:bg-white/3 transition-colors"
                  >
                    <td className="px-5 py-3 text-white font-medium max-w-xs truncate">
                      {c.title}
                    </td>
                    <td className="px-5 py-3 text-zinc-300">
                      {c.category || "—"}
                    </td>
                    <td className="px-5 py-3">
                      <StatusBadge variant={difficultyVariant(c.difficulty)}>
                        {difficultyLabel[c.difficulty] ?? c.difficulty ?? "—"}
                      </StatusBadge>
                    </td>
                    <td className="px-5 py-3">
                      {editingId === c.id ? (
                        <div className="flex items-center gap-2">
                          <input
                            type="number"
                            value={editPrice}
                            onChange={(e) => setEditPrice(e.target.value)}
                            className="w-20 px-2 py-1 bg-white/5 border border-white/8 rounded text-sm text-white focus:outline-none focus:border-[var(--accent)]"
                          />
                          <button
                            onClick={() => savePrice(c.id)}
                            className="text-xs text-emerald-400 hover:text-emerald-300 cursor-pointer"
                          >
                            OK
                          </button>
                          <button
                            onClick={() => setEditingId(null)}
                            className="text-xs text-zinc-500 hover:text-zinc-400 cursor-pointer"
                          >
                            X
                          </button>
                        </div>
                      ) : (
                        <span
                          onClick={() => startEdit(c)}
                          className="text-zinc-300 hover:text-white cursor-pointer"
                        >
                          {c.price ? `${c.price} ${c.currency || "UZS"}` : "Бесплатно"}
                        </span>
                      )}
                    </td>
                    <td className="px-5 py-3 text-zinc-300">
                      {c.enrolled_count ?? 0}
                    </td>
                    <td className="px-5 py-3">
                      <StatusBadge
                        variant={c.status === "published" ? "green" : "gray"}
                      >
                        {c.status === "published" ? "Опубликован" : "Черновик"}
                      </StatusBadge>
                    </td>
                    <td className="px-5 py-3">
                      <button
                        onClick={() => handleDelete(c.id)}
                        className="p-1.5 rounded hover:bg-red-500/10 text-zinc-500 hover:text-red-400 transition-colors cursor-pointer"
                        title="Удалить"
                      >
                        <Trash2 size={15} />
                      </button>
                    </td>
                  </tr>
                ))}
                {filtered.length === 0 && (
                  <tr>
                    <td
                      colSpan={7}
                      className="px-5 py-8 text-center text-zinc-500"
                    >
                      Курсы не найдены
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </PageTransition>
  );
}
