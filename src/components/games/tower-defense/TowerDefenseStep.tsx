import { useState, useRef, useCallback, useMemo, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Star,
  Heart,
  Play,
  ArrowUpCircle,
  RotateCcw,
  Trophy,
  Skull,
} from "lucide-react";
import type { LessonStep } from "@/services/courseApi";
import type { GameState, TowerKind, TDQuestion } from "./types";
import {
  COINS_PER_CORRECT,
  QUESTION_TIME,
  TOWER_CONFIG,
  UPGRADE_COSTS,
} from "./config";
import {
  createInitialState,
  generateWaves,
  buildSpawnQueue,
  placeTower,
  upgradeTower,
  canBuyTower,
  canUpgradeTower,
} from "./engine";
import { extractQuestions, splitIntoWaves } from "./questions";
import TDCanvas from "./TDCanvas";

interface Props {
  allSteps: LessonStep[];
  onAnswer: (correct: boolean) => void;
}

export default function TowerDefenseStep({ allSteps, onAnswer }: Props) {
  /* ── derived data (stable across renders) ─────────────── */
  const allQuestions = useMemo(() => extractQuestions(allSteps), [allSteps]);
  const questionWaves = useMemo(() => splitIntoWaves(allQuestions), [allQuestions]);
  const totalWaves = questionWaves.length;
  const waveConfigs = useMemo(() => generateWaves(totalWaves), [totalWaves]);

  /* ── core state ────────────────────────────────────────── */
  const [state, setState] = useState<GameState>(() => createInitialState(totalWaves));
  const [currentWave, setCurrentWave] = useState(0);
  const [qIndex, setQIndex] = useState(0);
  const [timeLeft, setTimeLeft] = useState(QUESTION_TIME);
  const [coinAnim, setCoinAnim] = useState(false);
  const [typedAnswer, setTypedAnswer] = useState("");
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  /* ── helpers ───────────────────────────────────────────── */
  const currentQuestions = questionWaves[currentWave] ?? [];
  const currentQ: TDQuestion | undefined = currentQuestions[qIndex];

  const clearTimer = useCallback(() => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  }, []);

  /* ── question timer ────────────────────────────────────── */
  useEffect(() => {
    if (state.phase !== "questions") {
      clearTimer();
      return;
    }

    setTimeLeft(QUESTION_TIME);
    clearTimer();

    timerRef.current = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          // Time's up — wrong answer, advance
          advanceQuestion(false);
          return QUESTION_TIME;
        }
        return prev - 1;
      });
    }, 1000);

    return clearTimer;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [state.phase, qIndex, currentWave]);

  /* ── advance to next question or build phase ───────────── */
  const advanceQuestion = useCallback(
    (correct: boolean) => {
      if (correct) {
        setState((s) => ({ ...s, coins: s.coins + COINS_PER_CORRECT }));
        setCoinAnim(true);
        setTimeout(() => setCoinAnim(false), 700);
      }

      const nextIdx = qIndex + 1;
      if (nextIdx >= currentQuestions.length) {
        // All questions in this wave done → build phase
        clearTimer();
        setState((s) => ({ ...s, phase: "build", selectedSlot: null, selectedTower: null }));
      } else {
        setQIndex(nextIdx);
        setTimeLeft(QUESTION_TIME);
        setTypedAnswer("");
      }
    },
    [qIndex, currentQuestions.length, clearTimer],
  );

  /* ── answer handlers ───────────────────────────────────── */
  const handleQuizAnswer = useCallback(
    (optionId: string) => {
      if (!currentQ || currentQ.type !== "quiz") return;
      const option = currentQ.options?.find((o) => o.id === optionId);
      advanceQuestion(!!option?.correct);
    },
    [currentQ, advanceQuestion],
  );

  const handleTrueFalse = useCallback(
    (answer: boolean) => {
      if (!currentQ || currentQ.type !== "true-false") return;
      advanceQuestion(answer === currentQ.correct);
    },
    [currentQ, advanceQuestion],
  );

  const handleTypeAnswer = useCallback(() => {
    if (!currentQ || currentQ.type !== "type-answer") return;
    const trimmed = typedAnswer.trim().toLowerCase();
    const accepted = currentQ.acceptedAnswers ?? [];
    const correct = accepted.some((a) => a.trim().toLowerCase() === trimmed);
    advanceQuestion(correct);
    setTypedAnswer("");
  }, [currentQ, typedAnswer, advanceQuestion]);

  /* ── build phase handlers ──────────────────────────────── */
  const handleSlotTap = useCallback((slotIndex: number) => {
    setState((s) => ({ ...s, selectedSlot: slotIndex, selectedTower: null }));
  }, []);

  const handleTowerTap = useCallback((towerId: string) => {
    setState((s) => ({ ...s, selectedTower: towerId, selectedSlot: null }));
  }, []);

  const handleBuyTower = useCallback(
    (kind: TowerKind) => {
      if (state.selectedSlot === null) return;
      setState((s) => {
        const next = placeTower(s, s.selectedSlot!, kind);
        return { ...next, selectedSlot: null };
      });
    },
    [state.selectedSlot],
  );

  const handleUpgrade = useCallback(() => {
    if (!state.selectedTower) return;
    setState((s) => {
      const next = upgradeTower(s, s.selectedTower!);
      return { ...next, selectedTower: null };
    });
  }, [state.selectedTower]);

  const handleStartWave = useCallback(() => {
    const waveCfg = waveConfigs[currentWave];
    if (!waveCfg) return;
    const queue = buildSpawnQueue(waveCfg);
    setState((s) => ({
      ...s,
      phase: "battle",
      spawnQueue: queue,
      spawnTimer: 0,
      enemies: [],
      projectiles: [],
      waveDone: false,
      selectedSlot: null,
      selectedTower: null,
    }));
  }, [currentWave, waveConfigs]);

  /* ── battle state updates from canvas ──────────────────── */
  const handleStateChange = useCallback(
    (next: GameState) => {
      setState(next);

      if (next.lives <= 0) {
        setState((s) => ({ ...s, phase: "result" }));
        return;
      }

      if (next.waveDone) {
        const nextWaveIdx = currentWave + 1;
        if (nextWaveIdx >= totalWaves) {
          setState((s) => ({ ...s, phase: "result" }));
        } else {
          setCurrentWave(nextWaveIdx);
          setQIndex(0);
          setTypedAnswer("");
          setState((s) => ({
            ...s,
            phase: "questions",
            wave: nextWaveIdx,
            waveDone: false,
          }));
        }
      }
    },
    [currentWave, totalWaves],
  );

  /* ── retry / continue ──────────────────────────────────── */
  const handleRetry = useCallback(() => {
    clearTimer();
    setState(createInitialState(totalWaves));
    setCurrentWave(0);
    setQIndex(0);
    setTypedAnswer("");
  }, [totalWaves, clearTimer]);

  const won = state.lives > 0;
  const stars = state.lives >= 3 ? 3 : state.lives >= 2 ? 2 : state.lives >= 1 ? 1 : 0;

  const selectedTowerObj = state.selectedTower
    ? state.towers.find((t) => t.id === state.selectedTower)
    : null;

  /* ── RENDER ────────────────────────────────────────────── */

  /* ─── QUESTIONS PHASE ──────────────────────────────────── */
  if (state.phase === "questions") {
    return (
      <div className="flex flex-col items-center gap-4 p-4">
        {/* header */}
        <div className="flex items-center gap-3">
          <h2 className="text-xl font-bold text-text">Заработай монеты!</h2>
          <span className="flex items-center gap-1 text-yellow-400 font-semibold">
            <Star className="w-5 h-5 fill-yellow-400" /> {state.coins}
          </span>
        </div>

        {/* coin animation */}
        <AnimatePresence>
          {coinAnim && (
            <motion.div
              key="coin-anim"
              initial={{ opacity: 1, y: 0 }}
              animate={{ opacity: 0, y: -40 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.6 }}
              className="text-yellow-400 font-bold text-lg absolute"
            >
              +{COINS_PER_CORRECT} ⭐
            </motion.div>
          )}
        </AnimatePresence>

        {/* timer bar */}
        <div className="w-full max-w-md h-2 bg-surface rounded-full overflow-hidden border border-border">
          <motion.div
            className="h-full bg-primary rounded-full"
            initial={{ width: "100%" }}
            animate={{ width: `${(timeLeft / QUESTION_TIME) * 100}%` }}
            transition={{ duration: 0.3 }}
          />
        </div>
        <span className="text-text-secondary text-sm">{timeLeft}s</span>

        {/* wave indicator */}
        <p className="text-text-secondary text-xs">
          Волна {currentWave + 1}/{totalWaves} — Вопрос {qIndex + 1}/{currentQuestions.length}
        </p>

        {/* question card */}
        {currentQ && (
          <div className="w-full max-w-md bg-surface border border-border rounded-xl p-5 flex flex-col gap-4">
            <p className="text-text font-medium text-center">{currentQ.question}</p>

            {/* quiz options */}
            {currentQ.type === "quiz" && currentQ.options && (
              <div className="flex flex-col gap-2">
                {currentQ.options.map((opt) => (
                  <button
                    key={opt.id}
                    onClick={() => handleQuizAnswer(opt.id)}
                    className="w-full py-3 px-4 bg-surface border border-border rounded-xl text-text hover:bg-primary/20 hover:border-primary transition-colors cursor-pointer text-left"
                  >
                    {opt.text}
                  </button>
                ))}
              </div>
            )}

            {/* true-false */}
            {currentQ.type === "true-false" && (
              <div className="flex gap-3 justify-center">
                <button
                  onClick={() => handleTrueFalse(true)}
                  className="flex-1 py-3 bg-green-600/20 border border-green-600/40 rounded-xl text-green-400 font-semibold hover:bg-green-600/30 transition-colors cursor-pointer"
                >
                  Верно
                </button>
                <button
                  onClick={() => handleTrueFalse(false)}
                  className="flex-1 py-3 bg-red-600/20 border border-red-600/40 rounded-xl text-red-400 font-semibold hover:bg-red-600/30 transition-colors cursor-pointer"
                >
                  Неверно
                </button>
              </div>
            )}

            {/* type-answer */}
            {currentQ.type === "type-answer" && (
              <div className="flex gap-2">
                <input
                  type="text"
                  value={typedAnswer}
                  onChange={(e) => setTypedAnswer(e.target.value)}
                  onKeyDown={(e) => e.key === "Enter" && handleTypeAnswer()}
                  placeholder="Введите ответ..."
                  className="flex-1 py-2 px-4 bg-surface border border-border rounded-xl text-text placeholder:text-text-secondary/50 outline-none focus:border-primary transition-colors"
                />
                <button
                  onClick={handleTypeAnswer}
                  className="py-2 px-5 bg-primary rounded-xl text-white font-semibold hover:opacity-90 transition-opacity cursor-pointer"
                >
                  OK
                </button>
              </div>
            )}
          </div>
        )}
      </div>
    );
  }

  /* ─── BUILD PHASE ──────────────────────────────────────── */
  if (state.phase === "build") {
    return (
      <div className="flex flex-col items-center gap-4 p-4">
        <div className="flex items-center gap-3">
          <h2 className="text-xl font-bold text-text">Размести башни</h2>
          <span className="flex items-center gap-1 text-yellow-400 font-semibold">
            <Star className="w-5 h-5 fill-yellow-400" /> {state.coins}
          </span>
          <span className="flex items-center gap-1 text-red-400 font-semibold">
            <Heart className="w-5 h-5 fill-red-400" /> {state.lives}
          </span>
        </div>

        <p className="text-text-secondary text-xs">
          Волна {currentWave + 1}/{totalWaves}
        </p>

        {/* canvas */}
        <TDCanvas
          state={state}
          onSlotTap={handleSlotTap}
          onTowerTap={handleTowerTap}
        />

        {/* tower buy buttons when slot selected */}
        {state.selectedSlot !== null && (
          <div className="flex gap-2">
            {(["blaster", "zapper", "cannon"] as TowerKind[]).map((kind) => {
              const cfg = TOWER_CONFIG[kind];
              const affordable = canBuyTower(state, kind);
              return (
                <button
                  key={kind}
                  onClick={() => handleBuyTower(kind)}
                  disabled={!affordable}
                  className={`flex flex-col items-center py-2 px-4 rounded-xl border transition-colors cursor-pointer ${
                    affordable
                      ? "bg-surface border-border text-text hover:border-primary hover:bg-primary/10"
                      : "bg-surface/50 border-border/50 text-text-secondary/50 cursor-not-allowed"
                  }`}
                >
                  <span className="text-2xl">{cfg.emoji}</span>
                  <span className="text-xs font-semibold">⭐ {cfg.cost}</span>
                </button>
              );
            })}
          </div>
        )}

        {/* upgrade button when tower selected */}
        {selectedTowerObj && (
          <div className="flex gap-2">
            {selectedTowerObj.level < 3 ? (
              <button
                onClick={handleUpgrade}
                disabled={!canUpgradeTower(state, selectedTowerObj.id)}
                className={`flex items-center gap-2 py-2 px-5 rounded-xl border transition-colors cursor-pointer ${
                  canUpgradeTower(state, selectedTowerObj.id)
                    ? "bg-surface border-border text-text hover:border-primary hover:bg-primary/10"
                    : "bg-surface/50 border-border/50 text-text-secondary/50 cursor-not-allowed"
                }`}
              >
                <ArrowUpCircle className="w-5 h-5" />
                <span className="font-semibold text-sm">
                  Улучшить Lvl {selectedTowerObj.level + 1} (⭐{" "}
                  {UPGRADE_COSTS[(selectedTowerObj.level + 1) as 2 | 3]})
                </span>
              </button>
            ) : (
              <span className="text-text-secondary text-sm py-2 px-4">
                Макс. уровень
              </span>
            )}
          </div>
        )}

        {/* start wave button */}
        <button
          onClick={handleStartWave}
          className="flex items-center gap-2 py-3 px-6 bg-primary rounded-xl text-white font-bold hover:opacity-90 transition-opacity cursor-pointer"
        >
          <Play className="w-5 h-5 fill-white" />
          Начать волну
        </button>
      </div>
    );
  }

  /* ─── BATTLE PHASE ─────────────────────────────────────── */
  if (state.phase === "battle") {
    return (
      <div className="flex flex-col items-center gap-4 p-4">
        <div className="flex items-center gap-3">
          <span className="flex items-center gap-1 text-yellow-400 font-semibold">
            <Star className="w-5 h-5 fill-yellow-400" /> {state.coins}
          </span>
          <span className="flex items-center gap-1 text-red-400 font-semibold">
            <Heart className="w-5 h-5 fill-red-400" /> {state.lives}
          </span>
          <span className="text-text-secondary text-sm">
            Волна {currentWave + 1}/{totalWaves}
          </span>
        </div>

        <TDCanvas
          state={state}
          onStateChange={handleStateChange}
        />
      </div>
    );
  }

  /* ─── RESULT PHASE ─────────────────────────────────────── */
  return (
    <div className="flex flex-col items-center gap-6 p-8">
      {won ? (
        <>
          <Trophy className="w-16 h-16 text-yellow-400" />
          <h2 className="text-2xl font-bold text-text">Защита пройдена!</h2>
          <div className="flex gap-2">
            {[1, 2, 3].map((i) => (
              <Star
                key={i}
                className={`w-10 h-10 ${
                  i <= stars
                    ? "text-yellow-400 fill-yellow-400"
                    : "text-text-secondary/30"
                }`}
              />
            ))}
          </div>
        </>
      ) : (
        <>
          <Skull className="w-16 h-16 text-red-400" />
          <h2 className="text-2xl font-bold text-text">Базу захватили!</h2>
          <button
            onClick={handleRetry}
            className="flex items-center gap-2 py-3 px-6 bg-surface border border-border rounded-xl text-text font-semibold hover:bg-primary/10 hover:border-primary transition-colors cursor-pointer"
          >
            <RotateCcw className="w-5 h-5" />
            Ещё раз
          </button>
        </>
      )}

      <button
        onClick={() => onAnswer(won)}
        className="py-3 px-8 bg-primary rounded-xl text-white font-bold hover:opacity-90 transition-opacity cursor-pointer"
      >
        Продолжить
      </button>
    </div>
  );
}
