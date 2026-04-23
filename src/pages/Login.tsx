import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { LogIn, Loader2 } from "lucide-react";
import { Input } from "@/components/ui/Input";
import { useAuthStore } from "@/store/authStore";
import { useTranslation } from "@/hooks/useTranslation";

export default function Login() {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const login = useAuthStore((s) => s.login);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.message || t("auth.loginFailed"));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-black flex items-center justify-center p-4 relative overflow-hidden">
      {/* Subtle radial glow behind card */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 600,
          height: 600,
          background: "radial-gradient(circle, rgba(249,115,22,0.06), transparent 70%)",
          transform: "translate(-50%, -50%)",
          left: "50%",
          top: "50%",
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md relative z-10"
      >
        {/* Brand */}
        <div className="text-center mb-8">
          <motion.h1
            className="text-3xl font-bold tracking-tight text-white"
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
          >
            Bars<span className="text-[#F97316]"> AI</span>
          </motion.h1>
          <p className="text-white/40 mt-2 text-sm">{t("auth.signInSubtitle")}</p>
        </div>

        {/* Form card */}
        <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-6">
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input
              label={t("auth.email")}
              type="email"
              placeholder={t("auth.emailPlaceholder")}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <Input
              label={t("auth.password")}
              type="password"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />

            {error && (
              <p className="text-red-400 text-sm">{error}</p>
            )}

            <div className="text-right">
              <Link to="/forgot-password" className="text-xs text-white/30 hover:text-[#FB923C] transition-colors">
                {t("auth.forgotPassword")}
              </Link>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-sm text-white transition-opacity disabled:opacity-50"
              style={{ background: "linear-gradient(135deg, #F97316, #FB923C)" }}
            >
              {loading ? <Loader2 className="animate-spin" size={18} /> : <LogIn size={18} />}
              {t("auth.signIn")}
            </button>
          </form>

          <p className="text-center text-white/40 text-sm mt-5">
            {t("auth.noAccount")}{" "}
            <Link to="/register" className="text-[#FB923C] hover:text-[#F97316] transition-colors">
              {t("auth.signUp")}
            </Link>
          </p>
        </div>
      </motion.div>
    </div>
  );
}
