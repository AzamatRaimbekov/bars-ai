import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { ArrowLeft, Check, X, Sparkles } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { useUserStore } from "@/store/userStore";
import { LESSONS } from "@/data/lessons";
import { XP_REWARDS } from "@/lib/constants";

export default function Lesson() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { completeLesson, addXP, completeNode } = useUserStore();
  const profile = useUserStore((s) => s.profile);

  const lesson = id ? LESSONS[id] : undefined;
  const [quizAnswers, setQuizAnswers] = useState<Record<number, number>>({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);

  if (!lesson) {
    return (
      <PageWrapper>
        <div className="text-center py-20">
          <p className="text-text-secondary">Lesson content coming soon!</p>
          <Button variant="ghost" className="mt-4" onClick={() => navigate(-1)}>
            <ArrowLeft size={14} /> Go Back
          </Button>
        </div>
      </PageWrapper>
    );
  }

  const handleQuizSubmit = () => {
    setQuizSubmitted(true);
    if (id) {
      completeLesson(id);
      addXP(XP_REWARDS.completeLesson);

      const nodeId = id.split("-").slice(0, 2).join("-");
      if (profile) {
        const allLessonsForNode = Object.keys(LESSONS).filter((k) => k.startsWith(nodeId));
        const completedAll = allLessonsForNode.every(
          (l) => l === id || profile.completedLessons.includes(l)
        );
        if (completedAll) completeNode(nodeId);
      }
    }
  };

  const allCorrect = lesson.quiz?.every((q, i) => quizAnswers[i] === q.correct) ?? true;

  return (
    <PageWrapper>
      <div className="max-w-3xl mx-auto">
        <button
          onClick={() => navigate(-1)}
          className="flex items-center gap-2 text-sm text-text-secondary hover:text-text mb-6 cursor-pointer"
        >
          <ArrowLeft size={14} /> Back
        </button>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
          <h1 className="text-2xl font-bold mb-6">{lesson.title}</h1>

          <div className="prose prose-invert max-w-none mb-8 text-sm leading-relaxed text-text-secondary whitespace-pre-line">
            {lesson.content}
          </div>

          {lesson.codeExamples?.map((ex, i) => (
            <Card key={i} className="mb-6 overflow-hidden">
              <div className="flex items-center gap-2 mb-3">
                <span className="text-xs text-text-secondary uppercase">{ex.language}</span>
              </div>
              <pre className="bg-bg rounded-xl p-4 overflow-x-auto text-sm font-mono">
                <code className="text-accent">{ex.code}</code>
              </pre>
            </Card>
          ))}

          {lesson.quiz && (
            <div className="space-y-4 mt-8">
              <h2 className="text-lg font-bold flex items-center gap-2">
                <Sparkles size={18} className="text-primary" /> Quiz
              </h2>

              {lesson.quiz.map((q, qi) => (
                <Card key={qi} className="space-y-3">
                  <p className="text-sm font-medium">{q.question}</p>
                  <div className="space-y-2">
                    {q.options.map((opt, oi) => {
                      const selected = quizAnswers[qi] === oi;
                      const isCorrect = quizSubmitted && q.correct === oi;
                      const isWrong = quizSubmitted && selected && q.correct !== oi;

                      return (
                        <button
                          key={oi}
                          onClick={() => !quizSubmitted && setQuizAnswers((a) => ({ ...a, [qi]: oi }))}
                          className={`w-full text-left px-4 py-2.5 rounded-xl border text-sm transition-all cursor-pointer ${
                            isCorrect
                              ? "border-success/50 bg-success/10 text-success"
                              : isWrong
                              ? "border-red-500/50 bg-red-500/10 text-red-400"
                              : selected
                              ? "border-primary/50 bg-primary/10 text-primary"
                              : "border-border hover:border-border/80 text-text-secondary"
                          }`}
                          disabled={quizSubmitted}
                        >
                          <span className="flex items-center gap-2">
                            {opt}
                            {isCorrect && <Check size={14} />}
                            {isWrong && <X size={14} />}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </Card>
              ))}

              {!quizSubmitted && (
                <Button
                  onClick={handleQuizSubmit}
                  disabled={Object.keys(quizAnswers).length < (lesson.quiz?.length ?? 0)}
                >
                  Submit Quiz
                </Button>
              )}

              {quizSubmitted && (
                <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }}>
                  <Card glow={allCorrect ? "#00FF94" : "#FFB800"}>
                    <p className="text-sm font-semibold">
                      {allCorrect ? "Perfect score! 🎉" : "Good effort! Review the correct answers above."}
                    </p>
                    <p className="text-xs text-success mt-2">+{XP_REWARDS.completeLesson} XP earned!</p>
                  </Card>
                </motion.div>
              )}
            </div>
          )}
        </motion.div>
      </div>
    </PageWrapper>
  );
}
