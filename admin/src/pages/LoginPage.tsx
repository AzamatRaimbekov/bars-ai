import { useState, type FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { LogIn, AlertCircle } from "lucide-react";
import { useAuthStore } from "../store/authStore";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const login = useAuthStore((s) => s.login);
  const navigate = useNavigate();

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
      navigate("/", { replace: true });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Ошибка входа");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-[var(--bg)]">
      <div className="w-full max-w-sm">
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold text-white">
            Bars AI{" "}
            <span className="text-[var(--accent)]">Admin</span>
          </h1>
          <p className="text-sm text-zinc-500 mt-2">
            Войдите в панель управления
          </p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="bg-[var(--surface)] rounded-xl border border-white/8 p-6 space-y-4"
        >
          {error && (
            <div className="flex items-center gap-2 text-sm text-red-400 bg-red-500/10 border border-red-500/20 rounded-lg px-3 py-2">
              <AlertCircle size={16} />
              {error}
            </div>
          )}

          <div>
            <label className="block text-sm text-zinc-400 mb-1.5">
              Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[var(--accent)] transition-colors"
              placeholder="admin@bars.ai"
            />
          </div>

          <div>
            <label className="block text-sm text-zinc-400 mb-1.5">
              Пароль
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full px-3 py-2 bg-white/5 border border-white/8 rounded-lg text-sm text-white placeholder-zinc-600 focus:outline-none focus:border-[var(--accent)] transition-colors"
              placeholder="••••••••"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full flex items-center justify-center gap-2 px-4 py-2.5 bg-[var(--accent)] hover:bg-[var(--accent)]/90 disabled:opacity-50 text-white text-sm font-medium rounded-lg transition-colors cursor-pointer"
          >
            <LogIn size={16} />
            {loading ? "Вход..." : "Войти"}
          </button>
        </form>
      </div>
    </div>
  );
}
