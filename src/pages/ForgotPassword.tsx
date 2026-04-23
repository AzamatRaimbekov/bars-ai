import { useState } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Mail, ArrowLeft, Loader2 } from 'lucide-react'
import { Input } from '@/components/ui/Input'
import { useTranslation } from '@/hooks/useTranslation'

export default function ForgotPassword() {
  const { t } = useTranslation()
  const [email, setEmail] = useState('')
  const [sent, setSent] = useState(false)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      await fetch('/api/auth/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      })
      setSent(true)
    } catch {
      setSent(true) // show success anyway (don't reveal if email exists)
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
          {sent ? (
            <div className="text-center space-y-4">
              <div className="w-12 h-12 rounded-full bg-green-500/10 flex items-center justify-center mx-auto">
                <Mail size={20} className="text-green-400" />
              </div>
              <p className="text-sm text-white/60">{t('auth.resetSent')}</p>
              <Link
                to="/login"
                className="inline-flex items-center gap-1 text-sm text-[#FB923C] hover:text-[#F97316] transition-colors"
              >
                <ArrowLeft size={14} /> {t('auth.backToLogin')}
              </Link>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <Input
                label={t('auth.email')}
                type="email"
                placeholder={t('auth.emailPlaceholder')}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
              <button
                type="submit"
                disabled={loading}
                className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-sm text-white transition-opacity disabled:opacity-50"
                style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
              >
                {loading ? <Loader2 className="animate-spin" size={18} /> : <Mail size={18} />}
                {t('auth.sendResetLink')}
              </button>
              <p className="text-center">
                <Link to="/login" className="text-sm text-white/30 hover:text-[#FB923C] transition-colors">
                  {t('auth.backToLogin')}
                </Link>
              </p>
            </form>
          )}
        </div>
      </motion.div>
    </div>
  )
}
