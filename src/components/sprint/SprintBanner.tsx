import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Trophy, ArrowRight } from 'lucide-react'
import { sprintApi, type Sprint, type MyTrophies } from '@/services/sprintApi'
import { Button } from '@/components/ui/Button'

export function SprintBanner() {
  const navigate = useNavigate()
  const [sprint, setSprint] = useState<Sprint | null>(null)
  const [trophies, setTrophies] = useState<MyTrophies | null>(null)

  useEffect(() => {
    Promise.all([
      sprintApi.getActive().catch(() => null),
      sprintApi.getMyTrophies().catch(() => null),
    ]).then(([s, t]) => {
      setSprint(s)
      setTrophies(t)
    })
  }, [])

  if (!sprint) return null

  const endDate = new Date(sprint.end_date)
  const now = new Date()
  const diffMs = endDate.getTime() - now.getTime()
  const daysLeft = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)))

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      className="relative rounded-2xl p-[1px] overflow-hidden"
      style={{
        background: 'linear-gradient(135deg, #EAB308, #F97316, #EAB308)',
      }}
    >
      <div className="bg-[#0A0A0A] rounded-2xl p-5 flex flex-col sm:flex-row items-start sm:items-center gap-4">
        <div className="w-10 h-10 rounded-xl bg-yellow-500/15 flex items-center justify-center shrink-0">
          <Trophy size={20} className="text-yellow-400" />
        </div>

        <div className="flex-1 min-w-0">
          <p className="text-xs text-yellow-400 uppercase tracking-wider font-medium mb-1">
            Sprint
          </p>
          <h3 className="text-base font-semibold text-white mb-1">
            {sprint.title}
          </h3>
          <div className="flex items-center gap-4 text-sm text-white/40">
            <span>
              {daysLeft > 0
                ? `${daysLeft} ${daysLeft === 1 ? 'день' : daysLeft < 5 ? 'дня' : 'дней'} осталось`
                : 'Завершается сегодня'}
            </span>
            {trophies && (
              <span className="text-yellow-400 font-bold">
                &#127942; {trophies.sprint} трофеев
              </span>
            )}
          </div>
        </div>

        <Button size="sm" onClick={() => navigate('/sprint')}>
          Посмотреть лидерборд <ArrowRight size={14} />
        </Button>
      </div>
    </motion.div>
  )
}
