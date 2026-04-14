import { apiFetch } from "./api";

export interface DailyQuest {
  id: string;
  title: { en: string; ru: string };
  description: { en: string; ru: string };
  xp_reward: number;
  target: number;
  progress: number;
  completed: boolean;
}

export interface DailyQuestsResponse {
  quests: DailyQuest[];
  date: string;
}

export async function getDailyQuests() {
  return apiFetch<DailyQuestsResponse>("/quests/daily");
}

export async function checkQuests() {
  return apiFetch<DailyQuestsResponse>("/quests/daily/check", { method: "POST" });
}
