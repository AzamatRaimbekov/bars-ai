import { useCallback } from "react";
import { useUserStore } from "@/store/userStore";
import { BADGES } from "@/data/achievements";
import { XP_REWARDS } from "@/lib/constants";

export function useGameification() {
  const { profile, addXP, earnBadge, updateStreak } = useUserStore();

  const checkBadges = useCallback(() => {
    if (!profile) return;

    for (const badge of BADGES) {
      if (profile.earnedBadges.includes(badge.id)) continue;
      if (badge.direction && badge.direction !== profile.direction) continue;

      let earned = false;
      switch (badge.id) {
        case "first-step":
          earned = profile.completedLessons.length >= 1;
          break;
        case "fast-learner":
          earned = profile.completedLessons.length >= 10;
          break;
        case "streak-7":
          earned = profile.streak >= 7;
          break;
        case "streak-30":
          earned = profile.streak >= 30;
          break;
        case "streak-100":
          earned = profile.streak >= 100;
          break;
        case "half-way":
          earned = profile.completedNodes.length >= 10;
          break;
        case "road-complete":
          earned = profile.completedNodes.length >= 20;
          break;
      }

      if (earned) earnBadge(badge.id);
    }
  }, [profile, earnBadge]);

  const onLessonComplete = useCallback(() => {
    addXP(XP_REWARDS.completeLesson);
    updateStreak();
    checkBadges();
  }, [addXP, updateStreak, checkBadges]);

  const onQuizPerfect = useCallback(() => {
    addXP(XP_REWARDS.perfectQuiz);
    checkBadges();
  }, [addXP, checkBadges]);

  const onInterviewComplete = useCallback(() => {
    addXP(XP_REWARDS.interviewSimulation);
    checkBadges();
  }, [addXP, checkBadges]);

  return { checkBadges, onLessonComplete, onQuizPerfect, onInterviewComplete };
}
