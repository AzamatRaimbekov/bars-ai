import { useEffect, useState } from "react";
import { Search, Users } from "lucide-react";
import { apiFetch } from "../lib/api";
import PageTransition from "../components/PageTransition";
import StatusBadge from "../components/StatusBadge";

interface User {
  id: string;
  email: string;
  name: string;
  role: string;
  direction: string;
  created_at: string;
  total_trophies: number;
}

export default function UsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);

  useEffect(() => {
    apiFetch<User[]>("/api/admin/users")
      .then(setUsers)
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const filtered = users.filter(
    (u) =>
      u.name?.toLowerCase().includes(search.toLowerCase()) ||
      u.email?.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <PageTransition>
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <Users size={20} className="text-blue-400" />
          <h1 className="text-xl font-bold text-white">
            Пользователи{" "}
            <span className="text-zinc-500 font-normal text-base">
              ({users.length})
            </span>
          </h1>
        </div>

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
                  <th className="px-5 py-3 font-medium">Имя</th>
                  <th className="px-5 py-3 font-medium">Email</th>
                  <th className="px-5 py-3 font-medium">Роль</th>
                  <th className="px-5 py-3 font-medium">Направление</th>
                  <th className="px-5 py-3 font-medium">Трофеи</th>
                  <th className="px-5 py-3 font-medium">Регистрация</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((u) => (
                  <tr
                    key={u.id}
                    onClick={() => setSelectedUser(u)}
                    className="border-t border-white/5 hover:bg-white/3 transition-colors cursor-pointer"
                  >
                    <td className="px-5 py-3 text-white font-medium">
                      {u.name || "—"}
                    </td>
                    <td className="px-5 py-3 text-zinc-300">{u.email}</td>
                    <td className="px-5 py-3">
                      <StatusBadge
                        variant={u.role === "admin" ? "purple" : "gray"}
                      >
                        {u.role}
                      </StatusBadge>
                    </td>
                    <td className="px-5 py-3 text-zinc-300">
                      {u.direction || "—"}
                    </td>
                    <td className="px-5 py-3 text-yellow-400">
                      {u.total_trophies}
                    </td>
                    <td className="px-5 py-3 text-zinc-400">
                      {new Date(u.created_at).toLocaleDateString("ru-RU")}
                    </td>
                  </tr>
                ))}
                {filtered.length === 0 && (
                  <tr>
                    <td
                      colSpan={6}
                      className="px-5 py-8 text-center text-zinc-500"
                    >
                      Пользователи не найдены
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* User detail modal */}
      {selectedUser && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
          onClick={() => setSelectedUser(null)}
        >
          <div
            className="bg-[var(--surface)] border border-white/8 rounded-xl p-6 w-full max-w-md"
            onClick={(e) => e.stopPropagation()}
          >
            <h2 className="text-lg font-bold text-white mb-4">
              Информация о пользователе
            </h2>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between">
                <span className="text-zinc-400">Имя</span>
                <span className="text-white">
                  {selectedUser.name || "—"}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-zinc-400">Email</span>
                <span className="text-white">{selectedUser.email}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-zinc-400">Роль</span>
                <StatusBadge
                  variant={selectedUser.role === "admin" ? "purple" : "gray"}
                >
                  {selectedUser.role}
                </StatusBadge>
              </div>
              <div className="flex justify-between">
                <span className="text-zinc-400">Направление</span>
                <span className="text-white">
                  {selectedUser.direction || "—"}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-zinc-400">Трофеи</span>
                <span className="text-yellow-400">
                  {selectedUser.total_trophies}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-zinc-400">Дата регистрации</span>
                <span className="text-white">
                  {new Date(selectedUser.created_at).toLocaleDateString(
                    "ru-RU"
                  )}
                </span>
              </div>
            </div>
            <button
              onClick={() => setSelectedUser(null)}
              className="mt-6 w-full py-2 bg-white/5 hover:bg-white/10 border border-white/8 rounded-lg text-sm text-zinc-300 transition-colors cursor-pointer"
            >
              Закрыть
            </button>
          </div>
        </div>
      )}
    </PageTransition>
  );
}
