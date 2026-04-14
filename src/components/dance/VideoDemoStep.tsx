import { useState } from "react"
import { Play, SkipForward } from "lucide-react"
import { Button } from "@/components/ui/Button"

interface StepVideoDemo {
  type: "video-demo"
  title: string
  videos: { url: string; angle: string }[]
  description?: string
}

export function VideoDemoStep({ step, onNext }: { step: StepVideoDemo; onNext: () => void }) {
  const [activeAngle, setActiveAngle] = useState(0)
  const [playbackRate, setPlaybackRate] = useState(1)
  const rates = [0.25, 0.5, 1]

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text">{step.title}</p>

      {/* Angle tabs */}
      {step.videos.length > 1 && (
        <div className="flex gap-2">
          {step.videos.map((v, i) => (
            <button key={i} onClick={() => setActiveAngle(i)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all cursor-pointer ${
                i === activeAngle ? "bg-primary/20 text-primary border border-primary/30" : "bg-white/5 text-white/50 border border-white/10"
              }`}>
              {v.angle === "front" ? "Спереди" : v.angle === "side" ? "Сбоку" : "Сзади"}
            </button>
          ))}
        </div>
      )}

      {/* Video player */}
      <div className="relative rounded-2xl overflow-hidden bg-black">
        <video
          key={step.videos[activeAngle]?.url}
          src={step.videos[activeAngle]?.url}
          controls
          className="w-full"
          style={{  }}
          onLoadedMetadata={(e) => { (e.target as HTMLVideoElement).playbackRate = playbackRate }}
        />
      </div>

      {/* Speed controls */}
      <div className="flex items-center gap-2">
        <span className="text-xs text-white/40">Скорость:</span>
        {rates.map(r => (
          <button key={r} onClick={() => setPlaybackRate(r)}
            className={`px-2.5 py-1 rounded-lg text-xs font-medium cursor-pointer ${
              r === playbackRate ? "bg-primary/20 text-primary" : "bg-white/5 text-white/50"
            }`}>
            {r}x
          </button>
        ))}
      </div>

      {step.description && <p className="text-sm text-white/50">{step.description}</p>}

      <Button onClick={onNext} className="w-full">
        Далее <SkipForward size={14} />
      </Button>
    </div>
  )
}
