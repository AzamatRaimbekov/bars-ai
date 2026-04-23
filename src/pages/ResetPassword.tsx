import { useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Lock, Loader2, CheckCircle } from 'lucide-react'
import { Input } from '@/components/ui/Input'
import { useTranslation } from '@/hooks/useTranslation'

export default function ResetPassword() {
  const { t } = useTranslation()
  const [searchParams] = useSearchParams()
  const token = searchParams.get('token') || ''
  const [password, setPassword] = useState('')
  const [confirm, setConfirm] = useState('')
  const [error, setError] = useState('')
  const [success, setSuccess] = useState(false)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    if (password !== confirm) {
      setError(t('auth.passwordMismatch'))
      return
    }
    setLoading(true)
    try {
      const resp = await fetch('/api/auth/reset-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token, new_password: password }),
      })
      if (!resp.ok) {
        const data = await resp.json().catch(() => ({}))
        throw new Error(data.detail || 'Error')
      }
      setSuccess(true)
    } catch (err: any) {
      setError(err.message?.includes('expired') || err.message?.includes('Invalid')
        ? t('auth.invalidToken')
        : err.message || 'Error')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-black flex items-center justify-center p-4 relative overflow-hidden">
      <div
        className="absolute pointer-events-none"
        style={{
          width: 600, height: 600,
          background: 'radial-gradient(circle, rgba(249,115,22,0.06), transparent 70%)',
          transform: 'translate(-50%, -50%)', left: '50%', top: '50%',
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md relative z-10"
      >
        <div className="text-center mb-8">
          <motion.h1
            className="text-3xl font-bold tracking-tight text-white"
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
          >
            Bars<span className="text-[#F97316]"> AI</span>
          </motion.h1>
          <p className="text-white/40 mt-2 text-sm">{t('auth.resetPassword')}</p>
        </div>

        <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-6">
          {success ? (
            <div className="text-center space-y-4">
              <div className="w-12 h-12 rounded-full bg-green-500/10 flex items-center justify-center mx-auto">
                <CheckCircle size={20} className="text-green-400" />
              </div>
              <p className="text-sm text-white/60">{t('auth.passwordReset')}</p>
              <Link
                to="/login"
                className="inline-flex items-center gap-2 px-6 py-2.5 rounded-xl font-semibold text-sm text-white transition-opacity"
                style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
              >
                {t('auth.signIn')}
              </Link>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <Input
                label={t('auth.newPassword')}
                type="password"
                placeholder={t('auth.passwordPlaceholder')}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                minLength={8}
              />
              <Input
                label={t('auth.confirmPassword')}
                type="password"
                placeholder="••••••••"
                value={confirm}
                onChange={(e) => setConfirm(e.target.value)}
                required
                minLength={8}
              />

              {error && <p className="text-red-400 text-sm">{error}</p>}

              <button
                type="submit"
                disabled={loading}
                className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-sm text-white transition-opacity disabled:opacity-50"
                style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
              >
                {loading ? <Loader2 className="animate-spin" size={18} /> : <Lock size={18} />}
                {t('auth.resetPassword')}
              </button>
            </form>
          )}
        </div>
      </motion.div>
    </div>
  )
}
