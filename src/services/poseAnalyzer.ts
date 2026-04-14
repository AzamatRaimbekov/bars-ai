import type { Landmark } from "./poseService"

// Joint definitions: [pointA, pointB (vertex), pointC]
const JOINT_DEFINITIONS: Record<string, [number, number, number]> = {
  leftElbow:     [11, 13, 15],
  rightElbow:    [12, 14, 16],
  leftShoulder:  [23, 11, 13],
  rightShoulder: [24, 12, 14],
  leftKnee:      [23, 25, 27],
  rightKnee:     [24, 26, 28],
  leftHip:       [11, 23, 25],
  rightHip:      [12, 24, 26],
  leftWrist:     [13, 15, 19],
  rightWrist:    [14, 16, 20],
}

function angle(a: Landmark, b: Landmark, c: Landmark): number {
  const radians = Math.atan2(c.y - b.y, c.x - b.x) - Math.atan2(a.y - b.y, a.x - b.x)
  let degrees = Math.abs(radians * 180 / Math.PI)
  if (degrees > 180) degrees = 360 - degrees
  return degrees
}

export function getJointAngles(landmarks: Landmark[]): Record<string, number> {
  const angles: Record<string, number> = {}
  for (const [name, [a, b, c]] of Object.entries(JOINT_DEFINITIONS)) {
    if (landmarks[a] && landmarks[b] && landmarks[c]) {
      angles[name] = angle(landmarks[a], landmarks[b], landmarks[c])
    }
  }
  return angles
}

export interface PoseComparison {
  score: number
  joints: Record<string, { score: number; diff: number }>
}

export function comparePoses(
  student: Record<string, number>,
  reference: Record<string, number>,
  tolerance = 15
): PoseComparison {
  let total = 0
  const joints: Record<string, { score: number; diff: number }> = {}
  const keys = Object.keys(reference)

  if (keys.length === 0) return { score: 0, joints }

  for (const key of keys) {
    const diff = Math.abs((student[key] || 0) - (reference[key] || 0))
    const score = Math.max(0, Math.round(100 - (diff / tolerance) * 100))
    joints[key] = { score, diff }
    total += score
  }

  return { score: Math.round(total / keys.length), joints }
}

/** Check if a timestamp lands on a musical beat */
export function isOnBeat(timestampMs: number, bpm: number, toleranceMs = 100): boolean {
  const beatInterval = 60000 / bpm
  const position = timestampMs % beatInterval
  return position < toleranceMs || position > beatInterval - toleranceMs
}

/** Calculate movement diversity from pose history */
export function diversityScore(poseHistory: Record<string, number>[], windowSize = 30): number {
  if (poseHistory.length < 2) return 0
  const recent = poseHistory.slice(-windowSize)
  const keys = Object.keys(recent[0] || {})
  if (keys.length === 0) return 0

  let totalVariance = 0
  for (const key of keys) {
    const values = recent.map(p => p[key] || 0)
    const mean = values.reduce((a, b) => a + b, 0) / values.length
    const variance = values.reduce((a, v) => a + (v - mean) ** 2, 0) / values.length
    totalVariance += variance
  }
  return Math.min(100, Math.round(totalVariance / keys.length / 10))
}

/** Calculate "cleanness" score — low jitter = high cleanness */
export function cleannessScore(poseHistory: Record<string, number>[], windowSize = 10): number {
  if (poseHistory.length < 3) return 50
  const recent = poseHistory.slice(-windowSize)
  const keys = Object.keys(recent[0] || {})
  if (keys.length === 0) return 50

  let totalJitter = 0
  for (const key of keys) {
    for (let i = 2; i < recent.length; i++) {
      const prev = recent[i - 1][key] || 0
      const curr = recent[i][key] || 0
      const prevPrev = recent[i - 2][key] || 0
      // Jitter = second derivative (acceleration)
      totalJitter += Math.abs(curr - 2 * prev + prevPrev)
    }
  }
  const avgJitter = totalJitter / (keys.length * Math.max(1, recent.length - 2))
  return Math.max(0, Math.min(100, Math.round(100 - avgJitter / 2)))
}

/** Calculate musicality — how often sharp movements align with beats */
export function musicalityScore(
  movementTimestamps: number[],
  bpm: number,
  toleranceMs = 120
): number {
  if (movementTimestamps.length === 0) return 0
  let onBeatCount = 0
  for (const ts of movementTimestamps) {
    if (isOnBeat(ts, bpm, toleranceMs)) onBeatCount++
  }
  return Math.round((onBeatCount / movementTimestamps.length) * 100)
}
