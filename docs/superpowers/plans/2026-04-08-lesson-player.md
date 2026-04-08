# Lesson Player (Duolingo-style) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current Lesson page with an immersive Duolingo-style lesson player — theory slides followed by auto-mixed mini-games, with a result screen showing stars and XP.

**Architecture:** LessonPlayer is a full-screen overlay that renders a sequence of steps (slides + games). An autoMix utility builds the session from lesson data. Each game type is an isolated component with a unified callback interface (`onAnswer(correct: boolean)`). ResultScreen handles scoring, XP, and node completion.

**Tech Stack:** React, TypeScript, Framer Motion (animations), Tailwind CSS (styling), existing Zustand stores

---

## File Map

### New files

| File | Responsibility |
|------|---------------|
| `src/types/lesson.ts` | Types: Slide, GameQuestion, LessonStep, LessonSession |
| `src/components/lesson/LessonPlayer.tsx` | Main container: progress bar, step rendering, state machine |
| `src/components/lesson/LessonSlide.tsx` | Theory slide card with title, content, code, image |
| `src/components/lesson/ResultScreen.tsx` | Stars, XP animation, unlock, retry/back buttons |
| `src/components/lesson/FeedbackOverlay.tsx` | Correct/wrong flash banner after each game answer |
| `src/components/lesson/games/QuizGame.tsx` | Multiple choice (4 options) |
| `src/components/lesson/games/FlashCardGame.tsx` | Flip card self-assessment |
| `src/components/lesson/games/MatchPairsGame.tsx` | Click-click pair matching |
| `src/components/lesson/games/FillBlanksGame.tsx` | Text with blanks, select answers |
| `src/components/lesson/games/DragOrderGame.tsx` | Drag-and-drop reorder |
| `src/components/lesson/games/TrueFalseGame.tsx` | True/False statement |
| `src/components/lesson/games/CodePuzzleGame.tsx` | Assemble code blocks in order |
| `src/components/lesson/games/TypeAnswerGame.tsx` | Type text answer |
| `src/components/lesson/autoMix.ts` | Build session: pick slides + random games from pool |
| `src/data/lessons/frontend-v2.ts` | Updated lesson data with slides + questions for first 4 lessons |

### Modified files

| File | Change |
|------|--------|
| `src/pages/Lesson.tsx` | Replace with LessonPlayer integration |
| `src/types/index.ts` | Re-export from lesson.ts |

---

## Task 1: Types & AutoMix Utility

**Files:**
- Create: `src/types/lesson.ts`
- Create: `src/components/lesson/autoMix.ts`

- [ ] **Step 1: Create src/types/lesson.ts**

```typescript
// src/types/lesson.ts

export interface Slide {
  title: { en: string; ru: string };
  content: { en: string; ru: string };
  code?: { language: string; code: string };
  image?: string;
}

export type GameType =
  | "quiz"
  | "match"
  | "fill_blanks"
  | "drag_order"
  | "true_false"
  | "code_puzzle"
  | "type_answer"
  | "flash_cards";

export interface GameQuestion {
  type: GameType;
  question: { en: string; ru: string };
  // quiz
  options?: { en: string; ru: string }[];
  correct?: number;
  // type_answer
  correctText?: { en: string; ru: string };
  // match, flash_cards
  pairs?: { term: { en: string; ru: string }; definition: { en: string; ru: string } }[];
  // drag_order, code_puzzle
  items?: { en: string; ru: string }[];
  // true_false
  statement?: { en: string; ru: string };
  answer?: boolean;
  // fill_blanks
  blanks?: {
    text: { en: string; ru: string };
    options: { en: string; ru: string }[];
    correctIndex: number;
  }[];
}

export interface LessonContentV2 {
  id: string;
  title: { en: string; ru: string };
  slides: Slide[];
  questions: GameQuestion[];
}

export type LessonStep =
  | { type: "slide"; data: Slide }
  | { type: "game"; gameType: GameType; data: GameQuestion };

export interface LessonSession {
  lessonId: string;
  steps: LessonStep[];
  currentStepIndex: number;
  errors: number;
  startedAt: number;
}
```

- [ ] **Step 2: Create src/components/lesson/autoMix.ts**

```typescript
// src/components/lesson/autoMix.ts
import type { LessonContentV2, LessonStep, LessonSession, GameType } from "@/types/lesson";

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

/**
 * Build a lesson session: slides first, then 4-5 auto-mixed games.
 * Avoids two consecutive games of the same type when possible.
 */
export function buildSession(lesson: LessonContentV2): LessonSession {
  const slideSteps: LessonStep[] = lesson.slides.map((s) => ({
    type: "slide",
    data: s,
  }));

  // Shuffle questions and pick 4-5
  const shuffled = shuffle(lesson.questions);
  const count = Math.min(shuffled.length, Math.max(4, Math.min(5, shuffled.length)));

  // Try to avoid consecutive same types
  const picked: typeof shuffled = [];
  const remaining = [...shuffled];

  while (picked.length < count && remaining.length > 0) {
    const lastType = picked.length > 0 ? picked[picked.length - 1].type : null;
    const differentIdx = remaining.findIndex((q) => q.type !== lastType);
    const idx = differentIdx !== -1 ? differentIdx : 0;
    picked.push(remaining.splice(idx, 1)[0]);
  }

  const gameSteps: LessonStep[] = picked.map((q) => ({
    type: "game",
    gameType: q.type,
    data: q,
  }));

  return {
    lessonId: lesson.id,
    steps: [...slideSteps, ...gameSteps],
    currentStepIndex: 0,
    errors: 0,
    startedAt: Date.now(),
  };
}

export function calculateStars(errors: number): number {
  if (errors === 0) return 3;
  if (errors <= 2) return 2;
  return 1;
}

export function calculateXP(stars: number): number {
  const base = 50;
  const bonus = stars === 3 ? 50 : stars === 2 ? 25 : 0;
  return base + bonus;
}
```

- [ ] **Step 3: Commit**

```bash
git add src/types/lesson.ts src/components/lesson/autoMix.ts
git commit -m "feat: add lesson types and autoMix session builder"
```

---

## Task 2: FeedbackOverlay & LessonSlide

**Files:**
- Create: `src/components/lesson/FeedbackOverlay.tsx`
- Create: `src/components/lesson/LessonSlide.tsx`

- [ ] **Step 1: Create FeedbackOverlay.tsx**

```tsx
// src/components/lesson/FeedbackOverlay.tsx
import { motion, AnimatePresence } from "framer-motion";
import { Check, X } from "lucide-react";

interface FeedbackOverlayProps {
  show: boolean;
  correct: boolean;
  message?: string;
}

const POSITIVE = ["Great!", "Perfect!", "Correct!", "Well done!", "Nailed it!"];
const NEGATIVE = ["Not quite", "Try to remember", "Incorrect", "Wrong answer"];

function randomFrom(arr: string[]) {
  return arr[Math.floor(Math.random() * arr.length)];
}

export function FeedbackOverlay({ show, correct, message }: FeedbackOverlayProps) {
  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ y: 100, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: 100, opacity: 0 }}
          transition={{ type: "spring", stiffness: 300, damping: 25 }}
          className={`fixed bottom-0 left-0 right-0 z-50 px-6 py-5 flex items-center gap-4 ${
            correct
              ? "bg-green-500/95 text-white"
              : "bg-red-500/95 text-white"
          }`}
          style={{ backdropFilter: "blur(8px)" }}
        >
          <div
            className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 ${
              correct ? "bg-green-400/30" : "bg-red-400/30"
            }`}
          >
            {correct ? <Check size={22} strokeWidth={3} /> : <X size={22} strokeWidth={3} />}
          </div>
          <div>
            <p className="font-bold text-lg">
              {message || (correct ? randomFrom(POSITIVE) : randomFrom(NEGATIVE))}
            </p>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
```

- [ ] **Step 2: Create LessonSlide.tsx**

```tsx
// src/components/lesson/LessonSlide.tsx
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { Slide } from "@/types/lesson";

interface LessonSlideProps {
  slide: Slide;
  onContinue: () => void;
}

export function LessonSlide({ slide, onContinue }: LessonSlideProps) {
  const { lang } = useTranslation();

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col h-full"
    >
      <div className="flex-1 overflow-y-auto px-1 pb-4">
        <h2 className="text-xl font-bold mb-4">{slide.title[lang]}</h2>

        <div className="text-sm text-text-secondary leading-relaxed whitespace-pre-line mb-6">
          {slide.content[lang]}
        </div>

        {slide.code && (
          <div className="rounded-xl bg-bg border border-border overflow-hidden mb-4">
            <div className="px-4 py-2 border-b border-border text-xs text-text-secondary uppercase">
              {slide.code.language}
            </div>
            <pre className="p-4 overflow-x-auto text-sm font-mono">
              <code className="text-accent">{slide.code.code}</code>
            </pre>
          </div>
        )}

        {slide.image && (
          <img
            src={slide.image}
            alt={slide.title[lang]}
            className="w-full rounded-xl border border-border mb-4"
          />
        )}
      </div>

      <div className="pt-4 border-t border-border">
        <Button className="w-full" onClick={onContinue}>
          Continue <ArrowRight size={16} />
        </Button>
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/components/lesson/FeedbackOverlay.tsx src/components/lesson/LessonSlide.tsx
git commit -m "feat: add FeedbackOverlay and LessonSlide components"
```

---

## Task 3: QuizGame & TrueFalseGame

**Files:**
- Create: `src/components/lesson/games/QuizGame.tsx`
- Create: `src/components/lesson/games/TrueFalseGame.tsx`

- [ ] **Step 1: Create QuizGame.tsx**

```tsx
// src/components/lesson/games/QuizGame.tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface QuizGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

export function QuizGame({ question, onAnswer }: QuizGameProps) {
  const { lang } = useTranslation();
  const [selected, setSelected] = useState<number | null>(null);
  const [answered, setAnswered] = useState(false);

  const handleSelect = (idx: number) => {
    if (answered) return;
    setSelected(idx);
    setAnswered(true);
    const isCorrect = idx === question.correct;
    setTimeout(() => onAnswer(isCorrect), 1200);
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-6"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      <div className="space-y-3">
        {question.options?.map((opt, i) => {
          const isSelected = selected === i;
          const isCorrectOption = question.correct === i;
          const showCorrect = answered && isCorrectOption;
          const showWrong = answered && isSelected && !isCorrectOption;

          return (
            <motion.button
              key={i}
              onClick={() => handleSelect(i)}
              disabled={answered}
              animate={showWrong ? { x: [0, -8, 8, -8, 0] } : {}}
              className={`w-full text-left px-5 py-4 rounded-2xl border-2 text-sm font-medium transition-all cursor-pointer ${
                showCorrect
                  ? "border-green-500 bg-green-500/15 text-green-400"
                  : showWrong
                  ? "border-red-500 bg-red-500/15 text-red-400"
                  : isSelected
                  ? "border-primary bg-primary/10 text-primary"
                  : "border-border hover:border-primary/40 text-text"
              }`}
            >
              <span className="flex items-center gap-3">
                <span
                  className={`w-8 h-8 rounded-full border-2 flex items-center justify-center text-xs font-bold shrink-0 ${
                    showCorrect
                      ? "border-green-500 bg-green-500/20 text-green-400"
                      : showWrong
                      ? "border-red-500 bg-red-500/20 text-red-400"
                      : isSelected
                      ? "border-primary bg-primary/20 text-primary"
                      : "border-border text-text-secondary"
                  }`}
                >
                  {String.fromCharCode(65 + i)}
                </span>
                {opt[lang]}
              </span>
            </motion.button>
          );
        })}
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 2: Create TrueFalseGame.tsx**

```tsx
// src/components/lesson/games/TrueFalseGame.tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { Check, X } from "lucide-react";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface TrueFalseGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

export function TrueFalseGame({ question, onAnswer }: TrueFalseGameProps) {
  const { lang } = useTranslation();
  const [answered, setAnswered] = useState(false);
  const [selected, setSelected] = useState<boolean | null>(null);

  const handleSelect = (value: boolean) => {
    if (answered) return;
    setSelected(value);
    setAnswered(true);
    const isCorrect = value === question.answer;
    setTimeout(() => onAnswer(isCorrect), 1200);
  };

  const correctAnswer = question.answer;

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-6"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      <div className="p-5 rounded-2xl bg-surface border border-border text-center">
        <p className="text-base">{question.statement?.[lang]}</p>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {[true, false].map((val) => {
          const isSelected = selected === val;
          const showCorrect = answered && val === correctAnswer;
          const showWrong = answered && isSelected && val !== correctAnswer;

          return (
            <motion.button
              key={String(val)}
              onClick={() => handleSelect(val)}
              disabled={answered}
              animate={showWrong ? { x: [0, -6, 6, -6, 0] } : {}}
              className={`flex items-center justify-center gap-3 py-5 rounded-2xl border-2 text-lg font-bold cursor-pointer transition-all ${
                showCorrect
                  ? "border-green-500 bg-green-500/15 text-green-400"
                  : showWrong
                  ? "border-red-500 bg-red-500/15 text-red-400"
                  : "border-border hover:border-primary/40 text-text"
              }`}
            >
              {val ? <Check size={24} /> : <X size={24} />}
              {val ? "True" : "False"}
            </motion.button>
          );
        })}
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/components/lesson/games/QuizGame.tsx src/components/lesson/games/TrueFalseGame.tsx
git commit -m "feat: add QuizGame and TrueFalseGame components"
```

---

## Task 4: MatchPairsGame & FlashCardGame

**Files:**
- Create: `src/components/lesson/games/MatchPairsGame.tsx`
- Create: `src/components/lesson/games/FlashCardGame.tsx`

- [ ] **Step 1: Create MatchPairsGame.tsx**

```tsx
// src/components/lesson/games/MatchPairsGame.tsx
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface MatchPairsGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function MatchPairsGame({ question, onAnswer }: MatchPairsGameProps) {
  const { lang } = useTranslation();
  const pairs = question.pairs ?? [];
  const [shuffledDefs, setShuffledDefs] = useState<number[]>([]);
  const [selectedTerm, setSelectedTerm] = useState<number | null>(null);
  const [selectedDef, setSelectedDef] = useState<number | null>(null);
  const [matched, setMatched] = useState<Set<number>>(new Set());
  const [wrong, setWrong] = useState<{ term: number; def: number } | null>(null);
  const [mistakes, setMistakes] = useState(0);

  useEffect(() => {
    setShuffledDefs(shuffle(pairs.map((_, i) => i)));
  }, [pairs]);

  useEffect(() => {
    if (selectedTerm !== null && selectedDef !== null) {
      const actualIdx = shuffledDefs[selectedDef];
      if (selectedTerm === actualIdx) {
        const next = new Set(matched);
        next.add(selectedTerm);
        setMatched(next);
        setSelectedTerm(null);
        setSelectedDef(null);
        if (next.size === pairs.length) {
          setTimeout(() => onAnswer(mistakes === 0), 600);
        }
      } else {
        setMistakes((m) => m + 1);
        setWrong({ term: selectedTerm, def: selectedDef });
        setTimeout(() => {
          setWrong(null);
          setSelectedTerm(null);
          setSelectedDef(null);
        }, 600);
      }
    }
  }, [selectedTerm, selectedDef]);

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-4"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>
      <p className="text-sm text-text-secondary">{matched.size} / {pairs.length} matched</p>

      <div className="grid grid-cols-2 gap-3">
        <div className="space-y-2">
          {pairs.map((p, i) => {
            const isMatched = matched.has(i);
            const isSelected = selectedTerm === i;
            const isWrong2 = wrong?.term === i;
            return (
              <motion.button
                key={`t-${i}`}
                onClick={() => !isMatched && setSelectedTerm(i)}
                animate={isWrong2 ? { x: [0, -5, 5, -5, 0] } : {}}
                disabled={isMatched}
                className={`w-full text-left px-4 py-3 rounded-xl border-2 text-sm transition-all cursor-pointer ${
                  isMatched ? "border-green-500/40 bg-green-500/10 text-green-400 opacity-50"
                  : isWrong2 ? "border-red-500 bg-red-500/10 text-red-400"
                  : isSelected ? "border-primary bg-primary/10 text-primary"
                  : "border-border hover:border-primary/30"
                }`}
              >
                {p.term[lang]}
              </motion.button>
            );
          })}
        </div>
        <div className="space-y-2">
          {shuffledDefs.map((origIdx, dispIdx) => {
            const isMatched = matched.has(origIdx);
            const isSelected = selectedDef === dispIdx;
            const isWrong2 = wrong?.def === dispIdx;
            return (
              <motion.button
                key={`d-${dispIdx}`}
                onClick={() => !isMatched && setSelectedDef(dispIdx)}
                animate={isWrong2 ? { x: [0, 5, -5, 5, 0] } : {}}
                disabled={isMatched}
                className={`w-full text-left px-4 py-3 rounded-xl border-2 text-sm transition-all cursor-pointer ${
                  isMatched ? "border-green-500/40 bg-green-500/10 text-green-400 opacity-50"
                  : isWrong2 ? "border-red-500 bg-red-500/10 text-red-400"
                  : isSelected ? "border-accent bg-accent/10 text-accent"
                  : "border-border hover:border-accent/30"
                }`}
              >
                {pairs[origIdx].definition[lang]}
              </motion.button>
            );
          })}
        </div>
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 2: Create FlashCardGame.tsx**

```tsx
// src/components/lesson/games/FlashCardGame.tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Check, X } from "lucide-react";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface FlashCardGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

export function FlashCardGame({ question, onAnswer }: FlashCardGameProps) {
  const { lang } = useTranslation();
  const pairs = question.pairs ?? [];
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [known, setKnown] = useState(0);

  const card = pairs[index];
  if (!card) return null;

  const handleKnow = () => {
    const newKnown = known + 1;
    setKnown(newKnown);
    advance(newKnown);
  };

  const handleDontKnow = () => {
    advance(known);
  };

  const advance = (knownCount: number) => {
    setFlipped(false);
    if (index >= pairs.length - 1) {
      const ratio = knownCount / pairs.length;
      setTimeout(() => onAnswer(ratio >= 0.6), 300);
    } else {
      setTimeout(() => setIndex((i) => i + 1), 200);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-4"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      <div className="flex items-center justify-between text-xs text-text-secondary">
        <span>{index + 1} / {pairs.length}</span>
        <span>{known} known</span>
      </div>

      <motion.div
        onClick={() => setFlipped(!flipped)}
        className="h-48 rounded-2xl border-2 border-border bg-surface cursor-pointer flex items-center justify-center p-6 select-none"
        whileHover={{ scale: 1.01 }}
        whileTap={{ scale: 0.99 }}
      >
        <AnimatePresence mode="wait">
          <motion.div
            key={flipped ? "back" : "front"}
            initial={{ rotateY: 90, opacity: 0 }}
            animate={{ rotateY: 0, opacity: 1 }}
            exit={{ rotateY: -90, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="text-center"
          >
            {flipped ? (
              <p className="text-sm text-accent leading-relaxed">{card.definition[lang]}</p>
            ) : (
              <p className="text-lg font-semibold">{card.term[lang]}</p>
            )}
          </motion.div>
        </AnimatePresence>
      </motion.div>

      {flipped && (
        <div className="grid grid-cols-2 gap-3">
          <button
            onClick={handleDontKnow}
            className="flex items-center justify-center gap-2 py-3 rounded-xl border-2 border-red-500/30 bg-red-500/10 text-red-400 text-sm font-medium cursor-pointer hover:bg-red-500/20"
          >
            <X size={16} /> Don't know
          </button>
          <button
            onClick={handleKnow}
            className="flex items-center justify-center gap-2 py-3 rounded-xl border-2 border-green-500/30 bg-green-500/10 text-green-400 text-sm font-medium cursor-pointer hover:bg-green-500/20"
          >
            <Check size={16} /> I know this
          </button>
        </div>
      )}

      {!flipped && (
        <p className="text-center text-xs text-text-secondary">Tap card to flip</p>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/components/lesson/games/MatchPairsGame.tsx src/components/lesson/games/FlashCardGame.tsx
git commit -m "feat: add MatchPairsGame and FlashCardGame components"
```

---

## Task 5: FillBlanksGame & TypeAnswerGame

**Files:**
- Create: `src/components/lesson/games/FillBlanksGame.tsx`
- Create: `src/components/lesson/games/TypeAnswerGame.tsx`

- [ ] **Step 1: Create FillBlanksGame.tsx**

```tsx
// src/components/lesson/games/FillBlanksGame.tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface FillBlanksGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

export function FillBlanksGame({ question, onAnswer }: FillBlanksGameProps) {
  const { lang } = useTranslation();
  const blanks = question.blanks ?? [];
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [submitted, setSubmitted] = useState(false);

  const handleSelect = (blankIdx: number, optionIdx: number) => {
    if (submitted) return;
    setAnswers((prev) => ({ ...prev, [blankIdx]: optionIdx }));
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const allCorrect = blanks.every((b, i) => answers[i] === b.correctIndex);
    setTimeout(() => onAnswer(allCorrect), 1200);
  };

  const allFilled = Object.keys(answers).length === blanks.length;

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-6"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      <div className="space-y-6">
        {blanks.map((blank, bi) => (
          <div key={bi} className="space-y-3">
            <p className="text-sm text-text-secondary">{blank.text[lang]}</p>
            <div className="flex flex-wrap gap-2">
              {blank.options.map((opt, oi) => {
                const isSelected = answers[bi] === oi;
                const isCorrect = submitted && oi === blank.correctIndex;
                const isWrong = submitted && isSelected && oi !== blank.correctIndex;

                return (
                  <button
                    key={oi}
                    onClick={() => handleSelect(bi, oi)}
                    disabled={submitted}
                    className={`px-4 py-2 rounded-xl border-2 text-sm font-medium cursor-pointer transition-all ${
                      isCorrect ? "border-green-500 bg-green-500/15 text-green-400"
                      : isWrong ? "border-red-500 bg-red-500/15 text-red-400"
                      : isSelected ? "border-primary bg-primary/10 text-primary"
                      : "border-border hover:border-primary/30 text-text"
                    }`}
                  >
                    {opt[lang]}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </div>

      {!submitted && (
        <Button onClick={handleSubmit} disabled={!allFilled} className="w-full">
          Check Answer
        </Button>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 2: Create TypeAnswerGame.tsx**

```tsx
// src/components/lesson/games/TypeAnswerGame.tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface TypeAnswerGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

function normalize(s: string): string {
  return s.trim().toLowerCase().replace(/\s+/g, " ");
}

export function TypeAnswerGame({ question, onAnswer }: TypeAnswerGameProps) {
  const { lang } = useTranslation();
  const [value, setValue] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleSubmit = () => {
    if (!value.trim()) return;
    setSubmitted(true);
    const correct = normalize(value) === normalize(question.correctText?.[lang] ?? "");
    setIsCorrect(correct);
    setTimeout(() => onAnswer(correct), 1200);
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-6"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      <div className="space-y-4">
        <Input
          placeholder="Type your answer..."
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !submitted && handleSubmit()}
          disabled={submitted}
        />

        {submitted && (
          <motion.div
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            className={`p-4 rounded-xl border-2 text-sm ${
              isCorrect
                ? "border-green-500/40 bg-green-500/10 text-green-400"
                : "border-red-500/40 bg-red-500/10 text-red-400"
            }`}
          >
            {isCorrect ? "Correct!" : `Correct answer: ${question.correctText?.[lang]}`}
          </motion.div>
        )}
      </div>

      {!submitted && (
        <Button onClick={handleSubmit} disabled={!value.trim()} className="w-full">
          Check
        </Button>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/components/lesson/games/FillBlanksGame.tsx src/components/lesson/games/TypeAnswerGame.tsx
git commit -m "feat: add FillBlanksGame and TypeAnswerGame components"
```

---

## Task 6: DragOrderGame & CodePuzzleGame

**Files:**
- Create: `src/components/lesson/games/DragOrderGame.tsx`
- Create: `src/components/lesson/games/CodePuzzleGame.tsx`

- [ ] **Step 1: Create DragOrderGame.tsx**

```tsx
// src/components/lesson/games/DragOrderGame.tsx
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { GripVertical } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface DragOrderGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function DragOrderGame({ question, onAnswer }: DragOrderGameProps) {
  const { lang } = useTranslation();
  const correctOrder = question.items ?? [];
  const [items, setItems] = useState<{ text: string; origIdx: number }[]>([]);
  const [dragIdx, setDragIdx] = useState<number | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  useEffect(() => {
    const indexed = correctOrder.map((item, i) => ({ text: item[lang], origIdx: i }));
    setItems(shuffle(indexed));
  }, [correctOrder, lang]);

  const moveItem = (from: number, to: number) => {
    if (submitted) return;
    const copy = [...items];
    const [moved] = copy.splice(from, 1);
    copy.splice(to, 0, moved);
    setItems(copy);
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const res = items.map((item, i) => item.origIdx === i);
    setResults(res);
    const allCorrect = res.every(Boolean);
    setTimeout(() => onAnswer(allCorrect), 1200);
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-6"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      <div className="space-y-2">
        {items.map((item, i) => (
          <motion.div
            key={item.origIdx}
            layout
            draggable={!submitted}
            onDragStart={() => setDragIdx(i)}
            onDragOver={(e) => { e.preventDefault(); }}
            onDrop={() => {
              if (dragIdx !== null && dragIdx !== i) {
                moveItem(dragIdx, i);
              }
              setDragIdx(null);
            }}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl border-2 text-sm cursor-grab active:cursor-grabbing transition-all ${
              submitted
                ? results[i]
                  ? "border-green-500/40 bg-green-500/10 text-green-400"
                  : "border-red-500/40 bg-red-500/10 text-red-400"
                : dragIdx === i
                ? "border-primary bg-primary/10 opacity-60"
                : "border-border bg-surface hover:border-primary/30"
            }`}
          >
            <GripVertical size={16} className="text-text-secondary shrink-0" />
            <span className="w-6 h-6 rounded-full border border-border flex items-center justify-center text-xs text-text-secondary shrink-0">
              {i + 1}
            </span>
            {item.text}
          </motion.div>
        ))}
      </div>

      {!submitted && (
        <Button onClick={handleSubmit} className="w-full">
          Check Order
        </Button>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 2: Create CodePuzzleGame.tsx**

```tsx
// src/components/lesson/games/CodePuzzleGame.tsx
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { GameQuestion } from "@/types/lesson";

interface CodePuzzleGameProps {
  question: GameQuestion;
  onAnswer: (correct: boolean) => void;
}

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function CodePuzzleGame({ question, onAnswer }: CodePuzzleGameProps) {
  const { lang } = useTranslation();
  const correctItems = question.items ?? [];

  const [available, setAvailable] = useState<{ text: string; origIdx: number }[]>([]);
  const [placed, setPlaced] = useState<{ text: string; origIdx: number }[]>([]);
  const [submitted, setSubmitted] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  useEffect(() => {
    const indexed = correctItems.map((item, i) => ({ text: item[lang], origIdx: i }));
    setAvailable(shuffle(indexed));
    setPlaced([]);
  }, [correctItems, lang]);

  const addToPlaced = (idx: number) => {
    if (submitted) return;
    const item = available[idx];
    setPlaced((p) => [...p, item]);
    setAvailable((a) => a.filter((_, i) => i !== idx));
  };

  const removeFromPlaced = (idx: number) => {
    if (submitted) return;
    const item = placed[idx];
    setAvailable((a) => [...a, item]);
    setPlaced((p) => p.filter((_, i) => i !== idx));
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const res = placed.map((item, i) => item.origIdx === i);
    setResults(res);
    const allCorrect = res.every(Boolean);
    setTimeout(() => onAnswer(allCorrect), 1200);
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col gap-6"
    >
      <h3 className="text-lg font-bold">{question.question[lang]}</h3>

      {/* Placed code lines */}
      <div className="min-h-[120px] rounded-2xl border-2 border-dashed border-border bg-bg/50 p-3 space-y-1.5">
        {placed.length === 0 && (
          <p className="text-sm text-text-secondary/50 text-center py-6">
            Tap code blocks below to assemble
          </p>
        )}
        {placed.map((item, i) => (
          <motion.button
            key={`p-${item.origIdx}`}
            layout
            onClick={() => removeFromPlaced(i)}
            className={`w-full text-left px-4 py-2 rounded-lg font-mono text-sm cursor-pointer transition-all ${
              submitted
                ? results[i]
                  ? "bg-green-500/15 border border-green-500/40 text-green-400"
                  : "bg-red-500/15 border border-red-500/40 text-red-400"
                : "bg-surface border border-border hover:border-primary/30"
            }`}
          >
            {item.text}
          </motion.button>
        ))}
      </div>

      {/* Available blocks */}
      <div className="flex flex-wrap gap-2">
        {available.map((item, i) => (
          <motion.button
            key={`a-${item.origIdx}`}
            layout
            onClick={() => addToPlaced(i)}
            disabled={submitted}
            className="px-4 py-2 rounded-lg border-2 border-border bg-surface font-mono text-sm cursor-pointer hover:border-primary/40 transition-all"
          >
            {item.text}
          </motion.button>
        ))}
      </div>

      {!submitted && placed.length === correctItems.length && (
        <Button onClick={handleSubmit} className="w-full">
          Check Code
        </Button>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/components/lesson/games/DragOrderGame.tsx src/components/lesson/games/CodePuzzleGame.tsx
git commit -m "feat: add DragOrderGame and CodePuzzleGame components"
```

---

## Task 7: ResultScreen

**Files:**
- Create: `src/components/lesson/ResultScreen.tsx`

- [ ] **Step 1: Create ResultScreen.tsx**

```tsx
// src/components/lesson/ResultScreen.tsx
import { useEffect } from "react";
import { motion } from "framer-motion";
import { Star, ArrowRight, RotateCcw } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { calculateStars, calculateXP } from "./autoMix";

interface ResultScreenProps {
  errors: number;
  onBackToMap: () => void;
  onRetry: () => void;
}

export function ResultScreen({ errors, onBackToMap, onRetry }: ResultScreenProps) {
  const stars = calculateStars(errors);
  const xp = calculateXP(stars);

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      className="flex flex-col items-center justify-center min-h-[60vh] gap-6 text-center"
    >
      {/* Stars */}
      <div className="flex items-end gap-3">
        {[1, 2, 3].map((i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 30, scale: 0 }}
            animate={{
              opacity: i <= stars ? 1 : 0.2,
              y: 0,
              scale: i === 2 ? 1.3 : 1,
            }}
            transition={{ delay: 0.3 + i * 0.25, type: "spring", stiffness: 200 }}
          >
            <Star
              size={i === 2 ? 56 : 44}
              fill={i <= stars ? "#FFD700" : "transparent"}
              stroke={i <= stars ? "#FFD700" : "#4B5563"}
              strokeWidth={2}
              className={i <= stars ? "drop-shadow-lg" : ""}
              style={i <= stars ? { filter: "drop-shadow(0 0 12px rgba(255,215,0,0.5))" } : {}}
            />
          </motion.div>
        ))}
      </div>

      {/* Title */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1.2 }}
      >
        <h2 className="text-2xl font-bold mb-1">
          {stars === 3 ? "Perfect!" : stars === 2 ? "Great Job!" : "Lesson Complete!"}
        </h2>
        <p className="text-text-secondary text-sm">
          {errors === 0 ? "No mistakes — flawless!" : `${errors} mistake${errors > 1 ? "s" : ""}`}
        </p>
      </motion.div>

      {/* XP */}
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 1.5, type: "spring" }}
        className="px-6 py-3 rounded-2xl bg-primary/15 border-2 border-primary/30"
      >
        <span className="text-2xl font-bold text-primary">+{xp} XP</span>
      </motion.div>

      {/* Buttons */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 2 }}
        className="flex gap-3 mt-4"
      >
        <Button variant="ghost" onClick={onRetry}>
          <RotateCcw size={16} /> Retry
        </Button>
        <Button onClick={onBackToMap}>
          Back to Map <ArrowRight size={16} />
        </Button>
      </motion.div>
    </motion.div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/lesson/ResultScreen.tsx
git commit -m "feat: add ResultScreen with stars, XP, and animations"
```

---

## Task 8: LessonPlayer (main container)

**Files:**
- Create: `src/components/lesson/LessonPlayer.tsx`

- [ ] **Step 1: Create LessonPlayer.tsx**

```tsx
// src/components/lesson/LessonPlayer.tsx
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
    if (session.currentStepIndex >= session.steps.length - 1) {
      setDone(true);
      // Save progress
      const stars = calculateStars(session.errors);
      const xp = calculateXP(stars);
      completeLesson(lesson.id);
      addXP(xp, stars === 3 ? "perfect_quiz" : "complete_lesson");

      // Check if all lessons for node are done
      const user = useAuthStore.getState().user;
      if (user) {
        const completedAfter = [...user.completed_lessons, lesson.id];
        const allDone = allLessonIdsForNode.every((id) => completedAfter.includes(id));
        if (allDone) completeNode(nodeId);
      }
      fetchUser();
    } else {
      setSession((s) => ({ ...s, currentStepIndex: s.currentStepIndex + 1 }));
    }
  }, [session, lesson.id, nodeId, allLessonIdsForNode]);

  const handleSlideNext = () => {
    advanceStep();
  };

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
      return <LessonSlide slide={step.data} onContinue={handleSlideNext} />;
    }

    const props = { question: step.data, onAnswer: handleGameAnswer };

    switch (step.gameType) {
      case "quiz": return <QuizGame {...props} />;
      case "true_false": return <TrueFalseGame {...props} />;
      case "match": return <MatchPairsGame {...props} />;
      case "flash_cards": return <FlashCardGame {...props} />;
      case "fill_blanks": return <FillBlanksGame {...props} />;
      case "type_answer": return <TypeAnswerGame {...props} />;
      case "drag_order": return <DragOrderGame {...props} />;
      case "code_puzzle": return <CodePuzzleGame {...props} />;
      default: return null;
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 z-50 bg-bg flex flex-col"
    >
      {/* Header: progress bar + close */}
      <div className="flex items-center gap-4 px-6 py-4">
        <button
          onClick={() => setShowExitConfirm(true)}
          className="w-8 h-8 rounded-full flex items-center justify-center hover:bg-surface transition-colors cursor-pointer"
        >
          <X size={20} className="text-text-secondary" />
        </button>

        <div className="flex-1 h-3 bg-surface rounded-full overflow-hidden">
          <motion.div
            className="h-full rounded-full bg-primary"
            animate={{ width: `${done ? 100 : progress}%` }}
            transition={{ duration: 0.4, ease: "easeOut" }}
          />
        </div>

        <span className="text-xs text-text-secondary min-w-[40px] text-right">
          {session.currentStepIndex + 1}/{session.steps.length}
        </span>
      </div>

      {/* Content */}
      <div className="flex-1 flex items-center justify-center px-6 overflow-y-auto">
        <div className="w-full max-w-xl">
          {done ? (
            <ResultScreen
              errors={session.errors}
              onBackToMap={onClose}
              onRetry={handleRetry}
            />
          ) : (
            <AnimatePresence mode="wait" key={session.currentStepIndex}>
              {currentStep && renderStep(currentStep)}
            </AnimatePresence>
          )}
        </div>
      </div>

      {/* Feedback overlay */}
      <FeedbackOverlay show={feedback.show} correct={feedback.correct} />

      {/* Exit confirmation */}
      <AnimatePresence>
        {showExitConfirm && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[60] bg-black/60 flex items-center justify-center p-6"
            onClick={() => setShowExitConfirm(false)}
          >
            <motion.div
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.9, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="bg-surface border border-border rounded-2xl p-6 max-w-sm w-full text-center space-y-4"
            >
              <h3 className="text-lg font-bold">Exit lesson?</h3>
              <p className="text-sm text-text-secondary">Your progress will be lost.</p>
              <div className="flex gap-3">
                <button
                  onClick={() => setShowExitConfirm(false)}
                  className="flex-1 py-2.5 rounded-xl border border-border text-sm font-medium cursor-pointer hover:bg-bg transition-all"
                >
                  Stay
                </button>
                <button
                  onClick={onClose}
                  className="flex-1 py-2.5 rounded-xl bg-red-500/15 border border-red-500/30 text-red-400 text-sm font-medium cursor-pointer hover:bg-red-500/25 transition-all"
                >
                  Exit
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/lesson/LessonPlayer.tsx
git commit -m "feat: add LessonPlayer main container with step rendering"
```

---

## Task 9: Sample Lesson Data (V2 format)

**Files:**
- Create: `src/data/lessons/frontend-v2.ts`

- [ ] **Step 1: Create frontend-v2.ts with rich data for first 2 lessons**

Create `src/data/lessons/frontend-v2.ts` with `LessonContentV2` data for `fe-1-1` (Document Structure) and `fe-1-2` (Common Tags). Each lesson must have 2-3 slides and 8-10 questions of varied types (quiz, true_false, match, fill_blanks, drag_order, code_puzzle, type_answer, flash_cards).

The data should include:
- **fe-1-1 slides:** HTML document structure basics (DOCTYPE, head, body, meta tags)
- **fe-1-1 questions:** Mix of all 8 game types about HTML structure
- **fe-1-2 slides:** Common HTML tags (headings, paragraphs, lists, links, images)
- **fe-1-2 questions:** Mix of all 8 game types about common tags

All text bilingual (en/ru). See `src/types/lesson.ts` for exact type shapes.

- [ ] **Step 2: Commit**

```bash
git add src/data/lessons/frontend-v2.ts
git commit -m "feat: add V2 lesson data for first 2 frontend lessons"
```

---

## Task 10: Update Lesson Page & Wire Everything

**Files:**
- Modify: `src/pages/Lesson.tsx`
- Modify: `src/data/lessons.ts`

- [ ] **Step 1: Update src/data/lessons.ts to export V2 lessons**

```typescript
// src/data/lessons.ts
import { FRONTEND_LESSONS } from "./lessons/frontend";
import { ENGLISH_LESSONS } from "./lessons/english";
import { CALLCENTER_LESSONS } from "./lessons/callcenter";
import { CIB_LESSONS } from "./lessons/cib";
import { FRONTEND_LESSONS_V2 } from "./lessons/frontend-v2";
import type { LessonContentV2 } from "@/types/lesson";

// Legacy types kept for backward compatibility
export interface VideoResource {
  title: string;
  url: string;
  duration?: string;
}

export interface FlashCardData {
  front: string;
  back: string;
}

export interface MatchPairData {
  term: string;
  definition: string;
}

export interface LessonContent {
  id: string;
  title: string;
  content: string;
  videos?: VideoResource[];
  codeExamples?: Array<{ language: string; code: string }>;
  quiz?: Array<{ question: string; options: string[]; correct: number }>;
  flashCards?: FlashCardData[];
  matchGame?: MatchPairData[];
}

export const LESSONS: Record<string, LessonContent> = {
  ...FRONTEND_LESSONS,
  ...ENGLISH_LESSONS,
  ...CALLCENTER_LESSONS,
  ...CIB_LESSONS,
};

export const LESSONS_V2: Record<string, LessonContentV2> = {
  ...FRONTEND_LESSONS_V2,
};
```

- [ ] **Step 2: Replace src/pages/Lesson.tsx**

```tsx
// src/pages/Lesson.tsx
import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { ArrowLeft } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Button } from "@/components/ui/Button";
import { LessonPlayer } from "@/components/lesson/LessonPlayer";
import { LESSONS_V2 } from "@/data/lessons";
import { useTranslation } from "@/hooks/useTranslation";
import { useUserStore } from "@/store/userStore";

export default function Lesson() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { t } = useTranslation();
  const profile = useUserStore((s) => s.profile);

  const lesson = id ? LESSONS_V2[id] : undefined;

  if (!lesson) {
    return (
      <PageWrapper>
        <div className="text-center py-20">
          <p className="text-text-secondary">{t("lesson.comingSoon")}</p>
          <Button variant="ghost" className="mt-4" onClick={() => navigate(-1)}>
            <ArrowLeft size={14} /> {t("lesson.goBack")}
          </Button>
        </div>
      </PageWrapper>
    );
  }

  // Determine node ID and all lesson IDs for this node
  const nodeId = id ? id.split("-").slice(0, 2).join("-") : "";
  const allLessonIds = Object.keys(LESSONS_V2).filter((k) => k.startsWith(nodeId));

  return (
    <LessonPlayer
      lesson={lesson}
      nodeId={nodeId}
      allLessonIdsForNode={allLessonIds}
      onClose={() => navigate("/roadmap")}
    />
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/Lesson.tsx src/data/lessons.ts
git commit -m "feat: wire LessonPlayer into Lesson page"
```

---

## Summary

| Task | Description | Files |
|------|-------------|-------|
| 1 | Types & AutoMix utility | lesson.ts, autoMix.ts |
| 2 | FeedbackOverlay & LessonSlide | FeedbackOverlay.tsx, LessonSlide.tsx |
| 3 | QuizGame & TrueFalseGame | QuizGame.tsx, TrueFalseGame.tsx |
| 4 | MatchPairsGame & FlashCardGame | MatchPairsGame.tsx, FlashCardGame.tsx |
| 5 | FillBlanksGame & TypeAnswerGame | FillBlanksGame.tsx, TypeAnswerGame.tsx |
| 6 | DragOrderGame & CodePuzzleGame | DragOrderGame.tsx, CodePuzzleGame.tsx |
| 7 | ResultScreen | ResultScreen.tsx |
| 8 | LessonPlayer (main container) | LessonPlayer.tsx |
| 9 | Sample lesson data (V2) | frontend-v2.ts |
| 10 | Wire into Lesson page | Lesson.tsx, lessons.ts |

**Total: 10 tasks, 15 new files, 2 modified files.**
