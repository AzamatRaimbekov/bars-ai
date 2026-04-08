import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface TypeAnswerGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

function normalize(s: string): string { return s.trim().toLowerCase().replace(/\s+/g, " "); }

export function TypeAnswerGame({ question, onAnswer }: TypeAnswerGameProps) {
  const { lang } = useTranslation();
  const [value, setValue] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleSubmit = () => {
    if (!value.trim()) return;
    setSubmitted(true);
    const correct = normalize(value) === normalize(question.correctText?.[lang] ?? "");
    setIsCorrect(correct);
    setTimeout(() => onAnswer(correct), 1200);
  };

  return (
    <motion.div initial={{opacity:0,x:40}} animate={{opacity:1,x:0}} exit={{opacity:0,x:-40}} className="flex flex-col gap-6">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="space-y-4">
        <Input placeholder="Type your answer..." value={value} onChange={e => setValue(e.target.value)}
          onKeyDown={e => e.key === "Enter" && !submitted && handleSubmit()} disabled={submitted} />
        {submitted && (
          <motion.div initial={{opacity:0,y:8}} animate={{opacity:1,y:0}}
            className={`p-4 rounded-xl border-2 text-sm ${isCorrect?"border-green-500/40 bg-green-500/10 text-green-400":"border-red-500/40 bg-red-500/10 text-red-400"}`}>
            {isCorrect ? "Correct!" : `Correct answer: ${question.correctText?.[lang]}`}
          </motion.div>
        )}
      </div>
      {!submitted && <Button onClick={handleSubmit} disabled={!value.trim()} className="w-full">Check</Button>}
    </motion.div>
  );
}
