import { useState, useRef, useCallback, useMemo, useEffect } from "react";
import { useParams } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { Star, Play, ArrowUpCircle, RotateCcw, Trophy, Skull } from "lucide-react";
import { courseApi } from "@/services/courseApi";
import type { LessonStep } from "@/services/courseApi";
import type { GameState, TowerKind, TDQuestion } from "./types";
import { COINS_PER_CORRECT, QUESTION_TIME, TOWER_CONFIG, UPGRADE_COSTS } from "./config";
import { createInitialState, generateWaves, buildSpawnQueue, placeTower, upgradeTower, canBuyTower, canUpgradeTower } from "./engine";
import { extractQuestions, splitIntoWaves } from "./questions";
import TDCanvas from "./TDCanvas";

interface Props {
  allSteps: LessonStep[];
  onAnswer: (correct: boolean) => void;
}

export default function TowerDefenseStep({ allSteps, onAnswer }: Props) {
  const { id: courseId } = useParams<{ id: string }>();

  // Load ALL course questions from ALL lessons
  const [allCourseQuestions, setAllCourseQuestions] = useState<TDQuestion[]>([]);
  const [loadingQuestions, setLoadingQuestions] = useState(true);

  useEffect(() => {
    if (!courseId) {
      setAllCourseQuestions(extractQuestions(allSteps));
      setLoadingQuestions(false);
      return;
    }

    // Single API call to get all steps from entire course
    courseApi.getAllSteps(courseId).then((data) => {
      const q = extractQuestions(data.steps);
      setAllCourseQuestions(q.length > 0 ? q : extractQuestions(allSteps));
      setLoadingQuestions(false);
    }).catch(() => {
      setAllCourseQuestions(extractQuestions(allSteps));
      setLoadingQuestions(false);
    });
  }, [courseId, allSteps]);

  const questionWaves = useMemo(() => splitIntoWaves(allCourseQuestions), [allCourseQuestions]);
  const totalWaves = questionWaves.length;
  const waveConfigs = useMemo(() => generateWaves(totalWaves), [totalWaves]);

  const [state, setState] = useState<GameState | null>(null);
  const [currentWave, setCurrentWave] = useState(0);

  // Initialize game state when questions are loaded
  useEffect(() => {
    if (!loadingQuestions && totalWaves > 0) {
      setState(createInitialState(totalWaves));
    }
  }, [loadingQuestions, totalWaves]);

  // Question modal state
  const [showQuestionModal, setShowQuestionModal] = useState(false);
  const [qIndex, setQIndex] = useState(0);
  const [timeLeft, setTimeLeft] = useState(QUESTION_TIME);
  const [typedAnswer, setTypedAnswer] = useState("");
  const [coinAnim, setCoinAnim] = useState(false);
  const [answered, setAnswered] = useState<"correct" | "wrong" | null>(null);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const currentQuestions = questionWaves[currentWave] ?? [];
  const currentQ: TDQuestion | undefined = currentQuestions[qIndex];

  // ── Timer ──────────────────────────────────────────────────

  const clearTimer = useCallback(() => {
    if (timerRef.current) { clearInterval(timerRef.current); timerRef.current = null; }
  }, []);

  useEffect(() => {
    if (!showQuestionModal) { clearTimer(); return; }
    setTimeLeft(QUESTION_TIME);
    clearTimer();
    timerRef.current = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) { advanceQuestion(false); return QUESTION_TIME; }
        return prev - 1;
      });
    }, 1000);
    return clearTimer;
  }, [showQuestionModal, qIndex]);

  // ── Question logic ─────────────────────────────────────────

  const advanceQuestion = useCallback((correct: boolean) => {
    setAnswered(correct ? "correct" : "wrong");
    if (correct) {
      setState((s) => s ? { ...s, coins: s.coins + COINS_PER_CORRECT } : s);
      setCoinAnim(true);
      setTimeout(() => setCoinAnim(false), 700);
    }

    setTimeout(() => {
      setAnswered(null);
      const nextIdx = qIndex + 1;
      if (nextIdx >= currentQuestions.length) {
        clearTimer();
        setShowQuestionModal(false);
        setQIndex(0);
        setState((s) => s ? { ...s, phase: "build", selectedSlot: null, selectedTower: null } : s);
      } else {
        setQIndex(nextIdx);
        setTimeLeft(QUESTION_TIME);
        setTypedAnswer("");
      }
    }, 600);
  }, [qIndex, currentQuestions.length, clearTimer]);

  const handleQuizAnswer = useCallback((optionId: string) => {
    if (!currentQ || currentQ.type !== "quiz" || answered) return;
    const opt = currentQ.options?.find((o) => o.id === optionId);
    advanceQuestion(!!opt?.correct);
  }, [currentQ, advanceQuestion, answered]);

  const handleTrueFalse = useCallback((answer: boolean) => {
    if (!currentQ || currentQ.type !== "true-false" || answered) return;
    advanceQuestion(answer === currentQ.correct);
  }, [currentQ, advanceQuestion, answered]);

  const handleTypeAnswer = useCallback(() => {
    if (!currentQ || currentQ.type !== "type-answer" || answered) return;
    const trimmed = typedAnswer.trim().toLowerCase();
    const accepted = currentQ.acceptedAnswers ?? [];
    advanceQuestion(accepted.some((a) => a.trim().toLowerCase() === trimmed));
    setTypedAnswer("");
  }, [currentQ, typedAnswer, advanceQuestion, answered]);

  // ── Build phase ────────────────────────────────────────────

  const handleSlotTap = useCallback((slotIndex: number) => {
    setState((s) => s ? { ...s, selectedSlot: slotIndex, selectedTower: null } : s);
  }, []);

  const handleTowerTap = useCallback((towerId: string) => {
    setState((s) => s ? { ...s, selectedTower: towerId, selectedSlot: null } : s);
  }, []);

  const handleBuyTower = useCallback((kind: TowerKind) => {
    setState((s) => {
      if (!s || s.selectedSlot === null) return s;
      return { ...placeTower(s, s.selectedSlot, kind), selectedSlot: null };
    });
  }, []);

  const handleUpgrade = useCallback(() => {
    setState((s) => {
      if (!s || !s.selectedTower) return s;
      return { ...upgradeTower(s, s.selectedTower), selectedTower: null };
    });
  }, []);

  const handleStartWave = useCallback(() => {
    const waveCfg = waveConfigs[currentWave];
    if (!waveCfg) return;
    const queue = buildSpawnQueue(waveCfg);
    setState((s) => s ? {
      ...s,
      phase: "battle",
      spawnQueue: queue,
      spawnTimer: 0,
      enemies: [],
      projectiles: [],
      waveDone: false,
      selectedSlot: null,
      selectedTower: null,
    } : s);
  }, [currentWave, waveConfigs]);

  // ── Battle callbacks ───────────────────────────────────────

  const handleStateChange = useCallback((next: GameState) => {
    setState(next);

    if (next.lives <= 0) {
      setState((s) => s ? { ...s, phase: "result" } : s);
      return;
    }

    if (next.waveDone) {
      const nextWaveIdx = currentWave + 1;
      if (nextWaveIdx >= totalWaves) {
        setState((s) => s ? { ...s, phase: "result" } : s);
      } else {
        setCurrentWave(nextWaveIdx);
        setQIndex(0);
        setTypedAnswer("");
        setAnswered(null);
        setState((s) => s ? { ...s, wave: nextWaveIdx, waveDone: false, phase: "build" } : s);
        setTimeout(() => setShowQuestionModal(true), 800);
      }
    }
  }, [currentWave, totalWaves]);

  // ── Retry ──────────────────────────────────────────────────

  const handleRetry = useCallback(() => {
    clearTimer();
    setState(createInitialState(totalWaves));
    setCurrentWave(0);
    setQIndex(0);
    setTypedAnswer("");
    setShowQuestionModal(false);
    setAnswered(null);
  }, [totalWaves, clearTimer]);

  // ── Loading state ──────────────────────────────────────────

  if (loadingQuestions || !state) {
    return (
      <div className="flex flex-col items-center justify-center gap-4 py-16">
        <div className="w-10 h-10 border-2 border-primary border-t-transparent rounded-full animate-spin" />
        <p className="text-text-secondary text-sm">Загрузка вопросов курса...</p>
      </div>
    );
  }

  const won = state.phase === "result" && state.lives > 0;
  const stars = state.lives >= 3 ? 3 : state.lives >= 2 ? 2 : state.lives >= 1 ? 1 : 0;
  const selectedTowerObj = state.selectedTower ? state.towers.find((t) => t.id === state.selectedTower) : null;

  // ── RENDER ─────────────────────────────────────────────────

  return (
    <div className="flex flex-col items-center gap-3 w-full max-w-[420px] mx-auto relative">

      {/* ── RESULT ── */}
      {state.phase === "result" && (
        <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="flex flex-col items-center gap-4 py-8">
          {won ? (
            <>
              <Trophy size={48} className="text-yellow-400" />
              <h2 className="text-xl font-bold text-text">Защита пройдена!</h2>
              <div className="flex gap-1">
                {[1, 2, 3].map((s) => (
                  <Star key={s} size={28} className={s <= stars ? "text-yellow-400 fill-yellow-400" : "text-white/20"} />
                ))}
              </div>
            </>
          ) : (
            <>
              <Skull size={48} className="text-red-400" />
              <h2 className="text-xl font-bold text-text">Базу захватили!</h2>
            </>
          )}
          <div className="flex gap-3 mt-4">
            {!won && (
              <button onClick={handleRetry} className="flex items-center gap-2 px-6 py-3 rounded-xl bg-surface border border-border text-text font-semibold cursor-pointer hover:bg-white/10 transition-colors">
                <RotateCcw size={16} /> Ещё раз
              </button>
            )}
            <button onClick={() => onAnswer(won)} className="flex items-center gap-2 px-6 py-3 rounded-xl bg-primary text-white font-semibold cursor-pointer hover:bg-primary/90 transition-colors">
              Продолжить
            </button>
          </div>
        </motion.div>
      )}

      {/* ── BUILD PHASE ── */}
      {state.phase === "build" && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full space-y-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-sm font-bold text-text">Волна {currentWave + 1}/{totalWaves}</span>
              <span className="flex items-center gap-1 text-yellow-400 font-semibold text-sm">
                <Star className="w-4 h-4 fill-yellow-400" /> {state.coins}
              </span>
              <span className="text-xs text-red-400">{"♥".repeat(state.lives)}</span>
            </div>
            <button onClick={handleStartWave} className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-primary text-white text-sm font-semibold cursor-pointer hover:bg-primary/90 transition-colors">
              <Play size={14} /> Начать волну
            </button>
          </div>

          <TDCanvas state={state} onStateChange={setState} onSlotTap={handleSlotTap} onTowerTap={handleTowerTap} />

          {state.selectedSlot !== null && (
            <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex gap-2 justify-center">
              {(["blaster", "zapper", "cannon"] as TowerKind[]).map((kind) => {
                const cfg = TOWER_CONFIG[kind];
                const affordable = canBuyTower(state, kind);
                return (
                  <button key={kind} onClick={() => handleBuyTower(kind)} disabled={!affordable}
                    className={`flex flex-col items-center gap-1 px-4 py-3 rounded-xl border text-xs font-medium transition-colors cursor-pointer disabled:opacity-30 disabled:cursor-default ${affordable ? "border-border bg-surface hover:border-white/30" : "border-border/50 bg-surface/50"}`}>
                    <span className="text-xl">{cfg.emoji}</span>
                    <span className="text-yellow-400">⭐ {cfg.cost}</span>
                  </button>
                );
              })}
            </motion.div>
          )}

          {selectedTowerObj && selectedTowerObj.level < 3 && (() => {
            const cost = UPGRADE_COSTS[(selectedTowerObj.level + 1) as 2 | 3];
            const affordable = canUpgradeTower(state, selectedTowerObj.id);
            return (
              <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex justify-center">
                <button onClick={handleUpgrade} disabled={!affordable}
                  className={`flex items-center gap-2 px-4 py-2.5 rounded-xl border text-sm font-medium cursor-pointer transition-colors disabled:opacity-30 disabled:cursor-default ${affordable ? "border-primary/50 bg-primary/10 text-primary" : "border-border bg-surface text-text-secondary"}`}>
                  <ArrowUpCircle size={16} /> Lvl {selectedTowerObj.level + 1} (⭐ {cost})
                </button>
              </motion.div>
            );
          })()}
        </motion.div>
      )}

      {/* ── BATTLE PHASE ── */}
      {state.phase === "battle" && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="w-full">
          <TDCanvas state={state} onStateChange={handleStateChange} onSlotTap={() => {}} onTowerTap={() => {}} />
        </motion.div>
      )}

      {/* ── QUESTION MODAL (between waves) ── */}
      <AnimatePresence>
        {showQuestionModal && currentQ && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
            <motion.div initial={{ scale: 0.9, y: 20 }} animate={{ scale: 1, y: 0 }} exit={{ scale: 0.9, y: 20 }}
              className="w-full max-w-md bg-[#16161e] border border-border rounded-2xl p-6 space-y-4 relative">

              <div className="flex items-center justify-between">
                <h3 className="text-lg font-bold text-text">Заработай монеты!</h3>
                <span className="flex items-center gap-1 text-yellow-400 font-semibold">
                  <Star className="w-4 h-4 fill-yellow-400" /> {state.coins}
                </span>
              </div>

              <AnimatePresence>
                {coinAnim && (
                  <motion.div key="coin" initial={{ opacity: 1, y: 0 }} animate={{ opacity: 0, y: -40 }} exit={{ opacity: 0 }}
                    className="absolute top-4 left-1/2 -translate-x-1/2 text-yellow-400 font-bold text-lg pointer-events-none">
                    +{COINS_PER_CORRECT} ⭐
                  </motion.div>
                )}
              </AnimatePresence>

              <div className="h-1.5 bg-white/5 rounded-full overflow-hidden">
                <motion.div className="h-full bg-primary rounded-full" animate={{ width: `${(timeLeft / QUESTION_TIME) * 100}%` }} transition={{ duration: 0.3 }} />
              </div>

              <p className="text-text-secondary text-xs text-center">
                Вопрос {qIndex + 1}/{currentQuestions.length} · {timeLeft}с
              </p>

              <div className="space-y-3">
                <p className="text-text font-medium text-center">{currentQ.question}</p>

                {currentQ.type === "quiz" && currentQ.options && (
                  <div className="flex flex-col gap-2">
                    {currentQ.options.map((opt) => (
                      <button key={opt.id} onClick={() => handleQuizAnswer(opt.id)} disabled={!!answered}
                        className={`w-full py-3 px-4 rounded-xl border text-left text-sm transition-colors cursor-pointer disabled:cursor-default ${
                          answered && opt.correct ? "border-green-500 bg-green-500/10 text-green-400" :
                          answered && !opt.correct ? "border-white/5 bg-white/2 text-text-secondary" :
                          "border-border bg-white/5 text-text hover:bg-primary/10 hover:border-primary/50"
                        }`}>
                        {opt.text}
                      </button>
                    ))}
                  </div>
                )}

                {currentQ.type === "true-false" && (
                  <div className="flex gap-3 justify-center">
                    <button onClick={() => handleTrueFalse(true)} disabled={!!answered}
                      className={`flex-1 py-3 rounded-xl border font-semibold transition-colors cursor-pointer disabled:cursor-default ${
                        answered === "correct" && currentQ.correct === true ? "border-green-500 bg-green-500/20 text-green-400" :
                        answered === "wrong" && currentQ.correct !== true ? "border-red-500 bg-red-500/20 text-red-400" :
                        "border-green-600/30 bg-green-600/10 text-green-400 hover:bg-green-600/20"
                      }`}>Верно</button>
                    <button onClick={() => handleTrueFalse(false)} disabled={!!answered}
                      className={`flex-1 py-3 rounded-xl border font-semibold transition-colors cursor-pointer disabled:cursor-default ${
                        answered === "correct" && currentQ.correct === false ? "border-green-500 bg-green-500/20 text-green-400" :
                        answered === "wrong" && currentQ.correct !== false ? "border-red-500 bg-red-500/20 text-red-400" :
                        "border-red-600/30 bg-red-600/10 text-red-400 hover:bg-red-600/20"
                      }`}>Неверно</button>
                  </div>
                )}

                {currentQ.type === "type-answer" && (
                  <div className="flex gap-2">
                    <input type="text" value={typedAnswer} onChange={(e) => setTypedAnswer(e.target.value)}
                      onKeyDown={(e) => e.key === "Enter" && handleTypeAnswer()} disabled={!!answered}
                      placeholder="Введите ответ..."
                      className="flex-1 py-2 px-4 bg-white/5 border border-border rounded-xl text-text placeholder:text-text-secondary/50 outline-none focus:border-primary transition-colors" />
                    <button onClick={handleTypeAnswer} disabled={!!answered}
                      className="py-2 px-5 bg-primary rounded-xl text-white font-semibold cursor-pointer hover:opacity-90 disabled:opacity-50">
                      OK
                    </button>
                  </div>
                )}
              </div>

              <AnimatePresence>
                {answered && (
                  <motion.div initial={{ opacity: 0, y: 5 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}
                    className={`text-center text-sm font-semibold ${answered === "correct" ? "text-green-400" : "text-red-400"}`}>
                    {answered === "correct" ? `Правильно! +${COINS_PER_CORRECT} ⭐` : "Неверно!"}
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
