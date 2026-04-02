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
