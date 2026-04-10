import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Loader2 } from "lucide-react";
import type { StepSentenceTranslation } from "@/services/courseApi";
import { checkTranslation } from "@/services/courseApi";

interface Props {
  step: StepSentenceTranslation;
  onAnswer: (correct: boolean) => void;
}

const langNames: Record<string, string> = {
  ru: "русского",
  en: "английский",
  kz: "казахский",
  de: "немецкий",
  fr: "французский",
};

export function SentenceTranslationStep({ step, onAnswer }: Props) {
  const [input, setInput] = useState("");
  const [checking, setChecking] = useState(false);
  const [result, setResult] = useState<{
    correct: boolean;
    feedback: string;
    suggested?: string;
  } | null>(null);

  const sourceName = langNames[step.sourceLanguage] ?? step.sourceLanguage;
  const targetName = langNames[step.targetLanguage] ?? step.targetLanguage;

  const handleSubmit = async () => {
    if (!input.trim() || checking || result) return;

    const normalized = input.trim().toLowerCase();

    // Fast local match
    const localMatch = step.acceptedAnswers.some(
      (a) => a.trim().toLowerCase() === normalized
    );

    if (localMatch) {
      setResult({ correct: true, feedback: "Отличный перевод!" });
      setTimeout(() => onAnswer(true), 1200);
      return;
    }

    // AI fallback
    if (step.aiCheck) {
      setChecking(true);
      try {
        const res = await checkTranslation({
          sentence: step.sentence,
          user_answer: input.trim(),
          source_language: step.sourceLanguage,
          target_language: step.targetLanguage,
        });
        setResult({
          correct: res.correct,
          feedback: res.feedback,
          suggested: res.correct ? undefined : res.suggested,
        });
        setTimeout(() => onAnswer(res.correct), 1200);
      } catch {
        // On API error, fall back to incorrect with suggestion
        setResult({
          correct: false,
          feedback: "Не удалось проверить перевод",
          suggested: step.acceptedAnswers[0],
        });
        setTimeout(() => onAnswer(false), 1200);
      } finally {
        setChecking(false);
      }
      return;
    }

    // No AI check — wrong
    setResult({
      correct: false,
      feedback: "Неправильный перевод",
      suggested: step.acceptedAnswers[0],
    });
    setTimeout(() => onAnswer(false), 1200);
  };

  return (
    <div className="flex flex-col items-center gap-6 w-full max-w-lg mx-auto">
      {/* Language hint */}
      <p className="text-sm text-text-secondary">
        Переведите с {sourceName} на {targetName}
      </p>

      {/* Sentence */}
      <p className="text-xl font-semibold text-text text-center leading-relaxed">
        {step.sentence}
      </p>

      {/* Textarea */}
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        disabled={!!result || checking}
        placeholder="Введите перевод..."
        rows={3}
        className="w-full rounded-xl border border-border bg-surface text-text p-4 text-base resize-none outline-none focus:border-primary/60 transition-colors placeholder:text-text-secondary/50 disabled:opacity-60"
      />

      {/* Checking spinner */}
      <AnimatePresence>
        {checking && (
          <motion.div
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 8 }}
            className="flex items-center gap-2 text-sm text-text-secondary"
          >
            <Loader2 className="w-4 h-4 animate-spin" />
            Проверяем перевод...
          </motion.div>
        )}
      </AnimatePresence>

      {/* Result card */}
      <AnimatePresence>
        {result && (
          <motion.div
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className={`w-full rounded-xl border-2 p-4 space-y-2 ${
              result.correct
                ? "border-success/60 bg-success/10"
                : "border-red-500/60 bg-red-500/10"
            }`}
          >
            <p
              className={`text-sm font-medium ${
                result.correct ? "text-success" : "text-red-400"
              }`}
            >
              {result.feedback}
            </p>
            {result.suggested && (
              <p className="text-sm text-text-secondary">
                Рекомендуемый ответ:{" "}
                <span className="text-text font-semibold">
                  {result.suggested}
                </span>
              </p>
            )}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Submit button */}
      <AnimatePresence>
        {input.trim() && !result && !checking && (
          <motion.button
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 10 }}
            onClick={handleSubmit}
            className="w-full py-3 rounded-xl bg-primary text-white font-semibold text-base transition-all hover:opacity-90 active:scale-[0.98] cursor-pointer"
          >
            Проверить
          </motion.button>
        )}
      </AnimatePresence>
    </div>
  );
}
