import type { EnemyKind, TowerKind } from "./types";

export const COINS_PER_CORRECT = 25;
export const QUESTION_TIME = 12;
export const QUESTIONS_PER_WAVE = 3;
export const INITIAL_LIVES = 3;
export const MIN_WAVES = 5;
export const STARTING_COINS = 30;
export const CANVAS_W = 400;
export const CANVAS_H = 600;

export const ENEMY_CONFIG: Record<EnemyKind, { emoji: string; color: string; hp: number; speed: number; size: number }> = {
  bug:    { emoji: "🐛", color: "#ef4444", hp: 2, speed: 0.06, size: 24 },
  glitch: { emoji: "⚡", color: "#f97316", hp: 3, speed: 0.045, size: 28 },
  virus:  { emoji: "🦠", color: "#a855f7", hp: 5, speed: 0.03, size: 34 },
  trojan: { emoji: "🐴", color: "#eab308", hp: 4, speed: 0.04, size: 30 },
  boss:   { emoji: "💀", color: "#dc2626", hp: 15, speed: 0.02, size: 42 },
};

export const TOWER_CONFIG: Record<TowerKind, { emoji: string; color: string; cost: number; damage: number; fireRate: number; range: number }> = {
  blaster: { emoji: "🔮", color: "#3b82f6", cost: 30, damage: 1, fireRate: 0.5, range: 80 },
  zapper:  { emoji: "⚡", color: "#8b5cf6", cost: 50, damage: 2, fireRate: 1.0, range: 110 },
  cannon:  { emoji: "🎯", color: "#10b981", cost: 80, damage: 3, fireRate: 2.0, range: 65 },
};

export const UPGRADE_COSTS: Record<2 | 3, number> = { 2: 40, 3: 70 };
export const UPGRADE_DAMAGE_MULT: Record<1 | 2 | 3, number> = { 1: 1, 2: 1.5, 3: 2 };
export const UPGRADE_RANGE_MULT: Record<1 | 2 | 3, number> = { 1: 1, 2: 1.15, 3: 1.3 };

export const BG_COLOR = "#111118";
export const ROAD_COLOR = "#1e1e2e";
export const ROAD_BORDER = "#ffffff10";
export const ROAD_DASH = "#ffffff08";
export const SLOT_BORDER = "#ffffff15";
export const HUD_BG = "#00000099";
