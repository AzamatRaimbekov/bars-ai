import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Check, X } from "lucide-react";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface FlashCardGameProps { question: GameQuestion; onAnswer: (correct: boolean) => void; }

export function FlashCardGame({ question, onAnswer }: FlashCardGameProps) {
  const { lang } = useTranslation();
  const pairs = question.pairs ?? [];
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [known, setKnown] = useState(0);
  const card = pairs[index];
  if (!card) return null;

  const advance = (knownCount: number) => {
    setFlipped(false);
    if (index >= pairs.length - 1) {
      setTimeout(() => onAnswer(knownCount / pairs.length >= 0.6), 300);
    } else { setTimeout(() => setIndex(i => i + 1), 200); }
  };

  return (
    <motion.div initial={{opacity:0,x:40}} animate={{opacity:1,x:0}} exit={{opacity:0,x:-40}} className="flex flex-col gap-4">
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <div className="flex items-center justify-between text-xs text-text-secondary">
        <span>{index+1} / {pairs.length}</span><span>{known} known</span>
      </div>
      <motion.div onClick={() => setFlipped(!flipped)}
        className="h-48 rounded-2xl border-2 border-border bg-surface cursor-pointer flex items-center justify-center p-6 select-none"
        whileHover={{scale:1.01}} whileTap={{scale:0.99}}>
        <AnimatePresence mode="wait">
          <motion.div key={flipped?"back":"front"} initial={{rotateY:90,opacity:0}} animate={{rotateY:0,opacity:1}} exit={{rotateY:-90,opacity:0}} transition={{duration:0.2}} className="text-center">
            {flipped ? <p className="text-sm text-accent leading-relaxed">{card.definition[lang]}</p>
              : <p className="text-lg font-semibold">{card.term[lang]}</p>}
          </motion.div>
        </AnimatePresence>
      </motion.div>
      {flipped ? (
        <div className="grid grid-cols-2 gap-3">
          <button onClick={() => advance(known)} className="flex items-center justify-center gap-2 py-3 rounded-xl border-2 border-red-500/30 bg-red-500/10 text-red-400 text-sm font-medium cursor-pointer hover:bg-red-500/20">
            <X size={16} /> Don't know
          </button>
          <button onClick={() => { setKnown(k=>k+1); advance(known+1); }} className="flex items-center justify-center gap-2 py-3 rounded-xl border-2 border-green-500/30 bg-green-500/10 text-green-400 text-sm font-medium cursor-pointer hover:bg-green-500/20">
            <Check size={16} /> I know this
          </button>
        </div>
      ) : <p className="text-center text-xs text-text-secondary">Tap card to flip</p>}
    </motion.div>
  );
}
