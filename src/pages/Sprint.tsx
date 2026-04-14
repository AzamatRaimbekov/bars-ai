import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { Trophy, Clock, Loader2 } from 'lucide-react'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { SprintLeaderboard } from '@/components/sprint/SprintLeaderboard'
import { PrizeCard } from '@/components/sprint/PrizeCard'
import { sprintApi, type Sprint as SprintType, type LeaderboardEntry, type MyTrophies } from '@/services/sprintApi'
import { useAuthStore } from '@/store/authStore'

function formatCountdown(endDate: string): string {
  const end = new Date(endDate)
  const now = new Date()
  const diff = end.getTime() - now.getTime()
  if (diff <= 0) return 'Завершен'

  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))

  if (days > 0) return `${days}д ${hours}ч ${minutes}м`
  return `${hours}ч ${minutes}м`
}

function formatDate(dateStr: string): string {
  return new Date(dateStr).toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' })
}

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function Sprint() {
  const currentUserId = useAuthStore((s) => s.user?.id)
  const [sprint, setSprint] = useState<SprintType | null>(null)
  const [leaderboard, setLeaderboard] = useState<LeaderboardEntry[]>([])
  const [myTrophies, setMyTrophies] = useState<MyTrophies | null>(null)
  const [loading, setLoading] = useState(true)
  const [countdown, setCountdown] = useState('')

  useEffect(() => {
    Promise.all([
      sprintApi.getActive().catch(() => null),
      sprintApi.getLeaderboard().catch(() => []),
      sprintApi.getMyTrophies().catch(() => null),
    ]).then(([s, lb, t]) => {
      setSprint(s)
      setLeaderboard(lb)
      setMyTrophies(t)
      if (s) setCountdown(formatCountdown(s.end_date))
    }).finally(() => setLoading(false))
  }, [])

  // Live countdown
  useEffect(() => {
    if (!sprint) return
    const interval = setInterval(() => {
      setCountdown(formatCountdown(sprint.end_date))
    }, 60000)
    return () => clearInterval(interval)
  }, [sprint])

  const myPlace = leaderboard.find((e) => e.user_id === currentUserId)?.place

  if (loading) {
    return (
      <PageWrapper>
        <div className="flex justify-center py-20">
          <Loader2 className="animate-spin text-[#F97316]" size={32} />
        </div>
      </PageWrapper>
    )
  }

  if (!sprint) {
    return (
      <PageWrapper>
        <div className="max-w-3xl mx-auto text-center py-20">
          <div className="w-16 h-16 rounded-2xl bg-yellow-500/10 flex items-center justify-center mx-auto mb-4">
            <Trophy size={28} className="text-yellow-400" />
          </div>
          <h1 className="text-2xl font-bold text-white mb-2">Нет активного спринта</h1>
          <p className="text-white/40">Следующий скоро!</p>
        </div>
      </PageWrapper>
    )
  }

  return (
    <PageWrapper>
      <motion.div variants={containerVariants} initial="hidden" animate="show" className="max-w-3xl mx-auto space-y-6">

        {/* Header */}
        <motion.div variants={itemVariants} className="text-center">
          <div className="inline-flex items-center gap-2 bg-yellow-500/10 text-yellow-400 rounded-full px-4 py-1.5 text-sm font-medium mb-4">
            <Clock size={14} />
            <span>{countdown}</span>
          </div>
          <h1 className="text-2xl font-bold text-white mb-1">{sprint.title}</h1>
          <p className="text-white/40 text-sm">
            {formatDate(sprint.start_date)} — {formatDate(sprint.end_date)}
          </p>
        </motion.div>

        {/* My Stats */}
        {myTrophies && (
          <motion.div variants={itemVariants} className="grid grid-cols-2 gap-3">
            <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-4 flex items-center gap-3 hover:border-white/12 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-yellow-500/10 flex items-center justify-center shrink-0">
                <Trophy size={18} className="text-yellow-400" />
              </div>
              <div>
                <p className="text-lg font-bold text-white">{myTrophies.sprint}</p>
                <p className="text-[11px] text-white/40">Мои трофеи</p>
              </div>
            </div>
            <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-4 flex items-center gap-3 hover:border-white/12 transition-colors">
              <div className="w-10 h-10 rounded-xl bg-[#F97316]/10 flex items-center justify-center shrink-0">
                <span className="text-lg">&#127941;</span>
              </div>
              <div>
                <p className="text-lg font-bold text-white">
                  {myPlace ? `#${myPlace}` : '—'}
                </p>
                <p className="text-[11px] text-white/40">Мое место</p>
              </div>
            </div>
          </motion.div>
        )}

        {/* Prize Cards */}
        {sprint.prizes && sprint.prizes.length > 0 && (
          <motion.div variants={itemVariants}>
            <h2 className="text-sm font-semibold text-white/70 uppercase tracking-wider mb-3">Призы</h2>
            <div className="grid grid-cols-3 gap-3">
              {sprint.prizes.slice(0, 3).map((prize) => (
                <PrizeCard
                  key={prize.place}
                  place={prize.place}
                  amount={prize.amount}
                  currency={prize.currency}
                  bonus={prize.bonus}
                />
              ))}
            </div>
          </motion.div>
        )}

        {/* Leaderboard */}
        <motion.div variants={itemVariants}>
          <h2 className="text-sm font-semibold text-white/70 uppercase tracking-wider mb-3">Лидерборд</h2>
          <SprintLeaderboard entries={leaderboard} currentUserId={currentUserId} />
        </motion.div>

      </motion.div>
    </PageWrapper>
  )
}
