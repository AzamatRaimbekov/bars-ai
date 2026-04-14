import { motion } from "framer-motion";
import { Sparkles, BookOpen } from "lucide-react";
import { Card } from "@/components/ui/Card";
import type { RecommendationItem } from "@/services/mentorApi";

interface RecommendationCardProps {
  recommendations: RecommendationItem[];
}

export function RecommendationCard({ recommendations }: RecommendationCardProps) {
  const top = recommendations.slice(0, 2);

  if (top.length === 0) return null;

  return (
    <Card className="relative overflow-hidden border-primary/15 bg-surface/60">
      {/* Gradient border accent */}
      <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-primary/50 to-transparent" />

      <div className="flex items-center gap-2 mb-3">
        <Sparkles size={16} className="text-primary" />
        <p className="text-sm font-semibold text-text">Рекомендации</p>
      </div>

      <div className="space-y-2">
        {top.map((rec) => (
          <motion.div
            key={rec.lesson_id}
            whileHover={{ x: 2 }}
            className="flex items-start gap-3 p-3 rounded-xl bg-white/3 hover:bg-white/5 transition-colors"
          >
            <div className="mt-0.5">
              <BookOpen size={14} className="text-text-secondary" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 mb-0.5">
                <p className="text-sm font-medium text-text truncate">
                  {rec.lesson_title}
                </p>
                <span
                  className={`shrink-0 text-[10px] font-bold px-1.5 py-0.5 rounded-full uppercase ${
                    rec.priority === "high"
                      ? "bg-orange-500/15 text-orange-400"
                      : "bg-blue-500/15 text-blue-400"
                  }`}
                >
                  {rec.priority === "high" ? "важно" : "далее"}
                </span>
              </div>
              <p className="text-xs text-text-secondary truncate">
                {rec.course_title}
              </p>
              <p className="text-xs text-text-secondary/70 mt-1">{rec.reason}</p>
            </div>
          </motion.div>
        ))}
      </div>
    </Card>
  );
}
