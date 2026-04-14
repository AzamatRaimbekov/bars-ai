import { useEffect, useRef, useState, useCallback } from "react"
import { poseService, type Landmark } from "@/services/poseService"
import { Camera, CameraOff, Loader2 } from "lucide-react"

interface CameraViewProps {
  onFrame?: (landmarks: Landmark[]) => void
  jointColors?: Record<string, string>
  mirrored?: boolean
  active?: boolean
  className?: string
}

// MediaPipe Pose connections (pairs of landmark indices)
const POSE_CONNECTIONS = [
  [11,12],[11,13],[13,15],[12,14],[14,16], // arms
  [11,23],[12,24],[23,24], // torso
  [23,25],[25,27],[24,26],[26,28], // legs
]

export function CameraView({ onFrame, jointColors, mirrored = true, active = true, className = "" }: CameraViewProps) {
  const videoRef = useRef<HTMLVideoElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const animRef = useRef<number>(0)
  const [ready, setReady] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [initializing, setInitializing] = useState(true)

  // Init camera + MediaPipe
  useEffect(() => {
    if (!active) return
    let stream: MediaStream | null = null

    const setup = async () => {
      setInitializing(true)
      try {
        stream = await navigator.mediaDevices.getUserMedia({
          video: { width: 640, height: 480, facingMode: "user" }
        })
        if (videoRef.current) {
          videoRef.current.srcObject = stream
          await videoRef.current.play()
        }
        await poseService.init()
        setReady(true)
        setError(null)
      } catch (err) {
        console.error("Camera/MediaPipe init error:", err)
        setError("Не удалось получить доступ к камере")
      } finally {
        setInitializing(false)
      }
    }
    setup()

    return () => {
      if (stream) stream.getTracks().forEach(t => t.stop())
      cancelAnimationFrame(animRef.current)
    }
  }, [active])

  // Detection loop
  useEffect(() => {
    if (!ready || !active) return

    const loop = () => {
      if (videoRef.current && canvasRef.current) {
        const landmarks = poseService.detect(videoRef.current, performance.now())
        if (landmarks) {
          drawSkeleton(canvasRef.current, landmarks, jointColors, mirrored)
          onFrame?.(landmarks)
        }
      }
      animRef.current = requestAnimationFrame(loop)
    }
    animRef.current = requestAnimationFrame(loop)

    return () => cancelAnimationFrame(animRef.current)
  }, [ready, active, onFrame, jointColors, mirrored])

  return (
    <div className={`relative bg-black rounded-2xl overflow-hidden ${className}`}>
      <video
        ref={videoRef}
        className="w-full h-full object-cover"
        style={{ transform: mirrored ? "scaleX(-1)" : "none" }}
        playsInline
        muted
      />
      <canvas
        ref={canvasRef}
        className="absolute inset-0 w-full h-full"
        width={640}
        height={480}
      />
      {initializing && (
        <div className="absolute inset-0 flex items-center justify-center bg-black/80">
          <div className="text-center">
            <Loader2 className="animate-spin text-primary mx-auto mb-2" size={32} />
            <p className="text-sm text-white/60">Загрузка камеры и MediaPipe...</p>
          </div>
        </div>
      )}
      {error && (
        <div className="absolute inset-0 flex items-center justify-center bg-black/80">
          <div className="text-center">
            <CameraOff className="text-red-400 mx-auto mb-2" size={32} />
            <p className="text-sm text-red-400">{error}</p>
          </div>
        </div>
      )}
    </div>
  )
}

function drawSkeleton(
  canvas: HTMLCanvasElement,
  landmarks: Landmark[],
  jointColors?: Record<string, string>,
  mirrored = true
) {
  const ctx = canvas.getContext("2d")
  if (!ctx) return
  const w = canvas.width
  const h = canvas.height
  ctx.clearRect(0, 0, w, h)

  // Draw connections
  ctx.strokeStyle = "rgba(255,255,255,0.4)"
  ctx.lineWidth = 2
  for (const [a, b] of POSE_CONNECTIONS) {
    const la = landmarks[a], lb = landmarks[b]
    if (!la || !lb) continue
    const ax = mirrored ? (1 - la.x) * w : la.x * w
    const ay = la.y * h
    const bx = mirrored ? (1 - lb.x) * w : lb.x * w
    const by = lb.y * h
    ctx.beginPath()
    ctx.moveTo(ax, ay)
    ctx.lineTo(bx, by)
    ctx.stroke()
  }

  // Draw joints
  const JOINT_MAP: Record<string, number[]> = {
    leftShoulder: [11], rightShoulder: [12],
    leftElbow: [13], rightElbow: [14],
    leftWrist: [15], rightWrist: [16],
    leftHip: [23], rightHip: [24],
    leftKnee: [25], rightKnee: [26],
  }

  for (const [name, indices] of Object.entries(JOINT_MAP)) {
    const color = jointColors?.[name] || "#00FF88"
    for (const idx of indices) {
      const l = landmarks[idx]
      if (!l) continue
      const x = mirrored ? (1 - l.x) * w : l.x * w
      const y = l.y * h
      ctx.fillStyle = color
      ctx.beginPath()
      ctx.arc(x, y, 5, 0, Math.PI * 2)
      ctx.fill()
    }
  }
}
