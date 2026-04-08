import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface FillBlanksGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

export function FillBlanksGame({ question, onAnswer }: FillBlanksGameProps) {
  const { lang } = useTranslation();
  const blanks = question.blanks ?? [];
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [submitted, setSubmitted] = useState(false);

  const handleSelect = (blankIdx: number, optionIdx: number) => {
    if (submitted) return;
    setAnswers(prev => ({ ...prev, [blankIdx]: optionIdx }));
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const allCorrect = blanks.every((b, i) => answers[i] === b.correctIndex);
    setTimeout(() => onAnswer(allCorrect), 1200);
  };

  return (
    <motion.div initial={{opacity:0,x:40}} animate={{opacity:1,x:0}} exit={{opacity:0,x:-40}} className="flex flex-col gap-6">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="space-y-6">
        {blanks.map((blank, bi) => (
          <div key={bi} className="space-y-3">
            <p className="text-sm text-text-secondary">{blank.text[lang]}</p>
            <div className="flex flex-wrap gap-2">
              {blank.options.map((opt, oi) => {
                const isSelected = answers[bi] === oi;
                const isCorrect = submitted && oi === blank.correctIndex;
                const isWrong = submitted && isSelected && oi !== blank.correctIndex;
                return (
                  <button key={oi} onClick={() => handleSelect(bi, oi)} disabled={submitted}
                    className={`px-4 py-2 rounded-xl border-2 text-sm font-medium cursor-pointer transition-all ${
                      isCorrect?"border-green-500 bg-green-500/15 text-green-400"
                      :isWrong?"border-red-500 bg-red-500/15 text-red-400"
                      :isSelected?"border-primary bg-primary/10 text-primary"
                      :"border-border hover:border-primary/30 text-text"}`}>
                    {opt[lang]}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </div>
      {!submitted && <Button onClick={handleSubmit} disabled={Object.keys(answers).length < blanks.length} className="w-full">Check Answer</Button>}
    </motion.div>
  );
}
