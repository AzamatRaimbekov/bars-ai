import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Trophy, RotateCcw, Timer } from "lucide-react";

interface MatchPair {
  term: string;
  definition: string;
}

interface MatchGameProps {
  pairs: MatchPair[];
  onComplete?: (timeSeconds: number) => void;
}

export function MatchGame({ pairs, onComplete }: MatchGameProps) {
  const [selectedTerm, setSelectedTerm] = useState<number | null>(null);
  const [selectedDef, setSelectedDef] = useState<number | null>(null);
  const [matched, setMatched] = useState<Set<number>>(new Set());
  const [wrong, setWrong] = useState<{ term: number; def: number } | null>(null);
  const [shuffledDefs, setShuffledDefs] = useState<number[]>([]);
  const [startTime] = useState(Date.now());
  const [elapsed, setElapsed] = useState(0);
  const [done, setDone] = useState(false);

  useEffect(() => {
    setShuffledDefs(
      pairs.map((_, i) => i).sort(() => Math.random() - 0.5)
    );
  }, [pairs]);

  useEffect(() => {
    if (done) return;
    const interval = setInterval(() => setElapsed(Math.floor((Date.now() - startTime) / 1000)), 1000);
    return () => clearInterval(interval);
  }, [startTime, done]);

  useEffect(() => {
    if (selectedTerm !== null && selectedDef !== null) {
      if (selectedTerm === shuffledDefs[selectedDef]) {
        const next = new Set(matched);
        next.add(selectedTerm);
        setMatched(next);
        setSelectedTerm(null);
        setSelectedDef(null);
        if (next.size === pairs.length) {
          setDone(true);
          onComplete?.(elapsed);
        }
      } else {
        setWrong({ term: selectedTerm, def: selectedDef });
        setTimeout(() => {
          setWrong(null);
          setSelectedTerm(null);
          setSelectedDef(null);
        }, 600);
      }
    }
  }, [selectedTerm, selectedDef]);

  const restart = () => {
    setSelectedTerm(null);
    setSelectedDef(null);
    setMatched(new Set());
    setWrong(null);
    setDone(false);
    setShuffledDefs(pairs.map((_, i) => i).sort(() => Math.random() - 0.5));
  };

  if (done) {
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="text-center py-8"
      >
        <Trophy size={40} className="mx-auto text-primary mb-3" />
        <p className="text-lg font-bold mb-1">All Matched!</p>
        <p className="text-sm text-text-secondary mb-4">
          Completed in {elapsed} seconds
        </p>
        <button
          onClick={restart}
          className="flex items-center gap-2 mx-auto px-4 py-2 rounded-xl bg-surface border border-border text-sm hover:border-primary/50 transition-all cursor-pointer"
        >
          <RotateCcw size={14} /> Play Again
        </button>
      </motion.div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between text-xs text-text-secondary">
        <span>{matched.size} / {pairs.length} matched</span>
        <span className="flex items-center gap-1"><Timer size={12} /> {elapsed}s</span>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {/* Terms */}
        <div className="space-y-2">
          {pairs.map((pair, i) => {
            const isMatched = matched.has(i);
            const isSelected = selectedTerm === i;
            const isWrong2 = wrong?.term === i;
            return (
              <motion.button
                key={`t-${i}`}
                onClick={() => !isMatched && setSelectedTerm(i)}
                animate={isWrong2 ? { x: [0, -5, 5, -5, 0] } : {}}
                className={`w-full text-left px-4 py-3 rounded-xl border text-sm transition-all cursor-pointer ${
                  isMatched
                    ? "border-success/40 bg-success/10 text-success opacity-60"
                    : isWrong2
                    ? "border-red-500/50 bg-red-500/10 text-red-400"
                    : isSelected
                    ? "border-primary/50 bg-primary/10 text-primary"
                    : "border-border hover:border-primary/30"
                }`}
                disabled={isMatched}
              >
                {pair.term}
              </motion.button>
            );
          })}
        </div>

        {/* Definitions (shuffled) */}
        <div className="space-y-2">
          {shuffledDefs.map((origIdx, displayIdx) => {
            const isMatched = matched.has(origIdx);
            const isSelected = selectedDef === displayIdx;
            const isWrong2 = wrong?.def === displayIdx;
            return (
              <motion.button
                key={`d-${displayIdx}`}
                onClick={() => !isMatched && setSelectedDef(displayIdx)}
                animate={isWrong2 ? { x: [0, 5, -5, 5, 0] } : {}}
                className={`w-full text-left px-4 py-3 rounded-xl border text-sm transition-all cursor-pointer ${
                  isMatched
                    ? "border-success/40 bg-success/10 text-success opacity-60"
                    : isWrong2
                    ? "border-red-500/50 bg-red-500/10 text-red-400"
                    : isSelected
                    ? "border-accent/50 bg-accent/10 text-accent"
                    : "border-border hover:border-accent/30"
                }`}
                disabled={isMatched}
              >
                {pairs[origIdx].definition}
              </motion.button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
