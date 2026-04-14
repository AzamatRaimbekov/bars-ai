import { useEffect, useState, useCallback } from "react";
import { motion } from "framer-motion";
import { Target, CheckCircle2, Zap, BookOpen, Flame, Brain, Clock, Award } from "lucide-react";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { useTranslation } from "@/hooks/useTranslation";
import { getDailyQuests, type DailyQuest } from "@/services/questApi";

const QUEST_ICONS: Record<string, typeof Target> = {
  complete_lessons_3: BookOpen,
  complete_lessons_1: BookOpen,
  complete_lessons_5: BookOpen,
  earn_xp_100: Zap,
  earn_xp_50: Zap,
  earn_xp_200: Zap,
  maintain_streak: Flame,
  complete_quiz_2: Brain,
  study_30min: Clock,
  complete_node: Award,
};

const QUEST_COLORS: Record<string, string> = {
  complete_lessons_3: "#F97316",
  complete_lessons_1: "#F97316",
  complete_lessons_5: "#F97316",
  earn_xp_100: "#FB923C",
  earn_xp_50: "#FB923C",
  earn_xp_200: "#FB923C",
  maintain_streak: "#F97316",
  complete_quiz_2: "#FB923C",
  study_30min: "#F97316",
  complete_node: "#FB923C",
};

export function DailyQuests() {
  const { t, lang } = useTranslation();
  const [quests, setQuests] = useState<DailyQuest[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchQuests = useCallback(async () => {
    try {
      const data = await getDailyQuests();
      setQuests(data.quests);
    } catch {
      // silently fail
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchQuests();
    const interval = setInterval(fetchQuests, 30000);
    return () => clearInterval(interval);
  }, [fetchQuests]);

  const completedCount = quests.filter((q) => q.completed).length;

  if (loading) {
    return (
      <div className="p-5 rounded-2xl bg-[#0A0A0A] border border-white/6">
        <div className="flex items-center gap-2 mb-4">
          <Target size={18} className="text-[#FB923C]" />
          <h3 className="text-sm font-semibold">{t("quests.daily")}</h3>
        </div>
        <div className="space-y-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="h-14 rounded-xl bg-white/4 animate-pulse" />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="p-5 rounded-2xl bg-[#0A0A0A] border border-white/6">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Target size={18} className="text-[#FB923C]" />
          <h3 className="text-sm font-semibold">{t("quests.daily")}</h3>
        </div>
        <span className="text-xs text-white/40">
          {completedCount}/{quests.length}
        </span>
      </div>

      <div className="space-y-3">
        {quests.map((quest, index) => {
          const Icon = QUEST_ICONS[quest.id] || Target;
          const color = QUEST_COLORS[quest.id] || "#F97316";
          const title = quest.title[lang] || quest.title.en;

          return (
            <motion.div
              key={quest.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`flex items-center gap-3 p-3 rounded-xl border transition-colors ${
                quest.completed
                  ? "border-[#F97316]/20 bg-[#F97316]/5"
                  : "border-white/6 bg-[#0A0A0A]"
              }`}
            >
              <div
                className="w-9 h-9 rounded-xl flex items-center justify-center shrink-0"
                style={{ backgroundColor: quest.completed ? "#F9731615" : `${color}15` }}
              >
                {quest.completed ? (
                  <CheckCircle2 size={18} className="text-[#FB923C]" />
                ) : (
                  <Icon size={18} style={{ color }} />
                )}
              </div>

              <div className="flex-1 min-w-0">
                <div className="flex items-center justify-between mb-1">
                  <p
                    className={`text-sm font-medium truncate ${
                      quest.completed ? "text-[#FB923C]/60 line-through" : "text-white"
                    }`}
                  >
                    {title}
                  </p>
                  <span className="text-xs text-white/40 ml-2 shrink-0">
                    {quest.completed
                      ? t("quests.completed")
                      : t("quests.progress", {
                          current: String(quest.progress),
                          target: String(quest.target),
                        })}
                  </span>
                </div>
                <ProgressBar
                  value={quest.progress}
                  max={quest.target}
                  color={quest.completed ? "#F97316" : color}
                />
              </div>

              {/* Reward pill */}
              <div className="flex items-center gap-1 shrink-0 ml-1 px-2 py-1 rounded-full bg-[#F97316]/10">
                <Zap size={11} className="text-[#FB923C]" />
                <span className="text-xs font-semibold text-[#FB923C]">
                  {quest.xp_reward}
                </span>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
