import { useState } from "react";
import { motion } from "framer-motion";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface QuizGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

export function QuizGame({ question, onAnswer }: QuizGameProps) {
  const { lang } = useTranslation();
  const [selected, setSelected] = useState<number | null>(null);
  const [answered, setAnswered] = useState(false);

  const handleSelect = (idx: number) => {
    if (answered) return;
    setSelected(idx);
    setAnswered(true);
    setTimeout(() => onAnswer(idx === question.correct), 1200);
  };

  return (
    <motion.div initial={{ opacity: 0, x: 40 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -40 }} className="flex flex-col gap-6">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="space-y-3">
        {question.options?.map((opt, i) => {
          const isSelected = selected === i;
          const isCorrectOpt = question.correct === i;
          const showCorrect = answered && isCorrectOpt;
          const showWrong = answered && isSelected && !isCorrectOpt;
          return (
            <motion.button key={i} onClick={() => handleSelect(i)} disabled={answered}
              animate={showWrong ? { x: [0, -8, 8, -8, 0] } : {}}
              className={`w-full text-left px-5 py-4 rounded-2xl border-2 text-sm font-medium transition-all cursor-pointer ${
                showCorrect ? "border-green-500 bg-green-500/15 text-green-400"
                : showWrong ? "border-red-500 bg-red-500/15 text-red-400"
                : isSelected ? "border-primary bg-primary/10 text-primary"
                : "border-border hover:border-primary/40 text-text"
              }`}>
              <span className="flex items-center gap-3">
                <span className={`w-8 h-8 rounded-full border-2 flex items-center justify-center text-xs font-bold shrink-0 ${
                  showCorrect ? "border-green-500 bg-green-500/20 text-green-400"
                  : showWrong ? "border-red-500 bg-red-500/20 text-red-400"
                  : isSelected ? "border-primary bg-primary/20 text-primary"
                  : "border-border text-text-secondary"
                }`}>{String.fromCharCode(65 + i)}</span>
                {opt[lang]}
              </span>
            </motion.button>
          );
        })}
      </div>
    </motion.div>
  );
}
