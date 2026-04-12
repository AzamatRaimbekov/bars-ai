export interface Point { x: number; y: number; }
export type TowerKind = "blaster" | "zapper" | "cannon";
export interface Tower { id: string; kind: TowerKind; level: 1 | 2 | 3; slotIndex: number; pos: Point; cooldown: number; }
export type EnemyKind = "bug" | "glitch" | "virus" | "trojan" | "boss";
export interface Enemy { id: string; kind: EnemyKind; hp: number; maxHp: number; progress: number; speed: number; flashTimer: number; }
export interface Projectile { id: string; from: Point; to: Point; color: string; timer: number; isAoe: boolean; aoeRadius: number; }
export interface WaveConfig { enemies: { kind: EnemyKind; count: number; delay: number }[]; }
export type GamePhase = "questions" | "build" | "battle" | "result";
export interface GameState { phase: GamePhase; coins: number; lives: number; maxLives: number; wave: number; totalWaves: number; towers: Tower[]; enemies: Enemy[]; projectiles: Projectile[]; spawnQueue: { kind: EnemyKind; delay: number }[]; spawnTimer: number; waveDone: boolean; selectedSlot: number | null; selectedTower: string | null; }
export interface TDQuestion { type: "quiz" | "true-false" | "type-answer" | "fill-blank"; question: string; options?: { id: string; text: string; correct: boolean }[]; statement?: string; correct?: boolean; acceptedAnswers?: string[]; text?: string; answers?: string[]; }
