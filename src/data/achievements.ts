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
