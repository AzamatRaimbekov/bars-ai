import type { Badge } from "@/types";

export const BADGES: Badge[] = [
  // ── Lessons ──────────────────────────────────────────────
  { id: "first-step", name: { en: "First Step", ru: "Первый шаг" }, description: { en: "Complete your first lesson", ru: "Пройдите первый урок" }, icon: "🚀", rarity: "Common", condition: "completedLessons >= 1" },
  { id: "fast-learner", name: { en: "Fast Learner", ru: "Быстрый ученик" }, description: { en: "Complete 10 lessons", ru: "Пройдите 10 уроков" }, icon: "⚡", rarity: "Rare", condition: "completedLessons >= 10" },
  { id: "bookworm", name: { en: "Bookworm", ru: "Книжный червь" }, description: { en: "Complete 25 lessons", ru: "Пройдите 25 уроков" }, icon: "📚", rarity: "Epic", condition: "completedLessons >= 25" },
  { id: "centurion", name: { en: "Centurion", ru: "Центурион" }, description: { en: "Complete 100 lessons", ru: "Пройдите 100 уроков" }, icon: "🏛️", rarity: "Legendary", condition: "completedLessons >= 100" },

  // ── Topics / Nodes ──────────────────────────────────────
  { id: "first-topic", name: { en: "First Topic", ru: "Первая тема" }, description: { en: "Complete your first topic", ru: "Завершите первую тему" }, icon: "📌", rarity: "Common", condition: "completedNodes >= 1" },
  { id: "five-topics", name: { en: "Getting Serious", ru: "Серьёзный подход" }, description: { en: "Complete 5 topics", ru: "Завершите 5 тем" }, icon: "🎯", rarity: "Rare", condition: "completedNodes >= 5" },
  { id: "ten-topics", name: { en: "Knowledge Hunter", ru: "Охотник за знаниями" }, description: { en: "Complete 10 topics", ru: "Завершите 10 тем" }, icon: "🔍", rarity: "Epic", condition: "completedNodes >= 10" },
  { id: "half-way", name: { en: "Half Way There", ru: "Полпути пройдено" }, description: { en: "Complete 50% of your roadmap", ru: "Пройдите 50% дорожной карты" }, icon: "🗺️", rarity: "Epic", condition: "roadmapProgress >= 50" },
  { id: "road-complete", name: { en: "Road Master", ru: "Мастер пути" }, description: { en: "Complete your entire roadmap", ru: "Пройдите всю дорожную карту" }, icon: "👑", rarity: "Legendary", condition: "roadmapProgress >= 100" },

  // ── Streaks ─────────────────────────────────────────────
  { id: "streak-3", name: { en: "Getting Started", ru: "Начало положено" }, description: { en: "3-day learning streak", ru: "3-дневная серия" }, icon: "🔥", rarity: "Common", condition: "streak >= 3" },
  { id: "streak-7", name: { en: "Week Warrior", ru: "Воин недели" }, description: { en: "7-day learning streak", ru: "7-дневная серия" }, icon: "🔥", rarity: "Rare", condition: "streak >= 7" },
  { id: "streak-14", name: { en: "Two Weeks Strong", ru: "Две недели силы" }, description: { en: "14-day learning streak", ru: "14-дневная серия" }, icon: "💪", rarity: "Rare", condition: "streak >= 14" },
  { id: "streak-30", name: { en: "Streak Legend", ru: "Легенда серий" }, description: { en: "30-day learning streak", ru: "30-дневная серия" }, icon: "🏆", rarity: "Epic", condition: "streak >= 30" },
  { id: "streak-60", name: { en: "Iron Will", ru: "Железная воля" }, description: { en: "60-day learning streak", ru: "60-дневная серия" }, icon: "⚔️", rarity: "Epic", condition: "streak >= 60" },
  { id: "streak-100", name: { en: "Unstoppable", ru: "Неостановимый" }, description: { en: "100-day learning streak", ru: "100-дневная серия" }, icon: "💎", rarity: "Legendary", condition: "streak >= 100" },

  // ── XP Milestones ───────────────────────────────────────
  { id: "xp-100", name: { en: "First Hundred", ru: "Первая сотня" }, description: { en: "Earn 100 XP", ru: "Заработайте 100 XP" }, icon: "✨", rarity: "Common", condition: "xp >= 100" },
  { id: "xp-500", name: { en: "Rising Star", ru: "Восходящая звезда" }, description: { en: "Earn 500 XP", ru: "Заработайте 500 XP" }, icon: "⭐", rarity: "Rare", condition: "xp >= 500" },
  { id: "xp-2000", name: { en: "XP Machine", ru: "Машина XP" }, description: { en: "Earn 2,000 XP", ru: "Заработайте 2 000 XP" }, icon: "🌟", rarity: "Epic", condition: "xp >= 2000" },
  { id: "xp-5000", name: { en: "XP Legend", ru: "Легенда XP" }, description: { en: "Earn 5,000 XP", ru: "Заработайте 5 000 XP" }, icon: "💫", rarity: "Epic", condition: "xp >= 5000" },
  { id: "xp-15000", name: { en: "XP God", ru: "Бог XP" }, description: { en: "Earn 15,000 XP", ru: "Заработайте 15 000 XP" }, icon: "🌠", rarity: "Legendary", condition: "xp >= 15000" },

  // ── Simulator ───────────────────────────────────────────
  { id: "first-interview", name: { en: "First Interview", ru: "Первое интервью" }, description: { en: "Complete your first interview simulation", ru: "Пройдите первую симуляцию интервью" }, icon: "🎤", rarity: "Common", condition: "interviewSessions >= 1" },
  { id: "interview-ready", name: { en: "Interview Ready", ru: "Готов к интервью" }, description: { en: "Pass 5 interview simulations", ru: "Пройдите 5 симуляций интервью" }, icon: "💼", rarity: "Epic", condition: "interviewSessions >= 5" },
  { id: "interview-master", name: { en: "Interview Master", ru: "Мастер интервью" }, description: { en: "Pass 20 interview simulations", ru: "Пройдите 20 симуляций интервью" }, icon: "🎩", rarity: "Legendary", condition: "interviewSessions >= 20" },

  // ── Voice ───────────────────────────────────────────────
  { id: "voice-first", name: { en: "Voice Debut", ru: "Голосовой дебют" }, description: { en: "Complete your first voice session", ru: "Пройдите первую голосовую сессию" }, icon: "🎙️", rarity: "Common", condition: "voiceSessions >= 1" },
  { id: "voice-warrior", name: { en: "Voice Warrior", ru: "Голосовой воин" }, description: { en: "Complete 10 voice sessions", ru: "Пройдите 10 голосовых сессий" }, icon: "🗣️", rarity: "Rare", condition: "voiceSessions >= 10" },

  // ── Levels ──────────────────────────────────────────────
  { id: "level-apprentice", name: { en: "Apprentice", ru: "Ученик" }, description: { en: "Reach Apprentice level", ru: "Достигните уровня Ученик" }, icon: "📘", rarity: "Common", condition: "level >= Apprentice" },
  { id: "level-practitioner", name: { en: "Practitioner", ru: "Практикант" }, description: { en: "Reach Practitioner level", ru: "Достигните уровня Практикант" }, icon: "📗", rarity: "Rare", condition: "level >= Practitioner" },
  { id: "level-expert", name: { en: "Expert", ru: "Эксперт" }, description: { en: "Reach Expert level", ru: "Достигните уровня Эксперт" }, icon: "📕", rarity: "Epic", condition: "level >= Expert" },
  { id: "level-master", name: { en: "Master", ru: "Мастер" }, description: { en: "Reach Master level", ru: "Достигните уровня Мастер" }, icon: "📓", rarity: "Legendary", condition: "level >= Master" },
  { id: "level-legend", name: { en: "Legend", ru: "Легенда" }, description: { en: "Reach Legend level", ru: "Достигните уровня Легенда" }, icon: "🏅", rarity: "Legendary", condition: "level >= Legend" },

  // ── Direction Mastery ───────────────────────────────────
  { id: "code-whisperer", name: { en: "Code Whisperer", ru: "Шёпот кода" }, description: { en: "Master all Frontend sections", ru: "Освойте все разделы Frontend" }, icon: "💻", rarity: "Legendary", direction: "frontend", condition: "allSectionsComplete" },
  { id: "fluent-speaker", name: { en: "Fluent Speaker", ru: "Свободная речь" }, description: { en: "Master all English sections", ru: "Освойте все разделы английского" }, icon: "🗣️", rarity: "Legendary", direction: "english", condition: "allSectionsComplete" },
  { id: "service-star", name: { en: "Service Star", ru: "Звезда сервиса" }, description: { en: "Master all Call Center sections", ru: "Освойте все разделы Call Center" }, icon: "⭐", rarity: "Legendary", direction: "callcenter", condition: "allSectionsComplete" },
  { id: "finance-guru", name: { en: "Finance Guru", ru: "Гуру финансов" }, description: { en: "Master all CIB sections", ru: "Освойте все разделы банкинга" }, icon: "💰", rarity: "Legendary", direction: "cib", condition: "allSectionsComplete" },

  // ── Special ─────────────────────────────────────────────
  { id: "night-owl", name: { en: "Night Owl", ru: "Ночная сова" }, description: { en: "Complete a lesson after midnight", ru: "Пройдите урок после полуночи" }, icon: "🦉", rarity: "Rare", condition: "nightLesson" },
  { id: "early-bird", name: { en: "Early Bird", ru: "Ранняя пташка" }, description: { en: "Complete a lesson before 7 AM", ru: "Пройдите урок до 7 утра" }, icon: "🐦", rarity: "Rare", condition: "earlyLesson" },
  { id: "perfectionist", name: { en: "Perfectionist", ru: "Перфекционист" }, description: { en: "Get 3 stars on 10 lessons", ru: "Получите 3 звезды в 10 уроках" }, icon: "💯", rarity: "Epic", condition: "perfectLessons >= 10" },
  { id: "speed-learner", name: { en: "Speed Learner", ru: "Скоростной ученик" }, description: { en: "Complete 5 lessons in one day", ru: "Пройдите 5 уроков за один день" }, icon: "⏱️", rarity: "Epic", condition: "lessonsToday >= 5" },
];
