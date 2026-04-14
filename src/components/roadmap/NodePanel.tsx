import { motion, AnimatePresence } from "framer-motion";
import { X, Clock, BookOpen, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { useTranslation } from "@/hooks/useTranslation";
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
  const { t, lang } = useTranslation();

  if (!node) return null;

  const completed = node.lessons.filter((l) => completedLessons.includes(l.id)).length;
  const total = node.lessons.length;

  return (
    <AnimatePresence>
      {node && (
        <>
          {/* Mobile overlay backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/50 z-40 lg:hidden"
          />
          <motion.div
            initial={{ x: 400, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: 400, opacity: 0 }}
            className="fixed right-0 bottom-0 lg:top-0 h-[85dvh] lg:h-full w-full sm:w-96 bg-[#111111] border-l border-t lg:border-t-0 border-white/6 z-50 p-5 lg:p-6 overflow-y-auto rounded-t-2xl lg:rounded-none"
          >
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-lg font-bold">{node.title[lang]}</h3>
              <button onClick={onClose} className="p-1 rounded-lg hover:bg-border/50 text-text-secondary cursor-pointer">
                <X size={20} />
              </button>
            </div>

            <p className="text-sm text-text-secondary mb-4">{node.description[lang]}</p>

            <div className="flex items-center gap-4 mb-4 text-xs text-text-secondary">
              <span className="flex items-center gap-1">
                <Clock size={12} /> {node.estimatedMinutes} {t("common.min")}
              </span>
              <span className="flex items-center gap-1">
                <BookOpen size={12} /> {total} {t("common.lessons")}
              </span>
            </div>

            <ProgressBar value={completed} max={total} color="#4ADE80" showLabel className="mb-6" />

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
                        : "border-white/6 hover:border-[#F97316]/30 text-text"
                    }`}
                  >
                    <span className="flex items-center gap-2">
                      {isDone && "✓ "}
                      {lesson.title[lang]}
                      <span className="ml-auto text-xs text-text-secondary">
                        {lesson.estimatedMinutes}m
                      </span>
                    </span>
                  </button>
                );
              })}
            </div>

            {status === "locked" ? (
              <div className="flex flex-col items-center gap-3 py-6">
                <img src="/images/mascot-confused.png" alt="Locked" className="w-28 h-28 lg:w-36 lg:h-36 object-contain drop-shadow-lg opacity-70" />
                <p className="text-sm text-text-secondary text-center">{t("roadmap.completePrevious")}</p>
              </div>
            ) : (
              <div className="flex flex-col items-center gap-4">
                <img
                  src={completed === total ? "/images/mascot-study.png" : "/images/mascot-thinking.png"}
                  alt="Mascot"
                  className="w-24 h-24 lg:w-32 lg:h-32 object-contain drop-shadow-lg"
                />
                <Button className="w-full" onClick={onStartAI}>
                  {t("roadmap.startWithAI")} <ArrowRight size={14} />
                </Button>
              </div>
            )}
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
