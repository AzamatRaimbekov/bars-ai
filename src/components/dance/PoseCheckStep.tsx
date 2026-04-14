import { useState, useCallback, useMemo } from "react"
import { CameraView } from "./CameraView"
import { ScoreIndicator } from "./ScoreIndicator"
import { getJointAngles, comparePoses } from "@/services/poseAnalyzer"
import type { Landmark } from "@/services/poseService"
import { Camera, RotateCcw } from "lucide-react"
import { Button } from "@/components/ui/Button"

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
      {/* Connections */}
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
      {/* Joints */}
      {landmarks.map((l, i) => {
        if (!l || i < 11 || i > 28) return null // only body landmarks
        return (
          <circle key={i} cx={l[0] * W} cy={l[1] * H} r={5} fill="#F97316" />
        )
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

export function PoseCheckStep({ step, onAnswer }: { step: StepPoseCheck; onAnswer: (ok: boolean) => void }) {
  const [currentLandmarks, setCurrentLandmarks] = useState<Landmark[] | null>(null)
  const [result, setResult] = useState<{ score: number; joints: Record<string, { score: number }> } | null>(null)
  const [jointColors, setJointColors] = useState<Record<string, string>>({})

  const refAngles = getJointAngles(
    step.referencePose.landmarks.map(([x,y,z]) => ({x,y,z}))
  )

  const handleFrame = useCallback((landmarks: Landmark[]) => {
    setCurrentLandmarks(landmarks)
    // Live preview colors
    const studentAngles = getJointAngles(landmarks)
    const comparison = comparePoses(studentAngles, refAngles)
    const colors: Record<string, string> = {}
    for (const [name, data] of Object.entries(comparison.joints)) {
      colors[name] = data.score >= 70 ? "#10B981" : data.score >= 40 ? "#F59E0B" : "#EF4444"
    }
    setJointColors(colors)
  }, [refAngles])

  const handleCapture = () => {
    if (!currentLandmarks) return
    const studentAngles = getJointAngles(currentLandmarks)
    const comparison = comparePoses(studentAngles, refAngles)
    setResult(comparison)
  }

  const handleRetry = () => setResult(null)

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>
      <p className="text-sm text-white/50">{step.description}</p>

      <div className="grid grid-cols-2 gap-3">
        {/* Reference — show image if available, otherwise draw skeleton from landmarks */}
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
        <CameraView
          onFrame={handleFrame}
          jointColors={jointColors}
          active={!result}
          className="aspect-[4/3]"
        />
      </div>

      {result ? (
        <div className="text-center space-y-3">
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
        <Button onClick={handleCapture} disabled={!currentLandmarks} className="w-full">
          <Camera size={14} /> Захватить позу
        </Button>
      )}
    </div>
  )
}
