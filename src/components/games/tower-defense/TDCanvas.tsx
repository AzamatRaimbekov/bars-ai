import { useRef, useEffect, useCallback } from "react";
import type { GameState, Point } from "./types";
import {
  CANVAS_W,
  CANVAS_H,
  BG_COLOR,
  ROAD_COLOR,
  SLOT_BORDER,
  ENEMY_CONFIG,
  TOWER_CONFIG,
  UPGRADE_RANGE_MULT,
  HUD_BG,
} from "./config";
import { PATH_POINTS, TOWER_SLOTS, getPositionAlongPath } from "./path";
import { tick } from "./engine";

/* ── helpers ─────────────────────────────────────────────── */

function roundRect(
  ctx: CanvasRenderingContext2D,
  x: number,
  y: number,
  w: number,
  h: number,
  r: number,
) {
  const hr = Math.min(r, w / 2, h / 2);
  ctx.beginPath();
  ctx.moveTo(x + hr, y);
  ctx.lineTo(x + w - hr, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + hr);
  ctx.lineTo(x + w, y + h - hr);
  ctx.quadraticCurveTo(x + w, y + h, x + w - hr, y + h);
  ctx.lineTo(x + hr, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - hr);
  ctx.lineTo(x, y + hr);
  ctx.quadraticCurveTo(x, y, x + hr, y);
  ctx.closePath();
}

function dist(a: Point, b: Point): number {
  const dx = a.x - b.x;
  const dy = a.y - b.y;
  return Math.sqrt(dx * dx + dy * dy);
}

/* ── draw functions ──────────────────────────────────────── */

function drawBackground(ctx: CanvasRenderingContext2D) {
  ctx.fillStyle = BG_COLOR;
  ctx.fillRect(0, 0, CANVAS_W, CANVAS_H);
}

function drawRoad(ctx: CanvasRenderingContext2D) {
  if (PATH_POINTS.length < 2) return;

  // Thick road
  ctx.save();
  ctx.lineWidth = 48;
  ctx.lineCap = "round";
  ctx.lineJoin = "round";
  ctx.strokeStyle = ROAD_COLOR;
  ctx.beginPath();
  ctx.moveTo(PATH_POINTS[0].x, PATH_POINTS[0].y);
  for (let i = 1; i < PATH_POINTS.length; i++) {
    ctx.lineTo(PATH_POINTS[i].x, PATH_POINTS[i].y);
  }
  ctx.stroke();
  ctx.restore();

  // Dashed center line
  ctx.save();
  ctx.lineWidth = 2;
  ctx.lineCap = "round";
  ctx.strokeStyle = "#ffffff10";
  ctx.setLineDash([8, 12]);
  ctx.beginPath();
  ctx.moveTo(PATH_POINTS[0].x, PATH_POINTS[0].y);
  for (let i = 1; i < PATH_POINTS.length; i++) {
    ctx.lineTo(PATH_POINTS[i].x, PATH_POINTS[i].y);
  }
  ctx.stroke();
  ctx.setLineDash([]);
  ctx.restore();
}

function drawBase(ctx: CanvasRenderingContext2D) {
  const last = PATH_POINTS[PATH_POINTS.length - 1];
  const bw = 56;
  const bh = 24;
  ctx.save();
  ctx.fillStyle = "#10b981";
  roundRect(ctx, last.x - bw / 2, last.y - bh / 2, bw, bh, 8);
  ctx.fill();
  ctx.fillStyle = "#fff";
  ctx.font = "bold 12px sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("BASE", last.x, last.y);
  ctx.restore();
}

function drawSlots(ctx: CanvasRenderingContext2D, state: GameState) {
  const occupied = new Set(state.towers.map((t) => t.slotIndex));

  for (let i = 0; i < TOWER_SLOTS.length; i++) {
    if (occupied.has(i)) continue;
    const slot = TOWER_SLOTS[i];
    const size = 36;
    const half = size / 2;
    const isSelected = state.selectedSlot === i;

    ctx.save();
    ctx.strokeStyle = isSelected ? "#3b82f6" : SLOT_BORDER;
    ctx.lineWidth = isSelected ? 2 : 1;
    ctx.setLineDash([4, 4]);
    roundRect(ctx, slot.x - half, slot.y - half, size, size, 8);
    ctx.stroke();
    ctx.setLineDash([]);

    if (isSelected) {
      ctx.fillStyle = "#3b82f620";
      roundRect(ctx, slot.x - half, slot.y - half, size, size, 8);
      ctx.fill();
    }

    ctx.fillStyle = isSelected ? "#3b82f6" : "#ffffff30";
    ctx.font = "bold 18px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("+", slot.x, slot.y + 1);
    ctx.restore();
  }
}

function drawTowers(ctx: CanvasRenderingContext2D, state: GameState) {
  for (const tower of state.towers) {
    const cfg = TOWER_CONFIG[tower.kind];
    const size = 20 + tower.level * 4;
    const half = size / 2;

    ctx.save();

    // Range circle when selected
    if (state.selectedTower === tower.id) {
      const range = cfg.range * UPGRADE_RANGE_MULT[tower.level];
      ctx.strokeStyle = cfg.color + "40";
      ctx.lineWidth = 1;
      ctx.setLineDash([6, 4]);
      ctx.beginPath();
      ctx.arc(tower.pos.x, tower.pos.y, range, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // Glow for level 3
    if (tower.level === 3) {
      ctx.shadowColor = cfg.color;
      ctx.shadowBlur = 12;
    }

    // Tower body
    ctx.fillStyle = cfg.color + "30";
    roundRect(ctx, tower.pos.x - half, tower.pos.y - half, size, size, 6);
    ctx.fill();
    ctx.strokeStyle = cfg.color;
    ctx.lineWidth = 1.5;
    roundRect(ctx, tower.pos.x - half, tower.pos.y - half, size, size, 6);
    ctx.stroke();

    // Reset shadow
    ctx.shadowColor = "transparent";
    ctx.shadowBlur = 0;

    // Emoji
    ctx.font = `${size * 0.6}px sans-serif`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(cfg.emoji, tower.pos.x, tower.pos.y + 1);

    // Level dots
    if (tower.level > 1) {
      const dotY = tower.pos.y + half + 5;
      for (let d = 0; d < tower.level; d++) {
        const dotX = tower.pos.x + (d - (tower.level - 1) / 2) * 6;
        ctx.fillStyle = cfg.color;
        ctx.beginPath();
        ctx.arc(dotX, dotY, 2, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    ctx.restore();
  }
}

function drawEnemies(ctx: CanvasRenderingContext2D, state: GameState) {
  for (const enemy of state.enemies) {
    const cfg = ENEMY_CONFIG[enemy.kind];
    const pos = getPositionAlongPath(enemy.progress);
    const half = cfg.size / 2;

    ctx.save();

    // White flash
    if (enemy.flashTimer > 0) {
      ctx.globalAlpha = 0.5 + enemy.flashTimer * 5;
      ctx.fillStyle = "#fff";
      roundRect(ctx, pos.x - half, pos.y - half, cfg.size, cfg.size, 6);
      ctx.fill();
      ctx.globalAlpha = 1;
    }

    // Enemy body
    ctx.fillStyle = cfg.color + "30";
    roundRect(ctx, pos.x - half, pos.y - half, cfg.size, cfg.size, 6);
    ctx.fill();
    ctx.strokeStyle = cfg.color;
    ctx.lineWidth = 1;
    roundRect(ctx, pos.x - half, pos.y - half, cfg.size, cfg.size, 6);
    ctx.stroke();

    // Emoji
    ctx.font = `${cfg.size * 0.6}px sans-serif`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(cfg.emoji, pos.x, pos.y + 1);

    // HP bar (only if damaged)
    if (enemy.hp < enemy.maxHp) {
      const barW = cfg.size;
      const barH = 4;
      const barY = pos.y - half - 7;
      const barX = pos.x - barW / 2;
      const ratio = Math.max(0, enemy.hp / enemy.maxHp);

      ctx.fillStyle = "#00000080";
      roundRect(ctx, barX, barY, barW, barH, 2);
      ctx.fill();

      ctx.fillStyle = ratio > 0.5 ? "#22c55e" : ratio > 0.25 ? "#eab308" : "#ef4444";
      roundRect(ctx, barX, barY, barW * ratio, barH, 2);
      ctx.fill();
    }

    ctx.restore();
  }
}

function drawProjectiles(ctx: CanvasRenderingContext2D, state: GameState) {
  for (const p of state.projectiles) {
    ctx.save();
    const alpha = Math.min(1, p.timer * 5);
    ctx.globalAlpha = alpha;

    // Line from -> to
    ctx.strokeStyle = p.color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(p.from.x, p.from.y);
    ctx.lineTo(p.to.x, p.to.y);
    ctx.stroke();

    // AoE expanding circle
    if (p.isAoe && p.aoeRadius > 0) {
      const expansion = 1 - p.timer / 0.3; // 0→1
      const radius = p.aoeRadius * expansion;
      ctx.strokeStyle = p.color + "60";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(p.to.x, p.to.y, radius, 0, Math.PI * 2);
      ctx.stroke();

      ctx.fillStyle = p.color + "15";
      ctx.beginPath();
      ctx.arc(p.to.x, p.to.y, radius, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.restore();
  }
}

function drawHUD(ctx: CanvasRenderingContext2D, state: GameState) {
  ctx.save();

  const pillH = 26;
  const pillR = 13;
  const padX = 10;
  const padY = 10;

  // Coins badge (top-left)
  const coinsText = `${state.coins}`;
  ctx.font = "bold 13px sans-serif";
  const coinsW = ctx.measureText(coinsText).width + 36;
  ctx.fillStyle = HUD_BG;
  roundRect(ctx, padX, padY, coinsW, pillH, pillR);
  ctx.fill();
  ctx.fillStyle = "#eab308";
  ctx.font = "14px sans-serif";
  ctx.textAlign = "left";
  ctx.textBaseline = "middle";
  ctx.fillText("\uD83E\uDE99", padX + 8, padY + pillH / 2 + 1);
  ctx.fillStyle = "#fde047";
  ctx.font = "bold 13px sans-serif";
  ctx.fillText(coinsText, padX + 26, padY + pillH / 2);

  // Lives badge
  const livesText = `${state.lives}`;
  const livesW = ctx.measureText(livesText).width + 36;
  const livesX = padX + coinsW + 8;
  ctx.fillStyle = HUD_BG;
  roundRect(ctx, livesX, padY, livesW, pillH, pillR);
  ctx.fill();
  ctx.fillStyle = "#ef4444";
  ctx.font = "14px sans-serif";
  ctx.textAlign = "left";
  ctx.textBaseline = "middle";
  ctx.fillText("\u2764\uFE0F", livesX + 8, padY + pillH / 2 + 1);
  ctx.fillStyle = "#fca5a5";
  ctx.font = "bold 13px sans-serif";
  ctx.fillText(livesText, livesX + 26, padY + pillH / 2);

  // Wave counter (top-right)
  const waveText = `Wave ${state.wave + 1}/${state.totalWaves}`;
  ctx.font = "bold 13px sans-serif";
  const waveW = ctx.measureText(waveText).width + 20;
  const waveX = CANVAS_W - padX - waveW;
  ctx.fillStyle = HUD_BG;
  roundRect(ctx, waveX, padY, waveW, pillH, pillR);
  ctx.fill();
  ctx.fillStyle = "#e2e8f0";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(waveText, waveX + waveW / 2, padY + pillH / 2);

  ctx.restore();
}

function drawFrame(ctx: CanvasRenderingContext2D, state: GameState) {
  drawBackground(ctx);
  drawRoad(ctx);
  drawBase(ctx);
  drawSlots(ctx, state);
  drawTowers(ctx, state);
  drawEnemies(ctx, state);
  drawProjectiles(ctx, state);
  drawHUD(ctx, state);
}

/* ── component ───────────────────────────────────────────── */

interface Props {
  state: GameState;
  onStateChange: (s: GameState) => void;
  onSlotTap: (slotIndex: number) => void;
  onTowerTap: (towerId: string) => void;
}

export default function TDCanvas({
  state,
  onStateChange,
  onSlotTap,
  onTowerTap,
}: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const stateRef = useRef(state);
  const rafRef = useRef<number>(0);
  const lastTimeRef = useRef<number>(0);

  // Keep stateRef in sync
  stateRef.current = state;

  /* ── DPR scaling setup ───────────────────────────────── */
  const getCtx = useCallback((): CanvasRenderingContext2D | null => {
    const canvas = canvasRef.current;
    if (!canvas) return null;
    const ctx = canvas.getContext("2d");
    if (!ctx) return null;

    const dpr = window.devicePixelRatio || 1;
    const needsResize =
      canvas.width !== CANVAS_W * dpr || canvas.height !== CANVAS_H * dpr;

    if (needsResize) {
      canvas.width = CANVAS_W * dpr;
      canvas.height = CANVAS_H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    return ctx;
  }, []);

  /* ── Battle animation loop ─────────────────────────── */
  useEffect(() => {
    if (state.phase !== "battle") return;

    lastTimeRef.current = 0;

    const loop = (timestamp: number) => {
      if (lastTimeRef.current === 0) {
        lastTimeRef.current = timestamp;
      }
      const dt = Math.min((timestamp - lastTimeRef.current) / 1000, 0.1);
      lastTimeRef.current = timestamp;

      const newState = tick(stateRef.current, dt);
      stateRef.current = newState;
      onStateChange(newState);

      const ctx = getCtx();
      if (ctx) drawFrame(ctx, newState);

      rafRef.current = requestAnimationFrame(loop);
    };

    rafRef.current = requestAnimationFrame(loop);

    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
    };
  }, [state.phase, getCtx, onStateChange]);

  /* ── Static draw on state change (non-battle) ──────── */
  useEffect(() => {
    if (state.phase === "battle") return;
    const ctx = getCtx();
    if (ctx) drawFrame(ctx, state);
  }, [state, getCtx]);

  /* ── Click / tap handler ───────────────────────────── */
  const handleClick = useCallback(
    (e: React.MouseEvent<HTMLCanvasElement>) => {
      const canvas = canvasRef.current;
      if (!canvas) return;

      const rect = canvas.getBoundingClientRect();
      const scaleX = CANVAS_W / rect.width;
      const scaleY = CANVAS_H / rect.height;
      const tapX = (e.clientX - rect.left) * scaleX;
      const tapY = (e.clientY - rect.top) * scaleY;
      const tap: Point = { x: tapX, y: tapY };

      const HIT_RADIUS = 28;

      // Check towers first (they sit on slots)
      for (const tower of stateRef.current.towers) {
        if (dist(tap, tower.pos) <= HIT_RADIUS) {
          onTowerTap(tower.id);
          return;
        }
      }

      // Then empty slots
      const occupied = new Set(stateRef.current.towers.map((t) => t.slotIndex));
      for (let i = 0; i < TOWER_SLOTS.length; i++) {
        if (occupied.has(i)) continue;
        if (dist(tap, TOWER_SLOTS[i]) <= HIT_RADIUS) {
          onSlotTap(i);
          return;
        }
      }
    },
    [onSlotTap, onTowerTap],
  );

  return (
    <canvas
      ref={canvasRef}
      onClick={handleClick}
      style={{
        width: "100%",
        maxWidth: CANVAS_W,
        height: "auto",
        aspectRatio: `${CANVAS_W} / ${CANVAS_H}`,
        display: "block",
        borderRadius: 12,
      }}
    />
  );
}
