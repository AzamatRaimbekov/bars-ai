# PathMind Learning Platform — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a gamified AI-powered learning platform with interactive roadmap, AI mentor chat with voice, interview simulator, and achievement system across 4 learning directions.

**Architecture:** Vite+React SPA with Zustand stores for state, React Router for navigation, React Flow for roadmap visualization. AI features call Claude API via a thin service layer. Voice uses Web Speech API. All user data persisted in localStorage.

**Tech Stack:** React 18, TypeScript, Vite, Tailwind CSS 3, Framer Motion, Zustand, React Router v6, React Flow, Lucide React, Anthropic Claude API (claude-sonnet-4-20250514), Web Speech API

---

## File Structure

```
src/
├── main.tsx                          — App entry, router setup
├── App.tsx                           — Root layout with router outlet
├── index.css                         — Tailwind directives, global styles, fonts
├── vite-env.d.ts                     — Vite type declarations
│
├── lib/
│   ├── cn.ts                         — clsx+twMerge utility
│   └── constants.ts                  — Colors, XP values, level thresholds
│
├── types/
│   ├── index.ts                      — Shared types: Direction, UserProfile, RoadmapNode, etc.
│   └── chat.ts                       — Chat message types
│
├── store/
│   ├── userStore.ts                  — User profile, XP, streak, direction, level
│   ├── roadmapStore.ts               — Node states, completion, current position
│   ├── chatStore.ts                  — Chat messages, conversation state
│   └── simulatorStore.ts             — Interview session state, scores
│
├── services/
│   ├── claudeApi.ts                  — Anthropic API calls (chat, assess, generate)
│   └── voiceService.ts               — Web Speech API wrapper (STT + TTS)
│
├── data/
│   ├── directions.ts                 — Direction configs (name, icon, color, mentor)
│   ├── roadmaps/
│   │   ├── frontend.ts               — Frontend dev roadmap nodes
│   │   ├── english.ts                — English language roadmap nodes
│   │   ├── callcenter.ts             — Call center roadmap nodes
│   │   └── cib.ts                    — CIB banking roadmap nodes
│   ├── achievements.ts               — Badge definitions
│   └── lessons.ts                    — Lesson content per node
│
├── hooks/
│   ├── useVoice.ts                   — Voice recording/playback hook
│   ├── useChat.ts                    — Chat with Claude hook
│   ├── useRoadmap.ts                 — Roadmap navigation hook
│   └── useGameification.ts           — XP/level/streak logic hook
│
├── components/
│   ├── ui/
│   │   ├── Button.tsx                — Primary/secondary/ghost variants
│   │   ├── Card.tsx                  — Glassmorphism card
│   │   ├── Badge.tsx                 — Achievement badge component
│   │   ├── Modal.tsx                 — Animated modal overlay
│   │   ├── ProgressBar.tsx           — Animated gradient progress bar
│   │   ├── ProgressRing.tsx          — Circular progress indicator
│   │   ├── Tooltip.tsx               — Hover tooltip
│   │   ├── Input.tsx                 — Styled text input
│   │   └── Chip.tsx                  — Suggestion chip
│   ├── layout/
│   │   ├── Sidebar.tsx               — Navigation sidebar with icons
│   │   ├── TopBar.tsx                — Greeting, streak, XP bar
│   │   └── PageWrapper.tsx           — Page container with sidebar+topbar
│   ├── roadmap/
│   │   ├── RoadmapCanvas.tsx         — React Flow canvas wrapper
│   │   ├── RoadmapNode.tsx           — Custom node component (locked/available/completed)
│   │   └── NodePanel.tsx             — Slide-over panel for node details
│   ├── chat/
│   │   ├── ChatWindow.tsx            — Full chat interface
│   │   ├── MessageBubble.tsx         — Single message (user/AI)
│   │   ├── VoiceButton.tsx           — Mic button with pulse animation
│   │   └── WaveformVisualizer.tsx    — Audio waveform display
│   ├── simulator/
│   │   ├── InterviewRoom.tsx         — Interview UI wrapper
│   │   ├── ScoreCard.tsx             — Score display after answer
│   │   └── TranscriptPanel.tsx       — Live transcript
│   └── gamification/
│       ├── XPBar.tsx                 — XP progress bar with level
│       ├── StreakCounter.tsx          — Fire icon + streak count
│       ├── BadgeReveal.tsx           — Animated badge unlock
│       └── LevelUpModal.tsx          — Level up celebration modal
│
├── pages/
│   ├── Onboarding.tsx                — 3-step wizard
│   ├── Dashboard.tsx                 — Main dashboard
│   ├── Roadmap.tsx                   — Interactive roadmap page
│   ├── Mentor.tsx                    — AI mentor chat page
│   ├── Simulator.tsx                 — Interview simulator page
│   ├── Lesson.tsx                    — Lesson viewer page
│   ├── Achievements.tsx              — Badges & leaderboard page
│   └── Profile.tsx                   — User profile & settings page
```

---

## Phase 1: Foundation

### Task 1: Project Scaffolding & Tailwind Setup

**Files:**
- Create: `package.json`, `vite.config.ts`, `tsconfig.json`, `tsconfig.app.json`, `tsconfig.node.json`, `tailwind.config.ts`, `postcss.config.js`, `index.html`, `src/main.tsx`, `src/App.tsx`, `src/index.css`, `src/vite-env.d.ts`, `.env.example`

- [ ] **Step 1: Scaffold Vite project and install all dependencies**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи"
npm create vite@latest . -- --template react-ts
npm install tailwindcss @tailwindcss/vite framer-motion zustand react-router-dom @xyflow/react lucide-react clsx tailwind-merge
npm install -D @types/node
```

- [ ] **Step 2: Configure Tailwind with design system colors**

Replace `src/index.css`:

```css
@import "tailwindcss";

@theme {
  --color-bg: #0A0A0F;
  --color-surface: #111118;
  --color-border: #1E1E2E;
  --color-primary: #6C63FF;
  --color-accent: #00D9FF;
  --color-success: #00FF94;
  --color-warning: #FFB800;
  --color-text: #F0F0FF;
  --color-text-secondary: #8888AA;
  --font-sans: "Inter", sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}

@layer base {
  * {
    @apply border-border;
  }

  body {
    @apply bg-bg text-text font-sans antialiased;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.02'/%3E%3C/svg%3E");
  }

  ::-webkit-scrollbar {
    width: 6px;
  }
  ::-webkit-scrollbar-track {
    background: var(--color-bg);
  }
  ::-webkit-scrollbar-thumb {
    background: var(--color-border);
    border-radius: 3px;
  }
}
```

- [ ] **Step 3: Update vite.config.ts with Tailwind plugin and path alias**

```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
```

- [ ] **Step 4: Add Google Fonts to index.html**

Update `index.html` `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<title>PathMind</title>
```

- [ ] **Step 5: Create .env.example**

```
VITE_ANTHROPIC_API_KEY=your-api-key-here
```

- [ ] **Step 6: Create src/lib/cn.ts utility**

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

- [ ] **Step 7: Create basic App.tsx with router**

```tsx
import { BrowserRouter, Routes, Route } from "react-router-dom";

function Placeholder({ name }: { name: string }) {
  return (
    <div className="flex h-screen items-center justify-center">
      <h1 className="text-2xl font-bold text-text-secondary">{name}</h1>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Placeholder name="Onboarding" />} />
        <Route path="/dashboard" element={<Placeholder name="Dashboard" />} />
        <Route path="/roadmap" element={<Placeholder name="Roadmap" />} />
        <Route path="/mentor" element={<Placeholder name="Mentor" />} />
        <Route path="/simulator" element={<Placeholder name="Simulator" />} />
        <Route path="/lesson/:id" element={<Placeholder name="Lesson" />} />
        <Route path="/achievements" element={<Placeholder name="Achievements" />} />
        <Route path="/profile" element={<Placeholder name="Profile" />} />
      </Routes>
    </BrowserRouter>
  );
}
```

- [ ] **Step 8: Verify dev server starts**

```bash
npm run dev
```

Expected: Vite dev server runs, browser shows "Onboarding" text on dark background.

- [ ] **Step 9: Commit**

```bash
git init && git add -A && git commit -m "feat: scaffold Vite+React+TS project with Tailwind design system"
```

---

### Task 2: Types, Constants & Direction Data

**Files:**
- Create: `src/types/index.ts`, `src/types/chat.ts`, `src/lib/constants.ts`, `src/data/directions.ts`

- [ ] **Step 1: Create shared types**

`src/types/index.ts`:

```ts
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
```

- [ ] **Step 2: Create chat types**

`src/types/chat.ts`:

```ts
export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: number;
}

export interface MentorConfig {
  name: string;
  avatar: string;
  systemPrompt: string;
  voiceName?: string;
}
```

- [ ] **Step 3: Create constants**

`src/lib/constants.ts`:

```ts
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
```

- [ ] **Step 4: Create direction configs with mentor system prompts**

`src/data/directions.ts`:

```ts
import type { Direction } from "@/types";
import type { MentorConfig } from "@/types/chat";

export interface DirectionConfig {
  id: Direction;
  name: string;
  description: string;
  icon: string;
  color: string;
  mentor: MentorConfig;
}

export const DIRECTIONS: Record<Direction, DirectionConfig> = {
  frontend: {
    id: "frontend",
    name: "Frontend Development",
    description: "Master HTML, CSS, JavaScript, React and modern web development",
    icon: "Code2",
    color: "#6C63FF",
    mentor: {
      name: "Alex",
      avatar: "👨‍💻",
      systemPrompt: `You are Alex, an expert Frontend developer mentor with 10 years of experience at top tech companies. You teach HTML, CSS, JavaScript, React, and modern web development. You speak in a friendly, encouraging way. You know the student's current level and roadmap position. Give practical examples, real code snippets, and career advice. Keep responses concise and actionable.`,
    },
  },
  english: {
    id: "english",
    name: "English Language",
    description: "Improve your business and conversational English skills",
    icon: "Languages",
    color: "#00FF94",
    mentor: {
      name: "Emma",
      avatar: "👩‍🏫",
      systemPrompt: `You are Emma, a certified English language teacher specializing in business and conversational English. You help students improve vocabulary, grammar, pronunciation tips, and confidence in speaking. Adapt to the student's level (A1-C2). Always correct mistakes gently and explain why. Keep responses concise.`,
    },
  },
  callcenter: {
    id: "callcenter",
    name: "Call Center Training",
    description: "Learn customer service, conflict resolution, and communication",
    icon: "Headphones",
    color: "#FFB800",
    mentor: {
      name: "Jordan",
      avatar: "🎧",
      systemPrompt: `You are Jordan, a call center training specialist with expertise in customer service, conflict resolution, and communication scripts. You train students for real call center scenarios, teach proper phone etiquette, handle objections, and build confidence. Keep responses practical and scenario-focused.`,
    },
  },
  cib: {
    id: "cib",
    name: "CIB Banking",
    description: "Corporate & Investment Banking concepts, operations, and interview prep",
    icon: "Building2",
    color: "#FFD700",
    mentor: {
      name: "Morgan",
      avatar: "🏦",
      systemPrompt: `You are Morgan, a Corporate & Investment Banking professional with experience at major banks. You mentor students on financial concepts, banking operations, Excel modeling basics, client communication, and interview preparation for banking roles. Keep responses professional and structured.`,
    },
  },
};
```

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: add types, constants, and direction configs"
```

---

### Task 3: Zustand Stores

**Files:**
- Create: `src/store/userStore.ts`, `src/store/roadmapStore.ts`, `src/store/chatStore.ts`, `src/store/simulatorStore.ts`

- [ ] **Step 1: Create user store with localStorage persistence**

`src/store/userStore.ts`:

```ts
import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { UserProfile, Direction, Level } from "@/types";
import { LEVELS_ORDERED, LEVEL_THRESHOLDS } from "@/lib/constants";

function calculateLevel(xp: number): Level {
  let current: Level = "Novice";
  for (const level of LEVELS_ORDERED) {
    if (xp >= LEVEL_THRESHOLDS[level]) current = level;
    else break;
  }
  return current;
}

function getToday(): string {
  return new Date().toISOString().split("T")[0];
}

interface UserState {
  profile: UserProfile | null;
  setProfile: (profile: UserProfile) => void;
  setDirection: (direction: Direction) => void;
  setAssessmentLevel: (level: "beginner" | "intermediate" | "advanced") => void;
  completeOnboarding: () => void;
  addXP: (amount: number) => void;
  completeNode: (nodeId: string) => void;
  completeLesson: (lessonId: string) => void;
  earnBadge: (badgeId: string) => void;
  updateStreak: () => void;
  reset: () => void;
}

export const useUserStore = create<UserState>()(
  persist(
    (set, get) => ({
      profile: null,

      setProfile: (profile) => set({ profile }),

      setDirection: (direction) =>
        set((s) => ({
          profile: s.profile ? { ...s.profile, direction } : null,
        })),

      setAssessmentLevel: (level) =>
        set((s) => ({
          profile: s.profile ? { ...s.profile, assessmentLevel: level } : null,
        })),

      completeOnboarding: () =>
        set((s) => ({
          profile: s.profile
            ? { ...s.profile, onboardingComplete: true }
            : null,
        })),

      addXP: (amount) =>
        set((s) => {
          if (!s.profile) return s;
          const newXP = s.profile.xp + amount;
          return {
            profile: {
              ...s.profile,
              xp: newXP,
              level: calculateLevel(newXP),
            },
          };
        }),

      completeNode: (nodeId) =>
        set((s) => {
          if (!s.profile) return s;
          if (s.profile.completedNodes.includes(nodeId)) return s;
          return {
            profile: {
              ...s.profile,
              completedNodes: [...s.profile.completedNodes, nodeId],
            },
          };
        }),

      completeLesson: (lessonId) =>
        set((s) => {
          if (!s.profile) return s;
          if (s.profile.completedLessons.includes(lessonId)) return s;
          return {
            profile: {
              ...s.profile,
              completedLessons: [...s.profile.completedLessons, lessonId],
            },
          };
        }),

      earnBadge: (badgeId) =>
        set((s) => {
          if (!s.profile) return s;
          if (s.profile.earnedBadges.includes(badgeId)) return s;
          return {
            profile: {
              ...s.profile,
              earnedBadges: [...s.profile.earnedBadges, badgeId],
            },
          };
        }),

      updateStreak: () =>
        set((s) => {
          if (!s.profile) return s;
          const today = getToday();
          const lastActive = s.profile.lastActiveDate;
          if (lastActive === today) return s;

          const yesterday = new Date();
          yesterday.setDate(yesterday.getDate() - 1);
          const yesterdayStr = yesterday.toISOString().split("T")[0];

          const newStreak =
            lastActive === yesterdayStr ? s.profile.streak + 1 : 1;

          return {
            profile: {
              ...s.profile,
              streak: newStreak,
              lastActiveDate: today,
            },
          };
        }),

      reset: () => set({ profile: null }),
    }),
    { name: "pathmind-user" }
  )
);
```

- [ ] **Step 2: Create roadmap store**

`src/store/roadmapStore.ts`:

```ts
import { create } from "zustand";
import type { RoadmapNodeData, NodeStatus } from "@/types";

interface RoadmapState {
  nodes: RoadmapNodeData[];
  selectedNodeId: string | null;
  setNodes: (nodes: RoadmapNodeData[]) => void;
  selectNode: (id: string | null) => void;
  getNodeStatus: (nodeId: string, completedNodes: string[]) => NodeStatus;
}

export const useRoadmapStore = create<RoadmapState>()((set, get) => ({
  nodes: [],
  selectedNodeId: null,

  setNodes: (nodes) => set({ nodes }),
  selectNode: (id) => set({ selectedNodeId: id }),

  getNodeStatus: (nodeId, completedNodes) => {
    if (completedNodes.includes(nodeId)) return "completed";
    const { nodes } = get();
    const nodeIndex = nodes.findIndex((n) => n.id === nodeId);
    if (nodeIndex <= 0) return "available";
    const prevNode = nodes[nodeIndex - 1];
    return completedNodes.includes(prevNode.id) ? "available" : "locked";
  },
}));
```

- [ ] **Step 3: Create chat store**

`src/store/chatStore.ts`:

```ts
import { create } from "zustand";
import type { ChatMessage } from "@/types/chat";

interface ChatState {
  messages: ChatMessage[];
  isLoading: boolean;
  addMessage: (message: ChatMessage) => void;
  setLoading: (loading: boolean) => void;
  clearMessages: () => void;
}

export const useChatStore = create<ChatState>()((set) => ({
  messages: [],
  isLoading: false,
  addMessage: (message) =>
    set((s) => ({ messages: [...s.messages, message] })),
  setLoading: (loading) => set({ isLoading: loading }),
  clearMessages: () => set({ messages: [] }),
}));
```

- [ ] **Step 4: Create simulator store**

`src/store/simulatorStore.ts`:

```ts
import { create } from "zustand";
import type { SimulatorSession, SimulatorQuestion } from "@/types";

interface SimulatorState {
  session: SimulatorSession | null;
  isInterviewing: boolean;
  startSession: (session: SimulatorSession) => void;
  addQuestion: (question: SimulatorQuestion) => void;
  nextQuestion: () => void;
  endSession: (overallScore: number) => void;
  setInterviewing: (v: boolean) => void;
  reset: () => void;
}

export const useSimulatorStore = create<SimulatorState>()((set) => ({
  session: null,
  isInterviewing: false,

  startSession: (session) => set({ session, isInterviewing: true }),

  addQuestion: (question) =>
    set((s) => {
      if (!s.session) return s;
      return {
        session: {
          ...s.session,
          questions: [...s.session.questions, question],
        },
      };
    }),

  nextQuestion: () =>
    set((s) => {
      if (!s.session) return s;
      return {
        session: { ...s.session, currentIndex: s.session.currentIndex + 1 },
      };
    }),

  endSession: (overallScore) =>
    set((s) => {
      if (!s.session) return s;
      return {
        session: { ...s.session, completed: true, overallScore },
        isInterviewing: false,
      };
    }),

  setInterviewing: (v) => set({ isInterviewing: v }),
  reset: () => set({ session: null, isInterviewing: false }),
}));
```

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: add Zustand stores for user, roadmap, chat, simulator"
```

---

### Task 4: Services (Claude API + Voice)

**Files:**
- Create: `src/services/claudeApi.ts`, `src/services/voiceService.ts`

- [ ] **Step 1: Create Claude API service**

`src/services/claudeApi.ts`:

```ts
import type { ChatMessage } from "@/types/chat";

const API_KEY = import.meta.env.VITE_ANTHROPIC_API_KEY;
const API_URL = "https://api.anthropic.com/v1/messages";

interface ClaudeResponse {
  content: Array<{ type: string; text: string }>;
}

export async function sendMessage(
  systemPrompt: string,
  messages: ChatMessage[]
): Promise<string> {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": API_KEY,
      "anthropic-version": "2023-06-01",
      "anthropic-dangerous-direct-browser-access": "true",
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 1024,
      system: systemPrompt,
      messages: messages.map((m) => ({
        role: m.role,
        content: m.content,
      })),
    }),
  });

  if (!response.ok) {
    throw new Error(`Claude API error: ${response.status}`);
  }

  const data: ClaudeResponse = await response.json();
  return data.content[0]?.text ?? "No response";
}

export async function assessLevel(
  direction: string,
  answers: string[]
): Promise<"beginner" | "intermediate" | "advanced"> {
  const systemPrompt = `You are assessing a student's level in ${direction}. Based on their answers to assessment questions, classify them as exactly one of: beginner, intermediate, advanced. Respond with ONLY that single word.`;

  const messages: ChatMessage[] = [
    {
      id: "assess",
      role: "user",
      content: `Here are the student's answers to assessment questions:\n${answers.map((a, i) => `Q${i + 1}: ${a}`).join("\n")}\n\nWhat is their level? Respond with only: beginner, intermediate, or advanced`,
      timestamp: Date.now(),
    },
  ];

  const result = await sendMessage(systemPrompt, messages);
  const level = result.trim().toLowerCase();
  if (level === "beginner" || level === "intermediate" || level === "advanced") {
    return level;
  }
  return "beginner";
}

export async function generateTip(
  direction: string,
  level: string
): Promise<string> {
  const messages: ChatMessage[] = [
    {
      id: "tip",
      role: "user",
      content: `Give me one short, actionable tip of the day for a ${level} ${direction} student. Max 2 sentences.`,
      timestamp: Date.now(),
    },
  ];

  return sendMessage(
    `You are a helpful ${direction} mentor. Be concise and practical.`,
    messages
  );
}

export async function scoreAnswer(
  question: string,
  answer: string,
  direction: string
): Promise<{ score: number; feedback: string; modelAnswer: string }> {
  const systemPrompt = `You are an expert interviewer for ${direction} positions. Score the candidate's answer on a scale of 1-10. Respond in this exact JSON format: {"score": <number>, "feedback": "<string>", "modelAnswer": "<string>"}`;

  const messages: ChatMessage[] = [
    {
      id: "score",
      role: "user",
      content: `Question: ${question}\n\nCandidate's answer: ${answer}\n\nScore this answer. Respond ONLY with JSON.`,
      timestamp: Date.now(),
    },
  ];

  const result = await sendMessage(systemPrompt, messages);
  try {
    return JSON.parse(result);
  } catch {
    return { score: 5, feedback: result, modelAnswer: "Could not parse response" };
  }
}
```

- [ ] **Step 2: Create voice service**

`src/services/voiceService.ts`:

```ts
type ListenCallback = (transcript: string, isFinal: boolean) => void;

class VoiceService {
  private recognition: SpeechRecognition | null = null;
  private synthesis = window.speechSynthesis;
  private isListening = false;

  init() {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      this.recognition = new SpeechRecognition();
      this.recognition.continuous = true;
      this.recognition.interimResults = true;
      this.recognition.lang = "en-US";
    }
  }

  startListening(onResult: ListenCallback, onEnd?: () => void) {
    if (!this.recognition || this.isListening) return;
    this.isListening = true;

    this.recognition.onresult = (event) => {
      const last = event.results[event.results.length - 1];
      onResult(last[0].transcript, last.isFinal);
    };

    this.recognition.onend = () => {
      this.isListening = false;
      onEnd?.();
    };

    this.recognition.onerror = () => {
      this.isListening = false;
      onEnd?.();
    };

    this.recognition.start();
  }

  stopListening() {
    if (this.recognition && this.isListening) {
      this.recognition.stop();
      this.isListening = false;
    }
  }

  speak(text: string, voiceName?: string): Promise<void> {
    return new Promise((resolve) => {
      this.synthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.95;
      utterance.pitch = 1;

      if (voiceName) {
        const voices = this.synthesis.getVoices();
        const voice = voices.find((v) => v.name.includes(voiceName));
        if (voice) utterance.voice = voice;
      }

      utterance.onend = () => resolve();
      utterance.onerror = () => resolve();
      this.synthesis.speak(utterance);
    });
  }

  stopSpeaking() {
    this.synthesis.cancel();
  }

  getIsListening() {
    return this.isListening;
  }

  isSupported() {
    return !!(window.SpeechRecognition || window.webkitSpeechRecognition);
  }
}

export const voiceService = new VoiceService();
```

- [ ] **Step 3: Add SpeechRecognition type declarations**

`src/vite-env.d.ts`:

```ts
/// <reference types="vite/client" />

interface Window {
  SpeechRecognition: typeof SpeechRecognition;
  webkitSpeechRecognition: typeof SpeechRecognition;
}
```

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: add Claude API service and voice service"
```

---

## Phase 2: UI Components

### Task 5: Core UI Components

**Files:**
- Create: `src/components/ui/Button.tsx`, `src/components/ui/Card.tsx`, `src/components/ui/ProgressBar.tsx`, `src/components/ui/ProgressRing.tsx`, `src/components/ui/Modal.tsx`, `src/components/ui/Input.tsx`, `src/components/ui/Chip.tsx`, `src/components/ui/Badge.tsx`, `src/components/ui/Tooltip.tsx`

- [ ] **Step 1: Create Button component**

`src/components/ui/Button.tsx`:

```tsx
import { cn } from "@/lib/cn";
import { motion } from "framer-motion";
import type { ButtonHTMLAttributes, ReactNode } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "ghost";
  size?: "sm" | "md" | "lg";
  children: ReactNode;
}

export function Button({
  variant = "primary",
  size = "md",
  className,
  children,
  ...props
}: ButtonProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      className={cn(
        "inline-flex items-center justify-center gap-2 rounded-xl font-medium transition-all duration-200 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed",
        {
          "bg-primary text-white shadow-lg shadow-primary/25 hover:shadow-primary/40":
            variant === "primary",
          "bg-surface border border-border text-text hover:border-primary/50":
            variant === "secondary",
          "bg-transparent text-text-secondary hover:text-text hover:bg-surface":
            variant === "ghost",
        },
        {
          "px-3 py-1.5 text-sm": size === "sm",
          "px-5 py-2.5 text-sm": size === "md",
          "px-7 py-3.5 text-base": size === "lg",
        },
        className
      )}
      {...(props as any)}
    >
      {children}
    </motion.button>
  );
}
```

- [ ] **Step 2: Create Card component**

`src/components/ui/Card.tsx`:

```tsx
import { cn } from "@/lib/cn";
import { motion } from "framer-motion";
import type { HTMLAttributes, ReactNode } from "react";

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  glow?: string;
  hover?: boolean;
}

export function Card({ children, className, glow, hover = false, ...props }: CardProps) {
  return (
    <motion.div
      whileHover={hover ? { y: -2, scale: 1.01 } : undefined}
      className={cn(
        "rounded-2xl border border-border bg-surface/80 backdrop-blur-xl p-6 relative overflow-hidden",
        hover && "cursor-pointer transition-colors hover:border-primary/30",
        className
      )}
      style={
        glow
          ? {
              boxShadow: `0 0 40px ${glow}15, inset 0 1px 0 ${glow}10`,
            }
          : undefined
      }
      {...(props as any)}
    >
      {children}
    </motion.div>
  );
}
```

- [ ] **Step 3: Create ProgressBar component**

`src/components/ui/ProgressBar.tsx`:

```tsx
import { cn } from "@/lib/cn";
import { motion } from "framer-motion";

interface ProgressBarProps {
  value: number;
  max?: number;
  color?: string;
  className?: string;
  showLabel?: boolean;
}

export function ProgressBar({
  value,
  max = 100,
  color = "#6C63FF",
  className,
  showLabel = false,
}: ProgressBarProps) {
  const percent = Math.min((value / max) * 100, 100);

  return (
    <div className={cn("w-full", className)}>
      {showLabel && (
        <div className="flex justify-between text-xs text-text-secondary mb-1">
          <span>{value}</span>
          <span>{max}</span>
        </div>
      )}
      <div className="h-2 rounded-full bg-border overflow-hidden">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${percent}%` }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="h-full rounded-full"
          style={{
            background: `linear-gradient(90deg, ${color}, ${color}99)`,
            boxShadow: `0 0 12px ${color}40`,
          }}
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Create ProgressRing component**

`src/components/ui/ProgressRing.tsx`:

```tsx
import { motion } from "framer-motion";

interface ProgressRingProps {
  value: number;
  max?: number;
  size?: number;
  strokeWidth?: number;
  color?: string;
  children?: React.ReactNode;
}

export function ProgressRing({
  value,
  max = 100,
  size = 120,
  strokeWidth = 8,
  color = "#6C63FF",
  children,
}: ProgressRingProps) {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const percent = Math.min(value / max, 1);
  const offset = circumference * (1 - percent);

  return (
    <div className="relative inline-flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="#1E1E2E"
          strokeWidth={strokeWidth}
        />
        <motion.circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke={color}
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          strokeDasharray={circumference}
          initial={{ strokeDashoffset: circumference }}
          animate={{ strokeDashoffset: offset }}
          transition={{ duration: 1, ease: "easeOut" }}
          style={{ filter: `drop-shadow(0 0 6px ${color}60)` }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">
        {children}
      </div>
    </div>
  );
}
```

- [ ] **Step 5: Create Modal, Input, Chip, Badge, Tooltip components**

`src/components/ui/Modal.tsx`:

```tsx
import { motion, AnimatePresence } from "framer-motion";
import { X } from "lucide-react";

interface ModalProps {
  open: boolean;
  onClose: () => void;
  children: React.ReactNode;
  title?: string;
}

export function Modal({ open, onClose, children, title }: ModalProps) {
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
        >
          <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" onClick={onClose} />
          <motion.div
            initial={{ scale: 0.9, opacity: 0, y: 20 }}
            animate={{ scale: 1, opacity: 1, y: 0 }}
            exit={{ scale: 0.9, opacity: 0, y: 20 }}
            className="relative z-10 w-full max-w-lg rounded-2xl border border-border bg-surface p-6"
          >
            <div className="flex items-center justify-between mb-4">
              {title && <h2 className="text-lg font-semibold">{title}</h2>}
              <button onClick={onClose} className="p-1 rounded-lg hover:bg-border/50 text-text-secondary cursor-pointer">
                <X size={20} />
              </button>
            </div>
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

`src/components/ui/Input.tsx`:

```tsx
import { cn } from "@/lib/cn";
import type { InputHTMLAttributes } from "react";

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
}

export function Input({ label, className, ...props }: InputProps) {
  return (
    <div className="w-full">
      {label && <label className="block text-sm text-text-secondary mb-1.5">{label}</label>}
      <input
        className={cn(
          "w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50",
          className
        )}
        {...props}
      />
    </div>
  );
}
```

`src/components/ui/Chip.tsx`:

```tsx
import { cn } from "@/lib/cn";
import { motion } from "framer-motion";

interface ChipProps {
  label: string;
  onClick?: () => void;
  active?: boolean;
  className?: string;
}

export function Chip({ label, onClick, active, className }: ChipProps) {
  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      onClick={onClick}
      className={cn(
        "px-4 py-2 rounded-full text-sm font-medium transition-all cursor-pointer border",
        active
          ? "bg-primary/20 border-primary/50 text-primary"
          : "bg-surface border-border text-text-secondary hover:border-primary/30 hover:text-text",
        className
      )}
    >
      {label}
    </motion.button>
  );
}
```

`src/components/ui/Badge.tsx`:

```tsx
import { cn } from "@/lib/cn";
import type { BadgeRarity } from "@/types";

const rarityStyles: Record<BadgeRarity, string> = {
  Common: "border-text-secondary/30 text-text-secondary",
  Rare: "border-primary/50 text-primary",
  Epic: "border-accent/50 text-accent",
  Legendary: "border-warning/50 text-warning",
};

interface BadgeProps {
  icon: string;
  name: string;
  rarity: BadgeRarity;
  locked?: boolean;
  className?: string;
}

export function Badge({ icon, name, rarity, locked, className }: BadgeProps) {
  return (
    <div
      className={cn(
        "flex flex-col items-center gap-2 p-4 rounded-2xl border bg-surface/50 transition-all",
        locked ? "opacity-40 grayscale" : rarityStyles[rarity],
        className
      )}
    >
      <span className="text-3xl">{icon}</span>
      <span className="text-xs font-medium text-center">{name}</span>
      <span
        className={cn(
          "text-[10px] uppercase tracking-wider font-semibold",
          locked ? "text-text-secondary/50" : rarityStyles[rarity]
        )}
      >
        {rarity}
      </span>
    </div>
  );
}
```

`src/components/ui/Tooltip.tsx`:

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

interface TooltipProps {
  content: string;
  children: React.ReactNode;
}

export function Tooltip({ content, children }: TooltipProps) {
  const [show, setShow] = useState(false);

  return (
    <div
      className="relative inline-flex"
      onMouseEnter={() => setShow(true)}
      onMouseLeave={() => setShow(false)}
    >
      {children}
      <AnimatePresence>
        {show && (
          <motion.div
            initial={{ opacity: 0, y: 4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 4 }}
            className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-3 py-1.5 rounded-lg bg-border text-xs text-text whitespace-nowrap z-50"
          >
            {content}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

- [ ] **Step 6: Commit**

```bash
git add -A && git commit -m "feat: add core UI components (Button, Card, ProgressBar, Modal, etc.)"
```

---

### Task 6: Layout Components

**Files:**
- Create: `src/components/layout/Sidebar.tsx`, `src/components/layout/TopBar.tsx`, `src/components/layout/PageWrapper.tsx`

- [ ] **Step 1: Create Sidebar**

`src/components/layout/Sidebar.tsx`:

```tsx
import { NavLink } from "react-router-dom";
import { cn } from "@/lib/cn";
import {
  LayoutDashboard,
  Map,
  MessageCircle,
  Mic,
  BookOpen,
  Trophy,
  User,
} from "lucide-react";

const navItems = [
  { to: "/dashboard", icon: LayoutDashboard, label: "Dashboard" },
  { to: "/roadmap", icon: Map, label: "Roadmap" },
  { to: "/mentor", icon: MessageCircle, label: "AI Mentor" },
  { to: "/simulator", icon: Mic, label: "Simulator" },
  { to: "/achievements", icon: Trophy, label: "Achievements" },
  { to: "/profile", icon: User, label: "Profile" },
];

export function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-full w-64 border-r border-border bg-surface/50 backdrop-blur-xl z-40 flex flex-col">
      <div className="p-6">
        <h1 className="text-xl font-bold">
          <span className="text-primary">Path</span>
          <span className="text-accent">Mind</span>
        </h1>
      </div>

      <nav className="flex-1 px-3 space-y-1">
        {navItems.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 px-4 py-2.5 rounded-xl text-sm font-medium transition-all",
                isActive
                  ? "bg-primary/10 text-primary"
                  : "text-text-secondary hover:text-text hover:bg-surface"
              )
            }
          >
            <Icon size={18} />
            {label}
          </NavLink>
        ))}
      </nav>

      <div className="p-4 mx-3 mb-4 rounded-xl bg-bg border border-border">
        <p className="text-xs text-text-secondary">AI-Powered Learning</p>
        <p className="text-xs text-primary mt-1">PathMind v1.0</p>
      </div>
    </aside>
  );
}
```

- [ ] **Step 2: Create TopBar**

`src/components/layout/TopBar.tsx`:

```tsx
import { useUserStore } from "@/store/userStore";
import { XPBar } from "@/components/gamification/XPBar";
import { StreakCounter } from "@/components/gamification/StreakCounter";

export function TopBar() {
  const profile = useUserStore((s) => s.profile);
  if (!profile) return null;

  const hour = new Date().getHours();
  const greeting =
    hour < 12 ? "Good morning" : hour < 18 ? "Good afternoon" : "Good evening";

  return (
    <header className="h-16 border-b border-border bg-surface/50 backdrop-blur-xl flex items-center justify-between px-6">
      <div>
        <h2 className="text-sm font-medium">
          {greeting}, <span className="text-primary">{profile.name}</span>
        </h2>
      </div>

      <div className="flex items-center gap-6">
        <XPBar />
        <StreakCounter />
      </div>
    </header>
  );
}
```

- [ ] **Step 3: Create PageWrapper**

`src/components/layout/PageWrapper.tsx`:

```tsx
import { Sidebar } from "./Sidebar";
import { TopBar } from "./TopBar";

export function PageWrapper({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <Sidebar />
      <div className="pl-64">
        <TopBar />
        <main className="p-6">{children}</main>
      </div>
    </div>
  );
}
```

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: add layout components (Sidebar, TopBar, PageWrapper)"
```

---

### Task 7: Gamification Components

**Files:**
- Create: `src/components/gamification/XPBar.tsx`, `src/components/gamification/StreakCounter.tsx`, `src/components/gamification/BadgeReveal.tsx`, `src/components/gamification/LevelUpModal.tsx`

- [ ] **Step 1: Create XPBar**

`src/components/gamification/XPBar.tsx`:

```tsx
import { useUserStore } from "@/store/userStore";
import { LEVELS_ORDERED, LEVEL_THRESHOLDS } from "@/lib/constants";
import { ProgressBar } from "@/components/ui/ProgressBar";

export function XPBar() {
  const profile = useUserStore((s) => s.profile);
  if (!profile) return null;

  const currentIdx = LEVELS_ORDERED.indexOf(profile.level);
  const nextLevel = LEVELS_ORDERED[currentIdx + 1];
  const currentThreshold = LEVEL_THRESHOLDS[profile.level];
  const nextThreshold = nextLevel ? LEVEL_THRESHOLDS[nextLevel] : currentThreshold;
  const progress = profile.xp - currentThreshold;
  const needed = nextThreshold - currentThreshold;

  return (
    <div className="flex items-center gap-3">
      <span className="text-xs font-semibold text-primary">{profile.level}</span>
      <div className="w-32">
        <ProgressBar value={progress} max={needed || 1} color="#6C63FF" />
      </div>
      <span className="text-xs text-text-secondary">{profile.xp} XP</span>
    </div>
  );
}
```

- [ ] **Step 2: Create StreakCounter**

`src/components/gamification/StreakCounter.tsx`:

```tsx
import { useUserStore } from "@/store/userStore";
import { Flame } from "lucide-react";
import { motion } from "framer-motion";

export function StreakCounter() {
  const streak = useUserStore((s) => s.profile?.streak ?? 0);

  return (
    <div className="flex items-center gap-2">
      <motion.div
        animate={streak > 0 ? { scale: [1, 1.2, 1] } : undefined}
        transition={{ repeat: Infinity, duration: 1.5 }}
      >
        <Flame
          size={18}
          className={streak > 0 ? "text-warning" : "text-text-secondary"}
          fill={streak > 0 ? "#FFB800" : "none"}
        />
      </motion.div>
      <span className="text-sm font-semibold">
        {streak} <span className="text-text-secondary font-normal">day{streak !== 1 ? "s" : ""}</span>
      </span>
    </div>
  );
}
```

- [ ] **Step 3: Create BadgeReveal**

`src/components/gamification/BadgeReveal.tsx`:

```tsx
import { motion, AnimatePresence } from "framer-motion";
import type { Badge as BadgeType } from "@/types";

interface BadgeRevealProps {
  badge: BadgeType | null;
  onClose: () => void;
}

export function BadgeReveal({ badge, onClose }: BadgeRevealProps) {
  return (
    <AnimatePresence>
      {badge && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
          onClick={onClose}
        >
          <motion.div
            initial={{ scale: 0, rotate: -180 }}
            animate={{ scale: 1, rotate: 0 }}
            exit={{ scale: 0, rotate: 180 }}
            transition={{ type: "spring", damping: 15 }}
            className="flex flex-col items-center gap-4 p-8 rounded-3xl border border-primary/30 bg-surface"
          >
            <motion.span
              className="text-7xl"
              animate={{ scale: [1, 1.3, 1] }}
              transition={{ repeat: 3, duration: 0.6 }}
            >
              {badge.icon}
            </motion.span>
            <h3 className="text-xl font-bold text-primary">Badge Unlocked!</h3>
            <p className="text-lg font-semibold">{badge.name}</p>
            <p className="text-sm text-text-secondary text-center max-w-xs">
              {badge.description}
            </p>
            <span className="text-xs uppercase tracking-wider text-warning font-bold">
              {badge.rarity}
            </span>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

- [ ] **Step 4: Create LevelUpModal**

`src/components/gamification/LevelUpModal.tsx`:

```tsx
import { Modal } from "@/components/ui/Modal";
import { motion } from "framer-motion";
import type { Level } from "@/types";

interface LevelUpModalProps {
  open: boolean;
  onClose: () => void;
  level: Level;
}

export function LevelUpModal({ open, onClose, level }: LevelUpModalProps) {
  return (
    <Modal open={open} onClose={onClose}>
      <div className="flex flex-col items-center gap-4 py-4">
        <motion.div
          animate={{ rotate: [0, 10, -10, 0], scale: [1, 1.2, 1] }}
          transition={{ repeat: 2, duration: 0.5 }}
          className="text-6xl"
        >
          🎉
        </motion.div>
        <h2 className="text-2xl font-bold">Level Up!</h2>
        <p className="text-lg text-primary font-semibold">{level}</p>
        <p className="text-sm text-text-secondary text-center">
          Keep going — you're making amazing progress!
        </p>
      </div>
    </Modal>
  );
}
```

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: add gamification components (XPBar, StreakCounter, BadgeReveal, LevelUpModal)"
```

---

## Phase 3: Pages

### Task 8: Onboarding Page

**Files:**
- Create: `src/pages/Onboarding.tsx`

- [ ] **Step 1: Create the full Onboarding page with 3-step wizard**

`src/pages/Onboarding.tsx`:

```tsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { Code2, Languages, Headphones, Building2, ArrowRight, Sparkles, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { DIRECTIONS } from "@/data/directions";
import { useUserStore } from "@/store/userStore";
import { sendMessage, assessLevel } from "@/services/claudeApi";
import type { Direction } from "@/types";
import type { ChatMessage } from "@/types/chat";

const iconMap = { Code2, Languages, Headphones, Building2 };
const directionList = Object.values(DIRECTIONS);

const ASSESSMENT_QUESTIONS: Record<Direction, string[]> = {
  frontend: [
    "What experience do you have with HTML and CSS?",
    "Have you worked with JavaScript before? If so, what have you built?",
    "Do you know what React is? Have you used any frameworks?",
    "Can you explain what responsive design means?",
    "What tools or code editors do you use for development?",
  ],
  english: [
    "How would you describe your current English level?",
    "Do you use English at work or in daily life?",
    "Can you tell me about your favorite hobby in English?",
    "What is the most difficult part of English for you?",
    "What is your goal with learning English?",
  ],
  callcenter: [
    "Have you ever worked in customer service or a call center?",
    "How would you handle an angry customer?",
    "What do you think makes good customer service?",
    "Are you comfortable speaking on the phone for long periods?",
    "Describe a time you resolved a conflict or problem for someone.",
  ],
  cib: [
    "What do you know about Corporate & Investment Banking?",
    "Have you studied finance or economics?",
    "Can you explain what a bond is?",
    "What financial tools or software have you used (e.g., Excel)?",
    "Why are you interested in a career in banking?",
  ],
};

export default function Onboarding() {
  const navigate = useNavigate();
  const { setProfile, completeOnboarding } = useUserStore();
  const [step, setStep] = useState(0);
  const [name, setName] = useState("");
  const [selectedDirection, setSelectedDirection] = useState<Direction | null>(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState<string[]>([]);
  const [currentAnswer, setCurrentAnswer] = useState("");
  const [chatMessages, setChatMessages] = useState<Array<{ role: "bot" | "user"; text: string }>>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [assessmentResult, setAssessmentResult] = useState<"beginner" | "intermediate" | "advanced" | null>(null);

  const handleDirectionSelect = (dir: Direction) => {
    setSelectedDirection(dir);
    setStep(1);
    const questions = ASSESSMENT_QUESTIONS[dir];
    setChatMessages([
      { role: "bot", text: `Hi ${name || "there"}! I'm going to ask you a few questions to understand your current level. Let's start!` },
      { role: "bot", text: questions[0] },
    ]);
  };

  const handleAnswer = async () => {
    if (!currentAnswer.trim() || !selectedDirection) return;

    const newAnswers = [...answers, currentAnswer];
    setAnswers(newAnswers);
    setChatMessages((prev) => [...prev, { role: "user", text: currentAnswer }]);
    setCurrentAnswer("");

    const questions = ASSESSMENT_QUESTIONS[selectedDirection];
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion((q) => q + 1);
      setChatMessages((prev) => [
        ...prev,
        { role: "bot", text: questions[currentQuestion + 1] },
      ]);
    } else {
      setIsLoading(true);
      setChatMessages((prev) => [
        ...prev,
        { role: "bot", text: "Great! Let me analyze your answers..." },
      ]);

      let level: "beginner" | "intermediate" | "advanced" = "beginner";
      try {
        level = await assessLevel(DIRECTIONS[selectedDirection].name, newAnswers);
      } catch {
        // fallback to beginner
      }

      setAssessmentResult(level);
      setIsLoading(false);
      setStep(2);
    }
  };

  const handleFinish = () => {
    if (!selectedDirection || !assessmentResult) return;
    setProfile({
      name: name || "Learner",
      direction: selectedDirection,
      level: "Novice",
      xp: 0,
      streak: 0,
      lastActiveDate: new Date().toISOString().split("T")[0],
      completedNodes: [],
      completedLessons: [],
      earnedBadges: [],
      assessmentLevel: assessmentResult,
      onboardingComplete: true,
    });
    completeOnboarding();
    navigate("/dashboard");
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        {/* Progress dots */}
        <div className="flex justify-center gap-2 mb-8">
          {[0, 1, 2].map((i) => (
            <motion.div
              key={i}
              className="h-2 rounded-full"
              animate={{
                width: step === i ? 32 : 8,
                backgroundColor: step >= i ? "#6C63FF" : "#1E1E2E",
              }}
              transition={{ duration: 0.3 }}
            />
          ))}
        </div>

        <AnimatePresence mode="wait">
          {/* Step 0: Choose direction */}
          {step === 0 && (
            <motion.div
              key="step0"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <div className="text-center mb-8">
                <h1 className="text-3xl font-bold mb-2">
                  Welcome to <span className="text-primary">Path</span>
                  <span className="text-accent">Mind</span>
                </h1>
                <p className="text-text-secondary">Choose your learning path</p>
              </div>

              <Input
                label="What's your name?"
                placeholder="Enter your name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />

              <div className="grid grid-cols-2 gap-4 mt-6">
                {directionList.map((dir) => {
                  const Icon = iconMap[dir.icon as keyof typeof iconMap];
                  return (
                    <Card
                      key={dir.id}
                      hover
                      glow={dir.color}
                      onClick={() => handleDirectionSelect(dir.id)}
                      className="flex flex-col items-center gap-3 text-center cursor-pointer"
                    >
                      <div
                        className="w-12 h-12 rounded-xl flex items-center justify-center"
                        style={{ backgroundColor: `${dir.color}15` }}
                      >
                        <Icon size={24} style={{ color: dir.color }} />
                      </div>
                      <h3 className="font-semibold text-sm">{dir.name}</h3>
                      <p className="text-xs text-text-secondary leading-relaxed">
                        {dir.description}
                      </p>
                    </Card>
                  );
                })}
              </div>
            </motion.div>
          )}

          {/* Step 1: Assessment chat */}
          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-4"
            >
              <div className="text-center mb-4">
                <h2 className="text-xl font-bold">Level Assessment</h2>
                <p className="text-text-secondary text-sm">
                  Question {Math.min(currentQuestion + 1, 5)} of 5
                </p>
              </div>

              <Card className="h-80 overflow-y-auto space-y-3">
                {chatMessages.map((msg, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
                  >
                    <div
                      className={`max-w-[80%] px-4 py-2.5 rounded-2xl text-sm ${
                        msg.role === "user"
                          ? "bg-primary text-white rounded-br-md"
                          : "bg-border/50 text-text rounded-bl-md"
                      }`}
                    >
                      {msg.text}
                    </div>
                  </motion.div>
                ))}
                {isLoading && (
                  <div className="flex justify-start">
                    <div className="bg-border/50 px-4 py-2.5 rounded-2xl rounded-bl-md">
                      <Loader2 className="animate-spin" size={16} />
                    </div>
                  </div>
                )}
              </Card>

              {!isLoading && currentQuestion < 5 && (
                <div className="flex gap-2">
                  <Input
                    placeholder="Type your answer..."
                    value={currentAnswer}
                    onChange={(e) => setCurrentAnswer(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && handleAnswer()}
                  />
                  <Button onClick={handleAnswer} disabled={!currentAnswer.trim()}>
                    <ArrowRight size={18} />
                  </Button>
                </div>
              )}
            </motion.div>
          )}

          {/* Step 2: Results + Start */}
          {step === 2 && assessmentResult && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="text-center space-y-6"
            >
              <motion.div
                animate={{ scale: [0.8, 1.1, 1] }}
                transition={{ duration: 0.6 }}
              >
                <Sparkles size={48} className="mx-auto text-primary" />
              </motion.div>

              <h2 className="text-2xl font-bold">Your Learning Plan is Ready!</h2>

              <Card glow="#6C63FF" className="text-left space-y-3">
                <p className="text-sm text-text-secondary">Assessment Result</p>
                <p className="text-lg font-semibold capitalize text-primary">
                  {assessmentResult} Level
                </p>
                <p className="text-sm text-text-secondary">
                  Direction: {selectedDirection && DIRECTIONS[selectedDirection].name}
                </p>
                <p className="text-sm text-text-secondary">
                  Your personalized roadmap has been generated with topics tailored to your {assessmentResult} level.
                </p>
              </Card>

              <Button size="lg" onClick={handleFinish}>
                Start Learning <ArrowRight size={18} />
              </Button>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "feat: add Onboarding page with 3-step wizard and AI assessment"
```

---

### Task 9: Roadmap Data

**Files:**
- Create: `src/data/roadmaps/frontend.ts`, `src/data/roadmaps/english.ts`, `src/data/roadmaps/callcenter.ts`, `src/data/roadmaps/cib.ts`, `src/data/achievements.ts`, `src/data/lessons.ts`

- [ ] **Step 1: Create frontend roadmap data**

`src/data/roadmaps/frontend.ts`:

```ts
import type { RoadmapNodeData } from "@/types";

export const frontendRoadmap: RoadmapNodeData[] = [
  // Section 1: HTML Foundations
  { id: "fe-1", title: "HTML Basics", description: "Learn the building blocks of the web — tags, elements, attributes, and document structure.", section: "HTML Foundations", sectionIndex: 0, nodeIndex: 0, estimatedMinutes: 30, lessons: [{ id: "fe-1-1", title: "Document Structure", estimatedMinutes: 15 }, { id: "fe-1-2", title: "Common Tags", estimatedMinutes: 15 }] },
  { id: "fe-2", title: "Forms & Tables", description: "Build interactive forms and structured data tables.", section: "HTML Foundations", sectionIndex: 0, nodeIndex: 1, estimatedMinutes: 25, lessons: [{ id: "fe-2-1", title: "Form Elements", estimatedMinutes: 15 }, { id: "fe-2-2", title: "Tables", estimatedMinutes: 10 }] },
  { id: "fe-3", title: "Semantic HTML", description: "Use semantic elements for better accessibility and SEO.", section: "HTML Foundations", sectionIndex: 0, nodeIndex: 2, estimatedMinutes: 20, lessons: [{ id: "fe-3-1", title: "Semantic Elements", estimatedMinutes: 20 }] },
  { id: "fe-4", title: "Accessibility Basics", description: "Make your websites usable for everyone.", section: "HTML Foundations", sectionIndex: 0, nodeIndex: 3, estimatedMinutes: 25, lessons: [{ id: "fe-4-1", title: "ARIA & A11y", estimatedMinutes: 25 }] },

  // Section 2: CSS Mastery
  { id: "fe-5", title: "CSS Fundamentals", description: "Selectors, properties, the box model, and cascade.", section: "CSS Mastery", sectionIndex: 1, nodeIndex: 0, estimatedMinutes: 35, lessons: [{ id: "fe-5-1", title: "Selectors & Box Model", estimatedMinutes: 20 }, { id: "fe-5-2", title: "Colors & Typography", estimatedMinutes: 15 }] },
  { id: "fe-6", title: "Flexbox", description: "Master flexible box layout for modern interfaces.", section: "CSS Mastery", sectionIndex: 1, nodeIndex: 1, estimatedMinutes: 30, lessons: [{ id: "fe-6-1", title: "Flexbox Layout", estimatedMinutes: 30 }] },
  { id: "fe-7", title: "CSS Grid", description: "Two-dimensional layout system for complex designs.", section: "CSS Mastery", sectionIndex: 1, nodeIndex: 2, estimatedMinutes: 30, lessons: [{ id: "fe-7-1", title: "Grid Layout", estimatedMinutes: 30 }] },
  { id: "fe-8", title: "Responsive Design", description: "Media queries, mobile-first, and fluid layouts.", section: "CSS Mastery", sectionIndex: 1, nodeIndex: 3, estimatedMinutes: 30, lessons: [{ id: "fe-8-1", title: "Media Queries", estimatedMinutes: 15 }, { id: "fe-8-2", title: "Mobile-First", estimatedMinutes: 15 }] },
  { id: "fe-9", title: "CSS Animations", description: "Transitions, keyframes, and motion design.", section: "CSS Mastery", sectionIndex: 1, nodeIndex: 4, estimatedMinutes: 25, lessons: [{ id: "fe-9-1", title: "Animations & Transitions", estimatedMinutes: 25 }] },

  // Section 3: JavaScript Core
  { id: "fe-10", title: "JS Fundamentals", description: "Variables, types, operators, and control flow.", section: "JavaScript Core", sectionIndex: 2, nodeIndex: 0, estimatedMinutes: 40, lessons: [{ id: "fe-10-1", title: "Variables & Types", estimatedMinutes: 20 }, { id: "fe-10-2", title: "Control Flow", estimatedMinutes: 20 }] },
  { id: "fe-11", title: "Functions & Scope", description: "Functions, closures, and scope chains.", section: "JavaScript Core", sectionIndex: 2, nodeIndex: 1, estimatedMinutes: 35, lessons: [{ id: "fe-11-1", title: "Functions & Closures", estimatedMinutes: 35 }] },
  { id: "fe-12", title: "Arrays & Objects", description: "Working with data structures and methods.", section: "JavaScript Core", sectionIndex: 2, nodeIndex: 2, estimatedMinutes: 35, lessons: [{ id: "fe-12-1", title: "Array Methods", estimatedMinutes: 20 }, { id: "fe-12-2", title: "Object Patterns", estimatedMinutes: 15 }] },
  { id: "fe-13", title: "DOM Manipulation", description: "Interact with the page using JavaScript.", section: "JavaScript Core", sectionIndex: 2, nodeIndex: 3, estimatedMinutes: 30, lessons: [{ id: "fe-13-1", title: "DOM API", estimatedMinutes: 30 }] },
  { id: "fe-14", title: "Async JavaScript", description: "Promises, async/await, and fetch API.", section: "JavaScript Core", sectionIndex: 2, nodeIndex: 4, estimatedMinutes: 40, lessons: [{ id: "fe-14-1", title: "Promises & Async/Await", estimatedMinutes: 20 }, { id: "fe-14-2", title: "Fetch API", estimatedMinutes: 20 }] },
  { id: "fe-15", title: "ES6+ Features", description: "Destructuring, spread, modules, and more.", section: "JavaScript Core", sectionIndex: 2, nodeIndex: 5, estimatedMinutes: 30, lessons: [{ id: "fe-15-1", title: "Modern JS Features", estimatedMinutes: 30 }] },

  // Section 4: React
  { id: "fe-16", title: "React Basics", description: "Components, JSX, and rendering.", section: "React", sectionIndex: 3, nodeIndex: 0, estimatedMinutes: 40, lessons: [{ id: "fe-16-1", title: "JSX & Components", estimatedMinutes: 20 }, { id: "fe-16-2", title: "Props & Rendering", estimatedMinutes: 20 }] },
  { id: "fe-17", title: "State & Events", description: "useState, event handling, and controlled components.", section: "React", sectionIndex: 3, nodeIndex: 1, estimatedMinutes: 35, lessons: [{ id: "fe-17-1", title: "useState & Events", estimatedMinutes: 35 }] },
  { id: "fe-18", title: "useEffect & Hooks", description: "Side effects, lifecycle, and custom hooks.", section: "React", sectionIndex: 3, nodeIndex: 2, estimatedMinutes: 40, lessons: [{ id: "fe-18-1", title: "useEffect", estimatedMinutes: 20 }, { id: "fe-18-2", title: "Custom Hooks", estimatedMinutes: 20 }] },
  { id: "fe-19", title: "React Router", description: "Client-side routing and navigation.", section: "React", sectionIndex: 3, nodeIndex: 3, estimatedMinutes: 25, lessons: [{ id: "fe-19-1", title: "Routing", estimatedMinutes: 25 }] },
  { id: "fe-20", title: "State Management", description: "Context, Zustand, and global state patterns.", section: "React", sectionIndex: 3, nodeIndex: 4, estimatedMinutes: 35, lessons: [{ id: "fe-20-1", title: "State Management", estimatedMinutes: 35 }] },

  // Section 5: Professional Skills
  { id: "fe-21", title: "TypeScript Basics", description: "Type safety for JavaScript.", section: "Professional Skills", sectionIndex: 4, nodeIndex: 0, estimatedMinutes: 40, lessons: [{ id: "fe-21-1", title: "TypeScript Fundamentals", estimatedMinutes: 40 }] },
  { id: "fe-22", title: "Testing", description: "Unit and integration testing with Jest and React Testing Library.", section: "Professional Skills", sectionIndex: 4, nodeIndex: 1, estimatedMinutes: 35, lessons: [{ id: "fe-22-1", title: "Testing React Apps", estimatedMinutes: 35 }] },
  { id: "fe-23", title: "Git & GitHub", description: "Version control, branching, and collaboration.", section: "Professional Skills", sectionIndex: 4, nodeIndex: 2, estimatedMinutes: 30, lessons: [{ id: "fe-23-1", title: "Git Workflow", estimatedMinutes: 30 }] },
  { id: "fe-24", title: "Performance", description: "Optimization techniques and web vitals.", section: "Professional Skills", sectionIndex: 4, nodeIndex: 3, estimatedMinutes: 30, lessons: [{ id: "fe-24-1", title: "Performance Optimization", estimatedMinutes: 30 }] },
  { id: "fe-25", title: "Deployment", description: "Build, deploy, and CI/CD basics.", section: "Professional Skills", sectionIndex: 4, nodeIndex: 4, estimatedMinutes: 25, lessons: [{ id: "fe-25-1", title: "Build & Deploy", estimatedMinutes: 25 }] },
];
```

- [ ] **Step 2: Create other 3 roadmap files (english, callcenter, cib) with similar structure**

Create `src/data/roadmaps/english.ts`, `src/data/roadmaps/callcenter.ts`, `src/data/roadmaps/cib.ts` — each with 20-25 nodes across 5 sections specific to that direction.

*(Full node data will be in implementation — each follows the same RoadmapNodeData[] shape with direction-appropriate topics.)*

- [ ] **Step 3: Create achievements data**

`src/data/achievements.ts`:

```ts
import type { Badge } from "@/types";

export const BADGES: Badge[] = [
  { id: "first-step", name: "First Step", description: "Complete your first lesson", icon: "🚀", rarity: "Common", condition: "completedLessons >= 1" },
  { id: "fast-learner", name: "Fast Learner", description: "Complete 10 lessons", icon: "⚡", rarity: "Rare", condition: "completedLessons >= 10" },
  { id: "voice-warrior", name: "Voice Warrior", description: "Complete 10 voice sessions", icon: "🎙️", rarity: "Rare", condition: "voiceSessions >= 10" },
  { id: "interview-ready", name: "Interview Ready", description: "Pass 5 interview simulations", icon: "💼", rarity: "Epic", condition: "interviewSessions >= 5" },
  { id: "streak-7", name: "Week Warrior", description: "7-day learning streak", icon: "🔥", rarity: "Rare", condition: "streak >= 7" },
  { id: "streak-30", name: "Streak Legend", description: "30-day learning streak", icon: "🏆", rarity: "Legendary", condition: "streak >= 30" },
  { id: "streak-100", name: "Unstoppable", description: "100-day learning streak", icon: "💎", rarity: "Legendary", condition: "streak >= 100" },
  { id: "half-way", name: "Half Way There", description: "Complete 50% of your roadmap", icon: "🗺️", rarity: "Epic", condition: "roadmapProgress >= 50" },
  { id: "road-complete", name: "Road Master", description: "Complete your entire roadmap", icon: "👑", rarity: "Legendary", condition: "roadmapProgress >= 100" },
  { id: "code-whisperer", name: "Code Whisperer", description: "Master all Frontend sections", icon: "💻", rarity: "Legendary", direction: "frontend", condition: "allSectionsComplete" },
  { id: "fluent-speaker", name: "Fluent Speaker", description: "Master all English sections", icon: "🗣️", rarity: "Legendary", direction: "english", condition: "allSectionsComplete" },
  { id: "service-star", name: "Service Star", description: "Master all Call Center sections", icon: "⭐", rarity: "Legendary", direction: "callcenter", condition: "allSectionsComplete" },
  { id: "finance-guru", name: "Finance Guru", description: "Master all CIB sections", icon: "💰", rarity: "Legendary", direction: "cib", condition: "allSectionsComplete" },
];
```

- [ ] **Step 4: Create lessons data stub**

`src/data/lessons.ts`:

```ts
export interface LessonContent {
  id: string;
  title: string;
  content: string;
  codeExamples?: Array<{ language: string; code: string }>;
  quiz?: Array<{ question: string; options: string[]; correct: number }>;
}

export const LESSONS: Record<string, LessonContent> = {
  "fe-1-1": {
    id: "fe-1-1",
    title: "Document Structure",
    content: `# HTML Document Structure

Every HTML page starts with a basic structure that tells the browser how to render the content.

## The DOCTYPE

The \`<!DOCTYPE html>\` declaration tells the browser this is an HTML5 document.

## The HTML Element

The \`<html>\` element is the root of the page. Inside it, you have:

- **\`<head>\`** — metadata, title, links to stylesheets
- **\`<body>\`** — visible content

## Basic Template

Every HTML file follows this pattern. The head contains information *about* the page, while the body contains the page itself.`,
    codeExamples: [
      {
        language: "html",
        code: `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My First Page</title>
</head>
<body>
  <h1>Hello World!</h1>
  <p>This is my first web page.</p>
</body>
</html>`,
      },
    ],
    quiz: [
      {
        question: "What does the <head> element contain?",
        options: ["Visible content", "Metadata and page info", "Images", "Links"],
        correct: 1,
      },
      {
        question: "Which declaration specifies HTML5?",
        options: ["<html5>", "<!DOCTYPE html>", "<version>5</version>", "<meta html5>"],
        correct: 1,
      },
    ],
  },
};
```

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: add roadmap data, achievements, and lesson content"
```

---

### Task 10: Dashboard Page

**Files:**
- Create: `src/pages/Dashboard.tsx`

- [ ] **Step 1: Create Dashboard page**

`src/pages/Dashboard.tsx`:

```tsx
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { BookOpen, Clock, Flame, Trophy, Sparkles, ArrowRight } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { ProgressRing } from "@/components/ui/ProgressRing";
import { useUserStore } from "@/store/userStore";
import { DIRECTIONS } from "@/data/directions";
import { generateTip } from "@/services/claudeApi";

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.1 } },
};
const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
};

export default function Dashboard() {
  const profile = useUserStore((s) => s.profile);
  const updateStreak = useUserStore((s) => s.updateStreak);
  const navigate = useNavigate();
  const [tip, setTip] = useState<string>("");

  useEffect(() => {
    if (!profile?.onboardingComplete) {
      navigate("/");
      return;
    }
    updateStreak();
  }, []);

  useEffect(() => {
    if (!profile) return;
    generateTip(DIRECTIONS[profile.direction].name, profile.assessmentLevel)
      .then(setTip)
      .catch(() => setTip("Keep learning every day — consistency beats intensity!"));
  }, [profile?.direction]);

  if (!profile) return null;

  const dirConfig = DIRECTIONS[profile.direction];
  const totalNodes = 25;
  const completedNodes = profile.completedNodes.length;
  const progressPercent = Math.round((completedNodes / totalNodes) * 100);

  const stats = [
    { icon: BookOpen, label: "Lessons", value: profile.completedLessons.length, color: "#6C63FF" },
    { icon: Clock, label: "Hours", value: Math.round(profile.completedLessons.length * 0.5), color: "#00D9FF" },
    { icon: Flame, label: "Streak", value: `${profile.streak} days`, color: "#FFB800" },
    { icon: Trophy, label: "Badges", value: profile.earnedBadges.length, color: "#00FF94" },
  ];

  return (
    <PageWrapper>
      <motion.div variants={containerVariants} initial="hidden" animate="show" className="max-w-5xl mx-auto space-y-6">
        {/* Continue Learning */}
        <motion.div variants={itemVariants}>
          <Card glow={dirConfig.color} className="flex items-center gap-6">
            <ProgressRing value={progressPercent} color={dirConfig.color} size={100} strokeWidth={8}>
              <span className="text-lg font-bold">{progressPercent}%</span>
            </ProgressRing>
            <div className="flex-1">
              <p className="text-xs text-text-secondary uppercase tracking-wider mb-1">Continue Learning</p>
              <h3 className="text-lg font-semibold mb-1">{dirConfig.name}</h3>
              <p className="text-sm text-text-secondary mb-3">
                {completedNodes} of {totalNodes} topics completed
              </p>
              <Button size="sm" onClick={() => navigate("/roadmap")}>
                Continue <ArrowRight size={14} />
              </Button>
            </div>
          </Card>
        </motion.div>

        {/* Stats Grid */}
        <motion.div variants={itemVariants} className="grid grid-cols-4 gap-4">
          {stats.map((stat) => (
            <Card key={stat.label} className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl flex items-center justify-center" style={{ backgroundColor: `${stat.color}15` }}>
                <stat.icon size={18} style={{ color: stat.color }} />
              </div>
              <div>
                <p className="text-lg font-bold">{stat.value}</p>
                <p className="text-xs text-text-secondary">{stat.label}</p>
              </div>
            </Card>
          ))}
        </motion.div>

        {/* AI Tip of the Day */}
        <motion.div variants={itemVariants}>
          <Card glow="#00D9FF" className="flex items-start gap-4">
            <div className="w-10 h-10 rounded-xl bg-accent/10 flex items-center justify-center shrink-0">
              <Sparkles size={18} className="text-accent" />
            </div>
            <div>
              <p className="text-xs text-accent uppercase tracking-wider mb-1">AI Tip of the Day</p>
              <p className="text-sm text-text-secondary leading-relaxed">
                {tip || "Loading your personalized tip..."}
              </p>
            </div>
          </Card>
        </motion.div>

        {/* Quick Actions */}
        <motion.div variants={itemVariants} className="grid grid-cols-3 gap-4">
          <Card hover onClick={() => navigate("/mentor")} className="text-center cursor-pointer">
            <p className="text-2xl mb-2">{dirConfig.mentor.avatar}</p>
            <p className="text-sm font-medium">Chat with {dirConfig.mentor.name}</p>
            <p className="text-xs text-text-secondary mt-1">AI Mentor</p>
          </Card>
          <Card hover onClick={() => navigate("/simulator")} className="text-center cursor-pointer">
            <p className="text-2xl mb-2">🎙️</p>
            <p className="text-sm font-medium">Practice Interview</p>
            <p className="text-xs text-text-secondary mt-1">Simulator</p>
          </Card>
          <Card hover onClick={() => navigate("/achievements")} className="text-center cursor-pointer">
            <p className="text-2xl mb-2">🏆</p>
            <p className="text-sm font-medium">View Achievements</p>
            <p className="text-xs text-text-secondary mt-1">{profile.earnedBadges.length} badges earned</p>
          </Card>
        </motion.div>
      </motion.div>
    </PageWrapper>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "feat: add Dashboard page with stats, progress, AI tip"
```

---

### Task 11: Roadmap Page with React Flow

**Files:**
- Create: `src/pages/Roadmap.tsx`, `src/components/roadmap/RoadmapCanvas.tsx`, `src/components/roadmap/RoadmapNode.tsx`, `src/components/roadmap/NodePanel.tsx`

- [ ] **Step 1: Create RoadmapNode (custom React Flow node)**

`src/components/roadmap/RoadmapNode.tsx`:

```tsx
import { memo } from "react";
import { Handle, Position, type NodeProps } from "@xyflow/react";
import { motion } from "framer-motion";
import { Check, Lock } from "lucide-react";
import type { NodeStatus } from "@/types";

export interface RoadmapNodeProps {
  title: string;
  status: NodeStatus;
  color: string;
  section: string;
}

export const RoadmapNodeComponent = memo(({ data }: NodeProps) => {
  const { title, status, color, section } = data as unknown as RoadmapNodeProps;

  return (
    <motion.div
      whileHover={status !== "locked" ? { scale: 1.05 } : undefined}
      className="relative"
    >
      <Handle type="target" position={Position.Top} className="!bg-transparent !border-0 !w-0 !h-0" />

      <div
        className={`w-44 px-4 py-3 rounded-2xl border-2 text-center transition-all ${
          status === "completed"
            ? "bg-surface border-success/50"
            : status === "available"
            ? "bg-surface border-primary/50 shadow-lg cursor-pointer"
            : "bg-bg/50 border-border/30 opacity-40 blur-[0.5px]"
        }`}
        style={
          status === "available"
            ? { boxShadow: `0 0 20px ${color}25` }
            : undefined
        }
      >
        <div className="flex items-center justify-center gap-2 mb-1">
          {status === "completed" && (
            <div className="w-5 h-5 rounded-full bg-success/20 flex items-center justify-center">
              <Check size={12} className="text-success" />
            </div>
          )}
          {status === "locked" && <Lock size={12} className="text-text-secondary/50" />}
        </div>
        <p className={`text-xs font-semibold ${status === "locked" ? "text-text-secondary/50" : "text-text"}`}>
          {title}
        </p>
        <p className="text-[10px] text-text-secondary/60 mt-0.5">{section}</p>
      </div>

      <Handle type="source" position={Position.Bottom} className="!bg-transparent !border-0 !w-0 !h-0" />
    </motion.div>
  );
});

RoadmapNodeComponent.displayName = "RoadmapNodeComponent";
```

- [ ] **Step 2: Create NodePanel (slide-over)**

`src/components/roadmap/NodePanel.tsx`:

```tsx
import { motion, AnimatePresence } from "framer-motion";
import { X, Clock, BookOpen, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { ProgressBar } from "@/components/ui/ProgressBar";
import type { RoadmapNodeData, NodeStatus } from "@/types";

interface NodePanelProps {
  node: RoadmapNodeData | null;
  status: NodeStatus;
  completedLessons: string[];
  onClose: () => void;
  onStartLesson: (lessonId: string) => void;
  onStartAI: () => void;
}

export function NodePanel({ node, status, completedLessons, onClose, onStartLesson, onStartAI }: NodePanelProps) {
  if (!node) return null;

  const completed = node.lessons.filter((l) => completedLessons.includes(l.id)).length;
  const total = node.lessons.length;

  return (
    <AnimatePresence>
      {node && (
        <motion.div
          initial={{ x: 400, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          exit={{ x: 400, opacity: 0 }}
          className="fixed right-0 top-0 h-full w-96 bg-surface border-l border-border z-50 p-6 overflow-y-auto"
        >
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-lg font-bold">{node.title}</h3>
            <button onClick={onClose} className="p-1 rounded-lg hover:bg-border/50 text-text-secondary cursor-pointer">
              <X size={20} />
            </button>
          </div>

          <p className="text-sm text-text-secondary mb-4">{node.description}</p>

          <div className="flex items-center gap-4 mb-4 text-xs text-text-secondary">
            <span className="flex items-center gap-1">
              <Clock size={12} /> {node.estimatedMinutes} min
            </span>
            <span className="flex items-center gap-1">
              <BookOpen size={12} /> {total} lessons
            </span>
          </div>

          <ProgressBar value={completed} max={total} color="#00FF94" showLabel className="mb-6" />

          <div className="space-y-2 mb-6">
            {node.lessons.map((lesson) => {
              const isDone = completedLessons.includes(lesson.id);
              return (
                <button
                  key={lesson.id}
                  onClick={() => !isDone && status !== "locked" && onStartLesson(lesson.id)}
                  disabled={status === "locked"}
                  className={`w-full text-left px-4 py-3 rounded-xl border text-sm transition-all cursor-pointer ${
                    isDone
                      ? "border-success/30 bg-success/5 text-success"
                      : status === "locked"
                      ? "border-border/30 text-text-secondary/50"
                      : "border-border hover:border-primary/30 text-text"
                  }`}
                >
                  <span className="flex items-center gap-2">
                    {isDone && "✓ "}
                    {lesson.title}
                    <span className="ml-auto text-xs text-text-secondary">
                      {lesson.estimatedMinutes}m
                    </span>
                  </span>
                </button>
              );
            })}
          </div>

          {status !== "locked" && (
            <Button className="w-full" onClick={onStartAI}>
              Start with AI Mentor <ArrowRight size={14} />
            </Button>
          )}
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

- [ ] **Step 3: Create RoadmapCanvas**

`src/components/roadmap/RoadmapCanvas.tsx`:

```tsx
import { useMemo, useCallback } from "react";
import {
  ReactFlow,
  Background,
  MiniMap,
  Controls,
  type Node,
  type Edge,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { RoadmapNodeComponent } from "./RoadmapNode";
import type { RoadmapNodeData, NodeStatus } from "@/types";

const nodeTypes = { roadmapNode: RoadmapNodeComponent };

interface RoadmapCanvasProps {
  roadmapData: RoadmapNodeData[];
  completedNodes: string[];
  color: string;
  onNodeClick: (nodeId: string) => void;
}

export function RoadmapCanvas({ roadmapData, completedNodes, color, onNodeClick }: RoadmapCanvasProps) {
  const getStatus = useCallback(
    (nodeId: string, index: number): NodeStatus => {
      if (completedNodes.includes(nodeId)) return "completed";
      if (index === 0) return "available";
      const prevNode = roadmapData[index - 1];
      return completedNodes.includes(prevNode.id) ? "available" : "locked";
    },
    [completedNodes, roadmapData]
  );

  const { nodes, edges } = useMemo(() => {
    const ns: Node[] = roadmapData.map((node, i) => ({
      id: node.id,
      type: "roadmapNode",
      position: {
        x: 300 + Math.sin(i * 0.8) * 150,
        y: i * 120,
      },
      data: {
        title: node.title,
        status: getStatus(node.id, i),
        color,
        section: node.section,
      },
    }));

    const es: Edge[] = roadmapData.slice(1).map((node, i) => ({
      id: `e-${roadmapData[i].id}-${node.id}`,
      source: roadmapData[i].id,
      target: node.id,
      animated: getStatus(node.id, i + 1) === "available",
      style: {
        stroke: completedNodes.includes(node.id)
          ? "#00FF94"
          : getStatus(node.id, i + 1) === "available"
          ? color
          : "#1E1E2E",
        strokeWidth: 2,
      },
    }));

    return { nodes: ns, edges: es };
  }, [roadmapData, completedNodes, color, getStatus]);

  return (
    <div className="w-full h-[calc(100vh-8rem)] rounded-2xl overflow-hidden border border-border bg-bg">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        onNodeClick={(_, node) => {
          const status = getStatus(node.id, roadmapData.findIndex((n) => n.id === node.id));
          if (status !== "locked") onNodeClick(node.id);
        }}
        fitView
        fitViewOptions={{ padding: 0.3 }}
        minZoom={0.3}
        maxZoom={1.5}
        proOptions={{ hideAttribution: true }}
      >
        <Background color="#1E1E2E" gap={20} size={1} />
        <MiniMap
          nodeColor={(n) => {
            const d = n.data as any;
            return d.status === "completed" ? "#00FF94" : d.status === "available" ? color : "#1E1E2E";
          }}
          style={{ background: "#111118", borderRadius: 12 }}
        />
        <Controls
          style={{ borderRadius: 12, overflow: "hidden", border: "1px solid #1E1E2E" }}
        />
      </ReactFlow>
    </div>
  );
}
```

- [ ] **Step 4: Create Roadmap page**

`src/pages/Roadmap.tsx`:

```tsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { RoadmapCanvas } from "@/components/roadmap/RoadmapCanvas";
import { NodePanel } from "@/components/roadmap/NodePanel";
import { useUserStore } from "@/store/userStore";
import { DIRECTIONS } from "@/data/directions";
import { frontendRoadmap } from "@/data/roadmaps/frontend";
import { englishRoadmap } from "@/data/roadmaps/english";
import { callcenterRoadmap } from "@/data/roadmaps/callcenter";
import { cibRoadmap } from "@/data/roadmaps/cib";
import type { Direction, RoadmapNodeData, NodeStatus } from "@/types";

const roadmapsByDirection: Record<Direction, RoadmapNodeData[]> = {
  frontend: frontendRoadmap,
  english: englishRoadmap,
  callcenter: callcenterRoadmap,
  cib: cibRoadmap,
};

export default function Roadmap() {
  const navigate = useNavigate();
  const profile = useUserStore((s) => s.profile);
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null);

  if (!profile) return null;

  const roadmap = roadmapsByDirection[profile.direction];
  const dirConfig = DIRECTIONS[profile.direction];
  const selectedNode = roadmap.find((n) => n.id === selectedNodeId) ?? null;

  const getStatus = (nodeId: string): NodeStatus => {
    if (profile.completedNodes.includes(nodeId)) return "completed";
    const idx = roadmap.findIndex((n) => n.id === nodeId);
    if (idx === 0) return "available";
    return profile.completedNodes.includes(roadmap[idx - 1].id) ? "available" : "locked";
  };

  return (
    <PageWrapper>
      <div className="relative">
        <RoadmapCanvas
          roadmapData={roadmap}
          completedNodes={profile.completedNodes}
          color={dirConfig.color}
          onNodeClick={setSelectedNodeId}
        />
        <NodePanel
          node={selectedNode}
          status={selectedNode ? getStatus(selectedNode.id) : "locked"}
          completedLessons={profile.completedLessons}
          onClose={() => setSelectedNodeId(null)}
          onStartLesson={(id) => navigate(`/lesson/${id}`)}
          onStartAI={() => navigate("/mentor")}
        />
      </div>
    </PageWrapper>
  );
}
```

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: add Roadmap page with React Flow canvas, custom nodes, and slide-over panel"
```

---

### Task 12: AI Mentor Chat Page

**Files:**
- Create: `src/pages/Mentor.tsx`, `src/components/chat/ChatWindow.tsx`, `src/components/chat/MessageBubble.tsx`, `src/components/chat/VoiceButton.tsx`, `src/components/chat/WaveformVisualizer.tsx`, `src/hooks/useChat.ts`, `src/hooks/useVoice.ts`

- [ ] **Step 1: Create useChat hook**

`src/hooks/useChat.ts`:

```ts
import { useCallback } from "react";
import { useChatStore } from "@/store/chatStore";
import { sendMessage } from "@/services/claudeApi";
import type { ChatMessage } from "@/types/chat";

export function useChat(systemPrompt: string) {
  const { messages, isLoading, addMessage, setLoading } = useChatStore();

  const send = useCallback(
    async (text: string) => {
      const userMsg: ChatMessage = {
        id: crypto.randomUUID(),
        role: "user",
        content: text,
        timestamp: Date.now(),
      };
      addMessage(userMsg);
      setLoading(true);

      try {
        const allMessages = [...messages, userMsg];
        const response = await sendMessage(systemPrompt, allMessages);
        const aiMsg: ChatMessage = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: response,
          timestamp: Date.now(),
        };
        addMessage(aiMsg);
        return response;
      } catch (error) {
        const errMsg: ChatMessage = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: "Sorry, I encountered an error. Please try again.",
          timestamp: Date.now(),
        };
        addMessage(errMsg);
        return null;
      } finally {
        setLoading(false);
      }
    },
    [messages, systemPrompt, addMessage, setLoading]
  );

  return { messages, isLoading, send };
}
```

- [ ] **Step 2: Create useVoice hook**

`src/hooks/useVoice.ts`:

```ts
import { useState, useCallback, useEffect } from "react";
import { voiceService } from "@/services/voiceService";

export function useVoice() {
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [transcript, setTranscript] = useState("");

  useEffect(() => {
    voiceService.init();
  }, []);

  const startListening = useCallback((onFinal?: (text: string) => void) => {
    setIsListening(true);
    setTranscript("");
    voiceService.startListening(
      (text, isFinal) => {
        setTranscript(text);
        if (isFinal && onFinal) onFinal(text);
      },
      () => setIsListening(false)
    );
  }, []);

  const stopListening = useCallback(() => {
    voiceService.stopListening();
    setIsListening(false);
  }, []);

  const speak = useCallback(async (text: string, voiceName?: string) => {
    setIsSpeaking(true);
    await voiceService.speak(text, voiceName);
    setIsSpeaking(false);
  }, []);

  const stopSpeaking = useCallback(() => {
    voiceService.stopSpeaking();
    setIsSpeaking(false);
  }, []);

  return {
    isListening,
    isSpeaking,
    transcript,
    startListening,
    stopListening,
    speak,
    stopSpeaking,
    isSupported: voiceService.isSupported(),
  };
}
```

- [ ] **Step 3: Create MessageBubble component**

`src/components/chat/MessageBubble.tsx`:

```tsx
import { motion } from "framer-motion";
import type { ChatMessage } from "@/types/chat";

interface MessageBubbleProps {
  message: ChatMessage;
  mentorAvatar?: string;
}

export function MessageBubble({ message, mentorAvatar }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`flex gap-3 ${isUser ? "flex-row-reverse" : ""}`}
    >
      <div className="w-8 h-8 rounded-full bg-surface border border-border flex items-center justify-center text-sm shrink-0">
        {isUser ? "👤" : mentorAvatar || "🤖"}
      </div>
      <div
        className={`max-w-[70%] px-4 py-3 rounded-2xl text-sm leading-relaxed ${
          isUser
            ? "bg-primary text-white rounded-tr-md"
            : "bg-surface border border-border text-text rounded-tl-md"
        }`}
      >
        <div className="whitespace-pre-wrap">{message.content}</div>
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 4: Create VoiceButton and WaveformVisualizer**

`src/components/chat/VoiceButton.tsx`:

```tsx
import { motion } from "framer-motion";
import { Mic, MicOff, Volume2 } from "lucide-react";
import { cn } from "@/lib/cn";

interface VoiceButtonProps {
  isListening: boolean;
  isSpeaking: boolean;
  onToggle: () => void;
  className?: string;
}

export function VoiceButton({ isListening, isSpeaking, onToggle, className }: VoiceButtonProps) {
  return (
    <motion.button
      whileTap={{ scale: 0.9 }}
      onClick={onToggle}
      className={cn(
        "relative w-12 h-12 rounded-full flex items-center justify-center transition-all cursor-pointer",
        isListening
          ? "bg-red-500/20 text-red-400 border-2 border-red-500/50"
          : isSpeaking
          ? "bg-accent/20 text-accent border-2 border-accent/50"
          : "bg-surface border-2 border-border text-text-secondary hover:border-primary/50 hover:text-primary",
        className
      )}
    >
      {isListening && (
        <motion.div
          className="absolute inset-0 rounded-full border-2 border-red-500/30"
          animate={{ scale: [1, 1.4, 1], opacity: [0.5, 0, 0.5] }}
          transition={{ repeat: Infinity, duration: 1.5 }}
        />
      )}
      {isListening ? <MicOff size={20} /> : isSpeaking ? <Volume2 size={20} /> : <Mic size={20} />}
    </motion.button>
  );
}
```

`src/components/chat/WaveformVisualizer.tsx`:

```tsx
import { motion } from "framer-motion";

interface WaveformVisualizerProps {
  active: boolean;
  color?: string;
}

export function WaveformVisualizer({ active, color = "#00D9FF" }: WaveformVisualizerProps) {
  if (!active) return null;

  return (
    <div className="flex items-center gap-1 h-8">
      {Array.from({ length: 5 }).map((_, i) => (
        <motion.div
          key={i}
          className="w-1 rounded-full"
          style={{ backgroundColor: color }}
          animate={{
            height: active ? [8, 24, 8] : 8,
          }}
          transition={{
            repeat: Infinity,
            duration: 0.8,
            delay: i * 0.15,
            ease: "easeInOut",
          }}
        />
      ))}
    </div>
  );
}
```

- [ ] **Step 5: Create ChatWindow component**

`src/components/chat/ChatWindow.tsx`:

```tsx
import { useState, useRef, useEffect } from "react";
import { Send, Loader2 } from "lucide-react";
import { MessageBubble } from "./MessageBubble";
import { VoiceButton } from "./VoiceButton";
import { WaveformVisualizer } from "./WaveformVisualizer";
import { Chip } from "@/components/ui/Chip";
import type { ChatMessage } from "@/types/chat";

interface ChatWindowProps {
  messages: ChatMessage[];
  isLoading: boolean;
  onSend: (text: string) => void;
  mentorAvatar: string;
  mentorName: string;
  voiceEnabled?: boolean;
  isListening?: boolean;
  isSpeaking?: boolean;
  transcript?: string;
  onVoiceToggle?: () => void;
  suggestions?: string[];
}

export function ChatWindow({
  messages,
  isLoading,
  onSend,
  mentorAvatar,
  mentorName,
  voiceEnabled,
  isListening,
  isSpeaking,
  transcript,
  onVoiceToggle,
  suggestions = [],
}: ChatWindowProps) {
  const [input, setInput] = useState("");
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages, isLoading]);

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input.trim());
    setInput("");
  };

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="flex items-center gap-3 px-6 py-4 border-b border-border">
        <span className="text-2xl">{mentorAvatar}</span>
        <div>
          <p className="font-semibold text-sm">{mentorName}</p>
          <p className="text-xs text-text-secondary">AI Mentor</p>
        </div>
        {isSpeaking && <WaveformVisualizer active color="#00D9FF" />}
      </div>

      {/* Messages */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} mentorAvatar={mentorAvatar} />
        ))}
        {isLoading && (
          <div className="flex gap-3">
            <div className="w-8 h-8 rounded-full bg-surface border border-border flex items-center justify-center text-sm">
              {mentorAvatar}
            </div>
            <div className="px-4 py-3 rounded-2xl bg-surface border border-border rounded-tl-md">
              <Loader2 className="animate-spin" size={16} />
            </div>
          </div>
        )}
      </div>

      {/* Transcript */}
      {isListening && transcript && (
        <div className="px-6 py-2 text-sm text-accent italic border-t border-border/50">
          {transcript}
        </div>
      )}

      {/* Suggestions */}
      {suggestions.length > 0 && messages.length < 3 && (
        <div className="flex gap-2 px-6 py-2 overflow-x-auto">
          {suggestions.map((s) => (
            <Chip key={s} label={s} onClick={() => onSend(s)} />
          ))}
        </div>
      )}

      {/* Input */}
      <div className="flex items-center gap-3 px-6 py-4 border-t border-border">
        {voiceEnabled && onVoiceToggle && (
          <VoiceButton
            isListening={isListening || false}
            isSpeaking={isSpeaking || false}
            onToggle={onVoiceToggle}
          />
        )}
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && handleSend()}
          placeholder={`Ask ${mentorName} anything...`}
          className="flex-1 bg-bg border border-border rounded-xl px-4 py-2.5 text-sm text-text outline-none focus:border-primary/50 placeholder:text-text-secondary/50"
        />
        <button
          onClick={handleSend}
          disabled={!input.trim() || isLoading}
          className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center text-white disabled:opacity-50 cursor-pointer hover:bg-primary/90 transition-colors"
        >
          <Send size={16} />
        </button>
      </div>
    </div>
  );
}
```

- [ ] **Step 6: Create Mentor page**

`src/pages/Mentor.tsx`:

```tsx
import { useCallback, useEffect } from "react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { ChatWindow } from "@/components/chat/ChatWindow";
import { useChat } from "@/hooks/useChat";
import { useVoice } from "@/hooks/useVoice";
import { useUserStore } from "@/store/userStore";
import { useChatStore } from "@/store/chatStore";
import { DIRECTIONS } from "@/data/directions";

const SUGGESTIONS: Record<string, string[]> = {
  frontend: ["Explain CSS Flexbox", "How do React hooks work?", "What's the DOM?", "Review my code approach"],
  english: ["Practice conversation", "Explain present perfect", "Help with pronunciation", "Business email writing"],
  callcenter: ["Handle angry customer", "Upsell techniques", "Phone greeting scripts", "Complaint resolution"],
  cib: ["What is DCF?", "Explain M&A process", "Banking interview prep", "Financial modeling basics"],
};

export default function Mentor() {
  const profile = useUserStore((s) => s.profile);
  const clearMessages = useChatStore((s) => s.clearMessages);

  const direction = profile?.direction ?? "frontend";
  const dirConfig = DIRECTIONS[direction];
  const mentor = dirConfig.mentor;

  const contextPrompt = `${mentor.systemPrompt}\n\nThe student's name is ${profile?.name}. Their current level is ${profile?.assessmentLevel}. They are studying ${dirConfig.name}.`;

  const { messages, isLoading, send } = useChat(contextPrompt);
  const voice = useVoice();

  useEffect(() => {
    return () => clearMessages();
  }, []);

  const handleSend = useCallback(
    async (text: string) => {
      const response = await send(text);
      if (response && voice.isSpeaking === false) {
        voice.speak(response);
      }
    },
    [send, voice]
  );

  const handleVoiceToggle = useCallback(() => {
    if (voice.isListening) {
      voice.stopListening();
      if (voice.transcript) {
        handleSend(voice.transcript);
      }
    } else if (voice.isSpeaking) {
      voice.stopSpeaking();
    } else {
      voice.startListening((finalText) => {
        handleSend(finalText);
      });
    }
  }, [voice, handleSend]);

  return (
    <PageWrapper>
      <div className="h-[calc(100vh-8rem)] rounded-2xl border border-border bg-surface/50 overflow-hidden">
        <ChatWindow
          messages={messages}
          isLoading={isLoading}
          onSend={handleSend}
          mentorAvatar={mentor.avatar}
          mentorName={mentor.name}
          voiceEnabled={voice.isSupported}
          isListening={voice.isListening}
          isSpeaking={voice.isSpeaking}
          transcript={voice.transcript}
          onVoiceToggle={handleVoiceToggle}
          suggestions={SUGGESTIONS[direction]}
        />
      </div>
    </PageWrapper>
  );
}
```

- [ ] **Step 7: Commit**

```bash
git add -A && git commit -m "feat: add AI Mentor chat page with voice support"
```

---

### Task 13: Interview Simulator Page

**Files:**
- Create: `src/pages/Simulator.tsx`, `src/components/simulator/InterviewRoom.tsx`, `src/components/simulator/ScoreCard.tsx`, `src/components/simulator/TranscriptPanel.tsx`

- [ ] **Step 1: Create ScoreCard component**

`src/components/simulator/ScoreCard.tsx`:

```tsx
import { motion } from "framer-motion";
import { Card } from "@/components/ui/Card";

interface ScoreCardProps {
  score: number;
  feedback: string;
  modelAnswer: string;
}

export function ScoreCard({ score, feedback, modelAnswer }: ScoreCardProps) {
  const color = score >= 7 ? "#00FF94" : score >= 4 ? "#FFB800" : "#FF4444";

  return (
    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
      <Card className="space-y-4">
        <div className="flex items-center gap-4">
          <div
            className="w-16 h-16 rounded-full flex items-center justify-center text-2xl font-bold border-4"
            style={{ borderColor: color, color }}
          >
            {score}
          </div>
          <div>
            <p className="text-sm font-semibold">Score</p>
            <p className="text-xs text-text-secondary">out of 10</p>
          </div>
        </div>
        <div>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-1">Feedback</p>
          <p className="text-sm leading-relaxed">{feedback}</p>
        </div>
        <div>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-1">Model Answer</p>
          <p className="text-sm text-text-secondary leading-relaxed">{modelAnswer}</p>
        </div>
      </Card>
    </motion.div>
  );
}
```

- [ ] **Step 2: Create TranscriptPanel component**

`src/components/simulator/TranscriptPanel.tsx`:

```tsx
import { motion } from "framer-motion";

interface TranscriptPanelProps {
  entries: Array<{ role: "interviewer" | "candidate"; text: string }>;
}

export function TranscriptPanel({ entries }: TranscriptPanelProps) {
  return (
    <div className="space-y-3 max-h-60 overflow-y-auto">
      {entries.map((entry, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className={`text-sm ${entry.role === "interviewer" ? "text-accent" : "text-text"}`}
        >
          <span className="text-xs text-text-secondary uppercase">
            {entry.role === "interviewer" ? "Interviewer" : "You"}:
          </span>{" "}
          {entry.text}
        </motion.div>
      ))}
    </div>
  );
}
```

- [ ] **Step 3: Create InterviewRoom component**

`src/components/simulator/InterviewRoom.tsx`:

```tsx
import { useState, useCallback } from "react";
import { motion } from "framer-motion";
import { Mic, MicOff, Timer, BarChart3 } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { ScoreCard } from "./ScoreCard";
import { TranscriptPanel } from "./TranscriptPanel";
import { WaveformVisualizer } from "@/components/chat/WaveformVisualizer";
import { useVoice } from "@/hooks/useVoice";
import { sendMessage, scoreAnswer } from "@/services/claudeApi";
import { useUserStore } from "@/store/userStore";
import { DIRECTIONS } from "@/data/directions";
import { XP_REWARDS } from "@/lib/constants";
import type { ChatMessage } from "@/types/chat";

interface InterviewRoomProps {
  mode: "technical" | "situation" | "voice";
  onEnd: () => void;
}

interface QA {
  question: string;
  answer: string;
  score?: number;
  feedback?: string;
  modelAnswer?: string;
}

export function InterviewRoom({ mode, onEnd }: InterviewRoomProps) {
  const profile = useUserStore((s) => s.profile);
  const addXP = useUserStore((s) => s.addXP);
  const direction = profile?.direction ?? "frontend";
  const dirConfig = DIRECTIONS[direction];

  const [questionIndex, setQuestionIndex] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [qas, setQas] = useState<QA[]>([]);
  const [isGenerating, setIsGenerating] = useState(false);
  const [showScore, setShowScore] = useState(false);
  const [lastScore, setLastScore] = useState<{ score: number; feedback: string; modelAnswer: string } | null>(null);
  const [completed, setCompleted] = useState(false);
  const [transcript, setTranscript] = useState<Array<{ role: "interviewer" | "candidate"; text: string }>>([]);

  const voice = useVoice();
  const isVoiceMode = mode === "voice";
  const totalQuestions = 5;

  const generateQuestion = useCallback(async () => {
    setIsGenerating(true);
    setShowScore(false);
    setLastScore(null);
    setAnswer("");

    const modeLabel = mode === "technical" ? "technical interview" : mode === "situation" ? "situational/role-play" : "voice-based interview";
    const pastQuestions = qas.map((q) => q.question).join("\n");
    const prompt = `You are conducting a ${modeLabel} for a ${dirConfig.name} position. Ask question ${questionIndex + 1} of ${totalQuestions}. ${pastQuestions ? `Previous questions (don't repeat):\n${pastQuestions}\n\n` : ""}Difficulty: ${questionIndex < 2 ? "easy" : questionIndex < 4 ? "medium" : "hard"}. Ask ONLY the question, nothing else.`;

    const messages: ChatMessage[] = [{ id: "q", role: "user", content: "Ask the next interview question.", timestamp: Date.now() }];

    try {
      const question = await sendMessage(prompt, messages);
      setCurrentQuestion(question);
      setTranscript((t) => [...t, { role: "interviewer", text: question }]);
      if (isVoiceMode) {
        await voice.speak(question);
      }
    } catch {
      setCurrentQuestion("Tell me about your experience in this field.");
    }
    setIsGenerating(false);
  }, [questionIndex, qas, direction, mode, voice, isVoiceMode, dirConfig.name]);

  const submitAnswer = useCallback(async () => {
    if (!answer.trim()) return;

    setTranscript((t) => [...t, { role: "candidate", text: answer }]);
    setIsGenerating(true);

    try {
      const result = await scoreAnswer(currentQuestion, answer, dirConfig.name);
      setLastScore(result);
      setShowScore(true);
      setQas((prev) => [...prev, { question: currentQuestion, answer, ...result }]);
    } catch {
      setLastScore({ score: 5, feedback: "Could not evaluate. Try again.", modelAnswer: "" });
      setShowScore(true);
    }

    setIsGenerating(false);
  }, [answer, currentQuestion, dirConfig.name]);

  const handleNext = () => {
    if (questionIndex >= totalQuestions - 1) {
      setCompleted(true);
      addXP(XP_REWARDS.interviewSimulation);
      return;
    }
    setQuestionIndex((i) => i + 1);
    generateQuestion();
  };

  const handleVoiceToggle = () => {
    if (voice.isListening) {
      voice.stopListening();
      if (voice.transcript) {
        setAnswer(voice.transcript);
      }
    } else {
      voice.startListening((text) => {
        setAnswer(text);
      });
    }
  };

  const avgScore = qas.length > 0
    ? Math.round(qas.reduce((sum, q) => sum + (q.score ?? 0), 0) / qas.length * 10) / 10
    : 0;

  if (completed) {
    return (
      <Card className="max-w-2xl mx-auto space-y-6 text-center">
        <motion.div animate={{ scale: [0.8, 1.1, 1] }} transition={{ duration: 0.5 }}>
          <BarChart3 size={48} className="mx-auto text-primary" />
        </motion.div>
        <h2 className="text-2xl font-bold">Interview Complete!</h2>
        <p className="text-4xl font-bold text-primary">{avgScore}/10</p>
        <p className="text-text-secondary text-sm">Average Score</p>
        <div className="space-y-3 text-left">
          {qas.map((qa, i) => (
            <div key={i} className="p-3 rounded-xl bg-bg border border-border">
              <p className="text-xs text-text-secondary mb-1">Q{i + 1}: {qa.question}</p>
              <p className="text-sm">Score: <span className="font-bold text-primary">{qa.score}/10</span></p>
            </div>
          ))}
        </div>
        <p className="text-sm text-success">+{XP_REWARDS.interviewSimulation} XP earned!</p>
        <Button onClick={onEnd}>Back to Menu</Button>
      </Card>
    );
  }

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {/* Interview Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-full bg-surface border-2 border-primary/30 flex items-center justify-center text-xl">
            {dirConfig.mentor.avatar}
          </div>
          <div>
            <p className="text-sm font-semibold">Interviewer</p>
            <p className="text-xs text-text-secondary">
              {mode === "technical" ? "Technical" : mode === "situation" ? "Situational" : "Voice"} Interview
            </p>
          </div>
          {voice.isSpeaking && <WaveformVisualizer active color="#00D9FF" />}
        </div>
        <div className="flex items-center gap-2 text-sm text-text-secondary">
          <Timer size={14} />
          Question {questionIndex + 1}/{totalQuestions}
        </div>
      </div>

      {/* Question */}
      {!currentQuestion && !isGenerating && (
        <Card className="text-center py-12">
          <p className="text-text-secondary mb-4">Ready to begin your interview?</p>
          <Button onClick={generateQuestion}>Start Interview</Button>
        </Card>
      )}

      {currentQuestion && (
        <Card glow="#6C63FF" className="space-y-4">
          <p className="text-sm leading-relaxed">{currentQuestion}</p>
        </Card>
      )}

      {/* Answer area */}
      {currentQuestion && !showScore && (
        <div className="space-y-3">
          {isVoiceMode && (
            <div className="flex items-center gap-3">
              <button
                onClick={handleVoiceToggle}
                className={`w-14 h-14 rounded-full flex items-center justify-center transition-all cursor-pointer ${
                  voice.isListening ? "bg-red-500/20 text-red-400 border-2 border-red-500/50" : "bg-surface border-2 border-border hover:border-primary/50"
                }`}
              >
                {voice.isListening ? <MicOff size={20} /> : <Mic size={20} />}
              </button>
              {voice.isListening && (
                <p className="text-sm text-accent italic">{voice.transcript || "Listening..."}</p>
              )}
            </div>
          )}
          <textarea
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            rows={4}
            placeholder="Type your answer..."
            className="w-full bg-bg border border-border rounded-xl px-4 py-3 text-sm text-text outline-none focus:border-primary/50 resize-none placeholder:text-text-secondary/50"
          />
          <Button onClick={submitAnswer} disabled={!answer.trim() || isGenerating}>
            {isGenerating ? "Evaluating..." : "Submit Answer"}
          </Button>
        </div>
      )}

      {/* Score */}
      {showScore && lastScore && (
        <div className="space-y-4">
          <ScoreCard score={lastScore.score} feedback={lastScore.feedback} modelAnswer={lastScore.modelAnswer} />
          <Button onClick={handleNext}>
            {questionIndex >= totalQuestions - 1 ? "Finish Interview" : "Next Question"}
          </Button>
        </div>
      )}

      {/* Transcript */}
      {transcript.length > 0 && (
        <Card className="mt-4">
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-3">Transcript</p>
          <TranscriptPanel entries={transcript} />
        </Card>
      )}
    </div>
  );
}
```

- [ ] **Step 4: Create Simulator page**

`src/pages/Simulator.tsx`:

```tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { Code2, Users, Mic } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { InterviewRoom } from "@/components/simulator/InterviewRoom";

type SimMode = "technical" | "situation" | "voice";

const modes = [
  { id: "technical" as SimMode, name: "Technical Interview", description: "Answer technical questions with AI evaluation", icon: Code2, color: "#6C63FF" },
  { id: "situation" as SimMode, name: "Situation Simulator", description: "Practice real-world customer scenarios", icon: Users, color: "#FFB800" },
  { id: "voice" as SimMode, name: "Voice Interview", description: "Fully voice-based interview simulation", icon: Mic, color: "#00D9FF" },
];

export default function Simulator() {
  const [selectedMode, setSelectedMode] = useState<SimMode | null>(null);

  if (selectedMode) {
    return (
      <PageWrapper>
        <InterviewRoom mode={selectedMode} onEnd={() => setSelectedMode(null)} />
      </PageWrapper>
    );
  }

  return (
    <PageWrapper>
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold mb-2">Interview Simulator</h1>
          <p className="text-text-secondary text-sm">Choose a mode to practice</p>
        </div>

        <div className="grid grid-cols-3 gap-4">
          {modes.map((mode) => (
            <motion.div key={mode.id} whileHover={{ y: -4 }}>
              <Card
                hover
                glow={mode.color}
                onClick={() => setSelectedMode(mode.id)}
                className="text-center cursor-pointer py-8"
              >
                <div
                  className="w-14 h-14 rounded-2xl flex items-center justify-center mx-auto mb-4"
                  style={{ backgroundColor: `${mode.color}15` }}
                >
                  <mode.icon size={24} style={{ color: mode.color }} />
                </div>
                <h3 className="font-semibold text-sm mb-2">{mode.name}</h3>
                <p className="text-xs text-text-secondary">{mode.description}</p>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </PageWrapper>
  );
}
```

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "feat: add Interview Simulator with technical, situation, and voice modes"
```

---

### Task 14: Lesson Page

**Files:**
- Create: `src/pages/Lesson.tsx`

- [ ] **Step 1: Create Lesson page**

`src/pages/Lesson.tsx`:

```tsx
import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { ArrowLeft, Check, X, Sparkles } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { useUserStore } from "@/store/userStore";
import { LESSONS } from "@/data/lessons";
import { XP_REWARDS } from "@/lib/constants";

export default function Lesson() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { completeLesson, addXP, completeNode } = useUserStore();
  const profile = useUserStore((s) => s.profile);

  const lesson = id ? LESSONS[id] : undefined;
  const [quizAnswers, setQuizAnswers] = useState<Record<number, number>>({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);

  if (!lesson) {
    return (
      <PageWrapper>
        <div className="text-center py-20">
          <p className="text-text-secondary">Lesson content coming soon!</p>
          <Button variant="ghost" className="mt-4" onClick={() => navigate(-1)}>
            <ArrowLeft size={14} /> Go Back
          </Button>
        </div>
      </PageWrapper>
    );
  }

  const handleQuizSubmit = () => {
    setQuizSubmitted(true);
    if (id) {
      completeLesson(id);
      addXP(XP_REWARDS.completeLesson);

      const nodeId = id.split("-").slice(0, 2).join("-");
      if (profile) {
        const nodePrefix = nodeId;
        const allLessonsForNode = Object.keys(LESSONS).filter((k) => k.startsWith(nodePrefix));
        const completedAll = allLessonsForNode.every(
          (l) => l === id || profile.completedLessons.includes(l)
        );
        if (completedAll) completeNode(nodeId);
      }
    }
  };

  const allCorrect = lesson.quiz?.every((q, i) => quizAnswers[i] === q.correct) ?? true;

  return (
    <PageWrapper>
      <div className="max-w-3xl mx-auto">
        <button
          onClick={() => navigate(-1)}
          className="flex items-center gap-2 text-sm text-text-secondary hover:text-text mb-6 cursor-pointer"
        >
          <ArrowLeft size={14} /> Back
        </button>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
          <h1 className="text-2xl font-bold mb-6">{lesson.title}</h1>

          {/* Content */}
          <div className="prose prose-invert max-w-none mb-8 text-sm leading-relaxed text-text-secondary whitespace-pre-line">
            {lesson.content}
          </div>

          {/* Code Examples */}
          {lesson.codeExamples?.map((ex, i) => (
            <Card key={i} className="mb-6 overflow-hidden">
              <div className="flex items-center gap-2 mb-3">
                <span className="text-xs text-text-secondary uppercase">{ex.language}</span>
              </div>
              <pre className="bg-bg rounded-xl p-4 overflow-x-auto text-sm font-mono">
                <code className="text-accent">{ex.code}</code>
              </pre>
            </Card>
          ))}

          {/* Quiz */}
          {lesson.quiz && (
            <div className="space-y-4 mt-8">
              <h2 className="text-lg font-bold flex items-center gap-2">
                <Sparkles size={18} className="text-primary" /> Quiz
              </h2>

              {lesson.quiz.map((q, qi) => (
                <Card key={qi} className="space-y-3">
                  <p className="text-sm font-medium">{q.question}</p>
                  <div className="space-y-2">
                    {q.options.map((opt, oi) => {
                      const selected = quizAnswers[qi] === oi;
                      const isCorrect = quizSubmitted && q.correct === oi;
                      const isWrong = quizSubmitted && selected && q.correct !== oi;

                      return (
                        <button
                          key={oi}
                          onClick={() => !quizSubmitted && setQuizAnswers((a) => ({ ...a, [qi]: oi }))}
                          className={`w-full text-left px-4 py-2.5 rounded-xl border text-sm transition-all cursor-pointer ${
                            isCorrect
                              ? "border-success/50 bg-success/10 text-success"
                              : isWrong
                              ? "border-red-500/50 bg-red-500/10 text-red-400"
                              : selected
                              ? "border-primary/50 bg-primary/10 text-primary"
                              : "border-border hover:border-border/80 text-text-secondary"
                          }`}
                          disabled={quizSubmitted}
                        >
                          <span className="flex items-center gap-2">
                            {opt}
                            {isCorrect && <Check size={14} />}
                            {isWrong && <X size={14} />}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </Card>
              ))}

              {!quizSubmitted && (
                <Button
                  onClick={handleQuizSubmit}
                  disabled={Object.keys(quizAnswers).length < (lesson.quiz?.length ?? 0)}
                >
                  Submit Quiz
                </Button>
              )}

              {quizSubmitted && (
                <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}>
                  <Card glow={allCorrect ? "#00FF94" : "#FFB800"}>
                    <p className="text-sm font-semibold">
                      {allCorrect ? "Perfect score! 🎉" : "Good effort! Review the correct answers above."}
                    </p>
                    <p className="text-xs text-success mt-2">+{XP_REWARDS.completeLesson} XP earned!</p>
                  </Card>
                </motion.div>
              )}
            </div>
          )}
        </motion.div>
      </div>
    </PageWrapper>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "feat: add Lesson page with content, code examples, and quiz"
```

---

### Task 15: Achievements Page

**Files:**
- Create: `src/pages/Achievements.tsx`

- [ ] **Step 1: Create Achievements page**

`src/pages/Achievements.tsx`:

```tsx
import { motion } from "framer-motion";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { Badge as BadgeComponent } from "@/components/ui/Badge";
import { useUserStore } from "@/store/userStore";
import { BADGES } from "@/data/achievements";

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.05 } },
};
const itemVariants = {
  hidden: { opacity: 0, scale: 0.8 },
  show: { opacity: 1, scale: 1 },
};

export default function Achievements() {
  const profile = useUserStore((s) => s.profile);
  if (!profile) return null;

  const earnedCount = profile.earnedBadges.length;
  const totalCount = BADGES.filter((b) => !b.direction || b.direction === profile.direction).length;

  // Streak calendar (last 30 days)
  const today = new Date();
  const days = Array.from({ length: 30 }, (_, i) => {
    const d = new Date(today);
    d.setDate(d.getDate() - (29 - i));
    const dateStr = d.toISOString().split("T")[0];
    const isActive = profile.lastActiveDate >= dateStr && profile.streak >= (30 - i);
    return { date: d, active: isActive };
  });

  return (
    <PageWrapper>
      <div className="max-w-4xl mx-auto space-y-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-2">Achievements</h1>
          <p className="text-text-secondary text-sm">
            {earnedCount} of {totalCount} badges unlocked
          </p>
        </div>

        {/* Streak Calendar */}
        <Card>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-3">Learning Streak</p>
          <div className="flex gap-1 flex-wrap">
            {days.map((day, i) => (
              <div
                key={i}
                className="w-6 h-6 rounded-sm"
                style={{
                  backgroundColor: day.active ? "#00FF9440" : "#1E1E2E",
                  border: day.active ? "1px solid #00FF9460" : "1px solid transparent",
                }}
                title={day.date.toLocaleDateString()}
              />
            ))}
          </div>
        </Card>

        {/* Badge Grid */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          animate="show"
          className="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-6 gap-4"
        >
          {BADGES.filter((b) => !b.direction || b.direction === profile.direction).map((badge) => {
            const isEarned = profile.earnedBadges.includes(badge.id);
            return (
              <motion.div key={badge.id} variants={itemVariants}>
                <BadgeComponent
                  icon={badge.icon}
                  name={badge.name}
                  rarity={badge.rarity}
                  locked={!isEarned}
                />
              </motion.div>
            );
          })}
        </motion.div>
      </div>
    </PageWrapper>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "feat: add Achievements page with badge grid and streak calendar"
```

---

### Task 16: Profile Page

**Files:**
- Create: `src/pages/Profile.tsx`

- [ ] **Step 1: Create Profile page**

`src/pages/Profile.tsx`:

```tsx
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { ProgressRing } from "@/components/ui/ProgressRing";
import { useUserStore } from "@/store/userStore";
import { DIRECTIONS } from "@/data/directions";
import { LEVEL_THRESHOLDS, LEVELS_ORDERED } from "@/lib/constants";

export default function Profile() {
  const profile = useUserStore((s) => s.profile);
  const reset = useUserStore((s) => s.reset);
  const navigate = useNavigate();

  if (!profile) return null;

  const dirConfig = DIRECTIONS[profile.direction];
  const currentIdx = LEVELS_ORDERED.indexOf(profile.level);
  const nextLevel = LEVELS_ORDERED[currentIdx + 1];
  const currentThreshold = LEVEL_THRESHOLDS[profile.level];
  const nextThreshold = nextLevel ? LEVEL_THRESHOLDS[nextLevel] : currentThreshold;
  const xpProgress = ((profile.xp - currentThreshold) / (nextThreshold - currentThreshold || 1)) * 100;

  const handleReset = () => {
    if (window.confirm("This will reset all your progress. Are you sure?")) {
      reset();
      navigate("/");
    }
  };

  return (
    <PageWrapper>
      <div className="max-w-2xl mx-auto space-y-6">
        {/* Profile Header */}
        <Card glow={dirConfig.color} className="flex items-center gap-6">
          <ProgressRing value={xpProgress} color={dirConfig.color} size={100} strokeWidth={6}>
            <span className="text-3xl">{dirConfig.mentor.avatar}</span>
          </ProgressRing>
          <div>
            <h2 className="text-xl font-bold">{profile.name}</h2>
            <p className="text-sm text-text-secondary">{dirConfig.name}</p>
            <div className="flex items-center gap-3 mt-2">
              <span className="text-xs px-3 py-1 rounded-full bg-primary/10 text-primary font-semibold">
                {profile.level}
              </span>
              <span className="text-xs text-text-secondary">{profile.xp} XP</span>
            </div>
          </div>
        </Card>

        {/* Stats */}
        <div className="grid grid-cols-2 gap-4">
          <Card>
            <p className="text-xs text-text-secondary mb-1">Assessment Level</p>
            <p className="font-semibold capitalize">{profile.assessmentLevel}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">Current Streak</p>
            <p className="font-semibold">{profile.streak} days</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">Lessons Completed</p>
            <p className="font-semibold">{profile.completedLessons.length}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">Topics Completed</p>
            <p className="font-semibold">{profile.completedNodes.length}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">Badges Earned</p>
            <p className="font-semibold">{profile.earnedBadges.length}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">Next Level</p>
            <p className="font-semibold">{nextLevel ?? "Max Level!"}</p>
          </Card>
        </div>

        {/* Actions */}
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.3 }}>
          <Button variant="ghost" onClick={handleReset} className="text-red-400 hover:text-red-300">
            Reset All Progress
          </Button>
        </motion.div>
      </div>
    </PageWrapper>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "feat: add Profile page with stats and settings"
```

---

## Phase 4: Wiring & Polish

### Task 17: Update App.tsx with all routes and auth guard

**Files:**
- Modify: `src/App.tsx`

- [ ] **Step 1: Update App.tsx with lazy-loaded routes and redirect logic**

```tsx
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useUserStore } from "@/store/userStore";
import Onboarding from "@/pages/Onboarding";
import Dashboard from "@/pages/Dashboard";
import Roadmap from "@/pages/Roadmap";
import Mentor from "@/pages/Mentor";
import Simulator from "@/pages/Simulator";
import Lesson from "@/pages/Lesson";
import Achievements from "@/pages/Achievements";
import Profile from "@/pages/Profile";

function AuthGuard({ children }: { children: React.ReactNode }) {
  const profile = useUserStore((s) => s.profile);
  if (!profile?.onboardingComplete) return <Navigate to="/" replace />;
  return <>{children}</>;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Onboarding />} />
        <Route path="/dashboard" element={<AuthGuard><Dashboard /></AuthGuard>} />
        <Route path="/roadmap" element={<AuthGuard><Roadmap /></AuthGuard>} />
        <Route path="/mentor" element={<AuthGuard><Mentor /></AuthGuard>} />
        <Route path="/simulator" element={<AuthGuard><Simulator /></AuthGuard>} />
        <Route path="/lesson/:id" element={<AuthGuard><Lesson /></AuthGuard>} />
        <Route path="/achievements" element={<AuthGuard><Achievements /></AuthGuard>} />
        <Route path="/profile" element={<AuthGuard><Profile /></AuthGuard>} />
      </Routes>
    </BrowserRouter>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "feat: wire all routes with auth guard"
```

---

### Task 18: Remaining roadmap data files

**Files:**
- Create: `src/data/roadmaps/english.ts`, `src/data/roadmaps/callcenter.ts`, `src/data/roadmaps/cib.ts`

- [ ] **Step 1: Create English roadmap (20 nodes, 5 sections)**

Create full data with sections: Grammar Foundations, Vocabulary Building, Speaking Skills, Business English, Advanced Communication.

- [ ] **Step 2: Create Call Center roadmap (20 nodes, 5 sections)**

Sections: Communication Basics, Phone Etiquette, Customer Service, Conflict Resolution, Advanced Skills.

- [ ] **Step 3: Create CIB roadmap (20 nodes, 5 sections)**

Sections: Financial Fundamentals, Banking Operations, Investment Banking, Financial Analysis, Interview Preparation.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "feat: add English, Call Center, and CIB roadmap data"
```

---

### Task 19: Final polish, verify build

- [ ] **Step 1: Run dev server and verify all pages load**

```bash
npm run dev
```

- [ ] **Step 2: Run production build to check for type errors**

```bash
npm run build
```

- [ ] **Step 3: Fix any TypeScript errors**

- [ ] **Step 4: Final commit**

```bash
git add -A && git commit -m "chore: fix build errors and polish"
```

---

## Summary

- **19 tasks**, ~80 steps total
- **Phase 1** (Tasks 1-4): Scaffolding, types, stores, services
- **Phase 2** (Tasks 5-7): UI components, layout, gamification
- **Phase 3** (Tasks 8-16): All 8 pages
- **Phase 4** (Tasks 17-19): Wiring, remaining data, polish

Each task produces a working commit. The app is functional after Task 17.
