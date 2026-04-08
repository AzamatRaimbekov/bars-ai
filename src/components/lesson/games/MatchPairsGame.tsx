import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface MatchPairsGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

function shuffle<T>(arr: T[]): T[] { const c=[...arr]; for(let i=c.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[c[i],c[j]]=[c[j],c[i]];} return c; }

export function MatchPairsGame({ question, onAnswer }: MatchPairsGameProps) {
  const { lang } = useTranslation();
  const pairs = question.pairs ?? [];
  const [shuffledDefs, setShuffledDefs] = useState<number[]>([]);
  const [selectedTerm, setSelectedTerm] = useState<number|null>(null);
  const [selectedDef, setSelectedDef] = useState<number|null>(null);
  const [matched, setMatched] = useState<Set<number>>(new Set());
  const [wrong, setWrong] = useState<{term:number;def:number}|null>(null);
  const [mistakes, setMistakes] = useState(0);

  useEffect(() => { setShuffledDefs(shuffle(pairs.map((_,i)=>i))); }, [pairs]);

  useEffect(() => {
    if (selectedTerm !== null && selectedDef !== null) {
      const actualIdx = shuffledDefs[selectedDef];
      if (selectedTerm === actualIdx) {
        const next = new Set(matched); next.add(selectedTerm); setMatched(next);
        setSelectedTerm(null); setSelectedDef(null);
        if (next.size === pairs.length) { setTimeout(() => onAnswer(mistakes === 0), 600); }
      } else {
        setMistakes(m => m + 1);
        setWrong({ term: selectedTerm, def: selectedDef });
        setTimeout(() => { setWrong(null); setSelectedTerm(null); setSelectedDef(null); }, 600);
      }
    }
  }, [selectedTerm, selectedDef]);

  return (
    <motion.div initial={{opacity:0,x:40}} animate={{opacity:1,x:0}} exit={{opacity:0,x:-40}} className="flex flex-col gap-4">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <p className="text-sm text-text-secondary">{matched.size} / {pairs.length} matched</p>
      <div className="grid grid-cols-2 gap-3">
        <div className="space-y-2">
          {pairs.map((p, i) => {
            const isMatched = matched.has(i); const isSelected = selectedTerm === i; const isWrong2 = wrong?.term === i;
            return (<motion.button key={`t-${i}`} onClick={() => !isMatched && setSelectedTerm(i)} animate={isWrong2?{x:[0,-5,5,-5,0]}:{}} disabled={isMatched}
              className={`w-full text-left px-4 py-3 rounded-xl border-2 text-sm transition-all cursor-pointer ${
                isMatched?"border-green-500/40 bg-green-500/10 text-green-400 opacity-50"
                :isWrong2?"border-red-500 bg-red-500/10 text-red-400"
                :isSelected?"border-primary bg-primary/10 text-primary"
                :"border-border hover:border-primary/30"}`}>{p.term[lang]}</motion.button>);
          })}
        </div>
        <div className="space-y-2">
          {shuffledDefs.map((origIdx, dispIdx) => {
            const isMatched = matched.has(origIdx); const isSelected = selectedDef === dispIdx; const isWrong2 = wrong?.def === dispIdx;
            return (<motion.button key={`d-${dispIdx}`} onClick={() => !isMatched && setSelectedDef(dispIdx)} animate={isWrong2?{x:[0,5,-5,5,0]}:{}} disabled={isMatched}
              className={`w-full text-left px-4 py-3 rounded-xl border-2 text-sm transition-all cursor-pointer ${
                isMatched?"border-green-500/40 bg-green-500/10 text-green-400 opacity-50"
                :isWrong2?"border-red-500 bg-red-500/10 text-red-400"
                :isSelected?"border-accent bg-accent/10 text-accent"
                :"border-border hover:border-accent/30"}`}>{pairs[origIdx].definition[lang]}</motion.button>);
          })}
        </div>
      </div>
    </motion.div>
  );
}
