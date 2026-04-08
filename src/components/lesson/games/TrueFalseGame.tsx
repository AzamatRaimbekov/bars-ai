import { useState } from "react";
import { motion } from "framer-motion";
import { Check, X } from "lucide-react";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface TrueFalseGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

export function TrueFalseGame({ question, onAnswer }: TrueFalseGameProps) {
  const { lang } = useTranslation();
  const [answered, setAnswered] = useState(false);
  const [selected, setSelected] = useState<boolean | null>(null);

  const handleSelect = (value: boolean) => {
    if (answered) return;
    setSelected(value);
    setAnswered(true);
    setTimeout(() => onAnswer(value === question.answer), 1200);
  };

  return (
    <motion.div initial={{ opacity: 0, x: 40 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -40 }} className="flex flex-col gap-6">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="p-5 rounded-2xl bg-surface border border-border text-center">
        <p className="text-base">{question.statement?.[lang]}</p>
      </div>
      <div className="grid grid-cols-2 gap-4">
        {[true, false].map((val) => {
          const isSelected = selected === val;
          const showCorrect = answered && val === question.answer;
          const showWrong = answered && isSelected && val !== question.answer;
          return (
            <motion.button key={String(val)} onClick={() => handleSelect(val)} disabled={answered}
              animate={showWrong ? { x: [0, -6, 6, -6, 0] } : {}}
              className={`flex items-center justify-center gap-3 py-5 rounded-2xl border-2 text-lg font-bold cursor-pointer transition-all ${
                showCorrect ? "border-green-500 bg-green-500/15 text-green-400"
                : showWrong ? "border-red-500 bg-red-500/15 text-red-400"
                : "border-border hover:border-primary/40 text-text"
              }`}>
              {val ? <Check size={24} /> : <X size={24} />}
              {val ? "True" : "False"}
            </motion.button>
          );
        })}
      </div>
    </motion.div>
  );
}
