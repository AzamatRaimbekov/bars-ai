import { useState, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X } from "lucide-react";
import { LessonSlide } from "./LessonSlide";
import { ResultScreen } from "./ResultScreen";
import { FeedbackOverlay } from "./FeedbackOverlay";
import { QuizGame } from "./games/QuizGame";
import { TrueFalseGame } from "./games/TrueFalseGame";
import { MatchPairsGame } from "./games/MatchPairsGame";
import { FlashCardGame } from "./games/FlashCardGame";
import { FillBlanksGame } from "./games/FillBlanksGame";
import { TypeAnswerGame } from "./games/TypeAnswerGame";
import { DragOrderGame } from "./games/DragOrderGame";
import { CodePuzzleGame } from "./games/CodePuzzleGame";
import { buildSession, calculateStars, calculateXP } from "./autoMix";
import { useUserStore } from "@/store/userStore";
import { useAuthStore } from "@/store/authStore";
import type { LessonContentV2, LessonSession, LessonStep } from "@/types/lesson";

interface LessonPlayerProps {
  lesson: LessonContentV2;
  nodeId: string;
  allLessonIdsForNode: string[];
  onClose: () => void;
}

export function LessonPlayer({ lesson, nodeId, allLessonIdsForNode, onClose }: LessonPlayerProps) {
  const [session, setSession] = useState<LessonSession>(() => buildSession(lesson));
  const [feedback, setFeedback] = useState<{ show: boolean; correct: boolean }>({ show: false, correct: false });
  const [done, setDone] = useState(false);
  const [showExitConfirm, setShowExitConfirm] = useState(false);

  const { completeLesson, addXP, completeNode } = useUserStore();
  const fetchUser = useAuthStore((s) => s.fetchUser);

  const currentStep = session.steps[session.currentStepIndex];
  const progress = ((session.currentStepIndex) / session.steps.length) * 100;

  const advanceStep = useCallback(() => {
    const nextIdx = session.currentStepIndex + 1;
    if (nextIdx >= session.steps.length) {
      setDone(true);
      const stars = calculateStars(session.errors);
      const xp = calculateXP(stars);
      completeLesson(lesson.id);
      addXP(xp, stars === 3 ? "perfect_quiz" : "complete_lesson");

      const user = useAuthStore.getState().user;
      if (user) {
        const completedAfter = [...(user.completed_lessons || []), lesson.id];
        const allDone = allLessonIdsForNode.every((id) => completedAfter.includes(id));
        if (allDone) completeNode(nodeId);
      }
      fetchUser();
    } else {
      setSession((s) => ({ ...s, currentStepIndex: nextIdx }));
    }
  }, [session.currentStepIndex, session.steps.length, session.errors, lesson.id, nodeId, allLessonIdsForNode, completeLesson, addXP, completeNode, fetchUser]);

  const handleSlideNext = () => advanceStep();

  const handleGameAnswer = useCallback((correct: boolean) => {
    setFeedback({ show: true, correct });
    if (!correct) {
      setSession((s) => ({ ...s, errors: s.errors + 1 }));
    }
    setTimeout(() => {
      setFeedback({ show: false, correct: false });
      advanceStep();
    }, 1500);
  }, [advanceStep]);

  const handleRetry = () => {
    setSession(buildSession(lesson));
    setDone(false);
  };

  const renderStep = (step: LessonStep) => {
    if (step.type === "slide") {
      return <LessonSlide key={session.currentStepIndex} slide={step.data} onContinue={handleSlideNext} />;
    }
    const props = { question: step.data, onAnswer: handleGameAnswer };
    switch (step.gameType) {
      case "quiz": return <QuizGame key={session.currentStepIndex} {...props} />;
      case "true_false": return <TrueFalseGame key={session.currentStepIndex} {...props} />;
      case "match": return <MatchPairsGame key={session.currentStepIndex} {...props} />;
      case "flash_cards": return <FlashCardGame key={session.currentStepIndex} {...props} />;
      case "fill_blanks": return <FillBlanksGame key={session.currentStepIndex} {...props} />;
      case "type_answer": return <TypeAnswerGame key={session.currentStepIndex} {...props} />;
      case "drag_order": return <DragOrderGame key={session.currentStepIndex} {...props} />;
      case "code_puzzle": return <CodePuzzleGame key={session.currentStepIndex} {...props} />;
      default: return null;
    }
  };

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="fixed inset-0 z-50 bg-bg flex flex-col">
      {/* Header */}
      <div className="flex items-center gap-4 px-6 py-4">
        <button onClick={() => setShowExitConfirm(true)} className="w-8 h-8 rounded-full flex items-center justify-center hover:bg-surface transition-colors cursor-pointer">
          <X size={20} className="text-text-secondary" />
        </button>
        <div className="flex-1 h-3 bg-surface rounded-full overflow-hidden">
          <motion.div className="h-full rounded-full bg-primary" animate={{ width: `${done ? 100 : progress}%` }} transition={{ duration: 0.4, ease: "easeOut" }} />
        </div>
        <span className="text-xs text-text-secondary min-w-[40px] text-right">{session.currentStepIndex + 1}/{session.steps.length}</span>
      </div>

      {/* Content */}
      <div className="flex-1 flex items-center justify-center px-6 overflow-y-auto">
        <div className="w-full max-w-xl">
          {done ? (
            <ResultScreen errors={session.errors} onBackToMap={onClose} onRetry={handleRetry} />
          ) : (
            <AnimatePresence mode="wait">
              {currentStep && renderStep(currentStep)}
            </AnimatePresence>
          )}
        </div>
      </div>

      <FeedbackOverlay show={feedback.show} correct={feedback.correct} />

      {/* Exit confirmation */}
      <AnimatePresence>
        {showExitConfirm && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-[60] bg-black/60 flex items-center justify-center p-6" onClick={() => setShowExitConfirm(false)}>
            <motion.div initial={{ scale: 0.9, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} exit={{ scale: 0.9, opacity: 0 }}
              onClick={(e) => e.stopPropagation()} className="bg-surface border border-border rounded-2xl p-6 max-w-sm w-full text-center space-y-4">
              <h3 className="text-lg font-bold">Exit lesson?</h3>
              <p className="text-sm text-text-secondary">Your progress will be lost.</p>
              <div className="flex gap-3">
                <button onClick={() => setShowExitConfirm(false)} className="flex-1 py-2.5 rounded-xl border border-border text-sm font-medium cursor-pointer hover:bg-bg transition-all">Stay</button>
                <button onClick={onClose} className="flex-1 py-2.5 rounded-xl bg-red-500/15 border border-red-500/30 text-red-400 text-sm font-medium cursor-pointer hover:bg-red-500/25 transition-all">Exit</button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
