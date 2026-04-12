import type {
  GameState,
  Enemy,
  Tower,
  Projectile,
  EnemyKind,
  TowerKind,
  WaveConfig,
} from "./types";
import {
  ENEMY_CONFIG,
  TOWER_CONFIG,
  UPGRADE_COSTS,
  UPGRADE_DAMAGE_MULT,
  UPGRADE_RANGE_MULT,
  INITIAL_LIVES,
} from "./config";
import { getPositionAlongPath, TOWER_SLOTS } from "./path";

/* ── unique ID counter ─────────────────────────────────── */

let _uid = 0;
export function uid(): string {
  return `e${++_uid}`;
}

/* ── wave generation ───────────────────────────────────── */

export function generateWaves(totalWaves: number): WaveConfig[] {
  const waves: WaveConfig[] = [];

  for (let i = 0; i < totalWaves; i++) {
    const ratio = i / Math.max(totalWaves - 1, 1);
    const enemies: WaveConfig["enemies"] = [];

    // Base count scales with wave index
    const base = 3 + Math.floor(i * 1.5);

    // Early waves (first third): bug + glitch
    if (ratio < 0.33) {
      enemies.push({ kind: "bug", count: base, delay: 0.8 });
      enemies.push({ kind: "glitch", count: Math.floor(base * 0.5), delay: 1.0 });
    }
    // Middle waves: + virus + trojan
    else if (ratio < 0.75) {
      enemies.push({ kind: "bug", count: Math.floor(base * 0.6), delay: 0.7 });
      enemies.push({ kind: "glitch", count: Math.floor(base * 0.4), delay: 0.9 });
      enemies.push({ kind: "virus", count: Math.floor(base * 0.3), delay: 1.2 });
      enemies.push({ kind: "trojan", count: Math.floor(base * 0.2), delay: 1.4 });
    }
    // Last waves: all types + boss
    else {
      enemies.push({ kind: "bug", count: Math.floor(base * 0.4), delay: 0.6 });
      enemies.push({ kind: "glitch", count: Math.floor(base * 0.3), delay: 0.8 });
      enemies.push({ kind: "virus", count: Math.floor(base * 0.3), delay: 1.0 });
      enemies.push({ kind: "trojan", count: Math.floor(base * 0.25), delay: 1.2 });
      enemies.push({ kind: "boss", count: 1 + Math.floor((i - totalWaves * 0.75) * 0.5), delay: 2.0 });
    }

    // Filter out zero-count entries
    waves.push({ enemies: enemies.filter((e) => e.count > 0) });
  }

  return waves;
}

/* ── spawn queue builder ───────────────────────────────── */

export function buildSpawnQueue(
  wave: WaveConfig,
): { kind: EnemyKind; delay: number }[] {
  // Flatten wave config into individual spawn entries
  const queue: { kind: EnemyKind; delay: number }[] = [];
  for (const group of wave.enemies) {
    for (let i = 0; i < group.count; i++) {
      queue.push({ kind: group.kind, delay: group.delay });
    }
  }

  // Fisher-Yates shuffle
  for (let i = queue.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [queue[i], queue[j]] = [queue[j], queue[i]];
  }

  return queue;
}

/* ── initial state ─────────────────────────────────────── */

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

/* ── tower purchase ────────────────────────────────────── */

export function canBuyTower(state: GameState, kind: TowerKind): boolean {
  return state.coins >= TOWER_CONFIG[kind].cost;
}

export function placeTower(
  state: GameState,
  slotIndex: number,
  kind: TowerKind,
): GameState {
  const config = TOWER_CONFIG[kind];
  if (state.coins < config.cost) return state;

  // Check slot is not already occupied
  if (state.towers.some((t) => t.slotIndex === slotIndex)) return state;
  if (slotIndex < 0 || slotIndex >= TOWER_SLOTS.length) return state;

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
    coins: state.coins - config.cost,
    towers: [...state.towers, tower],
  };
}

/* ── tower upgrades ────────────────────────────────────── */

export function canUpgradeTower(state: GameState, towerId: string): boolean {
  const tower = state.towers.find((t) => t.id === towerId);
  if (!tower || tower.level >= 3) return false;
  const nextLevel = (tower.level + 1) as 2 | 3;
  return state.coins >= UPGRADE_COSTS[nextLevel];
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
      t.id === towerId ? { ...t, level: nextLevel } : t,
    ),
  };
}

/* ── helpers ───────────────────────────────────────────── */

function dist(a: { x: number; y: number }, b: { x: number; y: number }): number {
  const dx = a.x - b.x;
  const dy = a.y - b.y;
  return Math.sqrt(dx * dx + dy * dy);
}

function createEnemy(kind: EnemyKind, progress: number = 0): Enemy {
  const cfg = ENEMY_CONFIG[kind];
  return {
    id: uid(),
    kind,
    hp: cfg.hp,
    maxHp: cfg.hp,
    progress,
    speed: cfg.speed,
    flashTimer: 0,
  };
}

/* ── main tick ─────────────────────────────────────────── */

export function tick(state: GameState, dt: number): GameState {
  if (state.phase !== "battle") return state;

  let {
    lives,
    spawnQueue,
    spawnTimer,
    enemies,
    towers,
    projectiles,
    waveDone,
    coins,
  } = state;

  // Work with mutable copies
  spawnQueue = [...spawnQueue];
  enemies = enemies.map((e) => ({ ...e }));
  towers = towers.map((t) => ({ ...t }));
  projectiles = projectiles.map((p) => ({ ...p }));

  const newProjectiles: Projectile[] = [];

  /* ── 1. Spawn enemies from queue ──────────────────────── */
  spawnTimer -= dt;
  if (spawnTimer <= 0 && spawnQueue.length > 0) {
    const next = spawnQueue.shift()!;
    enemies.push(createEnemy(next.kind));
    spawnTimer = next.delay;
  }

  /* ── 2. Move enemies along path ───────────────────────── */
  for (const enemy of enemies) {
    enemy.progress += enemy.speed * dt;

    // Glitch enemies randomly teleport forward
    if (enemy.kind === "glitch" && Math.random() < 0.005) {
      enemy.progress += 0.02;
    }

    // Decrease flash timer
    if (enemy.flashTimer > 0) {
      enemy.flashTimer = Math.max(0, enemy.flashTimer - dt);
    }
  }

  /* ── 3. Remove enemies that reached the end ───────────── */
  const leaked: Enemy[] = [];
  const alive: Enemy[] = [];
  for (const enemy of enemies) {
    if (enemy.progress >= 1) {
      leaked.push(enemy);
    } else {
      alive.push(enemy);
    }
  }
  lives -= leaked.length;
  enemies = alive;

  /* ── 4. Towers shoot ──────────────────────────────────── */
  for (const tower of towers) {
    tower.cooldown = Math.max(0, tower.cooldown - dt);
    if (tower.cooldown > 0) continue;
    if (enemies.length === 0) continue;

    const cfg = TOWER_CONFIG[tower.kind];
    const effectiveRange = cfg.range * UPGRADE_RANGE_MULT[tower.level];
    const effectiveDamage = cfg.damage * UPGRADE_DAMAGE_MULT[tower.level];

    // Find closest enemy in range
    let closest: Enemy | null = null;
    let closestDist = Infinity;

    for (const enemy of enemies) {
      if (enemy.hp <= 0) continue;
      const enemyPos = getPositionAlongPath(enemy.progress);
      const d = dist(tower.pos, enemyPos);
      if (d <= effectiveRange && d < closestDist) {
        closest = enemy;
        closestDist = d;
      }
    }

    if (!closest) continue;

    // Fire!
    tower.cooldown = cfg.fireRate;
    const targetPos = getPositionAlongPath(closest.progress);

    if (tower.kind === "cannon") {
      // AoE damage — hit all enemies within 40px of target
      const AOE_RADIUS = 40;
      for (const enemy of enemies) {
        if (enemy.hp <= 0) continue;
        const ePos = getPositionAlongPath(enemy.progress);
        if (dist(targetPos, ePos) <= AOE_RADIUS) {
          enemy.hp -= effectiveDamage;
          enemy.flashTimer = 0.1;
        }
      }
      newProjectiles.push({
        id: uid(),
        from: { ...tower.pos },
        to: { ...targetPos },
        color: cfg.color,
        timer: 0.3,
        isAoe: true,
        aoeRadius: AOE_RADIUS,
      });
    } else {
      // Single target damage
      closest.hp -= effectiveDamage;
      closest.flashTimer = 0.1;
      newProjectiles.push({
        id: uid(),
        from: { ...tower.pos },
        to: { ...targetPos },
        color: cfg.color,
        timer: 0.2,
        isAoe: false,
        aoeRadius: 0,
      });
    }
  }

  /* ── 5. Handle dead enemies (trojan spawns bugs) ──────── */
  const surviving: Enemy[] = [];
  for (const enemy of enemies) {
    if (enemy.hp <= 0) {
      // Grant coins for kill
      coins += 5;
      // Dead Trojan spawns 2 bugs at same position
      if (enemy.kind === "trojan") {
        surviving.push(createEnemy("bug", enemy.progress));
        surviving.push(createEnemy("bug", enemy.progress));
      }
    } else {
      surviving.push(enemy);
    }
  }
  enemies = surviving;

  /* ── 6. Update projectiles ────────────────────────────── */
  for (const p of projectiles) {
    p.timer -= dt;
  }
  projectiles = [...projectiles.filter((p) => p.timer > 0), ...newProjectiles];

  /* ── 7. Check wave done ───────────────────────────────── */
  waveDone = spawnQueue.length === 0 && enemies.length === 0;

  return {
    ...state,
    lives: Math.max(0, lives),
    coins,
    spawnQueue,
    spawnTimer,
    enemies,
    towers,
    projectiles,
    waveDone,
  };
}
