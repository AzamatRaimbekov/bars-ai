import { useState, useRef, useEffect, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Play, Pause, Eye, EyeOff } from "lucide-react";
import type { StepListeningComprehension } from "@/services/courseApi";

interface Props {
  step: StepListeningComprehension;
  onAnswer: (correct: boolean) => void;
}

export function ListeningComprehensionStep({ step, onAnswer }: Props) {
  const audioRef = useRef<HTMLAudioElement>(null);
  const progressRef = useRef<HTMLDivElement>(null);

  // Audio state
  const [playing, setPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [showTranscript, setShowTranscript] = useState(false);

  // Quiz state
  const [questionIdx, setQuestionIdx] = useState(0);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [answered, setAnswered] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  const question = step.questions[questionIdx];
  const total = step.questions.length;

  // Audio controls
  const togglePlay = useCallback(() => {
    const audio = audioRef.current;
    if (!audio) return;
    if (playing) {
      audio.pause();
    } else {
      audio.play();
    }
    setPlaying(!playing);
  }, [playing]);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    const onTimeUpdate = () => setCurrentTime(audio.currentTime);
    const onLoadedMetadata = () => setDuration(audio.duration);
    const onEnded = () => setPlaying(false);

    audio.addEventListener("timeupdate", onTimeUpdate);
    audio.addEventListener("loadedmetadata", onLoadedMetadata);
    audio.addEventListener("ended", onEnded);

    return () => {
      audio.removeEventListener("timeupdate", onTimeUpdate);
      audio.removeEventListener("loadedmetadata", onLoadedMetadata);
      audio.removeEventListener("ended", onEnded);
    };
  }, []);

  const handleSeek = (e: React.MouseEvent<HTMLDivElement>) => {
    const audio = audioRef.current;
    const bar = progressRef.current;
    if (!audio || !bar || !duration) return;
    const rect = bar.getBoundingClientRect();
    const ratio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
    audio.currentTime = ratio * duration;
    setCurrentTime(audio.currentTime);
  };

  const formatTime = (s: number) => {
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60);
    return `${m}:${sec.toString().padStart(2, "0")}`;
  };

  const progress = duration ? (currentTime / duration) * 100 : 0;

  // Quiz logic
  const handleAnswer = () => {
    if (!selectedId || answered) return;
    setAnswered(true);

    const correct = question.options.find((o) => o.id === selectedId)?.correct ?? false;
    const newResults = [...results, correct];
    setResults(newResults);

    setTimeout(() => {
      if (questionIdx < total - 1) {
        setQuestionIdx(questionIdx + 1);
        setSelectedId(null);
        setAnswered(false);
      } else {
        const allCorrect = newResults.every(Boolean);
        onAnswer(allCorrect);
      }
    }, 1200);
  };

  const getOptionClass = (opt: { id: string; correct: boolean }) => {
    const base =
      "w-full text-left px-4 py-3 rounded-xl border text-sm font-medium transition-all cursor-pointer";

    if (!answered) {
      if (selectedId === opt.id) {
        return `${base} border-primary bg-primary/10 text-primary`;
      }
      return `${base} border-border bg-surface text-text hover:border-primary/40`;
    }

    // After answering
    if (opt.correct) {
      return `${base} border-success/60 bg-success/10 text-success`;
    }
    if (selectedId === opt.id && !opt.correct) {
      return `${base} border-red-500/60 bg-red-500/10 text-red-400`;
    }
    return `${base} border-border bg-surface text-text-secondary opacity-50`;
  };

  return (
    <div className="flex flex-col gap-6 w-full max-w-lg mx-auto">
      {/* Audio player */}
      <audio ref={audioRef} src={step.audioUrl} preload="metadata" />

      <div className="bg-surface border border-border rounded-xl p-4 space-y-3">
        <div className="flex items-center gap-3">
          <motion.button
            whileTap={{ scale: 0.9 }}
            onClick={togglePlay}
            className="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center flex-shrink-0 cursor-pointer"
          >
            {playing ? <Pause size={18} /> : <Play size={18} className="ml-0.5" />}
          </motion.button>

          <div className="flex-1 space-y-1">
            <div
              ref={progressRef}
              onClick={handleSeek}
              className="h-2 rounded-full bg-border cursor-pointer relative overflow-hidden"
            >
              <motion.div
                className="absolute inset-y-0 left-0 bg-primary rounded-full"
                style={{ width: `${progress}%` }}
              />
            </div>
            <div className="flex justify-between text-xs text-text-secondary">
              <span>{formatTime(currentTime)}</span>
              <span>{formatTime(duration)}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Transcript toggle */}
      {step.transcript && (
        <div>
          <button
            onClick={() => setShowTranscript(!showTranscript)}
            className="flex items-center gap-2 text-sm text-text-secondary hover:text-text transition-colors cursor-pointer"
          >
            {showTranscript ? <EyeOff size={16} /> : <Eye size={16} />}
            {showTranscript ? "Скрыть текст" : "Показать текст"}
          </button>

          <AnimatePresence>
            {showTranscript && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: "auto" }}
                exit={{ opacity: 0, height: 0 }}
                transition={{ duration: 0.25 }}
                className="overflow-hidden"
              >
                <p className="mt-3 text-sm text-text-secondary leading-relaxed bg-surface border border-border rounded-xl p-4">
                  {step.transcript}
                </p>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      )}

      {/* Question counter */}
      <p className="text-sm text-text-secondary font-medium">
        Вопрос {questionIdx + 1} из {total}
      </p>

      {/* Question */}
      <AnimatePresence mode="wait">
        <motion.div
          key={questionIdx}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -20 }}
          transition={{ duration: 0.25 }}
          className="space-y-4"
        >
          <p className="text-base font-semibold text-text">{question.question}</p>

          <div className="flex flex-col gap-2">
            {question.options.map((opt) => (
              <motion.button
                key={opt.id}
                whileTap={!answered ? { scale: 0.98 } : {}}
                onClick={() => !answered && setSelectedId(opt.id)}
                className={getOptionClass(opt)}
                disabled={answered}
              >
                {opt.text}
              </motion.button>
            ))}
          </div>
        </motion.div>
      </AnimatePresence>

      {/* Submit button */}
      <AnimatePresence>
        {selectedId && !answered && (
          <motion.button
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 10 }}
            onClick={handleAnswer}
            className="w-full py-3 rounded-xl bg-primary text-white font-semibold text-base transition-all hover:opacity-90 active:scale-[0.98] cursor-pointer"
          >
            Ответить
          </motion.button>
        )}
      </AnimatePresence>
    </div>
  );
}
