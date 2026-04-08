import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { ProgressRing } from '@/components/ui/ProgressRing'
import { useUserStore } from '@/store/userStore'
import { useAuthStore } from '@/store/authStore'
import { DIRECTIONS } from '@/data/directions'
import { LEVEL_THRESHOLDS, LEVELS_ORDERED } from '@/lib/constants'
import { useTranslation } from '@/hooks/useTranslation'

export default function Profile() {
  const profile = useUserStore((s) => s.profile)
  const logout = useAuthStore((s) => s.logout)
  const navigate = useNavigate()
  const { t, lang, changeLanguage } = useTranslation()

  if (!profile) return null

  const dirConfig = DIRECTIONS[profile.direction]
  const currentIdx = LEVELS_ORDERED.indexOf(profile.level)
  const nextLevel = LEVELS_ORDERED[currentIdx + 1]
  const currentThreshold = LEVEL_THRESHOLDS[profile.level]
  const nextThreshold = nextLevel ? LEVEL_THRESHOLDS[nextLevel] : currentThreshold
  const xpProgress = ((profile.xp - currentThreshold) / (nextThreshold - currentThreshold || 1)) * 100

  const handleLogout = async () => {
    if (window.confirm(t('profile.resetConfirm'))) {
      await logout()
      navigate('/login')
    }
  }

  return (
    <PageWrapper>
      <div className="max-w-2xl mx-auto space-y-6">
        <Card glow={dirConfig?.color} className="flex items-center gap-6">
          <ProgressRing value={xpProgress} color={dirConfig?.color} size={100} strokeWidth={6}>
            <span className="text-3xl">{dirConfig?.mentor.avatar}</span>
          </ProgressRing>
          <div>
            <h2 className="text-xl font-bold">{profile.name}</h2>
            <p className="text-sm text-text-secondary">{t(`direction.${profile.direction}.name` as any)}</p>
            <div className="flex items-center gap-3 mt-2">
              <span className="text-xs px-3 py-1 rounded-full bg-primary/10 text-primary font-semibold">
                {t(`level.${profile.level}` as any)}
              </span>
              <span className="text-xs text-text-secondary">{profile.xp} XP</span>
            </div>
          </div>
        </Card>

        <div className="grid grid-cols-2 gap-4">
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t('profile.assessmentLevel')}</p>
            <p className="font-semibold capitalize">{profile.assessmentLevel}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t('profile.currentStreak')}</p>
            <p className="font-semibold">{profile.streak} {t('common.days')}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t('profile.lessonsCompleted')}</p>
            <p className="font-semibold">{profile.completedLessons.length}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t('profile.topicsCompleted')}</p>
            <p className="font-semibold">{profile.completedNodes.length}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t('profile.badgesEarned')}</p>
            <p className="font-semibold">{profile.earnedBadges.length}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t('profile.nextLevel')}</p>
            <p className="font-semibold">{nextLevel ? t(`level.${nextLevel}` as any) : t('profile.maxLevel')}</p>
          </Card>
        </div>

        <Card>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-3">{t('profile.language')}</p>
          <div className="flex gap-2">
            <Button
              size="sm"
              variant={lang === 'en' ? 'primary' : 'ghost'}
              onClick={() => changeLanguage('en')}
            >
              English
            </Button>
            <Button
              size="sm"
              variant={lang === 'ru' ? 'primary' : 'ghost'}
              onClick={() => changeLanguage('ru')}
            >
              Русский
            </Button>
          </div>
        </Card>

        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.3 }}>
          <Button variant="ghost" onClick={handleLogout} className="text-red-400 hover:text-red-300">
            {t('profile.reset')}
          </Button>
        </motion.div>
      </div>
    </PageWrapper>
  )
}
