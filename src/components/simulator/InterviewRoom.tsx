import { useState, useCallback } from "react";
import { motion } from "framer-motion";
import { Mic, MicOff, Timer, BarChart3 } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { ScoreCard } from "./ScoreCard";
import { TranscriptPanel } from "./TranscriptPanel";
import { WaveformVisualizer } from "@/components/chat/WaveformVisualizer";
import { useVoice } from "@/hooks/useVoice";
import { sendMessage, scoreAnswer } from "@/services/claudeApi";
import { useUserStore } from "@/store/userStore";
import { useTranslation } from "@/hooks/useTranslation";
import { DIRECTIONS } from "@/data/directions";
import { XP_REWARDS } from "@/lib/constants";
import type { ChatMessage } from "@/types/chat";

interface InterviewRoomProps {
  mode: "technical" | "situation" | "voice";
  onEnd: () => void;
}

interface QA {
  question: string;
  answer: string;
  score?: number;
  feedback?: string;
  modelAnswer?: string;
}

export function InterviewRoom({ mode, onEnd }: InterviewRoomProps) {
  const { t, lang } = useTranslation();
  const profile = useUserStore((s) => s.profile);
  const addXP = useUserStore((s) => s.addXP);
  const direction = profile?.direction ?? "frontend";
  const dirConfig = DIRECTIONS[direction];

  const [questionIndex, setQuestionIndex] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [qas, setQas] = useState<QA[]>([]);
  const [isGenerating, setIsGenerating] = useState(false);
  const [showScore, setShowScore] = useState(false);
  const [lastScore, setLastScore] = useState<{
    score: number;
    feedback: string;
    modelAnswer: string;
  } | null>(null);
  const [completed, setCompleted] = useState(false);
  const [transcript, setTranscript] = useState<
    Array<{ role: "interviewer" | "candidate"; text: string }>
  >([]);

  const voice = useVoice();
  const isVoiceMode = mode === "voice";
  const totalQuestions = 5;

  const generateQuestion = useCallback(async () => {
    setIsGenerating(true);
    setShowScore(false);
    setLastScore(null);
    setAnswer("");

    const modeLabel =
      mode === "technical"
        ? "technical interview"
        : mode === "situation"
        ? "situational/role-play"
        : "voice-based interview";
    const pastQuestions = qas.map((q) => q.question).join("\n");
    const langInstruction = lang === "ru" ? " IMPORTANT: Ask the question in Russian." : "";
    const prompt = `You are conducting a ${modeLabel} for a ${dirConfig.name} position. Ask question ${questionIndex + 1} of ${totalQuestions}. ${pastQuestions ? `Previous questions (don't repeat):\n${pastQuestions}\n\n` : ""}Difficulty: ${questionIndex < 2 ? "easy" : questionIndex < 4 ? "medium" : "hard"}. Ask ONLY the question, nothing else.${langInstruction}`;

    const messages: ChatMessage[] = [
      {
        id: "q",
        role: "user",
        content: "Ask the next interview question.",
        timestamp: Date.now(),
      },
    ];

    try {
      const question = await sendMessage(prompt, messages);
      setCurrentQuestion(question);
      setTranscript((t) => [...t, { role: "interviewer", text: question }]);
      if (isVoiceMode) {
        await voice.speak(question);
      }
    } catch {
      setCurrentQuestion(lang === "ru" ? "Расскажите о вашем опыте в этой области." : "Tell me about your experience in this field.");
    }
    setIsGenerating(false);
  }, [questionIndex, qas, direction, mode, voice, isVoiceMode, dirConfig.name]);

  const submitAnswer = useCallback(async () => {
    if (!answer.trim()) return;

    setTranscript((t) => [...t, { role: "candidate", text: answer }]);
    setIsGenerating(true);

    try {
      const result = await scoreAnswer(
        currentQuestion,
        answer,
        dirConfig.name
      );
      setLastScore(result);
      setShowScore(true);
      setQas((prev) => [
        ...prev,
        { question: currentQuestion, answer, ...result },
      ]);
    } catch {
      setLastScore({
        score: 5,
        feedback: t("sim.couldNotEvaluate"),
        modelAnswer: "",
      });
      setShowScore(true);
    }

    setIsGenerating(false);
  }, [answer, currentQuestion, dirConfig.name]);

  const handleNext = () => {
    if (questionIndex >= totalQuestions - 1) {
      setCompleted(true);
      addXP(XP_REWARDS.interviewSimulation);
      return;
    }
    setQuestionIndex((i) => i + 1);
    generateQuestion();
  };

  const handleVoiceToggle = () => {
    if (voice.isListening) {
      voice.stopListening();
      if (voice.transcript) {
        setAnswer(voice.transcript);
      }
    } else {
      voice.startListening((text) => {
        setAnswer(text);
      });
    }
  };

  const avgScore =
    qas.length > 0
      ? Math.round(
          (qas.reduce((sum, q) => sum + (q.score ?? 0), 0) / qas.length) * 10
        ) / 10
      : 0;

  if (completed) {
    return (
      <Card className="max-w-2xl mx-auto space-y-6 text-center">
        <motion.div
          animate={{ scale: [0.8, 1.1, 1] }}
          transition={{ duration: 0.5 }}
        >
          <BarChart3 size={48} className="mx-auto text-primary" />
        </motion.div>
        <h2 className="text-2xl font-bold">{t("sim.complete")}</h2>
        <p className="text-4xl font-bold text-primary">{avgScore}/10</p>
        <p className="text-text-secondary text-sm">{t("sim.avgScore")}</p>
        <div className="space-y-3 text-left">
          {qas.map((qa, i) => (
            <div key={i} className="p-3 rounded-xl bg-[#0A0A0A] border border-white/6">
              <p className="text-xs text-text-secondary mb-1">
                Q{i + 1}: {qa.question}
              </p>
              <p className="text-sm">
                {t("sim.scoreLabel")}:{" "}
                <span className="font-bold text-primary">{qa.score}/10</span>
              </p>
            </div>
          ))}
        </div>
        <p className="text-sm text-success">
          +{XP_REWARDS.interviewSimulation} {t("sim.xpEarned")}
        </p>
        <Button onClick={onEnd}>{t("sim.backToMenu")}</Button>
      </Card>
    );
  }

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {/* Interview Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-full bg-surface border-2 border-primary/30 flex items-center justify-center text-xl">
            {dirConfig.mentor.avatar}
          </div>
          <div>
            <p className="text-sm font-semibold">{t("sim.interviewer")}</p>
            <p className="text-xs text-text-secondary">
              {mode === "technical"
                ? t("sim.technical")
                : mode === "situation"
                ? t("sim.situational")
                : t("sim.voice")}{" "}
              {t("sim.interview")}
            </p>
          </div>
          {voice.isSpeaking && <WaveformVisualizer active color="#F97316" />}
        </div>
        <div className="flex items-center gap-2 text-sm text-text-secondary">
          <Timer size={14} />
          {t("sim.questionProgress", { current: String(questionIndex + 1), total: String(totalQuestions) })}
        </div>
      </div>

      {/* Question */}
      {!currentQuestion && !isGenerating && (
        <Card className="text-center py-12">
          <p className="text-text-secondary mb-4">
            {t("sim.readyToBegin")}
          </p>
          <Button onClick={generateQuestion}>{t("sim.startInterview")}</Button>
        </Card>
      )}

      {currentQuestion && (
        <Card glow="#F97316" className="space-y-4">
          <p className="text-sm leading-relaxed">{currentQuestion}</p>
        </Card>
      )}

      {/* Answer area */}
      {currentQuestion && !showScore && (
        <div className="space-y-3">
          {isVoiceMode && (
            <div className="flex items-center gap-3">
              <button
                onClick={handleVoiceToggle}
                className={`w-14 h-14 rounded-full flex items-center justify-center transition-all cursor-pointer ${
                  voice.isListening
                    ? "bg-red-500/20 text-red-400 border-2 border-red-500/50"
                    : "bg-surface border-2 border-border hover:border-primary/50"
                }`}
              >
                {voice.isListening ? (
                  <MicOff size={20} />
                ) : (
                  <Mic size={20} />
                )}
              </button>
              {voice.isListening && (
                <p className="text-sm text-accent italic">
                  {voice.transcript || t("voice.listening")}
                </p>
              )}
            </div>
          )}
          <textarea
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            rows={4}
            placeholder={t("sim.typeAnswer")}
            className="w-full bg-[#0A0A0A] border border-white/6 rounded-xl px-4 py-3 text-sm text-text outline-none focus:border-[#F97316]/40 resize-none placeholder:text-text-secondary/50"
          />
          <Button onClick={submitAnswer} disabled={!answer.trim() || isGenerating}>
            {isGenerating ? t("sim.evaluating") : t("sim.submitAnswer")}
          </Button>
        </div>
      )}

      {/* Score */}
      {showScore && lastScore && (
        <div className="space-y-4">
          <ScoreCard
            score={lastScore.score}
            feedback={lastScore.feedback}
            modelAnswer={lastScore.modelAnswer}
          />
          <Button onClick={handleNext}>
            {questionIndex >= totalQuestions - 1
              ? t("sim.finishInterview")
              : t("sim.nextQuestion")}
          </Button>
        </div>
      )}

      {/* Transcript */}
      {transcript.length > 0 && (
        <Card className="mt-4">
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-3">
            {t("sim.transcript")}
          </p>
          <TranscriptPanel entries={transcript} />
        </Card>
      )}
    </div>
  );
}
