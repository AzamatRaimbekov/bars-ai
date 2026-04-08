import { create } from "zustand";
import { apiFetch } from "@/services/api";

interface UserState {
  addXP: (amount: number, source: string) => Promise<void>;
  completeNode: (nodeId: string) => Promise<void>;
  completeLesson: (lessonId: string) => Promise<void>;
  earnBadge: (badgeId: string) => Promise<void>;
  updateStreak: () => Promise<void>;
}

export const useUserStore = create<UserState>()(() => ({
  addXP: async (amount, source) => {
    await apiFetch("/progress/xp", {
      method: "POST",
      body: JSON.stringify({ amount, source }),
    });
  },

  completeNode: async (nodeId) => {
    await apiFetch("/progress/node", {
      method: "POST",
      body: JSON.stringify({ node_id: nodeId }),
    });
  },

  completeLesson: async (lessonId) => {
    await apiFetch("/progress/lesson", {
      method: "POST",
      body: JSON.stringify({ lesson_id: lessonId }),
    });
  },

  earnBadge: async (badgeId) => {
    await apiFetch("/progress/badge", {
      method: "POST",
      body: JSON.stringify({ badge_id: badgeId }),
    });
  },

  updateStreak: async () => {
    await apiFetch("/progress/streak", { method: "POST" });
  },
}));
