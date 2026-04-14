import { motion } from 'framer-motion'
import { Crown, Trophy, Medal } from 'lucide-react'
import type { LeaderboardEntry } from '@/services/sprintApi'

const PODIUM_COLORS = [
  { bg: 'from-yellow-500/20 to-yellow-600/5', border: 'border-yellow-500/20', text: 'text-yellow-400' },
  { bg: 'from-white/10 to-white/5', border: 'border-white/10', text: 'text-white/60' },
  { bg: 'from-amber-700/15 to-amber-800/5', border: 'border-amber-700/20', text: 'text-amber-600' },
]

const PODIUM_ICONS = [Crown, Trophy, Medal]

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.04 } },
}

const itemVariants = {
  hidden: { opacity: 0, y: 12 },
  show: { opacity: 1, y: 0 },
}

function getInitials(name: string): string {
  return name.split(' ').map((w) => w[0]).join('').toUpperCase().slice(0, 2)
}

interface SprintLeaderboardProps {
  entries: LeaderboardEntry[]
  currentUserId?: string
}

export function SprintLeaderboard({ entries, currentUserId }: SprintLeaderboardProps) {
  if (entries.length === 0) {
    return (
      <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-16 text-center">
        <p className="text-white/40">Пока нет участников</p>
      </div>
    )
  }

  const top3 = entries.slice(0, 3)
  const rest = entries.slice(3)

  return (
    <div className="space-y-4">
      {/* Podium — Top 3 */}
      {top3.length > 0 && (
        <div className="flex items-end justify-center gap-3 pt-4 pb-2">
          {[1, 0, 2].map((podiumIndex) => {
            const entry = top3[podiumIndex]
            if (!entry) return <div key={podiumIndex} className="w-28" />
            const colors = PODIUM_COLORS[podiumIndex]
            const PodiumIcon = PODIUM_ICONS[podiumIndex]
            const isFirst = podiumIndex === 0
            const isMe = entry.user_id === currentUserId

            return (
              <motion.div
                key={entry.user_id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: podiumIndex * 0.1 }}
                className="flex flex-col items-center"
              >
                <div
                  className={[
                    'w-28 rounded-2xl border bg-[#0A0A0A] flex flex-col items-center gap-2 p-3',
                    isFirst ? 'pb-8 pt-5' : 'pb-6 pt-4',
                    colors.border,
                    isMe ? 'ring-2 ring-[#F97316]/30' : '',
                  ].join(' ')}
                >
                  <PodiumIcon size={isFirst ? 22 : 18} className={colors.text} />

                  {entry.avatar_url ? (
                    <img
                      src={entry.avatar_url}
                      alt={entry.name}
                      className={`rounded-full object-cover border-2 ${colors.border} ${isFirst ? 'w-16 h-16' : 'w-12 h-12'}`}
                    />
                  ) : (
                    <div
                      className={`rounded-full flex items-center justify-center font-bold bg-gradient-to-br ${colors.bg} border ${colors.border} ${isFirst ? 'w-16 h-16 text-lg' : 'w-12 h-12 text-sm'}`}
                    >
                      {getInitials(entry.name)}
                    </div>
                  )}

                  <div className="text-center w-full">
                    <p className={`font-semibold truncate px-1 text-white ${isFirst ? 'text-sm' : 'text-xs'}`}>
                      {entry.name}
                    </p>
                    {isMe && (
                      <p className="text-[10px] text-[#F97316] font-medium">Вы</p>
                    )}
                  </div>

                  <p className={`font-bold flex items-center gap-1 ${isFirst ? 'text-yellow-400 text-lg' : `${colors.text} text-base`}`}>
                    <span>&#127942;</span> {entry.trophies}
                  </p>
                </div>
              </motion.div>
            )
          })}
        </div>
      )}

      {/* Rows (4+) */}
      {rest.length > 0 && (
        <motion.div
          variants={containerVariants}
          initial="hidden"
          animate="show"
          className="space-y-1.5"
        >
          {rest.map((entry, idx) => {
            const isMe = entry.user_id === currentUserId
            const isEven = idx % 2 === 0

            return (
              <motion.div key={entry.user_id} variants={itemVariants}>
                <div
                  className={[
                    'flex items-center gap-3 rounded-xl px-3 py-2.5 transition-colors',
                    isMe
                      ? 'border-l-2 border-[#F97316] bg-[#F97316]/5 pl-2.5'
                      : isEven
                        ? 'bg-[#0A0A0A]'
                        : 'bg-transparent hover:bg-white/[0.02]',
                  ].join(' ')}
                >
                  <div className="w-8 text-center shrink-0">
                    <span className={`text-sm font-bold ${isMe ? 'text-[#F97316]' : 'text-white/30'}`}>
                      {entry.place}
                    </span>
                  </div>

                  {entry.avatar_url ? (
                    <img
                      src={entry.avatar_url}
                      alt={entry.name}
                      className="w-9 h-9 rounded-full object-cover border border-white/8 shrink-0"
                    />
                  ) : (
                    <div className="w-9 h-9 rounded-full flex items-center justify-center font-bold text-sm bg-white/5 border border-white/8 text-white/60 shrink-0">
                      {getInitials(entry.name)}
                    </div>
                  )}

                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      <p className="text-sm font-medium truncate text-white">{entry.name}</p>
                      {isMe && (
                        <span className="text-[10px] bg-[#F97316]/15 text-[#F97316] px-1.5 py-0.5 rounded-full font-medium shrink-0">
                          Вы
                        </span>
                      )}
                    </div>
                  </div>

                  <div className="text-right shrink-0">
                    <p className="text-sm font-bold text-yellow-400 flex items-center gap-1">
                      <span>&#127942;</span> {entry.trophies}
                    </p>
                  </div>
                </div>
              </motion.div>
            )
          })}
        </motion.div>
      )}
    </div>
  )
}
