import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { BookOpen, Clock, Flame, Trophy, Sparkles, ArrowRight, Bot, Mic, Award } from 'lucide-react'
import { DailyQuests } from '@/components/gamification/DailyQuests'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { ProgressRing } from '@/components/ui/ProgressRing'
import { useUserStore } from '@/store/userStore'
import { DIRECTIONS } from '@/data/directions'
import { generateTip } from '@/services/claudeApi'
import { useTranslation } from '@/hooks/useTranslation'

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.1 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function Dashboard() {
  const profile = useUserStore((s) => s.profile)
  const updateStreak = useUserStore((s) => s.updateStreak)
  const navigate = useNavigate()
  const { t } = useTranslation()
  const [tip, setTip] = useState<string>('')

  useEffect(() => {
    updateStreak()
  }, [])

  useEffect(() => {
    if (!profile) return
    generateTip(DIRECTIONS[profile.direction]?.name ?? profile.direction, profile.assessmentLevel)
      .then(setTip)
      .catch(() => setTip(t('dashboard.tipFallback')))
  }, [profile?.direction])

  if (!profile) return null

  const dirConfig = DIRECTIONS[profile.direction]
  if (!dirConfig) return null
  const totalNodes = 25
  const completedNodes = profile.completedNodes.length
  const progressPercent = Math.round((completedNodes / totalNodes) * 100)

  const stats = [
    { icon: BookOpen, label: t('dashboard.stats.lessons'), value: profile.completedLessons.length, color: '#F97316' },
    { icon: Clock, label: t('dashboard.stats.hours'), value: Math.round(profile.completedLessons.length * 0.5), color: '#FB923C' },
    { icon: Flame, label: t('dashboard.stats.streak'), value: `${profile.streak} ${t('common.days')}`, color: '#FFB800' },
    { icon: Trophy, label: t('dashboard.stats.badges'), value: profile.earnedBadges.length, color: '#F97316' },
  ]

  return (
    <PageWrapper>
      <motion.div variants={containerVariants} initial="hidden" animate="show" className="max-w-5xl mx-auto space-y-4 lg:space-y-6">

        {/* ── Continue Learning Card ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 flex items-center gap-4 lg:gap-6 relative overflow-hidden hover:border-white/12 transition-colors">
            {/* Subtle orange glow */}
            <div className="absolute inset-0 opacity-[0.04] pointer-events-none"
              style={{ background: 'radial-gradient(ellipse at 10% 50%, #F97316 0%, transparent 60%)' }} />
            <ProgressRing value={progressPercent} color="#F97316" size={80} strokeWidth={7}>
              <span className="text-base lg:text-lg font-bold">{progressPercent}%</span>
            </ProgressRing>
            <div className="flex-1 min-w-0 relative">
              <p className="text-xs text-white/40 uppercase tracking-wider mb-1">{t('dashboard.continueLearning')}</p>
              <h3 className="text-base lg:text-lg font-semibold mb-1 truncate text-white">{t(`direction.${profile.direction}.name` as any)}</h3>
              <p className="text-sm text-white/40 mb-3">
                {completedNodes} / {totalNodes} {t('dashboard.topicsCompleted')}
              </p>
              <Button size="sm" onClick={() => navigate('/roadmap')}>
                {t('common.continue')} <ArrowRight size={14} />
              </Button>
            </div>
            {/* Progress bar along bottom */}
            <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-white/5">
              <div
                className="h-full rounded-full"
                style={{
                  width: `${progressPercent}%`,
                  background: 'linear-gradient(90deg, #F97316, #FB923C)',
                }}
              />
            </div>
          </div>
        </motion.div>

        {/* ── Stats Grid ── */}
        <motion.div variants={itemVariants} className="grid grid-cols-2 lg:grid-cols-4 gap-3 lg:gap-4">
          {stats.map((stat) => (
            <div
              key={stat.label}
              className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-4 flex items-center gap-3 hover:border-white/12 transition-colors"
            >
              <div
                className="w-9 h-9 lg:w-10 lg:h-10 rounded-xl flex items-center justify-center shrink-0"
                style={{ backgroundColor: `${stat.color}18` }}
              >
                <stat.icon size={17} style={{ color: stat.color }} />
              </div>
              <div className="min-w-0">
                <p className="text-base lg:text-lg font-bold truncate text-white">{stat.value}</p>
                <p className="text-[11px] lg:text-xs text-white/40 truncate">{stat.label}</p>
              </div>
            </div>
          ))}
        </motion.div>

        {/* ── AI Tip Card ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 flex items-start gap-4 lg:gap-5 hover:border-white/12 transition-colors">
            <div className="w-10 h-10 rounded-xl bg-[#F97316]/10 flex items-center justify-center shrink-0 mt-0.5">
              <Sparkles size={18} className="text-[#F97316]" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-xs text-[#F97316] uppercase tracking-wider mb-1.5 font-medium">
                {t('dashboard.aiTip')}
              </p>
              <p className="text-sm text-white/50 leading-relaxed line-clamp-3">
                {tip || t('dashboard.tipLoading')}
              </p>
            </div>
          </div>
        </motion.div>

        {/* ── Daily Quests ── */}
        <motion.div variants={itemVariants}>
          <DailyQuests />
        </motion.div>

        {/* ── Quick Actions ── */}
        <motion.div variants={itemVariants} className="grid grid-cols-1 sm:grid-cols-3 gap-3 lg:gap-4">
          <button
            onClick={() => navigate('/mentor')}
            className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 lg:p-6 text-center hover:border-white/12 hover:bg-white/[0.02] transition-all cursor-pointer group"
          >
            <div className="w-12 h-12 rounded-2xl bg-[#F97316]/10 flex items-center justify-center mx-auto mb-3 group-hover:bg-[#F97316]/15 transition-colors">
              <Bot size={22} className="text-[#F97316]" />
            </div>
            <p className="text-sm font-medium text-white">{t('dashboard.chatWith', { name: dirConfig?.mentor.name })}</p>
            <p className="text-xs text-white/40 mt-1">{t('dashboard.aiMentor')}</p>
          </button>

          <button
            onClick={() => navigate('/simulator')}
            className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 lg:p-6 text-center hover:border-white/12 hover:bg-white/[0.02] transition-all cursor-pointer group"
          >
            <div className="w-12 h-12 rounded-2xl bg-[#FB923C]/10 flex items-center justify-center mx-auto mb-3 group-hover:bg-[#FB923C]/15 transition-colors">
              <Mic size={22} className="text-[#FB923C]" />
            </div>
            <p className="text-sm font-medium text-white">{t('dashboard.practiceInterview')}</p>
            <p className="text-xs text-white/40 mt-1">{t('dashboard.simulator')}</p>
          </button>

          <button
            onClick={() => navigate('/achievements')}
            className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 lg:p-6 text-center hover:border-white/12 hover:bg-white/[0.02] transition-all cursor-pointer group"
          >
            <div className="w-12 h-12 rounded-2xl bg-[#F97316]/10 flex items-center justify-center mx-auto mb-3 group-hover:bg-[#F97316]/15 transition-colors">
              <Award size={22} className="text-[#F97316]" />
            </div>
            <p className="text-sm font-medium text-white">{t('dashboard.viewAchievements')}</p>
            <p className="text-xs text-white/40 mt-1">{profile.earnedBadges.length} {t('dashboard.badgesEarned')}</p>
          </button>
        </motion.div>

      </motion.div>
    </PageWrapper>
  )
}
