import { PoseLandmarker, FilesetResolver, type NormalizedLandmark } from "@mediapipe/tasks-vision"

export type Landmark = { x: number; y: number; z: number }

class PoseService {
  private landmarker: PoseLandmarker | null = null
  private _ready = false

  get ready() { return this._ready }

  async init() {
    if (this._ready) return
    try {
      const vision = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm"
      )
      this.landmarker = await PoseLandmarker.createFromOptions(vision, {
        baseOptions: {
          modelAssetPath: "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task",
          delegate: "GPU",
        },
        runningMode: "VIDEO",
        numPoses: 1,
      })
      this._ready = true
    } catch (err) {
      console.error("Failed to init PoseLandmarker:", err)
      // Fallback to CPU
      try {
        const vision = await FilesetResolver.forVisionTasks(
          "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm"
        )
        this.landmarker = await PoseLandmarker.createFromOptions(vision, {
          baseOptions: {
            modelAssetPath: "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task",
            delegate: "CPU",
          },
          runningMode: "VIDEO",
          numPoses: 1,
        })
        this._ready = true
      } catch (err2) {
        console.error("Failed to init PoseLandmarker (CPU fallback):", err2)
      }
    }
  }

  detect(videoFrame: HTMLVideoElement, timestamp: number): Landmark[] | null {
    if (!this.landmarker) return null
    try {
      const result = this.landmarker.detectForVideo(videoFrame, timestamp)
      if (result.landmarks && result.landmarks.length > 0) {
        return result.landmarks[0].map((l: NormalizedLandmark) => ({ x: l.x, y: l.y, z: l.z }))
      }
    } catch {
      // Frame detection failed — skip
    }
    return null
  }

  destroy() {
    this.landmarker?.close()
    this.landmarker = null
    this._ready = false
  }
}

export const poseService = new PoseService()
