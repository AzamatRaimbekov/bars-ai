import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { BookOpen, Clock, Flame, Trophy, Sparkles, ArrowRight } from 'lucide-react'
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
  const totalNodes = 25
  const completedNodes = profile.completedNodes.length
  const progressPercent = Math.round((completedNodes / totalNodes) * 100)

  const stats = [
    { icon: BookOpen, label: t('dashboard.stats.lessons'), value: profile.completedLessons.length, color: '#6C63FF' },
    { icon: Clock, label: t('dashboard.stats.hours'), value: Math.round(profile.completedLessons.length * 0.5), color: '#00D9FF' },
    { icon: Flame, label: t('dashboard.stats.streak'), value: `${profile.streak} ${t('common.days')}`, color: '#FFB800' },
    { icon: Trophy, label: t('dashboard.stats.badges'), value: profile.earnedBadges.length, color: '#00FF94' },
  ]

  return (
    <PageWrapper>
      <motion.div variants={containerVariants} initial="hidden" animate="show" className="max-w-5xl mx-auto space-y-6">
        <motion.div variants={itemVariants}>
          <Card glow={dirConfig?.color} className="flex items-center gap-6">
            <ProgressRing value={progressPercent} color={dirConfig?.color} size={100} strokeWidth={8}>
              <span className="text-lg font-bold">{progressPercent}%</span>
            </ProgressRing>
            <div className="flex-1">
              <p className="text-xs text-text-secondary uppercase tracking-wider mb-1">{t('dashboard.continueLearning')}</p>
              <h3 className="text-lg font-semibold mb-1">{t(`direction.${profile.direction}.name` as any)}</h3>
              <p className="text-sm text-text-secondary mb-3">
                {completedNodes} / {totalNodes} {t('dashboard.topicsCompleted')}
              </p>
              <Button size="sm" onClick={() => navigate('/roadmap')}>
                {t('common.continue')} <ArrowRight size={14} />
              </Button>
            </div>
          </Card>
        </motion.div>

        <motion.div variants={itemVariants} className="grid grid-cols-4 gap-4">
          {stats.map((stat) => (
            <Card key={stat.label} className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl flex items-center justify-center" style={{ backgroundColor: `${stat.color}15` }}>
                <stat.icon size={18} style={{ color: stat.color }} />
              </div>
              <div>
                <p className="text-lg font-bold">{stat.value}</p>
                <p className="text-xs text-text-secondary">{stat.label}</p>
              </div>
            </Card>
          ))}
        </motion.div>

        <motion.div variants={itemVariants}>
          <Card glow="#00D9FF" className="flex items-start gap-4">
            <div className="w-10 h-10 rounded-xl bg-accent/10 flex items-center justify-center shrink-0">
              <Sparkles size={18} className="text-accent" />
            </div>
            <div>
              <p className="text-xs text-accent uppercase tracking-wider mb-1">{t('dashboard.aiTip')}</p>
              <p className="text-sm text-text-secondary leading-relaxed">
                {tip || t('dashboard.tipLoading')}
              </p>
            </div>
          </Card>
        </motion.div>

        <motion.div variants={itemVariants} className="grid grid-cols-3 gap-4">
          <Card hover onClick={() => navigate('/mentor')} className="text-center cursor-pointer">
            <p className="text-2xl mb-2">{dirConfig?.mentor.avatar}</p>
            <p className="text-sm font-medium">{t('dashboard.chatWith', { name: dirConfig?.mentor.name })}</p>
            <p className="text-xs text-text-secondary mt-1">{t('dashboard.aiMentor')}</p>
          </Card>
          <Card hover onClick={() => navigate('/simulator')} className="text-center cursor-pointer">
            <p className="text-2xl mb-2">🎙️</p>
            <p className="text-sm font-medium">{t('dashboard.practiceInterview')}</p>
            <p className="text-xs text-text-secondary mt-1">{t('dashboard.simulator')}</p>
          </Card>
          <Card hover onClick={() => navigate('/achievements')} className="text-center cursor-pointer">
            <p className="text-2xl mb-2">🏆</p>
            <p className="text-sm font-medium">{t('dashboard.viewAchievements')}</p>
            <p className="text-xs text-text-secondary mt-1">{profile.earnedBadges.length} {t('dashboard.badgesEarned')}</p>
          </Card>
        </motion.div>
      </motion.div>
    </PageWrapper>
  )
}
