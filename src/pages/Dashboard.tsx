import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { BookOpen, Flame, Trophy, Sparkles, ArrowRight, Bot, Mic, Award, Zap, GraduationCap, BarChart3 } from 'lucide-react'
import { DailyQuests } from '@/components/gamification/DailyQuests'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Button } from '@/components/ui/Button'
import { ProgressRing } from '@/components/ui/ProgressRing'
import { ProgressBar } from '@/components/ui/ProgressBar'
import { useUserStore } from '@/store/userStore'
import { DIRECTIONS } from '@/data/directions'
import { generateTip } from '@/services/claudeApi'
import { apiFetch } from '@/services/api'
import { SprintBanner } from '@/components/sprint/SprintBanner'
import { useTranslation } from '@/hooks/useTranslation'

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

interface CourseStats {
  course_id: string
  title: string
  thumbnail_url: string | null
  category: string
  total_lessons: number
  completed_lessons: number
  progress_percent: number
  xp_earned: number
}

interface DashboardStats {
  total_courses: number
  total_lessons: number
  total_completed: number
  total_xp: number
  overall_progress: number
  courses: CourseStats[]
}

export default function Dashboard() {
  const profile = useUserStore((s) => s.profile)
  const updateStreak = useUserStore((s) => s.updateStreak)
  const navigate = useNavigate()
  const { t, lang } = useTranslation()
  const [tip, setTip] = useState<string>('')
  const [stats, setStats] = useState<DashboardStats | null>(null)
  const [statsLoading, setStatsLoading] = useState(true)

  useEffect(() => {
    updateStreak()
  }, [])

  useEffect(() => {
    if (!profile) return
    generateTip(DIRECTIONS[profile.direction]?.name ?? profile.direction, profile.assessmentLevel)
      .then(setTip)
      .catch(() => setTip(t('dashboard.tipFallback')))
  }, [profile?.direction])

  // Load dashboard stats
  useEffect(() => {
    apiFetch<DashboardStats>('/courses/dashboard-stats')
      .then(setStats)
      .catch((err) => console.error('Failed to load dashboard stats:', err))
      .finally(() => setStatsLoading(false))
  }, [])

  if (!profile) return null

  const dirConfig = DIRECTIONS[profile.direction]
  if (!dirConfig) return null

  const topStats = [
    { icon: GraduationCap, label: lang === 'ru' ? 'Курсов' : 'Courses', value: stats?.total_courses ?? 0, color: '#F97316' },
    { icon: BookOpen, label: lang === 'ru' ? 'Уроков пройдено' : 'Lessons done', value: `${stats?.total_completed ?? 0}/${stats?.total_lessons ?? 0}`, color: '#FB923C' },
    { icon: Zap, label: 'XP', value: stats?.total_xp ?? profile.xp ?? 0, color: '#FFB800' },
    { icon: Flame, label: lang === 'ru' ? 'Дней подряд' : 'Day streak', value: profile.streak, color: '#F97316' },
  ]

  return (
    <PageWrapper>
      <motion.div variants={containerVariants} initial="hidden" animate="show" className="max-w-5xl mx-auto space-y-4 lg:space-y-6">

        {/* ── Overall Progress Card ── */}
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 flex items-center gap-4 lg:gap-6 relative overflow-hidden hover:border-white/12 transition-colors">
            <div className="absolute inset-0 opacity-[0.04] pointer-events-none"
              style={{ background: 'radial-gradient(ellipse at 10% 50%, #F97316 0%, transparent 60%)' }} />
            <ProgressRing value={stats?.overall_progress ?? 0} color="#F97316" size={80} strokeWidth={7}>
              <span className="text-base lg:text-lg font-bold">{stats?.overall_progress ?? 0}%</span>
            </ProgressRing>
            <div className="flex-1 min-w-0 relative">
              <p className="text-xs text-white/40 uppercase tracking-wider mb-1">
                {lang === 'ru' ? 'Общий прогресс' : 'Overall Progress'}
              </p>
              <h3 className="text-base lg:text-lg font-semibold mb-1 text-white">
                {stats?.total_courses
                  ? (lang === 'ru' ? `${stats.total_courses} курсов • ${stats.total_completed} уроков пройдено` : `${stats.total_courses} courses • ${stats.total_completed} lessons done`)
                  : (lang === 'ru' ? 'Запишитесь на курс чтобы начать' : 'Enroll in a course to start')}
              </h3>
              <p className="text-sm text-white/40 mb-3">
                {stats?.total_xp ? `${stats.total_xp} XP ${lang === 'ru' ? 'заработано' : 'earned'}` : ''}
              </p>
              <Button size="sm" onClick={() => navigate('/courses')}>
                {lang === 'ru' ? 'Все курсы' : 'All courses'} <ArrowRight size={14} />
              </Button>
            </div>
            <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-white/5">
              <div
                className="h-full rounded-full"
                style={{
                  width: `${stats?.overall_progress ?? 0}%`,
                  background: 'linear-gradient(90deg, #F97316, #FB923C)',
                }}
              />
            </div>
          </div>
        </motion.div>

        {/* ── Sprint Banner ── */}
        <motion.div variants={itemVariants}>
          <SprintBanner />
        </motion.div>

        {/* ── Create Course Banner ── */}
        <motion.div variants={itemVariants}>
          <div
            className="relative overflow-hidden rounded-2xl border border-purple-500/20 bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 p-5 cursor-pointer hover:border-purple-500/40 transition-all group"
            onClick={() => navigate('/teach')}
          >
            <div className="absolute inset-0 opacity-20 pointer-events-none"
              style={{ background: 'radial-gradient(ellipse at 80% 50%, #7C3AED 0%, transparent 60%)' }} />
            <div className="relative flex items-center gap-4">
              <div className="w-12 h-12 rounded-xl bg-purple-500/20 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
                <Sparkles size={24} className="text-purple-400" />
              </div>
              <div className="flex-1 min-w-0">
                <h3 className="text-base font-bold text-white mb-0.5">
                  {lang === 'ru' ? 'Создай свой курс — получи XP!' : 'Create a course — earn XP!'}
                </h3>
                <p className="text-sm text-white/50">
                  {lang === 'ru'
                    ? 'Поделись знаниями и получи 500 XP за каждый опубликованный курс'
                    : 'Share your knowledge and earn 500 XP for each published course'}
                </p>
              </div>
              <div className="hidden sm:flex items-center gap-1 text-purple-400 text-sm font-medium shrink-0">
                <Zap size={16} />
                <span>+500 XP</span>
                <ArrowRight size={16} className="group-hover:translate-x-1 transition-transform" />
              </div>
            </div>
          </div>
        </motion.div>

        {/* ── Stats Grid ── */}
        <motion.div variants={itemVariants} className="grid grid-cols-2 lg:grid-cols-4 gap-3 lg:gap-4">
          {topStats.map((stat) => (
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

        {/* ── Course Progress Cards ── */}
        {stats && stats.courses.length > 0 && (
          <motion.div variants={itemVariants}>
            <div className="flex items-center justify-between mb-3">
              <h2 className="text-sm font-semibold text-white/70 uppercase tracking-wider flex items-center gap-2">
                <BarChart3 size={14} />
                {lang === 'ru' ? 'Прогресс по курсам' : 'Course Progress'}
              </h2>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {stats.courses.map((course) => (
                <motion.button
                  key={course.course_id}
                  whileHover={{ scale: 1.01 }}
                  whileTap={{ scale: 0.99 }}
                  onClick={() => navigate(`/courses/${course.course_id}`)}
                  className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-4 text-left hover:border-white/12 transition-all cursor-pointer group"
                >
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1 min-w-0 pr-3">
                      <p className="text-sm font-medium text-white truncate group-hover:text-[#F97316] transition-colors">
                        {course.title}
                      </p>
                      <p className="text-[11px] text-white/30 mt-0.5">{course.category}</p>
                    </div>
                    <div className="text-right shrink-0">
                      <p className="text-sm font-bold text-[#F97316]">{course.progress_percent}%</p>
                      <p className="text-[10px] text-white/30">{course.xp_earned} XP</p>
                    </div>
                  </div>
                  <ProgressBar value={course.progress_percent} max={100} color="#F97316" />
                  <p className="text-[11px] text-white/30 mt-2">
                    {course.completed_lessons}/{course.total_lessons} {lang === 'ru' ? 'уроков' : 'lessons'}
                  </p>
                </motion.button>
              ))}
            </div>
          </motion.div>
        )}

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
