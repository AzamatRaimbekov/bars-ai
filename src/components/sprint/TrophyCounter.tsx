import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { sprintApi, type MyTrophies } from '@/services/sprintApi'

export function TrophyCounter() {
  const navigate = useNavigate()
  const [trophies, setTrophies] = useState<MyTrophies | null>(null)

  useEffect(() => {
    sprintApi.getMyTrophies()
      .then(setTrophies)
      .catch(() => {})
  }, [])

  if (!trophies || trophies.sprint === 0) return null

  return (
    <button
      onClick={() => navigate('/sprint')}
      className="bg-yellow-500/10 text-yellow-400 rounded-lg px-2.5 py-1 text-xs font-bold flex items-center gap-1 hover:bg-yellow-500/20 transition-colors cursor-pointer"
      title="Sprint trophies"
    >
      <span>&#127942;</span>
      <span>{trophies.sprint}</span>
    </button>
  )
}
