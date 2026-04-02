export type Direction = "frontend" | "english" | "callcenter" | "cib";

export type NodeStatus = "locked" | "available" | "completed";

export type Level = "Novice" | "Apprentice" | "Practitioner" | "Expert" | "Master" | "Legend";

export type BadgeRarity = "Common" | "Rare" | "Epic" | "Legendary";

export interface UserProfile {
  name: string;
  direction: Direction;
  level: Level;
  xp: number;
  streak: number;
  lastActiveDate: string;
  completedNodes: string[];
  completedLessons: string[];
  earnedBadges: string[];
  assessmentLevel: "beginner" | "intermediate" | "advanced";
  onboardingComplete: boolean;
}

export interface RoadmapNodeData {
  id: string;
  title: string;
  description: string;
  section: string;
  sectionIndex: number;
  nodeIndex: number;
  estimatedMinutes: number;
  lessons: LessonMeta[];
}

export interface LessonMeta {
  id: string;
  title: string;
  estimatedMinutes: number;
}

export interface Badge {
  id: string;
  name: string;
  description: string;
  icon: string;
  rarity: BadgeRarity;
  direction?: Direction;
  condition: string;
}

export interface SimulatorSession {
  id: string;
  mode: "technical" | "situation" | "voice";
  direction: Direction;
  questions: SimulatorQuestion[];
  currentIndex: number;
  completed: boolean;
  overallScore: number;
}

export interface SimulatorQuestion {
  question: string;
  userAnswer: string;
  score: number;
  feedback: string;
  modelAnswer: string;
}
