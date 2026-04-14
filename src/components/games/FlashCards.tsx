import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { RotateCcw, ChevronLeft, ChevronRight, Check } from "lucide-react";

interface FlashCard {
  front: string;
  back: string;
}

interface FlashCardsProps {
  cards: FlashCard[];
  onComplete?: (knownCount: number) => void;
}

export function FlashCards({ cards, onComplete }: FlashCardsProps) {
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [known, setKnown] = useState<Set<number>>(new Set());
  const [done, setDone] = useState(false);

  const card = cards[index];

  const handleKnow = () => {
    const next = new Set(known);
    next.add(index);
    setKnown(next);
    goNext();
  };

  const goNext = () => {
    setFlipped(false);
    if (index >= cards.length - 1) {
      setDone(true);
      onComplete?.(known.size + 1);
    } else {
      setTimeout(() => setIndex(i => i + 1), 200);
    }
  };

  const goPrev = () => {
    if (index > 0) {
      setFlipped(false);
      setTimeout(() => setIndex(i => i - 1), 200);
    }
  };

  const restart = () => {
    setIndex(0);
    setFlipped(false);
    setKnown(new Set());
    setDone(false);
  };

  if (done) {
    const pct = Math.round((known.size / cards.length) * 100);
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="text-center py-8"
      >
        <p className="text-4xl font-bold text-primary mb-2">{pct}%</p>
        <p className="text-sm text-text-secondary mb-4">
          {known.size} / {cards.length} cards mastered
        </p>
        <button
          onClick={restart}
          className="flex items-center gap-2 mx-auto px-4 py-2 rounded-xl bg-surface border border-border text-sm hover:border-primary/50 transition-all cursor-pointer"
        >
          <RotateCcw size={14} /> Try Again
        </button>
      </motion.div>
    );
  }

  return (
    <div className="space-y-4">
      {/* Progress */}
      <div className="flex items-center justify-between text-xs text-text-secondary">
        <span>{index + 1} / {cards.length}</span>
        <span>{known.size} mastered</span>
      </div>
      <div className="h-1 bg-border rounded-full overflow-hidden">
        <motion.div
          className="h-full bg-primary rounded-full"
          animate={{ width: `${((index + 1) / cards.length) * 100}%` }}
        />
      </div>

      {/* Card */}
      <motion.div
        onClick={() => setFlipped(!flipped)}
        className="relative h-48 rounded-2xl border-2 border-border bg-surface cursor-pointer flex items-center justify-center p-6 overflow-hidden select-none"
        whileHover={{ scale: 1.01 }}
        whileTap={{ scale: 0.99 }}
      >
        <AnimatePresence mode="wait">
          <motion.div
            key={flipped ? "back" : "front"}
            initial={{ rotateY: 90, opacity: 0 }}
            animate={{ rotateY: 0, opacity: 1 }}
            exit={{ rotateY: -90, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="text-center"
          >
            {flipped ? (
              <p className="text-sm text-accent leading-relaxed">{card.back}</p>
            ) : (
              <p className="text-lg font-semibold">{card.front}</p>
            )}
          </motion.div>
        </AnimatePresence>

        <span className="absolute bottom-3 right-4 text-[10px] text-text-secondary/50">
          {flipped ? "answer" : "tap to flip"}
        </span>
      </motion.div>

      {/* Controls */}
      <div className="flex items-center justify-center gap-3">
        <button
          onClick={goPrev}
          disabled={index === 0}
          className="w-10 h-10 rounded-xl bg-surface border border-border flex items-center justify-center disabled:opacity-30 cursor-pointer hover:border-primary/30 transition-all"
        >
          <ChevronLeft size={16} />
        </button>
        <button
          onClick={handleKnow}
          className="px-6 py-2.5 rounded-xl bg-success/10 border border-success/30 text-success text-sm font-medium flex items-center gap-2 cursor-pointer hover:bg-success/20 transition-all"
        >
          <Check size={14} /> I know this
        </button>
        <button
          onClick={goNext}
          className="px-6 py-2.5 rounded-xl bg-surface border border-border text-text-secondary text-sm font-medium cursor-pointer hover:border-primary/30 transition-all"
        >
          Skip
        </button>
        <button
          onClick={() => { setFlipped(false); setTimeout(() => setIndex(i => Math.min(i + 1, cards.length - 1)), 200); }}
          disabled={index >= cards.length - 1}
          className="w-10 h-10 rounded-xl bg-surface border border-border flex items-center justify-center disabled:opacity-30 cursor-pointer hover:border-primary/30 transition-all"
        >
          <ChevronRight size={16} />
        </button>
      </div>
    </div>
  );
}
