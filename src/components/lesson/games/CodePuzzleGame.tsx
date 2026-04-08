import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface CodePuzzleGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

function shuffle<T>(arr: T[]): T[] { const c=[...arr]; for(let i=c.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[c[i],c[j]]=[c[j],c[i]];} return c; }

export function CodePuzzleGame({ question, onAnswer }: CodePuzzleGameProps) {
  const { lang } = useTranslation();
  const correctItems = question.items ?? [];
  const [available, setAvailable] = useState<{text:string;origIdx:number}[]>([]);
  const [placed, setPlaced] = useState<{text:string;origIdx:number}[]>([]);
  const [submitted, setSubmitted] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  useEffect(() => {
    const indexed = correctItems.map((item, i) => ({ text: item[lang], origIdx: i }));
    setAvailable(shuffle(indexed)); setPlaced([]);
  }, [correctItems, lang]);

  const addToPlaced = (idx: number) => {
    if (submitted) return;
    setPlaced(p => [...p, available[idx]]); setAvailable(a => a.filter((_, i) => i !== idx));
  };

  const removeFromPlaced = (idx: number) => {
    if (submitted) return;
    setAvailable(a => [...a, placed[idx]]); setPlaced(p => p.filter((_, i) => i !== idx));
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const res = placed.map((item, i) => item.origIdx === i);
    setResults(res);
    setTimeout(() => onAnswer(res.every(Boolean)), 1200);
  };

  return (
    <motion.div initial={{opacity:0,x:40}} animate={{opacity:1,x:0}} exit={{opacity:0,x:-40}} className="flex flex-col gap-6">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="min-h-[120px] rounded-2xl border-2 border-dashed border-border bg-bg/50 p-3 space-y-1.5">
        {placed.length === 0 && <p className="text-sm text-text-secondary/50 text-center py-6">Tap code blocks below to assemble</p>}
        {placed.map((item, i) => (
          <motion.button key={`p-${item.origIdx}`} layout onClick={() => removeFromPlaced(i)}
            className={`w-full text-left px-4 py-2 rounded-lg font-mono text-sm cursor-pointer transition-all ${
              submitted ? results[i] ? "bg-green-500/15 border border-green-500/40 text-green-400" : "bg-red-500/15 border border-red-500/40 text-red-400"
              : "bg-surface border border-border hover:border-primary/30"}`}>{item.text}</motion.button>
        ))}
      </div>
      <div className="flex flex-wrap gap-2">
        {available.map((item, i) => (
          <motion.button key={`a-${item.origIdx}`} layout onClick={() => addToPlaced(i)} disabled={submitted}
            className="px-4 py-2 rounded-lg border-2 border-border bg-surface font-mono text-sm cursor-pointer hover:border-primary/40 transition-all">{item.text}</motion.button>
        ))}
      </div>
      {!submitted && placed.length === correctItems.length && <Button onClick={handleSubmit} className="w-full">Check Code</Button>}
    </motion.div>
  );
}
