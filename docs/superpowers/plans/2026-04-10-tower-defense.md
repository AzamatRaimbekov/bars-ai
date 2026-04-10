# Tower Defense Game Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Tower Defense mini-game as a step type in the course system — players answer lesson questions for coins, build/upgrade towers, and defend against waves of enemies.

**Architecture:** New step type `"tower-defense"` rendered in CourseStepPlayer. Game logic is pure functions in `engine.ts`, rendering via HTML5 Canvas in `TDCanvas.tsx`, React wrapper `TowerDefenseStep.tsx` manages phases (questions → build → battle → result). Questions are extracted from sibling steps of the same lesson.

**Tech Stack:** React, TypeScript, HTML5 Canvas, requestAnimationFrame

---

### Task 1: Types and config

**Files:**
- Create: `src/components/games/tower-defense/types.ts`
- Create: `src/components/games/tower-defense/config.ts`

- [ ] **Step 1: Create types.ts**

```typescript
// src/components/games/tower-defense/types.ts

export interface Point {
  x: number;
  y: number;
}

export type TowerKind = "blaster" | "zapper" | "cannon";

export interface Tower {
  id: string;
  kind: TowerKind;
  level: 1 | 2 | 3;
  slotIndex: number;
  pos: Point;
  cooldown: number; // seconds remaining until next shot
}

export type EnemyKind = "bug" | "glitch" | "virus" | "trojan" | "boss";

export interface Enemy {
  id: string;
  kind: EnemyKind;
  hp: number;
  maxHp: number;
  progress: number; // 0..1 along path
  speed: number; // progress per second
  flashTimer: number; // >0 means show white flash
}

export interface Projectile {
  id: string;
  from: Point;
  to: Point;
  color: string;
  timer: number; // seconds remaining
  isAoe: boolean;
  aoeRadius: number;
}

export interface WaveConfig {
  enemies: { kind: EnemyKind; count: number; delay: number }[];
}

export type GamePhase = "questions" | "build" | "battle" | "result";

export interface GameState {
  phase: GamePhase;
  coins: number;
  lives: number;
  maxLives: number;
  wave: number;
  totalWaves: number;
  towers: Tower[];
  enemies: Enemy[];
  projectiles: Projectile[];
  spawnQueue: { kind: EnemyKind; delay: number }[];
  spawnTimer: number;
  waveDone: boolean;
  selectedSlot: number | null;
  selectedTower: string | null;
}

export interface TDQuestion {
  type: "quiz" | "true-false" | "type-answer" | "fill-blank";
  question: string;
  options?: { id: string; text: string; correct: boolean }[];
  statement?: string;
  correct?: boolean;
  acceptedAnswers?: string[];
  text?: string;
  answers?: string[];
}
```

- [ ] **Step 2: Create config.ts**

```typescript
// src/components/games/tower-defense/config.ts

import type { EnemyKind, TowerKind } from "./types";

export const COINS_PER_CORRECT = 30;
export const QUESTION_TIME = 15; // seconds
export const QUESTIONS_PER_WAVE = 4;
export const INITIAL_LIVES = 3;

export const CANVAS_W = 400;
export const CANVAS_H = 600;

export const ENEMY_CONFIG: Record<EnemyKind, {
  emoji: string;
  color: string;
  hp: number;
  speed: number;
  size: number;
}> = {
  bug:    { emoji: "🐛", color: "#ef4444", hp: 2, speed: 0.06, size: 24 },
  glitch: { emoji: "⚡", color: "#f97316", hp: 3, speed: 0.045, size: 28 },
  virus:  { emoji: "🦠", color: "#a855f7", hp: 5, speed: 0.03, size: 34 },
  trojan: { emoji: "🐴", color: "#eab308", hp: 4, speed: 0.04, size: 30 },
  boss:   { emoji: "💀", color: "#dc2626", hp: 15, speed: 0.02, size: 42 },
};

export const TOWER_CONFIG: Record<TowerKind, {
  emoji: string;
  color: string;
  cost: number;
  damage: number;
  fireRate: number; // seconds between shots
  range: number; // pixels
}> = {
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
```

- [ ] **Step 3: Commit**

```bash
git add src/components/games/tower-defense/types.ts src/components/games/tower-defense/config.ts
git commit -m "feat(td): add types and config for Tower Defense game"
```

---

### Task 2: Path and slot definitions

**Files:**
- Create: `src/components/games/tower-defense/path.ts`

- [ ] **Step 1: Create path.ts**

```typescript
// src/components/games/tower-defense/path.ts

import type { Point } from "./types";
import { CANVAS_W, CANVAS_H } from "./config";

// Road waypoints: Friendly Road style with turns
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

// Convert normalized 0..1 coords to canvas pixels
export const PATH_POINTS: Point[] = RAW_POINTS.map((p) => ({
  x: p.x * CANVAS_W,
  y: p.y * CANVAS_H,
}));

// Cumulative distances for interpolation
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

/** Get canvas position for a progress value 0..1 along the path. */
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

// Tower slots: positions near the road but not on it
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
```

- [ ] **Step 2: Commit**

```bash
git add src/components/games/tower-defense/path.ts
git commit -m "feat(td): add path waypoints and tower slot positions"
```

---

### Task 3: Game engine (pure logic)

**Files:**
- Create: `src/components/games/tower-defense/engine.ts`

- [ ] **Step 1: Create engine.ts**

```typescript
// src/components/games/tower-defense/engine.ts

import type { GameState, Enemy, Tower, Projectile, EnemyKind, TowerKind, WaveConfig } from "./types";
import { ENEMY_CONFIG, TOWER_CONFIG, UPGRADE_COSTS, UPGRADE_DAMAGE_MULT, UPGRADE_RANGE_MULT, INITIAL_LIVES } from "./config";
import { getPositionAlongPath, TOWER_SLOTS } from "./path";

let _nextId = 0;
function uid(): string {
  return "e" + (++_nextId);
}

// ── Wave generation ──────────────────────────────────────────────────────

export function generateWaves(totalWaves: number): WaveConfig[] {
  const waves: WaveConfig[] = [];
  for (let w = 0; w < totalWaves; w++) {
    const enemies: WaveConfig["enemies"] = [];
    const base = 3 + w * 2;

    if (w < totalWaves - 1) {
      // Normal waves
      enemies.push({ kind: "bug", count: base, delay: 0.8 });
      if (w >= 1) enemies.push({ kind: "glitch", count: Math.floor(base * 0.5), delay: 1.2 });
      if (w >= 2) enemies.push({ kind: "virus", count: Math.floor(base * 0.3), delay: 1.5 });
      if (w >= 2) enemies.push({ kind: "trojan", count: Math.floor(base * 0.2), delay: 1.3 });
    } else {
      // Boss wave
      enemies.push({ kind: "bug", count: base, delay: 0.6 });
      enemies.push({ kind: "glitch", count: Math.floor(base * 0.5), delay: 1.0 });
      enemies.push({ kind: "virus", count: 2, delay: 1.5 });
      enemies.push({ kind: "boss", count: 1, delay: 2.0 });
    }
    waves.push({ enemies });
  }
  return waves;
}

// ── Spawn queue from wave config ─────────────────────────────────────────

export function buildSpawnQueue(wave: WaveConfig): { kind: EnemyKind; delay: number }[] {
  const queue: { kind: EnemyKind; delay: number }[] = [];
  for (const group of wave.enemies) {
    for (let i = 0; i < group.count; i++) {
      queue.push({ kind: group.kind, delay: group.delay });
    }
  }
  // Shuffle lightly — interleave types
  for (let i = queue.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [queue[i], queue[j]] = [queue[j], queue[i]];
  }
  return queue;
}

// ── Create initial state ─────────────────────────────────────────────────

export function createInitialState(totalWaves: number): GameState {
  return {
    phase: "questions",
    coins: 0,
    lives: INITIAL_LIVES,
    maxLives: INITIAL_LIVES,
    wave: 0,
    totalWaves,
    towers: [],
    enemies: [],
    projectiles: [],
    spawnQueue: [],
    spawnTimer: 0,
    waveDone: false,
    selectedSlot: null,
    selectedTower: null,
  };
}

// ── Tower actions ────────────────────────────────────────────────────────

export function canBuyTower(state: GameState, kind: TowerKind): boolean {
  return state.coins >= TOWER_CONFIG[kind].cost;
}

export function placeTower(state: GameState, slotIndex: number, kind: TowerKind): GameState {
  const cost = TOWER_CONFIG[kind].cost;
  if (state.coins < cost) return state;
  if (state.towers.some((t) => t.slotIndex === slotIndex)) return state;

  const tower: Tower = {
    id: uid(),
    kind,
    level: 1,
    slotIndex,
    pos: TOWER_SLOTS[slotIndex],
    cooldown: 0,
  };

  return {
    ...state,
    coins: state.coins - cost,
    towers: [...state.towers, tower],
    selectedSlot: null,
  };
}

export function canUpgradeTower(state: GameState, towerId: string): boolean {
  const tower = state.towers.find((t) => t.id === towerId);
  if (!tower || tower.level >= 3) return false;
  const cost = UPGRADE_COSTS[(tower.level + 1) as 2 | 3];
  return state.coins >= cost;
}

export function upgradeTower(state: GameState, towerId: string): GameState {
  const tower = state.towers.find((t) => t.id === towerId);
  if (!tower || tower.level >= 3) return state;
  const nextLevel = (tower.level + 1) as 2 | 3;
  const cost = UPGRADE_COSTS[nextLevel];
  if (state.coins < cost) return state;

  return {
    ...state,
    coins: state.coins - cost,
    towers: state.towers.map((t) =>
      t.id === towerId ? { ...t, level: nextLevel } : t
    ),
    selectedTower: null,
  };
}

// ── Battle tick ──────────────────────────────────────────────────────────

function spawnEnemy(kind: EnemyKind): Enemy {
  const cfg = ENEMY_CONFIG[kind];
  return {
    id: uid(),
    kind,
    hp: cfg.hp,
    maxHp: cfg.hp,
    progress: 0,
    speed: cfg.speed,
    flashTimer: 0,
  };
}

function dist(a: { x: number; y: number }, b: { x: number; y: number }): number {
  const dx = a.x - b.x;
  const dy = a.y - b.y;
  return Math.sqrt(dx * dx + dy * dy);
}

export function tick(state: GameState, dt: number): GameState {
  if (state.phase !== "battle") return state;

  let { enemies, towers, projectiles, spawnQueue, spawnTimer, lives, waveDone, coins } = state;

  // Clone arrays
  enemies = enemies.map((e) => ({ ...e }));
  towers = towers.map((t) => ({ ...t }));
  projectiles = projectiles.map((p) => ({ ...p }));
  spawnQueue = [...spawnQueue];

  // 1. Spawn enemies
  spawnTimer -= dt;
  if (spawnTimer <= 0 && spawnQueue.length > 0) {
    const next = spawnQueue.shift()!;
    enemies.push(spawnEnemy(next.kind));
    spawnTimer = next.delay;
  }

  // 2. Move enemies
  const survived: Enemy[] = [];
  for (const e of enemies) {
    e.progress += e.speed * dt;
    e.flashTimer = Math.max(0, e.flashTimer - dt);

    // Glitch teleport
    if (e.kind === "glitch" && Math.random() < 0.005) {
      e.progress += 0.02;
    }

    if (e.progress >= 1) {
      lives--;
    } else if (e.hp > 0) {
      survived.push(e);
    } else {
      // Dead — Trojan spawns 2 bugs
      if (e.kind === "trojan") {
        const b1 = spawnEnemy("bug");
        b1.progress = e.progress;
        const b2 = spawnEnemy("bug");
        b2.progress = Math.max(0, e.progress - 0.02);
        survived.push(b1, b2);
      }
    }
  }
  enemies = survived;

  // 3. Tower shooting
  const newProjectiles: Projectile[] = [];
  for (const tower of towers) {
    tower.cooldown -= dt;
    if (tower.cooldown > 0) continue;

    const cfg = TOWER_CONFIG[tower.kind];
    const range = cfg.range * UPGRADE_RANGE_MULT[tower.level];
    const damage = cfg.damage * UPGRADE_DAMAGE_MULT[tower.level];

    // Find closest enemy in range
    let target: Enemy | null = null;
    let minDist = Infinity;
    for (const e of enemies) {
      if (e.hp <= 0) continue;
      const ePos = getPositionAlongPath(e.progress);
      const d = dist(tower.pos, ePos);
      if (d <= range && d < minDist) {
        target = e;
        minDist = d;
      }
    }

    if (target) {
      tower.cooldown = cfg.fireRate;
      const targetPos = getPositionAlongPath(target.progress);

      if (tower.kind === "cannon") {
        // AoE damage
        for (const e of enemies) {
          const ePos = getPositionAlongPath(e.progress);
          if (dist(targetPos, ePos) <= 40) {
            e.hp -= damage;
            e.flashTimer = 0.1;
          }
        }
        newProjectiles.push({
          id: uid(), from: tower.pos, to: targetPos,
          color: cfg.color, timer: 0.3, isAoe: true, aoeRadius: 40,
        });
      } else {
        target.hp -= damage;
        target.flashTimer = 0.1;
        newProjectiles.push({
          id: uid(), from: tower.pos, to: targetPos,
          color: cfg.color, timer: 0.2, isAoe: false, aoeRadius: 0,
        });
      }
    }
  }

  // 4. Update projectiles
  projectiles = [...projectiles, ...newProjectiles]
    .map((p) => ({ ...p, timer: p.timer - dt }))
    .filter((p) => p.timer > 0);

  // 5. Check wave done
  waveDone = spawnQueue.length === 0 && enemies.length === 0;

  return {
    ...state,
    enemies,
    towers,
    projectiles,
    spawnQueue,
    spawnTimer,
    lives: Math.max(0, lives),
    waveDone,
    coins,
  };
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/games/tower-defense/engine.ts
git commit -m "feat(td): add game engine with spawning, movement, shooting, and wave logic"
```

---

### Task 4: Question extraction utility

**Files:**
- Create: `src/components/games/tower-defense/questions.ts`

- [ ] **Step 1: Create questions.ts**

```typescript
// src/components/games/tower-defense/questions.ts

import type { LessonStep } from "@/services/courseApi";
import type { TDQuestion } from "./types";
import { QUESTIONS_PER_WAVE } from "./config";

/** Extract answerable questions from sibling lesson steps. */
export function extractQuestions(steps: LessonStep[]): TDQuestion[] {
  const questions: TDQuestion[] = [];

  for (const step of steps) {
    if (step.type === "tower-defense") continue;

    if (step.type === "quiz") {
      questions.push({
        type: "quiz",
        question: step.question,
        options: step.options,
      });
    } else if (step.type === "true-false") {
      questions.push({
        type: "true-false",
        question: step.statement,
        statement: step.statement,
        correct: step.correct,
      });
    } else if (step.type === "type-answer") {
      questions.push({
        type: "type-answer",
        question: step.question,
        acceptedAnswers: step.acceptedAnswers,
      });
    } else if (step.type === "fill-blank") {
      questions.push({
        type: "fill-blank",
        question: "Заполните пропуск",
        text: step.text,
        answers: step.answers,
      });
    }
  }

  return questions;
}

/** Shuffle and split questions into wave-sized groups. */
export function splitIntoWaves(questions: TDQuestion[]): TDQuestion[][] {
  // Shuffle
  const shuffled = [...questions];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }

  const waves: TDQuestion[][] = [];
  for (let i = 0; i < shuffled.length; i += QUESTIONS_PER_WAVE) {
    waves.push(shuffled.slice(i, i + QUESTIONS_PER_WAVE));
  }

  // At least 1 wave
  if (waves.length === 0) {
    waves.push([]);
  }

  return waves;
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/games/tower-defense/questions.ts
git commit -m "feat(td): add question extraction and wave splitting utility"
```

---

### Task 5: Canvas renderer

**Files:**
- Create: `src/components/games/tower-defense/TDCanvas.tsx`

- [ ] **Step 1: Create TDCanvas.tsx**

```tsx
// src/components/games/tower-defense/TDCanvas.tsx

import { useRef, useEffect, useCallback } from "react";
import type { GameState, Point } from "./types";
import { CANVAS_W, CANVAS_H, BG_COLOR, ROAD_COLOR, SLOT_BORDER, ENEMY_CONFIG, TOWER_CONFIG, UPGRADE_RANGE_MULT, HUD_BG } from "./config";
import { PATH_POINTS, TOWER_SLOTS, getPositionAlongPath } from "./path";
import { tick } from "./engine";

interface Props {
  state: GameState;
  onStateChange: (s: GameState) => void;
  onSlotTap: (slotIndex: number) => void;
  onTowerTap: (towerId: string) => void;
}

export default function TDCanvas({ state, onStateChange, onSlotTap, onTowerTap }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const stateRef = useRef(state);
  const rafRef = useRef(0);
  const lastTimeRef = useRef(0);

  stateRef.current = state;

  // Game loop (only during battle phase)
  useEffect(() => {
    if (state.phase !== "battle") return;

    lastTimeRef.current = performance.now();

    const loop = (now: number) => {
      const dt = Math.min((now - lastTimeRef.current) / 1000, 0.1);
      lastTimeRef.current = now;
      const next = tick(stateRef.current, dt);
      stateRef.current = next;
      onStateChange(next);
      draw(next);
      rafRef.current = requestAnimationFrame(loop);
    };

    rafRef.current = requestAnimationFrame(loop);
    return () => cancelAnimationFrame(rafRef.current);
  }, [state.phase]);

  // Static draw when not in battle
  useEffect(() => {
    if (state.phase === "battle") return;
    draw(state);
  }, [state]);

  const draw = useCallback((s: GameState) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const dpr = window.devicePixelRatio || 1;
    canvas.width = CANVAS_W * dpr;
    canvas.height = CANVAS_H * dpr;
    ctx.scale(dpr, dpr);

    // Background
    ctx.fillStyle = BG_COLOR;
    ctx.fillRect(0, 0, CANVAS_W, CANVAS_H);

    // Road
    ctx.beginPath();
    ctx.moveTo(PATH_POINTS[0].x, PATH_POINTS[0].y);
    for (let i = 1; i < PATH_POINTS.length; i++) {
      ctx.lineTo(PATH_POINTS[i].x, PATH_POINTS[i].y);
    }
    ctx.strokeStyle = ROAD_COLOR;
    ctx.lineWidth = 48;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.stroke();

    // Road dashes
    ctx.setLineDash([10, 8]);
    ctx.strokeStyle = "#ffffff08";
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.setLineDash([]);

    // BASE label at end
    const endPt = PATH_POINTS[PATH_POINTS.length - 1];
    ctx.fillStyle = "#4ade80";
    roundRect(ctx, endPt.x - 32, endPt.y - 12, 64, 24, 8);
    ctx.fill();
    ctx.fillStyle = "#000";
    ctx.font = "bold 10px system-ui";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("BASE", endPt.x, endPt.y);

    // Tower slots (empty)
    TOWER_SLOTS.forEach((slot, i) => {
      if (s.towers.some((t) => t.slotIndex === i)) return;
      ctx.strokeStyle = s.selectedSlot === i ? "#ffffff60" : SLOT_BORDER;
      ctx.lineWidth = 1.5;
      ctx.setLineDash([5, 4]);
      roundRect(ctx, slot.x - 24, slot.y - 24, 48, 48, 14);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ffffff15";
      ctx.font = "20px system-ui";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText("+", slot.x, slot.y);
    });

    // Towers
    for (const tower of s.towers) {
      const cfg = TOWER_CONFIG[tower.kind];
      const sz = 20 + tower.level * 4;

      // Range ring (show when selected)
      if (s.selectedTower === tower.id) {
        const range = cfg.range * UPGRADE_RANGE_MULT[tower.level];
        ctx.beginPath();
        ctx.arc(tower.pos.x, tower.pos.y, range, 0, Math.PI * 2);
        ctx.strokeStyle = cfg.color + "30";
        ctx.lineWidth = 1;
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Tower body
      ctx.fillStyle = cfg.color;
      ctx.shadowColor = cfg.color;
      ctx.shadowBlur = tower.level >= 3 ? 15 : tower.level >= 2 ? 8 : 0;
      roundRect(ctx, tower.pos.x - sz / 2, tower.pos.y - sz / 2, sz, sz, sz * 0.3);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Level 2+ border
      if (tower.level >= 2) {
        ctx.strokeStyle = "#ffffff30";
        ctx.lineWidth = 1.5;
        roundRect(ctx, tower.pos.x - sz / 2, tower.pos.y - sz / 2, sz, sz, sz * 0.3);
        ctx.stroke();
      }

      // Emoji
      ctx.font = `${sz * 0.55}px system-ui`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(cfg.emoji, tower.pos.x, tower.pos.y);
    }

    // Enemies
    for (const enemy of s.enemies) {
      const pos = getPositionAlongPath(enemy.progress);
      const cfg = ENEMY_CONFIG[enemy.kind];
      const sz = cfg.size;

      // Shadow
      ctx.shadowColor = cfg.color;
      ctx.shadowBlur = 8;
      ctx.fillStyle = enemy.flashTimer > 0 ? "#ffffff" : cfg.color;
      roundRect(ctx, pos.x - sz / 2, pos.y - sz / 2, sz, sz, sz * 0.35);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Emoji
      ctx.font = `${sz * 0.55}px system-ui`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(cfg.emoji, pos.x, pos.y);

      // HP bar
      if (enemy.hp < enemy.maxHp) {
        const barW = sz;
        const barH = 3;
        const barX = pos.x - barW / 2;
        const barY = pos.y - sz / 2 - 6;
        ctx.fillStyle = "#00000080";
        roundRect(ctx, barX, barY, barW, barH, 1.5);
        ctx.fill();
        ctx.fillStyle = cfg.color;
        roundRect(ctx, barX, barY, barW * (enemy.hp / enemy.maxHp), barH, 1.5);
        ctx.fill();
      }
    }

    // Projectiles
    for (const p of s.projectiles) {
      ctx.globalAlpha = Math.min(1, p.timer * 5);
      if (p.isAoe) {
        ctx.beginPath();
        ctx.arc(p.to.x, p.to.y, p.aoeRadius * (1 - p.timer), 0, Math.PI * 2);
        ctx.strokeStyle = p.color;
        ctx.lineWidth = 2;
        ctx.stroke();
      } else {
        ctx.beginPath();
        ctx.moveTo(p.from.x, p.from.y);
        ctx.lineTo(p.to.x, p.to.y);
        ctx.strokeStyle = p.color;
        ctx.lineWidth = 2;
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
    }

    // HUD
    drawHUD(ctx, s);
  }, []);

  function drawHUD(ctx: CanvasRenderingContext2D, s: GameState) {
    const y = 14;
    // Coins
    ctx.fillStyle = HUD_BG;
    roundRect(ctx, 8, y - 8, 70, 22, 11);
    ctx.fill();
    ctx.fillStyle = "#eab308";
    ctx.font = "bold 11px system-ui";
    ctx.textAlign = "left";
    ctx.fillText(`⭐ ${s.coins}`, 16, y + 4);

    // Lives
    ctx.fillStyle = HUD_BG;
    roundRect(ctx, 86, y - 8, 60, 22, 11);
    ctx.fill();
    ctx.fillStyle = "#ef4444";
    ctx.textAlign = "left";
    ctx.fillText("♥".repeat(s.lives), 94, y + 4);

    // Wave
    ctx.fillStyle = HUD_BG;
    roundRect(ctx, CANVAS_W - 88, y - 8, 80, 22, 11);
    ctx.fill();
    ctx.fillStyle = "#64748b";
    ctx.textAlign = "right";
    ctx.font = "11px system-ui";
    ctx.fillText(`Wave ${s.wave + 1}/${s.totalWaves}`, CANVAS_W - 16, y + 4);
  }

  // Handle taps
  const handleClick = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const scaleX = CANVAS_W / rect.width;
    const scaleY = CANVAS_H / rect.height;
    const x = (e.clientX - rect.left) * scaleX;
    const y = (e.clientY - rect.top) * scaleY;

    // Check tower tap
    for (const tower of state.towers) {
      const dx = x - tower.pos.x;
      const dy = y - tower.pos.y;
      if (Math.sqrt(dx * dx + dy * dy) < 28) {
        onTowerTap(tower.id);
        return;
      }
    }

    // Check slot tap
    for (let i = 0; i < TOWER_SLOTS.length; i++) {
      if (state.towers.some((t) => t.slotIndex === i)) continue;
      const dx = x - TOWER_SLOTS[i].x;
      const dy = y - TOWER_SLOTS[i].y;
      if (Math.sqrt(dx * dx + dy * dy) < 28) {
        onSlotTap(i);
        return;
      }
    }
  };

  return (
    <canvas
      ref={canvasRef}
      onClick={handleClick}
      style={{ width: "100%", maxWidth: CANVAS_W, height: "auto", aspectRatio: `${CANVAS_W}/${CANVAS_H}`, cursor: "pointer" }}
    />
  );
}

function roundRect(ctx: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + r);
  ctx.lineTo(x + w, y + h - r);
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  ctx.lineTo(x + r, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - r);
  ctx.lineTo(x, y + r);
  ctx.quadraticCurveTo(x, y, x + r, y);
  ctx.closePath();
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/games/tower-defense/TDCanvas.tsx
git commit -m "feat(td): add Canvas renderer with road, enemies, towers, projectiles, and HUD"
```

---

### Task 6: Main TowerDefenseStep React component

**Files:**
- Create: `src/components/games/tower-defense/TowerDefenseStep.tsx`

- [ ] **Step 1: Create TowerDefenseStep.tsx**

```tsx
// src/components/games/tower-defense/TowerDefenseStep.tsx

import { useState, useCallback, useMemo, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Star, Heart, Play, ArrowUpCircle, RotateCcw, Trophy, Skull } from "lucide-react";
import type { LessonStep } from "@/services/courseApi";
import type { GameState, TowerKind, TDQuestion } from "./types";
import { COINS_PER_CORRECT, QUESTION_TIME, TOWER_CONFIG, UPGRADE_COSTS } from "./config";
import { createInitialState, generateWaves, buildSpawnQueue, placeTower, upgradeTower, canBuyTower, canUpgradeTower } from "./engine";
import { extractQuestions, splitIntoWaves } from "./questions";
import TDCanvas from "./TDCanvas";

interface Props {
  allSteps: LessonStep[];
  onAnswer: (correct: boolean) => void;
}

export default function TowerDefenseStep({ allSteps, onAnswer }: Props) {
  // Extract and split questions once
  const allQuestions = useMemo(() => extractQuestions(allSteps), [allSteps]);
  const questionWaves = useMemo(() => splitIntoWaves(allQuestions), [allQuestions]);
  const totalWaves = questionWaves.length;
  const waves = useMemo(() => generateWaves(totalWaves), [totalWaves]);

  const [state, setState] = useState<GameState>(() => createInitialState(totalWaves));
  const [qIndex, setQIndex] = useState(0); // index within current wave's questions
  const [coinAnim, setCoinAnim] = useState<string | null>(null);
  const [timer, setTimer] = useState(QUESTION_TIME);
  const timerRef = useRef<ReturnType<typeof setInterval>>();

  const currentQuestions = questionWaves[state.wave] || [];
  const currentQ = currentQuestions[qIndex];

  // ── Question phase ────────────────────────────────────────────────────

  const startTimer = useCallback(() => {
    setTimer(QUESTION_TIME);
    clearInterval(timerRef.current);
    timerRef.current = setInterval(() => {
      setTimer((t) => {
        if (t <= 1) {
          clearInterval(timerRef.current);
          handleQuestionAnswer(false);
          return 0;
        }
        return t - 1;
      });
    }, 1000);
  }, []);

  const handleQuestionAnswer = useCallback((correct: boolean) => {
    clearInterval(timerRef.current);

    if (correct) {
      setState((s) => ({ ...s, coins: s.coins + COINS_PER_CORRECT }));
      setCoinAnim(`+${COINS_PER_CORRECT} ⭐`);
      setTimeout(() => setCoinAnim(null), 1000);
    }

    if (qIndex < currentQuestions.length - 1) {
      setQIndex((i) => i + 1);
      startTimer();
    } else {
      // Questions done → build phase
      setState((s) => ({ ...s, phase: "build" }));
    }
  }, [qIndex, currentQuestions.length, startTimer]);

  // Start timer on first render of questions phase
  const hasStartedTimer = useRef(false);
  if (state.phase === "questions" && !hasStartedTimer.current) {
    hasStartedTimer.current = true;
    setTimeout(startTimer, 500);
  }

  // ── Build phase ───────────────────────────────────────────────────────

  const handleSlotTap = useCallback((slotIndex: number) => {
    setState((s) => ({
      ...s,
      selectedSlot: s.selectedSlot === slotIndex ? null : slotIndex,
      selectedTower: null,
    }));
  }, []);

  const handleTowerTap = useCallback((towerId: string) => {
    setState((s) => ({
      ...s,
      selectedTower: s.selectedTower === towerId ? null : towerId,
      selectedSlot: null,
    }));
  }, []);

  const handleBuyTower = useCallback((kind: TowerKind) => {
    if (state.selectedSlot === null) return;
    setState((s) => placeTower(s, s.selectedSlot!, kind));
  }, [state.selectedSlot]);

  const handleUpgrade = useCallback(() => {
    if (!state.selectedTower) return;
    setState((s) => upgradeTower(s, s.selectedTower!));
  }, [state.selectedTower]);

  const handleStartWave = useCallback(() => {
    const waveConfig = waves[state.wave];
    const queue = buildSpawnQueue(waveConfig);
    setState((s) => ({
      ...s,
      phase: "battle",
      spawnQueue: queue,
      spawnTimer: 0.5,
      waveDone: false,
      selectedSlot: null,
      selectedTower: null,
    }));
  }, [state.wave, waves]);

  // ── Battle phase ──────────────────────────────────────────────────────

  const handleStateChange = useCallback((newState: GameState) => {
    if (newState.lives <= 0) {
      setState({ ...newState, phase: "result" });
      return;
    }
    if (newState.waveDone) {
      if (newState.wave >= newState.totalWaves - 1) {
        setState({ ...newState, phase: "result" });
      } else {
        // Next wave: go back to questions
        const nextWave = newState.wave + 1;
        setState({
          ...newState,
          phase: "questions",
          wave: nextWave,
          waveDone: false,
        });
        setQIndex(0);
        hasStartedTimer.current = false;
      }
      return;
    }
    setState(newState);
  }, []);

  // ── Retry ─────────────────────────────────────────────────────────────

  const handleRetry = useCallback(() => {
    setState(createInitialState(totalWaves));
    setQIndex(0);
    hasStartedTimer.current = false;
  }, [totalWaves]);

  // ── Render ────────────────────────────────────────────────────────────

  const won = state.phase === "result" && state.lives > 0;
  const stars = state.lives >= 3 ? 3 : state.lives >= 2 ? 2 : state.lives >= 1 ? 1 : 0;

  return (
    <div className="flex flex-col items-center gap-4 w-full max-w-[420px] mx-auto">
      {/* ── QUESTIONS PHASE ── */}
      {state.phase === "questions" && currentQ && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-bold text-text">Заработай монеты!</h3>
            <span className="text-sm text-yellow-400 font-semibold">⭐ {state.coins}</span>
          </div>

          {/* Timer bar */}
          <div className="h-1.5 bg-surface rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-primary rounded-full"
              animate={{ width: `${(timer / QUESTION_TIME) * 100}%` }}
              transition={{ duration: 0.3 }}
            />
          </div>

          {/* Question */}
          <div className="bg-surface rounded-xl p-4 border border-border">
            <p className="text-sm text-text-secondary mb-1">
              Вопрос {qIndex + 1} из {currentQuestions.length}
            </p>
            <p className="text-text font-medium mb-3">{currentQ.question}</p>

            {currentQ.type === "quiz" && currentQ.options && (
              <div className="flex flex-col gap-2">
                {currentQ.options.map((opt) => (
                  <button
                    key={opt.id}
                    onClick={() => handleQuestionAnswer(opt.correct)}
                    className="w-full text-left px-3 py-2.5 rounded-xl border border-border bg-white/5 text-text text-sm hover:border-primary/50 transition-colors cursor-pointer"
                  >
                    {opt.text}
                  </button>
                ))}
              </div>
            )}

            {currentQ.type === "true-false" && (
              <div className="flex gap-3">
                <button onClick={() => handleQuestionAnswer(currentQ.correct === true)} className="flex-1 py-2.5 rounded-xl border border-border bg-white/5 text-text text-sm hover:border-green-500/50 cursor-pointer">Верно</button>
                <button onClick={() => handleQuestionAnswer(currentQ.correct === false)} className="flex-1 py-2.5 rounded-xl border border-border bg-white/5 text-text text-sm hover:border-red-500/50 cursor-pointer">Неверно</button>
              </div>
            )}
          </div>

          {/* Coin animation */}
          <AnimatePresence>
            {coinAnim && (
              <motion.div
                initial={{ opacity: 1, y: 0 }}
                animate={{ opacity: 0, y: -40 }}
                exit={{ opacity: 0 }}
                className="fixed top-1/2 left-1/2 -translate-x-1/2 text-2xl font-bold text-yellow-400 pointer-events-none"
              >
                {coinAnim}
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      )}

      {/* ── BUILD PHASE ── */}
      {state.phase === "build" && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-text">Размести башни</h3>
            <button
              onClick={handleStartWave}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-primary text-white text-sm font-semibold cursor-pointer hover:bg-primary/90 transition-colors"
            >
              <Play size={14} /> Начать волну
            </button>
          </div>

          <TDCanvas state={state} onStateChange={setState} onSlotTap={handleSlotTap} onTowerTap={handleTowerTap} />

          {/* Tower shop */}
          {state.selectedSlot !== null && (
            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex gap-2 justify-center">
              {(["blaster", "zapper", "cannon"] as TowerKind[]).map((kind) => {
                const cfg = TOWER_CONFIG[kind];
                const affordable = canBuyTower(state, kind);
                return (
                  <button
                    key={kind}
                    onClick={() => handleBuyTower(kind)}
                    disabled={!affordable}
                    className={`flex flex-col items-center gap-1 px-4 py-3 rounded-xl border text-xs font-medium transition-colors cursor-pointer disabled:opacity-30 disabled:cursor-default ${
                      affordable ? "border-border bg-surface hover:border-white/30" : "border-border/50 bg-surface/50"
                    }`}
                  >
                    <span className="text-xl">{cfg.emoji}</span>
                    <span className="text-yellow-400">⭐ {cfg.cost}</span>
                  </button>
                );
              })}
            </motion.div>
          )}

          {/* Upgrade popup */}
          {state.selectedTower && (() => {
            const tower = state.towers.find((t) => t.id === state.selectedTower);
            if (!tower || tower.level >= 3) return null;
            const cost = UPGRADE_COSTS[(tower.level + 1) as 2 | 3];
            const affordable = canUpgradeTower(state, tower.id);
            return (
              <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex justify-center">
                <button
                  onClick={handleUpgrade}
                  disabled={!affordable}
                  className={`flex items-center gap-2 px-4 py-2.5 rounded-xl border text-sm font-medium cursor-pointer transition-colors disabled:opacity-30 disabled:cursor-default ${
                    affordable ? "border-primary/50 bg-primary/10 text-primary" : "border-border bg-surface text-text-secondary"
                  }`}
                >
                  <ArrowUpCircle size={16} /> Улучшить Lvl {tower.level + 1} (⭐ {cost})
                </button>
              </motion.div>
            );
          })()}
        </motion.div>
      )}

      {/* ── BATTLE PHASE ── */}
      {state.phase === "battle" && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full">
          <TDCanvas state={state} onStateChange={handleStateChange} onSlotTap={() => {}} onTowerTap={() => {}} />
        </motion.div>
      )}

      {/* ── RESULT PHASE ── */}
      {state.phase === "result" && (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="w-full flex flex-col items-center gap-4 py-8">
          {won ? (
            <>
              <Trophy size={48} className="text-yellow-400" />
              <h2 className="text-xl font-bold text-text">Защита пройдена!</h2>
              <div className="flex gap-1">
                {[1, 2, 3].map((s) => (
                  <Star key={s} size={28} className={s <= stars ? "text-yellow-400 fill-yellow-400" : "text-white/20"} />
                ))}
              </div>
            </>
          ) : (
            <>
              <Skull size={48} className="text-red-400" />
              <h2 className="text-xl font-bold text-text">Базу захватили!</h2>
            </>
          )}

          <div className="flex gap-3 mt-4">
            {!won && (
              <button
                onClick={handleRetry}
                className="flex items-center gap-2 px-6 py-3 rounded-xl bg-surface border border-border text-text font-semibold cursor-pointer hover:bg-white/10 transition-colors"
              >
                <RotateCcw size={16} /> Ещё раз
              </button>
            )}
            <button
              onClick={() => onAnswer(won)}
              className="flex items-center gap-2 px-6 py-3 rounded-xl bg-primary text-white font-semibold cursor-pointer hover:bg-primary/90 transition-colors"
            >
              Продолжить
            </button>
          </div>
        </motion.div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/games/tower-defense/TowerDefenseStep.tsx
git commit -m "feat(td): add TowerDefenseStep React component with all 4 phases"
```

---

### Task 7: Wire into CourseStepPlayer and courseApi

**Files:**
- Modify: `src/services/courseApi.ts:61-87` (StepType union)
- Modify: `src/services/courseApi.ts:268-294` (LessonStep union)
- Modify: `src/components/courses/CourseStepPlayer.tsx` (imports + renderStep)

- [ ] **Step 1: Add step type and interface to courseApi.ts**

In `src/services/courseApi.ts`, add `"tower-defense"` to StepType union (after `"cloze-passage"` on line 87):

```typescript
  | "cloze-passage"
  | "tower-defense";
```

Add interface after StepClozePassage (around line 267):

```typescript
export interface StepTowerDefense {
  type: "tower-defense";
}
```

Add to LessonStep union (after `StepClozePassage` on line 294):

```typescript
  | StepClozePassage
  | StepTowerDefense;
```

- [ ] **Step 2: Add to CourseStepPlayer.tsx**

Add import at top (after line 44):

```typescript
import TowerDefenseStep from "../games/tower-defense/TowerDefenseStep";
```

Add type import (inside the `import type { ... } from "@/services/courseApi"` block):

```typescript
  StepTowerDefense,
```

Add case in `renderStep` switch (after cloze-passage case, around line 2736):

```typescript
      case "tower-defense":
        return (
          <TowerDefenseStep
            allSteps={steps}
            onAnswer={handleInteractiveAnswer}
          />
        );
```

Note: `steps` is available from the component's props — `CourseStepPlayerProps.steps`.

- [ ] **Step 3: Commit**

```bash
git add src/services/courseApi.ts src/components/courses/CourseStepPlayer.tsx
git commit -m "feat(td): wire tower-defense step into CourseStepPlayer"
```

---

### Task 8: Add to StepEditor

**Files:**
- Modify: `src/components/courses/StepEditor.tsx`

- [ ] **Step 1: Add type import**

Add to imports from `@/services/courseApi`:
```typescript
  type StepTowerDefense,
```

Add icon import from lucide-react:
```typescript
  Shield,
```

- [ ] **Step 2: Add default step case**

In `defaultStep` function, add after `cloze-passage` case:

```typescript
    case "tower-defense":
      return { type: "tower-defense" };
```

- [ ] **Step 3: Add to STEP_TYPES array**

After cloze-passage entry:

```typescript
  { type: "tower-defense", label: "Tower Defense", icon: <Shield size={14} />, color: "#ef4444" },
```

- [ ] **Step 4: Add form rendering**

After cloze-passage form conditional:

```tsx
              {step.type === "tower-defense" && (
                <div className="text-sm text-text-secondary px-1">
                  Игра Tower Defense. Вопросы берутся автоматически из других шагов этого урока.
                  Убедитесь что в уроке есть quiz, true-false или type-answer шаги.
                </div>
              )}
```

- [ ] **Step 5: Commit**

```bash
git add src/components/courses/StepEditor.tsx
git commit -m "feat(td): add tower-defense to StepEditor with info form"
```

---

### Task 9: TypeScript check and build verification

**Files:** None (verification only)

- [ ] **Step 1: Run TypeScript check**

```bash
npx tsc --noEmit
```

Expected: no errors.

- [ ] **Step 2: Run Vite build**

```bash
npx vite build 2>&1 | grep -E "✓|error|Error|MISSING"
```

Expected: `✓ built` with no MISSING_EXPORT or compilation errors (PWA warning is OK).

- [ ] **Step 3: Fix any issues found and commit**

```bash
git add -A
git commit -m "fix(td): address build issues"
```
