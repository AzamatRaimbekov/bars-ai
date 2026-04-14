import { useState, useCallback, useRef, useEffect } from "react"
import { CameraView } from "./CameraView"
import { ScoreIndicator } from "./ScoreIndicator"
import { getJointAngles, comparePoses } from "@/services/poseAnalyzer"
import type { Landmark } from "@/services/poseService"
import { RotateCcw, Check } from "lucide-react"
import { Button } from "@/components/ui/Button"
import { motion } from "framer-motion"

const SKELETON_CONNECTIONS: [number, number][] = [
  [11,12],[11,13],[13,15],[12,14],[14,16],
  [11,23],[12,24],[23,24],
  [23,25],[25,27],[24,26],[26,28],
]

function ReferenceSkeleton({ landmarks }: { landmarks: number[][] }) {
  const W = 300, H = 400
  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-full">
      <rect width={W} height={H} fill="#0A0A0A" />
      {SKELETON_CONNECTIONS.map(([a, b], i) => {
        const la = landmarks[a], lb = landmarks[b]
        if (!la || !lb) return null
        return (
          <line key={i}
            x1={la[0] * W} y1={la[1] * H}
            x2={lb[0] * W} y2={lb[1] * H}
            stroke="#F97316" strokeWidth={3} strokeLinecap="round" opacity={0.7}
          />
        )
      })}
      {landmarks.map((l, i) => {
        if (!l || i < 11 || i > 28) return null
        return <circle key={i} cx={l[0] * W} cy={l[1] * H} r={5} fill="#F97316" />
      })}
      <text x={W/2} y={H - 10} textAnchor="middle" fill="rgba(255,255,255,0.3)" fontSize={12}>
        Эталонная поза
      </text>
    </svg>
  )
}

interface StepPoseCheck {
  type: "pose-check"
  title: string
  description: string
  referencePose: { landmarks: number[][] }
  referenceImage?: string
  threshold: number
}

const HOLD_DURATION = 2000 // ms to hold pose for auto-capture

export function PoseCheckStep({ step, onAnswer }: { step: StepPoseCheck; onAnswer: (ok: boolean) => void }) {
  const [liveScore, setLiveScore] = useState(0)
  const [holdProgress, setHoldProgress] = useState(0) // 0-100
  const [result, setResult] = useState<{ score: number; joints: Record<string, { score: number }> } | null>(null)
  const [jointColors, setJointColors] = useState<Record<string, string>>({})

  const holdStartRef = useRef<number | null>(null)
  const lastComparisonRef = useRef<{ score: number; joints: Record<string, { score: number }> } | null>(null)

  const refAngles = getJointAngles(
    step.referencePose.landmarks.map(([x,y,z]) => ({x,y,z}))
  )

  const handleFrame = useCallback((landmarks: Landmark[]) => {
    if (result) return // already captured

    const studentAngles = getJointAngles(landmarks)
    const comparison = comparePoses(studentAngles, refAngles)
    lastComparisonRef.current = comparison
    setLiveScore(comparison.score)

    // Update joint colors
    const colors: Record<string, string> = {}
    for (const [name, data] of Object.entries(comparison.joints)) {
      colors[name] = data.score >= 70 ? "#10B981" : data.score >= 40 ? "#F59E0B" : "#EF4444"
    }
    setJointColors(colors)

    // Auto-capture: if score >= threshold, start counting hold time
    const now = Date.now()
    if (comparison.score >= step.threshold) {
      if (!holdStartRef.current) {
        holdStartRef.current = now
      }
      const elapsed = now - holdStartRef.current
      const progress = Math.min(100, (elapsed / HOLD_DURATION) * 100)
      setHoldProgress(progress)

      // Auto-capture after holding for HOLD_DURATION
      if (elapsed >= HOLD_DURATION) {
        setResult(comparison)
        holdStartRef.current = null
        setHoldProgress(100)
      }
    } else {
      // Score dropped below threshold — reset hold timer
      holdStartRef.current = null
      setHoldProgress(0)
    }
  }, [refAngles, result, step.threshold])

  const handleRetry = () => {
    setResult(null)
    setHoldProgress(0)
    holdStartRef.current = null
    lastComparisonRef.current = null
  }

  const scoreColor = liveScore >= step.threshold ? "#10B981" : liveScore >= 40 ? "#F59E0B" : "#EF4444"

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>
      <p className="text-sm text-white/50">{step.description}</p>

      <div className="grid grid-cols-2 gap-3">
        {/* Reference */}
        <div className="rounded-2xl overflow-hidden bg-black border border-white/10 aspect-[4/3] flex items-center justify-center">
          {step.referenceImage ? (
            <img src={step.referenceImage} alt="Reference pose" className="w-full h-full object-cover" />
          ) : step.referencePose?.landmarks?.length > 0 ? (
            <ReferenceSkeleton landmarks={step.referencePose.landmarks} />
          ) : (
            <p className="text-white/30 text-sm">Эталонная поза</p>
          )}
        </div>

        {/* Camera */}
        <div className="relative">
          <CameraView
            onFrame={handleFrame}
            jointColors={jointColors}
            active={!result}
            className="aspect-[4/3]"
          />
          {/* Live score overlay */}
          {!result && (
            <div className="absolute top-2 left-2 right-2 flex items-center justify-between">
              <div className="bg-black/70 rounded-lg px-3 py-1.5 backdrop-blur-sm">
                <span className="text-xs text-white/50">Совпадение: </span>
                <span className="text-sm font-bold" style={{ color: scoreColor }}>{liveScore}%</span>
              </div>
              {liveScore >= step.threshold && (
                <div className="bg-black/70 rounded-lg px-3 py-1.5 backdrop-blur-sm text-xs text-green-400 font-medium">
                  Держи позу!
                </div>
              )}
            </div>
          )}
          {/* Hold progress bar */}
          {!result && holdProgress > 0 && (
            <div className="absolute bottom-2 left-2 right-2">
              <div className="h-2 bg-black/50 rounded-full overflow-hidden backdrop-blur-sm">
                <motion.div
                  className="h-full rounded-full bg-green-400"
                  initial={{ width: 0 }}
                  animate={{ width: `${holdProgress}%` }}
                  transition={{ duration: 0.1 }}
                />
              </div>
              <p className="text-center text-[10px] text-green-400/80 mt-1">
                {holdProgress < 100 ? `Держи ${Math.ceil((HOLD_DURATION - (holdProgress / 100 * HOLD_DURATION)) / 1000)} сек...` : ""}
              </p>
            </div>
          )}
        </div>
      </div>

      {result ? (
        <div className="text-center space-y-3">
          <div className="flex items-center justify-center gap-2 text-green-400">
            <Check size={20} />
            <span className="font-semibold">Поза зафиксирована!</span>
          </div>
          <ScoreIndicator score={result.score} size={90} label="Совпадение" />
          {result.score >= step.threshold ? (
            <div>
              <p className="text-green-400 font-medium">Отлично! Поза верная!</p>
              <Button onClick={() => onAnswer(true)} className="mt-3 w-full">Продолжить</Button>
            </div>
          ) : (
            <div>
              <p className="text-red-400 font-medium">Нужно точнее. Попробуй ещё раз.</p>
              <Button variant="secondary" onClick={handleRetry} className="mt-3 w-full">
                <RotateCcw size={14} /> Ещё раз
              </Button>
            </div>
          )}
        </div>
      ) : (
        <div className="text-center">
          <p className="text-sm text-white/40">
            {liveScore < step.threshold
              ? `Повторяй эталонную позу. Нужно набрать ${step.threshold}% совпадения.`
              : "Отлично! Держи позу 2 секунды для автоматической фиксации."
            }
          </p>
        </div>
      )}
    </div>
  )
}
