import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { GripVertical } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface DragOrderGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

function shuffle<T>(arr: T[]): T[] { const c=[...arr]; for(let i=c.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[c[i],c[j]]=[c[j],c[i]];} return c; }

export function DragOrderGame({ question, onAnswer }: DragOrderGameProps) {
  const { lang } = useTranslation();
  const correctOrder = question.items ?? [];
  const [items, setItems] = useState<{text:string;origIdx:number}[]>([]);
  const [dragIdx, setDragIdx] = useState<number|null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  useEffect(() => {
    const indexed = correctOrder.map((item, i) => ({ text: item[lang], origIdx: i }));
    setItems(shuffle(indexed));
  }, [correctOrder, lang]);

  const moveItem = (from: number, to: number) => {
    if (submitted) return;
    const copy = [...items]; const [moved] = copy.splice(from, 1); copy.splice(to, 0, moved); setItems(copy);
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const res = items.map((item, i) => item.origIdx === i);
    setResults(res);
    setTimeout(() => onAnswer(res.every(Boolean)), 1200);
  };

  return (
    <motion.div initial={{opacity:0,x:40}} animate={{opacity:1,x:0}} exit={{opacity:0,x:-40}} className="flex flex-col gap-6">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="space-y-2">
        {items.map((item, i) => (
          <motion.div key={item.origIdx} layout draggable={!submitted}
            onDragStart={() => setDragIdx(i)}
            onDragOver={e => e.preventDefault()}
            onDrop={() => { if (dragIdx !== null && dragIdx !== i) moveItem(dragIdx, i); setDragIdx(null); }}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl border-2 text-sm cursor-grab active:cursor-grabbing transition-all ${
              submitted ? results[i] ? "border-green-500/40 bg-green-500/10 text-green-400" : "border-red-500/40 bg-red-500/10 text-red-400"
              : dragIdx === i ? "border-primary bg-primary/10 opacity-60"
              : "border-border bg-surface hover:border-primary/30"}`}>
            <GripVertical size={16} className="text-text-secondary shrink-0" />
            <span className="w-6 h-6 rounded-full border border-border flex items-center justify-center text-xs text-text-secondary shrink-0">{i+1}</span>
            {item.text}
          </motion.div>
        ))}
      </div>
      {!submitted && <Button onClick={handleSubmit} className="w-full">Check Order</Button>}
    </motion.div>
  );
}
