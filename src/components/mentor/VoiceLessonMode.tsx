import { motion, AnimatePresence } from "framer-motion";
import { X, Mic, SkipForward, RotateCcw, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/Button";

const PHASES = [
  { key: "intro", label: "Введение" },
  { key: "explain", label: "Объяснение" },
  { key: "check", label: "Проверка" },
  { key: "practice", label: "Практика" },
  { key: "summary", label: "Итог" },
] as const;

interface VoiceLessonModeProps {
  phase: string;
  progress: number;
  content: string;
  isLoading: boolean;
  onNext: () => void;
  onRepeat: () => void;
  onAnswer: (text: string) => void;
  onClose: () => void;
}

export function VoiceLessonMode({
  phase,
  progress,
  content,
  isLoading,
  onNext,
  onRepeat,
  onAnswer,
  onClose,
}: VoiceLessonModeProps) {
  const currentIdx = PHASES.findIndex((p) => p.key === phase);

  const handleMicClick = () => {
    // For now, prompt user input via a simple browser prompt
    // This will be replaced with actual voice recognition integration
    const answer = window.prompt("Ваш ответ:");
    if (answer?.trim()) {
      onAnswer(answer.trim());
    }
  };

  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="fixed inset-0 z-50 flex flex-col bg-bg/98 backdrop-blur-2xl"
      >
        {/* Top bar */}
        <div className="flex items-center justify-between px-6 py-4">
          <p className="text-sm font-semibold text-text">Голосовой урок</p>
          <button
            onClick={onClose}
            className="p-2 rounded-xl text-text-secondary hover:text-text hover:bg-surface transition-all cursor-pointer"
          >
            <X size={18} />
          </button>
        </div>

        {/* Phase progress bar */}
        <div className="px-6 pb-4">
          <div className="flex items-center gap-1 mb-2">
            {PHASES.map((p, i) => {
              const isActive = i === currentIdx;
              const isComplete = i < currentIdx;
              return (
                <div key={p.key} className="flex-1 flex flex-col items-center gap-1">
                  <div
                    className={`w-full h-1.5 rounded-full transition-colors ${
                      isComplete
                        ? "bg-primary"
                        : isActive
                        ? "bg-primary/60"
                        : "bg-white/8"
                    }`}
                  />
                  <span
                    className={`text-[10px] font-medium transition-colors ${
                      isActive
                        ? "text-primary"
                        : isComplete
                        ? "text-primary/60"
                        : "text-text-secondary/50"
                    }`}
                  >
                    {p.label}
                  </span>
                </div>
              );
            })}
          </div>
          {/* Overall progress */}
          <div className="w-full h-0.5 bg-white/5 rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-primary rounded-full"
              initial={{ width: 0 }}
              animate={{ width: `${progress * 100}%` }}
              transition={{ duration: 0.5, ease: "easeOut" }}
            />
          </div>
        </div>

        {/* Content area */}
        <div className="flex-1 flex items-center justify-center px-6 py-8 overflow-y-auto">
          <AnimatePresence mode="wait">
            {isLoading ? (
              <motion.div
                key="loading"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="flex flex-col items-center gap-4"
              >
                <Loader2 size={32} className="animate-spin text-primary" />
                <p className="text-sm text-text-secondary">Ментор думает...</p>
              </motion.div>
            ) : (
              <motion.div
                key={phase + content.slice(0, 20)}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                transition={{ duration: 0.3 }}
                className="max-w-2xl w-full"
              >
                <div className="bg-surface/50 border border-border rounded-2xl p-6 md:p-8">
                  <p className="text-base md:text-lg text-text leading-relaxed whitespace-pre-wrap">
                    {content}
                  </p>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        {/* Bottom actions */}
        <div className="flex items-center justify-center gap-4 px-6 pb-8">
          <Button
            variant="secondary"
            size="md"
            onClick={onRepeat}
            disabled={isLoading}
          >
            <RotateCcw size={16} />
            Повтори
          </Button>

          <motion.button
            whileTap={{ scale: 0.9 }}
            onClick={handleMicClick}
            disabled={isLoading}
            className="w-16 h-16 rounded-full bg-primary/15 border-2 border-primary/30 flex items-center justify-center text-primary hover:bg-primary/25 transition-all cursor-pointer disabled:opacity-50"
          >
            <Mic size={24} />
          </motion.button>

          <Button
            variant="primary"
            size="md"
            onClick={onNext}
            disabled={isLoading || phase === "complete" || phase === "summary"}
          >
            Далее
            <SkipForward size={16} />
          </Button>
        </div>
      </motion.div>
    </AnimatePresence>
  );
}
