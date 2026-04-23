import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  BookOpen, Clock, Flame, Trophy, Star, Target, Zap,
  LogOut, ChevronRight, Globe, Award, TrendingUp, Shield, Lock,
} from 'lucide-react'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { ProgressBar } from '@/components/ui/ProgressBar'
import { ProgressRing } from '@/components/ui/ProgressRing'
import { apiFetch } from '@/services/api'
import { useUserStore } from '@/store/userStore'
import { useAuthStore } from '@/store/authStore'
import { DIRECTIONS } from '@/data/directions'
import { LEVEL_THRESHOLDS, LEVELS_ORDERED } from '@/lib/constants'
import { useTranslation } from '@/hooks/useTranslation'
import { frontendRoadmap } from '@/data/roadmaps/frontend'
import type { Level } from '@/types'

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  show: { opacity: 1, y: 0 },
}

const LEVEL_ICONS: Record<Level, typeof Star> = {
  Novice: Shield,
  Apprentice: Target,
  Practitioner: Zap,
  Expert: Award,
  Master: TrendingUp,
  Legend: Star,
}

// Updated level colors: orange-warm palette replacing purple/cyan
const LEVEL_COLORS: Record<Level, string> = {
  Novice: '#888899',
  Apprentice: '#F97316',
  Practitioner: '#FB923C',
  Expert: '#FFB800',
  Master: '#FF6B6B',
  Legend: '#FFD700',
}

export default function Profile() {
  const profile = useUserStore((s) => s.profile)
  const logout = useAuthStore((s) => s.logout)
  const navigate = useNavigate()
  const { t, lang, changeLanguage } = useTranslation()

  const [showPasswordForm, setShowPasswordForm] = useState(false)
  const [currentPw, setCurrentPw] = useState('')
  const [newPw, setNewPw] = useState('')
  const [confirmPw, setConfirmPw] = useState('')
  const [pwError, setPwError] = useState('')
  const [pwSuccess, setPwSuccess] = useState(false)
  const [pwLoading, setPwLoading] = useState(false)

  if (!profile) return null

  const dirConfig = DIRECTIONS[profile.direction]
  const validLevel = LEVELS_ORDERED.includes(profile.level) ? profile.level : 'Legend' as Level
  const currentIdx = LEVELS_ORDERED.indexOf(validLevel)
  const nextLevel = LEVELS_ORDERED[currentIdx + 1]
  const currentThreshold = LEVEL_THRESHOLDS[validLevel] ?? 0
  const nextThreshold = nextLevel ? LEVEL_THRESHOLDS[nextLevel] : currentThreshold
  const xpInLevel = profile.xp - currentThreshold
  const xpNeeded = nextThreshold - currentThreshold || 1
  const xpProgress = Math.round((xpInLevel / xpNeeded) * 100)

  const totalNodes = 25
  const completedNodes = profile.completedNodes.length
  const roadmapProgress = Math.round((completedNodes / totalNodes) * 100)

  // Determine which tier user is in based on completed nodes
  const tier = completedNodes >= 20 ? 'Senior' : completedNodes >= 9 ? 'Middle' : 'Junior'
  const tierColor = tier === 'Senior' ? '#FF6B6B' : tier === 'Middle' ? '#FFB800' : '#F97316'

  const LevelIcon = LEVEL_ICONS[validLevel] ?? Star
  const levelColor = LEVEL_COLORS[validLevel] ?? '#FFD700'

  const handleLogout = async () => {
    if (window.confirm(t('profile.resetConfirm'))) {
      await logout()
      navigate('/login')
    }
  }

  const handleChangePassword = async () => {
    setPwError('')
    setPwSuccess(false)
    if (newPw.length < 8) { setPwError(t('profile.newPassword') + ' — min 8'); return }
    if (newPw !== confirmPw) { setPwError(t('profile.passwordMismatch')); return }
    setPwLoading(true)
    try {
      await apiFetch('/users/me/password', {
        method: 'POST',
        body: JSON.stringify({ current_password: currentPw, new_password: newPw }),
      })
      setPwSuccess(true)
      setCurrentPw('')
      setNewPw('')
      setConfirmPw('')
      setShowPasswordForm(false)
    } catch (err: any) {
      setPwError(err.message?.includes('Wrong') ? t('profile.wrongPassword') : (err.message || 'Error'))
    } finally {
      setPwLoading(false)
    }
  }

  const stats = [
    { icon: BookOpen, label: t('profile.lessonsCompleted'), value: profile.completedLessons.length, color: '#F97316' },
    { icon: Target, label: t('profile.topicsCompleted'), value: `${completedNodes}/${totalNodes}`, color: '#FB923C' },
    { icon: Clock, label: t('profile.hours'), value: Math.round(profile.completedLessons.length * 0.4), color: '#F97316' },
    { icon: Flame, label: t('profile.currentStreak'), value: `${profile.streak} ${t('common.days')}`, color: '#FFB800' },
    { icon: Trophy, label: t('profile.badgesEarned'), value: profile.earnedBadges.length, color: '#FB923C' },
    { icon: Zap, label: 'XP', value: profile.xp, color: '#FFD700' },
  ]

  return (
    <PageWrapper>
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="show"
        className="max-w-2xl mx-auto space-y-5"
      >
        {/* ── Hero Card ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 relative overflow-hidden">
            {/* Subtle orange glow */}
            <div
              className="absolute inset-0 opacity-[0.06] pointer-events-none"
              style={{ background: 'radial-gradient(ellipse at 80% 20%, #F97316 0%, transparent 60%)' }}
            />
            <div className="relative flex items-center gap-5">
              {/* Avatar with XP progress ring */}
              <div className="relative">
                <ProgressRing value={xpProgress} color="#F97316" size={96} strokeWidth={5}>
                  <div
                    className="w-16 h-16 rounded-full flex items-center justify-center text-2xl font-bold border-2 border-[#F97316]/30"
                    style={{ background: '#F9731618', color: '#F97316' }}
                  >
                    {profile.name.charAt(0).toUpperCase()}
                  </div>
                </ProgressRing>
                <motion.div
                  className="absolute -bottom-1 -right-1 w-8 h-8 rounded-full flex items-center justify-center border-2 border-[#0A0A0A]"
                  style={{ background: levelColor }}
                  animate={{ scale: [1, 1.1, 1] }}
                  transition={{ repeat: Infinity, duration: 2 }}
                >
                  <LevelIcon size={14} className="text-white" />
                </motion.div>
              </div>

              <div className="flex-1 min-w-0">
                <h2 className="text-xl font-bold truncate text-white">{profile.name}</h2>
                <p className="text-sm text-white/40 mt-0.5">
                  {t(`direction.${profile.direction}.name` as any)}
                </p>
                <div className="flex items-center gap-2 mt-2 flex-wrap">
                  <span
                    className="text-xs px-3 py-1 rounded-full font-bold"
                    style={{ background: `${levelColor}18`, color: levelColor }}
                  >
                    {t(`level.${profile.level}` as any)}
                  </span>
                  <span
                    className="text-xs px-3 py-1 rounded-full font-bold"
                    style={{ background: `${tierColor}18`, color: tierColor }}
                  >
                    {tier}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </motion.div>

        {/* ── XP Progress ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Zap size={16} className="text-[#F97316]" />
                <span className="text-sm font-semibold text-white">{t(`level.${profile.level}` as any)}</span>
              </div>
              <span className="text-xs text-white/40">
                {xpInLevel} / {xpNeeded} XP
              </span>
            </div>
            <ProgressBar value={xpInLevel} max={xpNeeded} color="#F97316" />
            {nextLevel && (
              <p className="text-xs text-white/40 mt-2 text-center">
                {xpNeeded - xpInLevel} {t('profile.xpToNext')}{' '}
                <span style={{ color: LEVEL_COLORS[nextLevel] }} className="font-semibold">
                  {t(`level.${nextLevel}` as any)}
                </span>
              </p>
            )}
          </div>
        </motion.div>

        {/* ── Roadmap Progress ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5">
            <div className="flex items-center justify-between mb-3">
              <span className="text-sm font-semibold text-white">{t('profile.courseProgress')}</span>
              <span className="text-xs font-bold text-[#F97316]">
                {roadmapProgress}%
              </span>
            </div>
            <ProgressBar value={completedNodes} max={totalNodes} color="#F97316" />
            <div className="flex justify-between mt-3 text-[11px] text-white/40">
              <span className={completedNodes >= 0 ? 'text-[#F97316] font-semibold' : ''}>Junior</span>
              <span className={completedNodes >= 9 ? 'text-[#FFB800] font-semibold' : ''}>Middle</span>
              <span className={completedNodes >= 20 ? 'text-[#FF6B6B] font-semibold' : ''}>Senior</span>
            </div>
            {/* Segmented progress dots */}
            <div className="flex mt-1 gap-0.5">
              {Array.from({ length: totalNodes }, (_, i) => (
                <div
                  key={i}
                  className="h-1.5 flex-1 rounded-full transition-colors"
                  style={{
                    backgroundColor: i < completedNodes
                      ? (i < 9 ? '#F97316' : i < 20 ? '#FFB800' : '#FF6B6B')
                      : '#ffffff0a',
                  }}
                />
              ))}
            </div>
          </div>
        </motion.div>

        {/* ── Stats Grid ── */}
        <motion.div variants={itemVariants} className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          {stats.map((stat) => (
            <div
              key={stat.label}
              className="bg-[#0A0A0A] border border-white/6 rounded-2xl py-4 px-4 hover:border-white/12 transition-colors"
            >
              <div className="flex items-center gap-2.5">
                <div
                  className="w-9 h-9 rounded-xl flex items-center justify-center shrink-0"
                  style={{ backgroundColor: `${stat.color}18` }}
                >
                  <stat.icon size={16} style={{ color: stat.color }} />
                </div>
                <div className="min-w-0">
                  <p className="text-lg font-bold leading-tight text-white">{stat.value}</p>
                  <p className="text-[10px] text-white/40 truncate">{stat.label}</p>
                </div>
              </div>
            </div>
          ))}
        </motion.div>

        {/* ── Level Journey ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5">
            <p className="text-xs text-white/40 uppercase tracking-wider mb-4">
              {t('profile.levelJourney')}
            </p>
            <div className="flex items-center gap-1">
              {LEVELS_ORDERED.map((level, i) => {
                const isReached = i <= currentIdx
                const isCurrent = i === currentIdx
                const Icon = LEVEL_ICONS[level]
                const color = LEVEL_COLORS[level]
                return (
                  <div key={level} className="flex items-center flex-1">
                    <motion.div
                      className="flex flex-col items-center gap-1 flex-1"
                      animate={isCurrent ? { scale: [1, 1.05, 1] } : {}}
                      transition={{ repeat: Infinity, duration: 2 }}
                    >
                      <div
                        className="w-8 h-8 lg:w-10 lg:h-10 rounded-full flex items-center justify-center border-2 transition-all"
                        style={{
                          backgroundColor: isReached ? `${color}18` : '#ffffff05',
                          borderColor: isReached ? color : '#ffffff10',
                          boxShadow: isCurrent ? `0 0 16px ${color}40` : 'none',
                        }}
                      >
                        <Icon size={14} style={{ color: isReached ? color : '#ffffff30' }} />
                      </div>
                      <span
                        className="text-[9px] lg:text-[10px] font-medium text-center leading-tight"
                        style={{ color: isReached ? color : '#ffffff30' }}
                      >
                        {t(`level.${level}` as any)}
                      </span>
                    </motion.div>
                    {i < LEVELS_ORDERED.length - 1 && (
                      <ChevronRight size={12} className="text-white/10 shrink-0 mx-0.5" />
                    )}
                  </div>
                )
              })}
            </div>
          </div>
        </motion.div>

        {/* ── Language ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Globe size={16} className="text-white/40" />
                <span className="text-sm font-medium text-white">{t('profile.language')}</span>
              </div>
              <div className="flex gap-2">
                <Button
                  size="sm"
                  variant={lang === 'en' ? 'primary' : 'ghost'}
                  onClick={() => changeLanguage('en')}
                >
                  EN
                </Button>
                <Button
                  size="sm"
                  variant={lang === 'ru' ? 'primary' : 'ghost'}
                  onClick={() => changeLanguage('ru')}
                >
                  RU
                </Button>
              </div>
            </div>
          </div>
        </motion.div>

        {/* ── Security ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5">
            <button
              onClick={() => { setShowPasswordForm(!showPasswordForm); setPwError(''); setPwSuccess(false) }}
              className="flex items-center justify-between w-full"
            >
              <div className="flex items-center gap-2">
                <Lock size={16} className="text-white/40" />
                <span className="text-sm font-medium text-white">{t('profile.security')}</span>
              </div>
              <ChevronRight
                size={16}
                className={`text-white/30 transition-transform ${showPasswordForm ? 'rotate-90' : ''}`}
              />
            </button>

            {showPasswordForm && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                className="mt-4 space-y-3"
              >
                <input
                  type="password"
                  placeholder={t('profile.currentPassword')}
                  value={currentPw}
                  onChange={(e) => setCurrentPw(e.target.value)}
                  className="w-full bg-transparent border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white outline-none focus:border-[#F97316]/50 placeholder:text-white/30"
                />
                <input
                  type="password"
                  placeholder={t('profile.newPassword')}
                  value={newPw}
                  onChange={(e) => setNewPw(e.target.value)}
                  className="w-full bg-transparent border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white outline-none focus:border-[#F97316]/50 placeholder:text-white/30"
                />
                <input
                  type="password"
                  placeholder={t('profile.confirmPassword')}
                  value={confirmPw}
                  onChange={(e) => setConfirmPw(e.target.value)}
                  className="w-full bg-transparent border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white outline-none focus:border-[#F97316]/50 placeholder:text-white/30"
                />

                {pwError && <p className="text-red-400 text-xs">{pwError}</p>}
                {pwSuccess && <p className="text-green-400 text-xs">{t('profile.passwordChanged')}</p>}

                <button
                  onClick={handleChangePassword}
                  disabled={pwLoading || !currentPw || !newPw || !confirmPw}
                  className="w-full py-2.5 rounded-xl font-semibold text-sm text-white disabled:opacity-40 transition-opacity"
                  style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
                >
                  {pwLoading ? '...' : t('profile.changePassword')}
                </button>
              </motion.div>
            )}
          </div>
        </motion.div>

        {/* ── Logout ── */}
        <motion.div variants={itemVariants}>
          <button
            onClick={handleLogout}
            className="w-full flex items-center justify-center gap-2 py-3 rounded-xl text-sm text-red-400/60 hover:text-red-400 hover:bg-red-500/8 transition-all cursor-pointer border border-transparent hover:border-red-500/10"
          >
            <LogOut size={16} />
            {t('profile.logout')}
          </button>
        </motion.div>
      </motion.div>
    </PageWrapper>
  )
}
