import { useState, useRef, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Mic, Square, Play, Loader2, Volume2 } from "lucide-react";
import type { StepPronunciation } from "@/services/courseApi";
import { transcribeAudio } from "@/services/courseApi";

interface Props {
  step: StepPronunciation;
  onAnswer: (correct: boolean) => void;
}

type Phase = "idle" | "recording" | "transcribing" | "result";

function normalize(s: string): string {
  return s
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s]/gu, "")
    .trim();
}

export default function PronunciationStep({ step, onAnswer }: Props) {
  const [phase, setPhase] = useState<Phase>("idle");
  const [recognized, setRecognized] = useState<string | null>(null);
  const [isCorrect, setIsCorrect] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  const playReference = useCallback(() => {
    if (!step.audioUrl) return;
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
    const audio = new Audio(step.audioUrl);
    audioRef.current = audio;
    audio.play().catch(() => {});
  }, [step.audioUrl]);

  const startRecording = useCallback(async () => {
    setError(null);
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream, { mimeType: "audio/webm" });
      chunksRef.current = [];

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) chunksRef.current.push(e.data);
      };

      recorder.onstop = async () => {
        stream.getTracks().forEach((t) => t.stop());
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        setPhase("transcribing");

        try {
          const { text } = await transcribeAudio(blob);
          setRecognized(text);
          const normalizedResult = normalize(text);
          const correct = step.acceptedForms.some(
            (form) => normalize(form) === normalizedResult
          );
          setIsCorrect(correct);
          setPhase("result");
          setTimeout(() => onAnswer(correct), 1500);
        } catch {
          setError("Ошибка распознавания речи");
          setPhase("idle");
          setTimeout(() => onAnswer(false), 1500);
        }
      };

      mediaRecorderRef.current = recorder;
      recorder.start();
      setPhase("recording");
    } catch {
      setError("Нет доступа к микрофону");
      setTimeout(() => onAnswer(false), 1500);
    }
  }, [step.acceptedForms, onAnswer]);

  const stopRecording = useCallback(() => {
    if (mediaRecorderRef.current && mediaRecorderRef.current.state === "recording") {
      mediaRecorderRef.current.stop();
    }
  }, []);

  const handleMicClick = () => {
    if (phase === "idle") {
      startRecording();
    } else if (phase === "recording") {
      stopRecording();
    }
  };

  return (
    <div className="flex flex-col items-center gap-6 w-full max-w-md mx-auto">
      {/* Word display */}
      <div className="text-center space-y-2">
        <p className="text-3xl font-bold text-text">{step.word}</p>
        {step.phonetic && (
          <p className="text-lg text-text-secondary">{step.phonetic}</p>
        )}
      </div>

      {/* Reference audio button */}
      {step.audioUrl && (
        <motion.button
          whileTap={{ scale: 0.95 }}
          onClick={playReference}
          className="flex items-center gap-2 px-4 py-2 rounded-xl border border-border bg-surface text-text-secondary text-sm font-medium transition-all hover:border-primary/40 hover:text-primary cursor-pointer"
        >
          <Volume2 className="w-4 h-4" />
          Прослушать эталон
        </motion.button>
      )}

      {/* Microphone button */}
      <motion.button
        whileTap={{ scale: 0.9 }}
        onClick={handleMicClick}
        disabled={phase === "transcribing" || phase === "result"}
        className={`w-20 h-20 rounded-full flex items-center justify-center transition-all cursor-pointer ${
          phase === "recording"
            ? "bg-red-500 text-white animate-pulse"
            : "bg-primary/20 text-primary"
        } ${
          phase === "transcribing" || phase === "result"
            ? "opacity-50 cursor-not-allowed"
            : ""
        }`}
      >
        {phase === "recording" ? (
          <Square className="w-8 h-8" />
        ) : (
          <Mic className="w-8 h-8" />
        )}
      </motion.button>

      {phase === "idle" && !error && (
        <p className="text-sm text-text-secondary">
          Нажмите на микрофон и произнесите слово
        </p>
      )}

      {/* Transcribing spinner */}
      <AnimatePresence>
        {phase === "transcribing" && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className="flex items-center gap-2 text-text-secondary"
          >
            <Loader2 className="w-5 h-5 animate-spin" />
            <span className="text-sm">Распознаём речь...</span>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Error message */}
      <AnimatePresence>
        {error && (
          <motion.p
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className="text-sm text-red-400 font-medium"
          >
            {error}
          </motion.p>
        )}
      </AnimatePresence>

      {/* Result card */}
      <AnimatePresence>
        {phase === "result" && recognized !== null && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className={`w-full rounded-xl border p-4 text-center space-y-1 ${
              isCorrect
                ? "border-success/60 bg-success/10"
                : "border-red-500/60 bg-red-500/10"
            }`}
          >
            <p className="text-sm text-text-secondary">
              Распознано:{" "}
              <span className="font-semibold text-text">{recognized}</span>
            </p>
            <p
              className={`text-base font-semibold ${
                isCorrect ? "text-success" : "text-red-400"
              }`}
            >
              {isCorrect ? "Правильно!" : "Неправильно"}
            </p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
