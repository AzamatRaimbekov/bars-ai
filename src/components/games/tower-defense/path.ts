import type { Point } from "./types";
import { CANVAS_W, CANVAS_H } from "./config";

const RAW_POINTS: Point[] = [
  { x: 0.15, y: 0.00 },
  { x: 0.15, y: 0.15 },
  { x: 0.85, y: 0.15 },
  { x: 0.85, y: 0.35 },
  { x: 0.15, y: 0.35 },
  { x: 0.15, y: 0.55 },
  { x: 0.85, y: 0.55 },
  { x: 0.85, y: 0.75 },
  { x: 0.50, y: 0.75 },
  { x: 0.50, y: 0.92 },
];

export const PATH_POINTS: Point[] = RAW_POINTS.map((p) => ({
  x: p.x * CANVAS_W,
  y: p.y * CANVAS_H,
}));

function buildDistances(pts: Point[]): number[] {
  const d = [0];
  for (let i = 1; i < pts.length; i++) {
    const dx = pts[i].x - pts[i - 1].x;
    const dy = pts[i].y - pts[i - 1].y;
    d.push(d[i - 1] + Math.sqrt(dx * dx + dy * dy));
  }
  return d;
}

const DISTANCES = buildDistances(PATH_POINTS);
const TOTAL_LENGTH = DISTANCES[DISTANCES.length - 1];

export function getPositionAlongPath(progress: number): Point {
  const clamped = Math.max(0, Math.min(1, progress));
  const targetDist = clamped * TOTAL_LENGTH;
  for (let i = 1; i < DISTANCES.length; i++) {
    if (DISTANCES[i] >= targetDist) {
      const segLen = DISTANCES[i] - DISTANCES[i - 1];
      const t = segLen === 0 ? 0 : (targetDist - DISTANCES[i - 1]) / segLen;
      return {
        x: PATH_POINTS[i - 1].x + (PATH_POINTS[i].x - PATH_POINTS[i - 1].x) * t,
        y: PATH_POINTS[i - 1].y + (PATH_POINTS[i].y - PATH_POINTS[i - 1].y) * t,
      };
    }
  }
  return PATH_POINTS[PATH_POINTS.length - 1];
}

export const TOWER_SLOTS: Point[] = [
  { x: 0.38 * CANVAS_W, y: 0.08 * CANVAS_H },
  { x: 0.60 * CANVAS_W, y: 0.24 * CANVAS_H },
  { x: 0.38 * CANVAS_W, y: 0.24 * CANVAS_H },
  { x: 0.60 * CANVAS_W, y: 0.44 * CANVAS_H },
  { x: 0.38 * CANVAS_W, y: 0.44 * CANVAS_H },
  { x: 0.60 * CANVAS_W, y: 0.64 * CANVAS_H },
  { x: 0.30 * CANVAS_W, y: 0.64 * CANVAS_H },
  { x: 0.50 * CANVAS_W, y: 0.83 * CANVAS_H },
];
