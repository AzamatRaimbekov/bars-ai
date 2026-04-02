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
