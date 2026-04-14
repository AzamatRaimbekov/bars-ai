import { useState, useRef, useCallback, useEffect } from "react"
import { CameraView } from "./CameraView"
import { ScoreIndicator } from "./ScoreIndicator"
import { getJointAngles, diversityScore, cleannessScore, musicalityScore } from "@/services/poseAnalyzer"
import type { Landmark } from "@/services/poseService"
import { Button } from "@/components/ui/Button"
import { Flame, Music, Zap } from "lucide-react"

interface StepBattleSim {
  type: "battle-sim"
  title: string
  music: string
  duration: number
  bpm: number
}

export function BattleSimStep({ step, onAnswer }: { step: StepBattleSim; onAnswer: (ok: boolean) => void }) {
  const [started, setStarted] = useState(false)
  const [timeLeft, setTimeLeft] = useState(step.duration)
  const [finished, setFinished] = useState(false)
  const audioRef = useRef<HTMLAudioElement>(null)
  const historyRef = useRef<Record<string, number>[]>([])
  const sharpMovesRef = useRef<number[]>([])
  const prevAnglesRef = useRef<Record<string, number> | null>(null)
  const startTimeRef = useRef(0)

  useEffect(() => {
    if (!started || finished) return
    startTimeRef.current = Date.now()
    const interval = setInterval(() => {
      setTimeLeft(t => {
        if (t <= 1) {
          clearInterval(interval)
          setFinished(true)
          audioRef.current?.pause()
          return 0
        }
        return t - 1
      })
    }, 1000)
    return () => clearInterval(interval)
  }, [started, finished])

  const handleFrame = useCallback((landmarks: Landmark[]) => {
    if (!started || finished) return
    const angles = getJointAngles(landmarks)
    historyRef.current.push(angles)

    // Detect sharp movements for musicality
    if (prevAnglesRef.current) {
      const totalDiff = Object.keys(angles).reduce((sum, key) =>
        sum + Math.abs((angles[key] || 0) - (prevAnglesRef.current?.[key] || 0)), 0)
      if (totalDiff > 50) {
        sharpMovesRef.current.push(Date.now() - startTimeRef.current)
      }
    }
    prevAnglesRef.current = angles
  }, [started, finished])

  const diversity = diversityScore(historyRef.current)
  const cleanness = cleannessScore(historyRef.current)
  const musicality2 = musicalityScore(sharpMovesRef.current, step.bpm)
  const overall = Math.round((diversity + cleanness + musicality2) / 3)

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>
      <audio ref={audioRef} src={step.music} />

      {!started ? (
        <div className="text-center space-y-4 py-8">
          <div className="w-20 h-20 rounded-full bg-red-500/10 border-2 border-red-500/30 flex items-center justify-center mx-auto">
            <Flame size={36} className="text-red-400" />
          </div>
          <h3 className="text-lg font-bold text-white">Battle Mode</h3>
          <p className="text-sm text-white/50">Фристайл {step.duration} секунд. Покажи всё что умеешь!</p>
          <Button onClick={() => { setStarted(true); audioRef.current?.play() }} className="w-full bg-red-500 hover:bg-red-600">
            Начать баттл
          </Button>
        </div>
      ) : (
        <>
          <div className="flex items-center justify-between">
            <span className="text-2xl font-bold text-white">{timeLeft}с</span>
            {!finished && <span className="text-xs text-red-400 animate-pulse font-medium">LIVE BATTLE</span>}
          </div>

          <CameraView onFrame={handleFrame} active={!finished} className="aspect-[4/3] rounded-2xl border-2 border-red-500/30" />

          {finished && (
            <div className="space-y-4">
              <div className="grid grid-cols-3 gap-3">
                <div className="bg-white/5 rounded-xl p-3 text-center">
                  <Zap size={16} className="text-yellow-400 mx-auto mb-1" />
                  <p className="text-lg font-bold text-white">{cleanness}%</p>
                  <p className="text-[10px] text-white/40">Чистота</p>
                </div>
                <div className="bg-white/5 rounded-xl p-3 text-center">
                  <Music size={16} className="text-blue-400 mx-auto mb-1" />
                  <p className="text-lg font-bold text-white">{musicality2}%</p>
                  <p className="text-[10px] text-white/40">Музыкальность</p>
                </div>
                <div className="bg-white/5 rounded-xl p-3 text-center">
                  <Flame size={16} className="text-orange-400 mx-auto mb-1" />
                  <p className="text-lg font-bold text-white">{diversity}%</p>
                  <p className="text-[10px] text-white/40">Разнообразие</p>
                </div>
              </div>
              <div className="text-center">
                <ScoreIndicator score={overall} size={90} label="Общий балл" />
              </div>
              <Button onClick={() => onAnswer(overall >= 50)} className="w-full">
                Продолжить
              </Button>
            </div>
          )}
        </>
      )}
    </div>
  )
}
