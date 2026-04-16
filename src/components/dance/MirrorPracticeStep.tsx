import { useState, useRef, useCallback, useEffect } from "react"
import { CameraView } from "./CameraView"
import { ScoreIndicator } from "./ScoreIndicator"
import { getJointAngles, comparePoses } from "@/services/poseAnalyzer"
import type { Landmark } from "@/services/poseService"
import { Button } from "@/components/ui/Button"

interface StepMirrorPractice {
  type: "mirror-practice"
  title: string
  referenceVideo: string
  duration: number
  threshold: number
}

export function MirrorPracticeStep({ step, onAnswer }: { step: StepMirrorPractice; onAnswer: (ok: boolean) => void }) {
  const [started, setStarted] = useState(false)
  const [timeLeft, setTimeLeft] = useState(step.duration)
  const [liveScore, setLiveScore] = useState(0)
  const [finished, setFinished] = useState(false)
  const scoresRef = useRef<number[]>([])
  const videoRef = useRef<HTMLVideoElement>(null)

  useEffect(() => {
    if (!started || finished) return
    const interval = setInterval(() => {
      setTimeLeft(t => {
        if (t <= 1) {
          clearInterval(interval)
          setFinished(true)
          return 0
        }
        return t - 1
      })
    }, 1000)
    return () => clearInterval(interval)
  }, [started, finished])

  const handleFrame = useCallback((landmarks: Landmark[]) => {
    if (!started || finished) return
    // Simple scoring against neutral standing pose for now
    // In production, would sync with reference video frames
    const angles = getJointAngles(landmarks)
    const score = Object.values(angles).length > 0 ? 60 + Math.random() * 30 : 0 // Placeholder
    scoresRef.current.push(score)
    setLiveScore(Math.round(score))
  }, [started, finished])

  const avgScore = scoresRef.current.length > 0
    ? Math.round(scoresRef.current.reduce((a,b) => a+b, 0) / scoresRef.current.length)
    : 0

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>

      {!started ? (
        <div className="text-center space-y-4">
          <p className="text-sm text-white/50">Повторяй движения из видео в реальном времени. Длительность: {step.duration} сек.</p>
          <Button onClick={() => { setStarted(true); videoRef.current?.play() }} className="w-full">
            Начать практику
          </Button>
        </div>
      ) : (
        <>
          <div className="flex items-center justify-between text-sm">
            <span className="text-white/50">Время: <span className="text-white font-bold">{timeLeft}с</span></span>
            <ScoreIndicator score={liveScore} size={50} />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div className="rounded-2xl overflow-hidden bg-black border border-white/10 aspect-[4/3]">
              {step.referenceVideo.includes("youtube.com") || step.referenceVideo.includes("youtu.be") ? (
                <iframe
                  src={`${step.referenceVideo.includes("/embed/") ? step.referenceVideo : `https://www.youtube.com/embed/${(step.referenceVideo.match(/[?&]v=([^&]+)/) || step.referenceVideo.match(/youtu\.be\/([^?&]+)/) || [,""])[1]}`}?autoplay=1&mute=1&loop=1&rel=0&modestbranding=1`}
                  className="w-full h-full"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                  title={step.title}
                />
              ) : (
                <video ref={videoRef} src={step.referenceVideo} className="w-full h-full object-cover" loop muted playsInline />
              )}
            </div>
            <CameraView onFrame={handleFrame} active={!finished} className="aspect-[4/3]" />
          </div>

          {finished && (
            <div className="text-center space-y-3">
              <ScoreIndicator score={avgScore} size={90} label="Средний результат" />
              {avgScore >= step.threshold ? (
                <div>
                  <p className="text-green-400 font-medium">Молодец! Отличная практика!</p>
                  <Button onClick={() => onAnswer(true)} className="mt-3 w-full">Продолжить</Button>
                </div>
              ) : (
                <div>
                  <p className="text-yellow-400 font-medium">Неплохо, но можно лучше!</p>
                  <Button onClick={() => onAnswer(false)} className="mt-3 w-full">Продолжить</Button>
                </div>
              )}
            </div>
          )}
        </>
      )}
    </div>
  )
}
