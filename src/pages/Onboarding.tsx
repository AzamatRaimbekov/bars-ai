import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { Code2, Languages, Headphones, Building2, ArrowRight, Sparkles, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { DIRECTIONS } from "@/data/directions";
import { useUserStore } from "@/store/userStore";
import { assessLevel } from "@/services/claudeApi";
import type { Direction } from "@/types";

const iconMap = { Code2, Languages, Headphones, Building2 };
const directionList = Object.values(DIRECTIONS);

const ASSESSMENT_QUESTIONS: Record<Direction, string[]> = {
  frontend: [
    "What experience do you have with HTML and CSS?",
    "Have you worked with JavaScript before? If so, what have you built?",
    "Do you know what React is? Have you used any frameworks?",
    "Can you explain what responsive design means?",
    "What tools or code editors do you use for development?",
  ],
  english: [
    "How would you describe your current English level?",
    "Do you use English at work or in daily life?",
    "Can you tell me about your favorite hobby in English?",
    "What is the most difficult part of English for you?",
    "What is your goal with learning English?",
  ],
  callcenter: [
    "Have you ever worked in customer service or a call center?",
    "How would you handle an angry customer?",
    "What do you think makes good customer service?",
    "Are you comfortable speaking on the phone for long periods?",
    "Describe a time you resolved a conflict or problem for someone.",
  ],
  cib: [
    "What do you know about Corporate & Investment Banking?",
    "Have you studied finance or economics?",
    "Can you explain what a bond is?",
    "What financial tools or software have you used (e.g., Excel)?",
    "Why are you interested in a career in banking?",
  ],
};

export default function Onboarding() {
  const navigate = useNavigate();
  const { setProfile, completeOnboarding } = useUserStore();
  const [step, setStep] = useState(0);
  const [name, setName] = useState("");
  const [selectedDirection, setSelectedDirection] = useState<Direction | null>(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState<string[]>([]);
  const [currentAnswer, setCurrentAnswer] = useState("");
  const [chatMessages, setChatMessages] = useState<Array<{ role: "bot" | "user"; text: string }>>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [assessmentResult, setAssessmentResult] = useState<"beginner" | "intermediate" | "advanced" | null>(null);

  const handleDirectionSelect = (dir: Direction) => {
    setSelectedDirection(dir);
    setStep(1);
    const questions = ASSESSMENT_QUESTIONS[dir];
    setChatMessages([
      { role: "bot", text: `Hi ${name || "there"}! I'm going to ask you a few questions to understand your current level. Let's start!` },
      { role: "bot", text: questions[0] },
    ]);
  };

  const handleAnswer = async () => {
    if (!currentAnswer.trim() || !selectedDirection) return;

    const newAnswers = [...answers, currentAnswer];
    setAnswers(newAnswers);
    setChatMessages((prev) => [...prev, { role: "user", text: currentAnswer }]);
    setCurrentAnswer("");

    const questions = ASSESSMENT_QUESTIONS[selectedDirection];
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion((q) => q + 1);
      setChatMessages((prev) => [
        ...prev,
        { role: "bot", text: questions[currentQuestion + 1] },
      ]);
    } else {
      setIsLoading(true);
      setChatMessages((prev) => [
        ...prev,
        { role: "bot", text: "Great! Let me analyze your answers..." },
      ]);

      let level: "beginner" | "intermediate" | "advanced" = "beginner";
      try {
        level = await assessLevel(DIRECTIONS[selectedDirection].name, newAnswers);
      } catch {
        // fallback to beginner
      }

      setAssessmentResult(level);
      setIsLoading(false);
      setStep(2);
    }
  };

  const handleFinish = () => {
    if (!selectedDirection || !assessmentResult) return;
    setProfile({
      name: name || "Learner",
      direction: selectedDirection,
      level: "Novice",
      xp: 0,
      streak: 0,
      lastActiveDate: new Date().toISOString().split("T")[0],
      completedNodes: [],
      completedLessons: [],
      earnedBadges: [],
      assessmentLevel: assessmentResult,
      onboardingComplete: true,
    });
    completeOnboarding();
    navigate("/dashboard");
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <div className="flex justify-center gap-2 mb-8">
          {[0, 1, 2].map((i) => (
            <motion.div
              key={i}
              className="h-2 rounded-full"
              animate={{
                width: step === i ? 32 : 8,
                backgroundColor: step >= i ? "#6C63FF" : "#1E1E2E",
              }}
              transition={{ duration: 0.3 }}
            />
          ))}
        </div>

        <AnimatePresence mode="wait">
          {step === 0 && (
            <motion.div
              key="step0"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <div className="text-center mb-8">
                <h1 className="text-3xl font-bold mb-2">
                  Welcome to <span className="text-primary">Path</span>
                  <span className="text-accent">Mind</span>
                </h1>
                <p className="text-text-secondary">Choose your learning path</p>
              </div>

              <Input
                label="What's your name?"
                placeholder="Enter your name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />

              <div className="grid grid-cols-2 gap-4 mt-6">
                {directionList.map((dir) => {
                  const Icon = iconMap[dir.icon as keyof typeof iconMap];
                  return (
                    <Card
                      key={dir.id}
                      hover
                      glow={dir.color}
                      onClick={() => handleDirectionSelect(dir.id)}
                      className="flex flex-col items-center gap-3 text-center cursor-pointer"
                    >
                      <div
                        className="w-12 h-12 rounded-xl flex items-center justify-center"
                        style={{ backgroundColor: `${dir.color}15` }}
                      >
                        <Icon size={24} style={{ color: dir.color }} />
                      </div>
                      <h3 className="font-semibold text-sm">{dir.name}</h3>
                      <p className="text-xs text-text-secondary leading-relaxed">
                        {dir.description}
                      </p>
                    </Card>
                  );
                })}
              </div>
            </motion.div>
          )}

          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-4"
            >
              <div className="text-center mb-4">
                <h2 className="text-xl font-bold">Level Assessment</h2>
                <p className="text-text-secondary text-sm">
                  Question {Math.min(currentQuestion + 1, 5)} of 5
                </p>
              </div>

              <Card className="h-80 overflow-y-auto space-y-3">
                {chatMessages.map((msg, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
                  >
                    <div
                      className={`max-w-[80%] px-4 py-2.5 rounded-2xl text-sm ${
                        msg.role === "user"
                          ? "bg-primary text-white rounded-br-md"
                          : "bg-border/50 text-text rounded-bl-md"
                      }`}
                    >
                      {msg.text}
                    </div>
                  </motion.div>
                ))}
                {isLoading && (
                  <div className="flex justify-start">
                    <div className="bg-border/50 px-4 py-2.5 rounded-2xl rounded-bl-md">
                      <Loader2 className="animate-spin" size={16} />
                    </div>
                  </div>
                )}
              </Card>

              {!isLoading && currentQuestion < 5 && (
                <div className="flex gap-2">
                  <Input
                    placeholder="Type your answer..."
                    value={currentAnswer}
                    onChange={(e) => setCurrentAnswer(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && handleAnswer()}
                  />
                  <Button onClick={handleAnswer} disabled={!currentAnswer.trim()}>
                    <ArrowRight size={18} />
                  </Button>
                </div>
              )}
            </motion.div>
          )}

          {step === 2 && assessmentResult && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="text-center space-y-6"
            >
              <motion.div
                animate={{ scale: [0.8, 1.1, 1] }}
                transition={{ duration: 0.6 }}
              >
                <Sparkles size={48} className="mx-auto text-primary" />
              </motion.div>

              <h2 className="text-2xl font-bold">Your Learning Plan is Ready!</h2>

              <Card glow="#6C63FF" className="text-left space-y-3">
                <p className="text-sm text-text-secondary">Assessment Result</p>
                <p className="text-lg font-semibold capitalize text-primary">
                  {assessmentResult} Level
                </p>
                <p className="text-sm text-text-secondary">
                  Direction: {selectedDirection && DIRECTIONS[selectedDirection].name}
                </p>
                <p className="text-sm text-text-secondary">
                  Your personalized roadmap has been generated with topics tailored to your {assessmentResult} level.
                </p>
              </Card>

              <Button size="lg" onClick={handleFinish}>
                Start Learning <ArrowRight size={18} />
              </Button>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
