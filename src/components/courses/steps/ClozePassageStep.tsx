import { useState, useCallback, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import type { StepClozePassage } from "@/services/courseApi";

interface Props {
  step: StepClozePassage;
  onAnswer: (correct: boolean) => void;
}

export default function ClozePassageStep({ step, onAnswer }: Props) {
  // Build an index of only blank segments
  const blankIndices = useMemo(() => {
    const indices: number[] = [];
    step.segments.forEach((seg, i) => {
      if (seg.type === "blank") indices.push(i);
    });
    return indices;
  }, [step.segments]);

  const [answers, setAnswers] = useState<Record<number, string>>(() => {
    const init: Record<number, string> = {};
    blankIndices.forEach((i) => (init[i] = ""));
    return init;
  });

  const [checked, setChecked] = useState(false);
  const [results, setResults] = useState<Record<number, boolean>>({});

  const allFilled = useMemo(
    () => blankIndices.every((i) => answers[i].trim() !== ""),
    [answers, blankIndices],
  );

  const handleChange = useCallback((segIndex: number, value: string) => {
    setAnswers((prev) => ({ ...prev, [segIndex]: value }));
  }, []);

  const handleCheck = useCallback(() => {
    const res: Record<number, boolean> = {};
    let allCorrect = true;

    blankIndices.forEach((i) => {
      const seg = step.segments[i];
      if (seg.type === "blank") {
        const correct =
          answers[i].trim().toLowerCase() === seg.answer.trim().toLowerCase();
        res[i] = correct;
        if (!correct) allCorrect = false;
      }
    });

    setResults(res);
    setChecked(true);

    setTimeout(() => {
      onAnswer(allCorrect);
    }, 1500);
  }, [answers, blankIndices, step.segments, onAnswer]);

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35 }}
      className="flex flex-col gap-5"
    >
      {/* Instruction */}
      <p className="text-text-secondary text-sm font-medium leading-relaxed">
        {step.instruction}
      </p>

      {/* Passage with inline blanks */}
      <div className="bg-surface rounded-xl border border-border p-5 leading-[2.2] text-text text-[15px]">
        {step.segments.map((seg, i) => {
          if (seg.type === "text") {
            return <span key={i}>{seg.value}</span>;
          }

          // Blank segment
          const isChecked = checked;
          const isCorrect = results[i];

          // Border/bg color based on result
          let borderClass = "border-border";
          let bgClass = "bg-white/5";
          if (isChecked) {
            borderClass = isCorrect
              ? "border-emerald-500"
              : "border-red-500";
            bgClass = isCorrect ? "bg-emerald-500/10" : "bg-red-500/10";
          }

          const baseClasses = `inline-block mx-1 align-baseline rounded-lg border text-sm transition-colors duration-300 ${borderClass} ${bgClass}`;

          if (seg.options && seg.options.length > 0) {
            // Dropdown select
            return (
              <span key={i} className="inline-block align-baseline mx-1">
                <select
                  value={answers[i]}
                  onChange={(e) => handleChange(i, e.target.value)}
                  disabled={checked}
                  className={`${baseClasses} px-2 py-1 text-text bg-transparent outline-none cursor-pointer appearance-none pr-6`}
                  style={{
                    backgroundImage: checked
                      ? "none"
                      : `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%239ca3af' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E")`,
                    backgroundRepeat: "no-repeat",
                    backgroundPosition: "right 6px center",
                  }}
                >
                  <option value="" disabled className="bg-surface text-text-secondary">
                    ...
                  </option>
                  {seg.options.map((opt) => (
                    <option key={opt} value={opt} className="bg-surface text-text">
                      {opt}
                    </option>
                  ))}
                </select>

                {/* Show correct answer below if wrong */}
                {isChecked && !isCorrect && (
                  <motion.span
                    initial={{ opacity: 0, y: -4 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="block text-xs text-emerald-400 mt-0.5 ml-1"
                  >
                    {seg.answer}
                  </motion.span>
                )}
              </span>
            );
          }

          // Text input
          return (
            <span key={i} className="inline-block align-baseline mx-1">
              <input
                type="text"
                value={answers[i]}
                onChange={(e) => handleChange(i, e.target.value)}
                disabled={checked}
                placeholder="..."
                className={`${baseClasses} px-2 py-1 text-text outline-none placeholder:text-text-secondary/50 w-28`}
              />

              {/* Show correct answer below if wrong */}
              {isChecked && !isCorrect && (
                <motion.span
                  initial={{ opacity: 0, y: -4 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="block text-xs text-emerald-400 mt-0.5 ml-1"
                >
                  {seg.answer}
                </motion.span>
              )}
            </span>
          );
        })}
      </div>

      {/* Check button */}
      <AnimatePresence>
        {allFilled && !checked && (
          <motion.div
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 8 }}
            className="flex justify-center"
          >
            <button
              onClick={handleCheck}
              className="px-6 py-2.5 rounded-xl bg-primary text-white font-semibold text-sm hover:brightness-110 active:scale-[0.97] transition-all"
            >
              Проверить
            </button>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Result summary */}
      <AnimatePresence>
        {checked && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className={`text-center text-sm font-medium py-2 rounded-xl ${
              blankIndices.every((i) => results[i])
                ? "text-emerald-400 bg-emerald-500/10"
                : "text-amber-400 bg-amber-500/10"
            }`}
          >
            {blankIndices.every((i) => results[i])
              ? "Все верно!"
              : `Правильно ${blankIndices.filter((i) => results[i]).length} из ${blankIndices.length}`}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
