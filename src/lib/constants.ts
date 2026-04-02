import type { Level } from "@/types";

export const LEVEL_THRESHOLDS: Record<Level, number> = {
  Novice: 0,
  Apprentice: 500,
  Practitioner: 1500,
  Expert: 4000,
  Master: 8000,
  Legend: 15000,
};

export const LEVELS_ORDERED: Level[] = [
  "Novice", "Apprentice", "Practitioner", "Expert", "Master", "Legend",
];

export const XP_REWARDS = {
  completeLesson: 50,
  perfectQuiz: 100,
  interviewSimulation: 200,
  dailyStreak: 25,
} as const;

export const STREAK_MILESTONES = [7, 30, 100] as const;

export const DIRECTION_COLORS = {
  frontend: { primary: "#6C63FF", secondary: "#818CF8" },
  english: { primary: "#00FF94", secondary: "#34D399" },
  callcenter: { primary: "#FFB800", secondary: "#FBBF24" },
  cib: { primary: "#FFD700", secondary: "#F59E0B" },
} as const;
