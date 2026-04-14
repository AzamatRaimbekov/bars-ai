import { useState, useRef, useCallback, useEffect } from "react"
import { CameraView } from "./CameraView"
import { ScoreIndicator } from "./ScoreIndicator"
import { getJointAngles, comparePoses } from "@/services/poseAnalyzer"
import type { Landmark } from "@/services/poseService"
import { Button } from "@/components/ui/Button"
import { Music } from "lucide-react"

interface Move {
  name: string
  pose: { landmarks: number[][] }
  beatStart: number
  beatEnd: number
}

interface StepComboChallenge {
  type: "combo-challenge"
  title: string
  music: string
  bpm: number
  moves: Move[]
  threshold: number
}

export function ComboChallengeStep({ step, onAnswer }: { step: StepComboChallenge; onAnswer: (ok: boolean) => void }) {
  const [started, setStarted] = useState(false)
  const [currentMove, setCurrentMove] = useState(0)
  const [moveScores, setMoveScores] = useState<number[]>([])
  const [finished, setFinished] = useState(false)
  const audioRef = useRef<HTMLAudioElement>(null)
  const beatRef = useRef(0)

  useEffect(() => {
    if (!started || finished) return
    const beatInterval = 60000 / step.bpm
    const interval = setInterval(() => {
      beatRef.current++
      const move = step.moves.findIndex(m => beatRef.current >= m.beatStart && beatRef.current <= m.beatEnd)
      if (move >= 0) setCurrentMove(move)
      if (beatRef.current > (step.moves[step.moves.length - 1]?.beatEnd || 0) + 4) {
        setFinished(true)
        audioRef.current?.pause()
      }
    }, beatInterval)
    return () => clearInterval(interval)
  }, [started, finished, step])

  const handleFrame = useCallback((landmarks: Landmark[]) => {
    if (!started || finished) return
    const move = step.moves[currentMove]
    if (!move) return
    const studentAngles = getJointAngles(landmarks)
    const refAngles = getJointAngles(move.pose.landmarks.map(([x,y,z]) => ({x,y,z})))
    const result = comparePoses(studentAngles, refAngles)
    setMoveScores(prev => {
      const next = [...prev]
      next[currentMove] = Math.max(next[currentMove] || 0, result.score)
      return next
    })
  }, [started, finished, currentMove, step.moves])

  const avgScore = moveScores.length > 0
    ? Math.round(moveScores.reduce((a,b) => a+b, 0) / moveScores.length)
    : 0

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>
      <audio ref={audioRef} src={step.music} />

      {!started ? (
        <div className="text-center space-y-4">
          <Music className="text-primary mx-auto" size={40} />
          <p className="text-sm text-white/50">Связка из {step.moves.length} движений под музыку</p>
          <Button onClick={() => { setStarted(true); audioRef.current?.play() }} className="w-full">
            Начать
          </Button>
        </div>
      ) : (
        <>
          {/* Current move indicator */}
          <div className="flex gap-2 overflow-x-auto pb-2">
            {step.moves.map((m, i) => (
              <div key={i} className={`px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap ${
                i === currentMove ? "bg-primary/20 text-primary border border-primary/30" :
                moveScores[i] !== undefined ? "bg-green-500/10 text-green-400 border border-green-500/20" :
                "bg-white/5 text-white/30 border border-white/10"
              }`}>
                {m.name} {moveScores[i] !== undefined && `${moveScores[i]}%`}
              </div>
            ))}
          </div>

          <CameraView onFrame={handleFrame} active={!finished} className="aspect-[4/3] rounded-2xl" />

          {finished && (
            <div className="text-center space-y-3">
              <ScoreIndicator score={avgScore} size={90} label="Общий результат" />
              <Button onClick={() => onAnswer(avgScore >= step.threshold)} className="w-full">
                Продолжить
              </Button>
            </div>
          )}
        </>
      )}
    </div>
  )
}
