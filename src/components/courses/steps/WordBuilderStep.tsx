import { useState, useCallback, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import type { StepWordBuilder } from "@/services/courseApi";

interface Props {
  step: StepWordBuilder;
  onAnswer: (correct: boolean) => void;
}

interface Letter {
  char: string;
  id: number;
}

function shuffleArray<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function WordBuilderStep({ step, onAnswer }: Props) {
  const letters = useMemo<Letter[]>(
    () =>
      shuffleArray(
        step.word.split("").map((char, i) => ({ char, id: i }))
      ),
    [step.word]
  );

  const [placed, setPlaced] = useState<(Letter | null)[]>(
    () => Array(step.word.length).fill(null)
  );
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [draggedLetter, setDraggedLetter] = useState<Letter | null>(null);

  const placedIds = new Set(
    placed.filter((l): l is Letter => l !== null).map((l) => l.id)
  );
  const available = letters.filter((l) => !placedIds.has(l.id));
  const allFilled = placed.every((l) => l !== null);

  const placeLetter = useCallback(
    (letter: Letter) => {
      if (checked) return;
      setPlaced((prev) => {
        const next = [...prev];
        const emptyIdx = next.findIndex((l) => l === null);
        if (emptyIdx !== -1) {
          next[emptyIdx] = letter;
        }
        return next;
      });
    },
    [checked]
  );

  const removeLetter = useCallback(
    (slotIdx: number) => {
      if (checked) return;
      setPlaced((prev) => {
        const next = [...prev];
        next[slotIdx] = null;
        return next;
      });
    },
    [checked]
  );

  const handleDropOnSlot = useCallback(
    (slotIdx: number) => {
      if (checked || !draggedLetter) return;
      setPlaced((prev) => {
        const next = [...prev];
        if (next[slotIdx] === null) {
          next[slotIdx] = draggedLetter;
        }
        return next;
      });
      setDraggedLetter(null);
    },
    [checked, draggedLetter]
  );

  const handleCheck = () => {
    const answer = placed.map((l) => l?.char ?? "").join("");
    const correct = answer.toLowerCase() === step.word.toLowerCase();
    setIsCorrect(correct);
    setChecked(true);
    setTimeout(() => onAnswer(correct), 1200);
  };

  return (
    <div className="flex flex-col items-center gap-6 w-full max-w-md mx-auto">
      {/* Hint */}
      <div className="text-center space-y-3">
        {step.image && (
          <img
            src={step.image}
            alt={step.hint}
            className="w-24 h-24 object-cover rounded-xl mx-auto border border-border"
          />
        )}
        <p className="text-lg font-semibold text-text">{step.hint}</p>
        <p className="text-sm text-text-secondary">Собери слово из букв</p>
      </div>

      {/* Slots */}
      <div className="flex gap-2 justify-center flex-wrap">
        {placed.map((letter, idx) => (
          <motion.button
            key={`slot-${idx}`}
            layout
            onClick={() => letter && removeLetter(idx)}
            onDragOver={(e) => {
              e.preventDefault();
              (e.currentTarget as HTMLElement).classList.add("border-primary/60");
            }}
            onDragLeave={(e) => {
              (e.currentTarget as HTMLElement).classList.remove("border-primary/60");
            }}
            onDrop={(e) => {
              e.preventDefault();
              (e.currentTarget as HTMLElement).classList.remove("border-primary/60");
              handleDropOnSlot(idx);
            }}
            className={`w-11 h-12 rounded-xl border-2 text-lg font-bold flex items-center justify-center transition-all cursor-pointer ${
              checked
                ? isCorrect
                  ? "border-success/60 bg-success/10 text-success"
                  : "border-red-500/60 bg-red-500/10 text-red-400"
                : letter
                ? "border-primary/50 bg-primary/10 text-primary"
                : "border-border border-dashed bg-surface"
            }`}
            disabled={checked}
            whileTap={!checked && letter ? { scale: 0.9 } : {}}
          >
            <AnimatePresence mode="wait">
              {letter && (
                <motion.span
                  key={letter.id}
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: 10 }}
                  transition={{ duration: 0.15 }}
                >
                  {letter.char}
                </motion.span>
              )}
            </AnimatePresence>
          </motion.button>
        ))}
      </div>

      {/* Correct answer shown on wrong */}
      <AnimatePresence>
        {checked && !isCorrect && (
          <motion.p
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className="text-sm text-text-secondary"
          >
            Правильный ответ:{" "}
            <span className="text-success font-semibold">{step.word}</span>
          </motion.p>
        )}
      </AnimatePresence>

      {/* Available letters */}
      <div className="flex gap-2 justify-center flex-wrap min-h-[48px]">
        <AnimatePresence>
          {available.map((letter) => (
            <motion.button
              key={`avail-${letter.id}`}
              layout
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.8 }}
              transition={{ duration: 0.15 }}
              onClick={() => placeLetter(letter)}
              draggable={!checked}
              onDragStart={() => setDraggedLetter(letter)}
              onDragEnd={() => setDraggedLetter(null)}
              whileTap={!checked ? { scale: 0.9 } : {}}
              whileHover={!checked ? { scale: 1.05 } : {}}
              className="w-11 h-12 rounded-xl border border-border bg-surface text-lg font-bold text-text flex items-center justify-center transition-all cursor-pointer hover:border-primary/40 active:bg-primary/10"
              disabled={checked}
            >
              {letter.char}
            </motion.button>
          ))}
        </AnimatePresence>
      </div>

      {/* Check button */}
      <AnimatePresence>
        {allFilled && !checked && (
          <motion.button
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 10 }}
            onClick={handleCheck}
            className="w-full py-3 rounded-xl bg-primary text-white font-semibold text-base transition-all hover:opacity-90 active:scale-[0.98] cursor-pointer"
          >
            Проверить
          </motion.button>
        )}
      </AnimatePresence>
    </div>
  );
}
