import { useState, useRef } from "react"
import { Play, SkipForward, Pause } from "lucide-react"
import { Button } from "@/components/ui/Button"

interface Keyframe {
  time: number
  pose: { landmarks: number[][] }
  description: string
}

interface StepSlowMotion {
  type: "slow-motion"
  title: string
  video: string
  keyframes: Keyframe[]
}

function isYouTubeUrl(url: string) {
  return url.includes("youtube.com") || url.includes("youtu.be")
}

function toYouTubeEmbed(url: string): string {
  if (url.includes("/embed/")) return url
  const match = url.match(/[?&]v=([^&]+)/) || url.match(/youtu\.be\/([^?&]+)/)
  if (match) return `https://www.youtube.com/embed/${match[1]}`
  return url
}

export function SlowMotionStep({ step, onNext }: { step: StepSlowMotion; onNext: () => void }) {
  const videoRef = useRef<HTMLVideoElement>(null)
  const [currentKF, setCurrentKF] = useState(0)
  const [paused, setPaused] = useState(true)
  const [allViewed, setAllViewed] = useState(false)

  const isYT = isYouTubeUrl(step.video)

  const handleTimeUpdate = () => {
    if (!videoRef.current) return
    const time = videoRef.current.currentTime
    const kf = step.keyframes[currentKF]
    if (kf && Math.abs(time - kf.time) < 0.3) {
      videoRef.current.pause()
      setPaused(true)
    }
  }

  const handleContinue = () => {
    if (currentKF >= step.keyframes.length - 1) {
      setAllViewed(true)
      return
    }
    setCurrentKF(prev => prev + 1)
    if (!isYT) {
      setPaused(false)
      videoRef.current?.play()
    }
  }

  const handleStart = () => {
    if (isYT) {
      setPaused(false)
      return
    }
    if (!videoRef.current) return
    videoRef.current.playbackRate = 0.25
    videoRef.current.play()
    setPaused(false)
  }

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>

      {/* Progress dots */}
      <div className="flex gap-1.5 justify-center">
        {step.keyframes.map((_, i) => (
          <div key={i} className={`w-2 h-2 rounded-full ${
            i < currentKF ? "bg-green-400" : i === currentKF ? "bg-primary" : "bg-white/20"
          }`} />
        ))}
      </div>

      <div className="relative rounded-2xl overflow-hidden bg-black aspect-video">
        {isYT ? (
          <iframe
            src={`${toYouTubeEmbed(step.video)}?rel=0&modestbranding=1`}
            className="w-full h-full"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            title={step.title}
          />
        ) : (
          <video
            ref={videoRef}
            src={step.video}
            onTimeUpdate={handleTimeUpdate}
            className="w-full h-full object-contain"
            playsInline
          />
        )}
        {!isYT && (
          <div className="absolute top-2 right-2 bg-black/60 px-2 py-1 rounded-lg text-xs text-white/70">
            0.25x
          </div>
        )}
      </div>

      {/* Keyframe description */}
      {step.keyframes[currentKF] && (
        <div className="bg-primary/10 border border-primary/20 rounded-xl p-4">
          <p className="text-sm text-text font-medium">Ключевой момент {currentKF + 1}/{step.keyframes.length}</p>
          <p className="text-sm text-white/60 mt-1">{step.keyframes[currentKF].description}</p>
        </div>
      )}

      {!allViewed ? (
        currentKF === 0 && paused ? (
          <Button onClick={handleStart} className="w-full">
            <Play size={14} /> Начать разбор
          </Button>
        ) : (
          <Button onClick={handleContinue} className="w-full">
            <SkipForward size={14} /> {currentKF >= step.keyframes.length - 1 ? "Завершить" : "Далее"}
          </Button>
        )
      ) : (
        <Button onClick={onNext} className="w-full">
          Завершить разбор
        </Button>
      )}
    </div>
  )
}
