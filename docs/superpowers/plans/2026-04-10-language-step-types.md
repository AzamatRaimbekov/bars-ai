# Language Step Types Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 5 new lesson step types optimized for language learning: listening-comprehension, pronunciation, word-builder, sentence-translation, cloze-passage.

**Architecture:** Each step is a standalone React component in `src/components/courses/steps/`. They plug into the existing `CourseStepPlayer.tsx` via its `renderStep` switch. Two new backend endpoints (`/api/ai/transcribe` and `/api/ai/check-translation`) handle Whisper and Claude calls.

**Tech Stack:** React + TypeScript + Framer Motion + Tailwind (frontend), FastAPI + OpenAI Whisper + Anthropic Claude (backend)

---

### Task 1: Add types and interfaces to courseApi.ts

**Files:**
- Modify: `src/services/courseApi.ts:61-82` (StepType union)
- Modify: `src/services/courseApi.ts:213-240` (interfaces + LessonStep union)

- [ ] **Step 1: Add 5 new step types to StepType union**

In `src/services/courseApi.ts`, find the `StepType` union (line 61-82) and add after `"snippet-order"`:

```typescript
export type StepType =
  | "info"
  | "quiz"
  | "drag-order"
  | "code-puzzle"
  | "fill-blank"
  | "matching"
  | "true-false"
  | "flashcards"
  | "type-answer"
  | "image-hotspot"
  | "code-editor"
  | "timeline"
  | "category-sort"
  | "video"
  | "audio"
  | "embed"
  | "terminal-sim"
  | "multi-select"
  | "conversation-sim"
  | "highlight-text"
  | "snippet-order"
  | "listening-comprehension"
  | "pronunciation"
  | "word-builder"
  | "sentence-translation"
  | "cloze-passage";
```

- [ ] **Step 2: Add 5 new interfaces after StepSnippetOrder (line ~217)**

```typescript
export interface StepListeningComprehension {
  type: "listening-comprehension";
  audioUrl: string;
  transcript?: string;
  questions: {
    question: string;
    options: { id: string; text: string; correct: boolean }[];
  }[];
}

export interface StepPronunciation {
  type: "pronunciation";
  word: string;
  audioUrl?: string;
  phonetic?: string;
  acceptedForms: string[];
}

export interface StepWordBuilder {
  type: "word-builder";
  hint: string;
  word: string;
  image?: string;
}

export interface StepSentenceTranslation {
  type: "sentence-translation";
  sentence: string;
  sourceLanguage: string;
  targetLanguage: string;
  acceptedAnswers: string[];
  aiCheck: boolean;
}

export interface ClozeSegment =
  | { type: "text"; value: string }
  | { type: "blank"; answer: string; options?: string[] };

export interface StepClozePassage {
  type: "cloze-passage";
  instruction: string;
  segments: ClozeSegment[];
}
```

- [ ] **Step 3: Add new types to LessonStep union (line ~219-240)**

```typescript
export type LessonStep =
  | StepInfo
  | StepQuiz
  | StepDragOrder
  | StepCodePuzzle
  | StepFillBlank
  | StepMatching
  | StepTrueFalse
  | StepFlashcards
  | StepTypeAnswer
  | StepImageHotspot
  | StepCodeEditor
  | StepTimeline
  | StepCategorySort
  | StepVideo
  | StepAudio
  | StepEmbed
  | StepTerminalSim
  | StepMultiSelect
  | StepConversationSim
  | StepHighlightText
  | StepSnippetOrder
  | StepListeningComprehension
  | StepPronunciation
  | StepWordBuilder
  | StepSentenceTranslation
  | StepClozePassage;
```

- [ ] **Step 4: Add API helper functions for pronunciation and translation**

At the end of `courseApi.ts`, add inside the `courseApi` object or as standalone exports:

```typescript
export async function transcribeAudio(audioBlob: Blob): Promise<{ text: string; confidence: number }> {
  const formData = new FormData();
  formData.append("audio", audioBlob, "recording.webm");
  const token = sessionStorage.getItem("pathmind_access_token");
  const resp = await fetch("/api/ai/transcribe", {
    method: "POST",
    headers: token ? { Authorization: `Bearer ${token}` } : {},
    credentials: "include",
    body: formData,
  });
  if (!resp.ok) throw new Error("Transcription failed");
  return resp.json();
}

export async function checkTranslation(data: {
  sentence: string;
  user_answer: string;
  source_language: string;
  target_language: string;
}): Promise<{ correct: boolean; feedback: string; suggested: string }> {
  return apiFetch("/ai/check-translation", {
    method: "POST",
    body: JSON.stringify(data),
  });
}
```

- [ ] **Step 5: Commit**

```bash
git add src/services/courseApi.ts
git commit -m "feat: add types and API helpers for 5 new language step types"
```

---

### Task 2: Create WordBuilderStep component

**Files:**
- Create: `src/components/courses/steps/WordBuilderStep.tsx`

This is the simplest component — no backend calls, pure frontend logic.

- [ ] **Step 1: Create the component file**

Create `src/components/courses/steps/WordBuilderStep.tsx`:

```tsx
import { useState, useMemo, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import type { StepWordBuilder } from "@/services/courseApi";

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

interface Props {
  step: StepWordBuilder;
  onAnswer: (correct: boolean) => void;
}

export default function WordBuilderStep({ step, onAnswer }: Props) {
  const letters = useMemo(
    () => shuffle(step.word.split("").map((ch, i) => ({ id: `${ch}-${i}`, char: ch }))),
    [step.word],
  );

  const [placed, setPlaced] = useState<typeof letters>([]);
  const [available, setAvailable] = useState(letters);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleTap = useCallback(
    (letter: (typeof letters)[0]) => {
      if (checked) return;
      setPlaced((p) => [...p, letter]);
      setAvailable((a) => a.filter((l) => l.id !== letter.id));
    },
    [checked],
  );

  const handleRemove = useCallback(
    (letter: (typeof letters)[0]) => {
      if (checked) return;
      setAvailable((a) => [...a, letter]);
      setPlaced((p) => p.filter((l) => l.id !== letter.id));
    },
    [checked],
  );

  const handleCheck = () => {
    const userWord = placed.map((l) => l.char).join("");
    const correct = userWord.toLowerCase() === step.word.toLowerCase();
    setIsCorrect(correct);
    setChecked(true);
    setTimeout(() => onAnswer(correct), 1200);
  };

  const handleDrop = useCallback(
    (e: React.DragEvent, _slotIndex: number) => {
      if (checked) return;
      e.preventDefault();
      const id = e.dataTransfer.getData("letter-id");
      const letter = available.find((l) => l.id === id);
      if (letter) {
        setPlaced((p) => [...p, letter]);
        setAvailable((a) => a.filter((l) => l.id !== id));
      }
    },
    [available, checked],
  );

  return (
    <div className="flex flex-col items-center gap-8 w-full max-w-md mx-auto">
      {/* Hint / image */}
      {step.image && (
        <img src={step.image} alt={step.hint} className="w-32 h-32 object-contain rounded-xl" />
      )}
      <p className="text-lg text-text-secondary text-center">{step.hint}</p>

      {/* Slots */}
      <div className="flex gap-2 justify-center flex-wrap">
        {step.word.split("").map((_, i) => {
          const letter = placed[i];
          return (
            <div
              key={i}
              onDragOver={(e) => e.preventDefault()}
              onDrop={(e) => handleDrop(e, i)}
              onClick={() => letter && handleRemove(letter)}
              className={`w-11 h-12 rounded-lg border-2 flex items-center justify-center text-lg font-bold transition-colors cursor-pointer ${
                checked
                  ? isCorrect
                    ? "border-green-500 bg-green-500/10 text-green-400"
                    : "border-red-500 bg-red-500/10 text-red-400"
                  : letter
                    ? "border-primary/50 bg-primary/10 text-text"
                    : "border-border bg-surface"
              }`}
            >
              <AnimatePresence mode="wait">
                {letter && (
                  <motion.span
                    key={letter.id}
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    exit={{ scale: 0 }}
                    transition={{ type: "spring", stiffness: 400, damping: 20 }}
                  >
                    {letter.char}
                  </motion.span>
                )}
              </AnimatePresence>
            </div>
          );
        })}
      </div>

      {/* Available letters */}
      <div className="flex gap-2 justify-center flex-wrap">
        {available.map((letter) => (
          <motion.button
            key={letter.id}
            layout
            onClick={() => handleTap(letter)}
            draggable
            onDragStart={(e: any) => e.dataTransfer?.setData("letter-id", letter.id)}
            whileTap={{ scale: 0.9 }}
            className="w-11 h-12 rounded-lg bg-surface border border-border text-text font-bold text-lg flex items-center justify-center cursor-pointer hover:border-primary/50 transition-colors"
          >
            {letter.char}
          </motion.button>
        ))}
      </div>

      {/* Check button */}
      {placed.length === step.word.length && !checked && (
        <motion.button
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          onClick={handleCheck}
          className="px-8 py-3 rounded-xl bg-primary text-white font-semibold cursor-pointer hover:bg-primary/90 transition-colors"
        >
          Проверить
        </motion.button>
      )}

      {/* Result */}
      {checked && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className={`text-lg font-semibold ${isCorrect ? "text-green-400" : "text-red-400"}`}
        >
          {isCorrect ? "Правильно!" : `Ответ: ${step.word}`}
        </motion.p>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/courses/steps/WordBuilderStep.tsx
git commit -m "feat: add WordBuilderStep component"
```

---

### Task 3: Create ClozePassageStep component

**Files:**
- Create: `src/components/courses/steps/ClozePassageStep.tsx`

- [ ] **Step 1: Create the component file**

Create `src/components/courses/steps/ClozePassageStep.tsx`:

```tsx
import { useState } from "react";
import { motion } from "framer-motion";
import type { StepClozePassage } from "@/services/courseApi";

interface Props {
  step: StepClozePassage;
  onAnswer: (correct: boolean) => void;
}

export default function ClozePassageStep({ step, onAnswer }: Props) {
  const blanks = step.segments.filter((s) => s.type === "blank");
  const [answers, setAnswers] = useState<Record<number, string>>(
    () => Object.fromEntries(blanks.map((_, i) => [i, ""])),
  );
  const [checked, setChecked] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  const handleChange = (blankIndex: number, value: string) => {
    setAnswers((prev) => ({ ...prev, [blankIndex]: value }));
  };

  const handleCheck = () => {
    let blankIdx = 0;
    const res: boolean[] = [];
    for (const seg of step.segments) {
      if (seg.type === "blank") {
        res.push(answers[blankIdx]?.trim().toLowerCase() === seg.answer.trim().toLowerCase());
        blankIdx++;
      }
    }
    setResults(res);
    setChecked(true);
    const allCorrect = res.every(Boolean);
    setTimeout(() => onAnswer(allCorrect), 1500);
  };

  const allFilled = Object.values(answers).every((v) => v.trim().length > 0);

  let blankCounter = 0;

  return (
    <div className="flex flex-col gap-6 w-full max-w-lg mx-auto">
      <p className="text-sm text-text-secondary">{step.instruction}</p>

      <div className="text-text leading-8 text-base">
        {step.segments.map((seg, segIdx) => {
          if (seg.type === "text") {
            return <span key={segIdx}>{seg.value}</span>;
          }

          const idx = blankCounter++;
          const isCorrect = results[idx];

          if (seg.options && seg.options.length > 0) {
            // Dropdown mode
            return (
              <select
                key={segIdx}
                value={answers[idx] || ""}
                onChange={(e) => handleChange(idx, e.target.value)}
                disabled={checked}
                className={`inline-block mx-1 px-2 py-0.5 rounded-lg border text-sm bg-surface outline-none transition-colors ${
                  checked
                    ? isCorrect
                      ? "border-green-500 bg-green-500/10 text-green-400"
                      : "border-red-500 bg-red-500/10 text-red-400"
                    : "border-border focus:border-primary/50"
                }`}
              >
                <option value="">—</option>
                {seg.options.map((opt) => (
                  <option key={opt} value={opt}>
                    {opt}
                  </option>
                ))}
              </select>
            );
          }

          // Input mode
          return (
            <input
              key={segIdx}
              type="text"
              value={answers[idx] || ""}
              onChange={(e) => handleChange(idx, e.target.value)}
              disabled={checked}
              placeholder="..."
              className={`inline-block mx-1 w-24 px-2 py-0.5 rounded-lg border text-sm bg-surface outline-none text-center transition-colors ${
                checked
                  ? isCorrect
                    ? "border-green-500 bg-green-500/10 text-green-400"
                    : "border-red-500 bg-red-500/10 text-red-400"
                  : "border-border focus:border-primary/50"
              }`}
            />
          );
        })}
      </div>

      {/* Show correct answers on error */}
      {checked && results.some((r) => !r) && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="text-sm text-text-secondary">
          <span className="text-red-400 font-medium">Правильные ответы: </span>
          {blanks.map((b, i) => (
            <span key={i}>
              {!results[i] && (
                <span className="text-green-400">{b.type === "blank" ? b.answer : ""}</span>
              )}
              {i < blanks.length - 1 && !results[i] && ", "}
            </span>
          ))}
        </motion.div>
      )}

      {!checked && allFilled && (
        <motion.button
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          onClick={handleCheck}
          className="self-center px-8 py-3 rounded-xl bg-primary text-white font-semibold cursor-pointer hover:bg-primary/90 transition-colors"
        >
          Проверить
        </motion.button>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/courses/steps/ClozePassageStep.tsx
git commit -m "feat: add ClozePassageStep component"
```

---

### Task 4: Create ListeningComprehensionStep component

**Files:**
- Create: `src/components/courses/steps/ListeningComprehensionStep.tsx`

- [ ] **Step 1: Create the component file**

Create `src/components/courses/steps/ListeningComprehensionStep.tsx`:

```tsx
import { useState, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Play, Pause, Eye, EyeOff } from "lucide-react";
import type { StepListeningComprehension } from "@/services/courseApi";

interface Props {
  step: StepListeningComprehension;
  onAnswer: (correct: boolean) => void;
}

export default function ListeningComprehensionStep({ step, onAnswer }: Props) {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [playing, setPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const [showTranscript, setShowTranscript] = useState(false);

  const [currentQ, setCurrentQ] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);

  const question = step.questions[currentQ];

  const togglePlay = () => {
    const audio = audioRef.current;
    if (!audio) return;
    if (playing) {
      audio.pause();
    } else {
      audio.play();
    }
    setPlaying(!playing);
  };

  const handleTimeUpdate = () => {
    const audio = audioRef.current;
    if (!audio || !audio.duration) return;
    setProgress((audio.currentTime / audio.duration) * 100);
  };

  const handleSeek = (e: React.MouseEvent<HTMLDivElement>) => {
    const audio = audioRef.current;
    if (!audio || !audio.duration) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const pct = (e.clientX - rect.left) / rect.width;
    audio.currentTime = pct * audio.duration;
  };

  const handleSelect = (optionId: string) => {
    if (checked) return;
    setSelected(optionId);
  };

  const handleCheck = () => {
    if (!selected) return;
    const correct = question.options.find((o) => o.id === selected)?.correct ?? false;
    const newCount = correctCount + (correct ? 1 : 0);
    setCorrectCount(newCount);
    setChecked(true);

    setTimeout(() => {
      if (currentQ < step.questions.length - 1) {
        setCurrentQ((q) => q + 1);
        setSelected(null);
        setChecked(false);
      } else {
        onAnswer(newCount === step.questions.length);
      }
    }, 1200);
  };

  return (
    <div className="flex flex-col gap-6 w-full max-w-lg mx-auto">
      {/* Audio player */}
      <audio
        ref={audioRef}
        src={step.audioUrl}
        onTimeUpdate={handleTimeUpdate}
        onEnded={() => setPlaying(false)}
      />
      <div className="bg-surface rounded-xl p-4 border border-border">
        <div className="flex items-center gap-3">
          <button
            onClick={togglePlay}
            className="w-10 h-10 rounded-full bg-primary/20 text-primary flex items-center justify-center cursor-pointer hover:bg-primary/30 transition-colors"
          >
            {playing ? <Pause size={18} /> : <Play size={18} />}
          </button>
          <div className="flex-1 h-2 bg-white/8 rounded-full cursor-pointer" onClick={handleSeek}>
            <div
              className="h-full bg-primary rounded-full transition-all"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* Transcript toggle */}
        {step.transcript && (
          <div className="mt-3">
            <button
              onClick={() => setShowTranscript(!showTranscript)}
              className="flex items-center gap-1.5 text-xs text-text-secondary hover:text-text transition-colors cursor-pointer"
            >
              {showTranscript ? <EyeOff size={14} /> : <Eye size={14} />}
              {showTranscript ? "Скрыть текст" : "Показать текст"}
            </button>
            <AnimatePresence>
              {showTranscript && (
                <motion.p
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  className="text-sm text-text-secondary mt-2 overflow-hidden"
                >
                  {step.transcript}
                </motion.p>
              )}
            </AnimatePresence>
          </div>
        )}
      </div>

      {/* Question */}
      <div>
        <p className="text-xs text-text-secondary mb-1">
          Вопрос {currentQ + 1} из {step.questions.length}
        </p>
        <p className="text-text font-medium mb-4">{question.question}</p>

        <div className="flex flex-col gap-2">
          {question.options.map((opt) => {
            const isSelected = selected === opt.id;
            const showResult = checked && isSelected;
            return (
              <button
                key={opt.id}
                onClick={() => handleSelect(opt.id)}
                className={`w-full text-left px-4 py-3 rounded-xl border text-sm transition-colors cursor-pointer ${
                  showResult
                    ? opt.correct
                      ? "border-green-500 bg-green-500/10 text-green-400"
                      : "border-red-500 bg-red-500/10 text-red-400"
                    : isSelected
                      ? "border-primary bg-primary/10 text-text"
                      : "border-border bg-surface text-text hover:border-white/20"
                }`}
              >
                {opt.text}
              </button>
            );
          })}
        </div>
      </div>

      {selected && !checked && (
        <motion.button
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          onClick={handleCheck}
          className="self-center px-8 py-3 rounded-xl bg-primary text-white font-semibold cursor-pointer hover:bg-primary/90 transition-colors"
        >
          Ответить
        </motion.button>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/courses/steps/ListeningComprehensionStep.tsx
git commit -m "feat: add ListeningComprehensionStep component"
```

---

### Task 5: Create SentenceTranslationStep component

**Files:**
- Create: `src/components/courses/steps/SentenceTranslationStep.tsx`

- [ ] **Step 1: Create the component file**

Create `src/components/courses/steps/SentenceTranslationStep.tsx`:

```tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { Loader2 } from "lucide-react";
import { checkTranslation } from "@/services/courseApi";
import type { StepSentenceTranslation } from "@/services/courseApi";

interface Props {
  step: StepSentenceTranslation;
  onAnswer: (correct: boolean) => void;
}

export default function SentenceTranslationStep({ step, onAnswer }: Props) {
  const [input, setInput] = useState("");
  const [checking, setChecking] = useState(false);
  const [result, setResult] = useState<{
    correct: boolean;
    feedback: string;
    suggested: string;
  } | null>(null);

  const handleSubmit = async () => {
    if (!input.trim()) return;
    const normalized = input.trim().toLowerCase();

    // Fast check against accepted answers
    const fastMatch = step.acceptedAnswers.some(
      (a) => a.trim().toLowerCase() === normalized,
    );

    if (fastMatch) {
      setResult({ correct: true, feedback: "Отлично! Перевод верный.", suggested: input.trim() });
      setTimeout(() => onAnswer(true), 1200);
      return;
    }

    // AI check if enabled
    if (step.aiCheck) {
      setChecking(true);
      try {
        const res = await checkTranslation({
          sentence: step.sentence,
          user_answer: input.trim(),
          source_language: step.sourceLanguage,
          target_language: step.targetLanguage,
        });
        setResult(res);
        setTimeout(() => onAnswer(res.correct), 1500);
      } catch {
        // Fallback: treat as incorrect
        setResult({
          correct: false,
          feedback: "Не удалось проверить. Попробуйте ещё раз.",
          suggested: step.acceptedAnswers[0] || "",
        });
        setTimeout(() => onAnswer(false), 1500);
      } finally {
        setChecking(false);
      }
      return;
    }

    // No AI, no match — incorrect
    setResult({
      correct: false,
      feedback: "Неверно.",
      suggested: step.acceptedAnswers[0] || "",
    });
    setTimeout(() => onAnswer(false), 1200);
  };

  const langNames: Record<string, string> = {
    ru: "русского",
    en: "английский",
    kz: "казахский",
    de: "немецкий",
    fr: "французский",
  };

  return (
    <div className="flex flex-col gap-6 w-full max-w-lg mx-auto items-center">
      <p className="text-xs text-text-secondary">
        Переведите с {langNames[step.sourceLanguage] || step.sourceLanguage} на{" "}
        {langNames[step.targetLanguage] || step.targetLanguage}
      </p>

      <p className="text-xl text-text font-semibold text-center">{step.sentence}</p>

      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        disabled={!!result || checking}
        rows={3}
        placeholder="Ваш перевод..."
        className="w-full rounded-xl border border-border bg-surface px-4 py-3 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none"
      />

      {!result && !checking && input.trim() && (
        <motion.button
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          onClick={handleSubmit}
          className="px-8 py-3 rounded-xl bg-primary text-white font-semibold cursor-pointer hover:bg-primary/90 transition-colors"
        >
          Проверить
        </motion.button>
      )}

      {checking && (
        <div className="flex items-center gap-2 text-text-secondary text-sm">
          <Loader2 size={16} className="animate-spin" />
          Проверяем перевод...
        </div>
      )}

      {result && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className={`w-full rounded-xl p-4 border ${
            result.correct
              ? "border-green-500/30 bg-green-500/10"
              : "border-red-500/30 bg-red-500/10"
          }`}
        >
          <p className={`font-medium ${result.correct ? "text-green-400" : "text-red-400"}`}>
            {result.correct ? "Правильно!" : "Неверно"}
          </p>
          <p className="text-sm text-text-secondary mt-1">{result.feedback}</p>
          {!result.correct && result.suggested && (
            <p className="text-sm text-text mt-2">
              Правильный вариант: <span className="text-green-400">{result.suggested}</span>
            </p>
          )}
        </motion.div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/courses/steps/SentenceTranslationStep.tsx
git commit -m "feat: add SentenceTranslationStep component"
```

---

### Task 6: Create PronunciationStep component

**Files:**
- Create: `src/components/courses/steps/PronunciationStep.tsx`

- [ ] **Step 1: Create the component file**

Create `src/components/courses/steps/PronunciationStep.tsx`:

```tsx
import { useState, useRef } from "react";
import { motion } from "framer-motion";
import { Mic, Square, Play, Loader2, Volume2 } from "lucide-react";
import { transcribeAudio } from "@/services/courseApi";
import type { StepPronunciation } from "@/services/courseApi";

interface Props {
  step: StepPronunciation;
  onAnswer: (correct: boolean) => void;
}

export default function PronunciationStep({ step, onAnswer }: Props) {
  const [recording, setRecording] = useState(false);
  const [processing, setProcessing] = useState(false);
  const [result, setResult] = useState<{ text: string; correct: boolean } | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const audioRef = useRef<HTMLAudioElement>(null);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream, { mimeType: "audio/webm" });
      mediaRecorderRef.current = mediaRecorder;
      chunksRef.current = [];

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) chunksRef.current.push(e.data);
      };

      mediaRecorder.onstop = async () => {
        stream.getTracks().forEach((t) => t.stop());
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        setProcessing(true);

        try {
          const res = await transcribeAudio(blob);
          const normalized = res.text.trim().toLowerCase().replace(/[.,!?;:]/g, "");
          const correct = step.acceptedForms.some(
            (f) => f.trim().toLowerCase().replace(/[.,!?;:]/g, "") === normalized,
          );
          setResult({ text: res.text, correct });
          setTimeout(() => onAnswer(correct), 1500);
        } catch {
          setResult({ text: "Ошибка распознавания", correct: false });
          setTimeout(() => onAnswer(false), 1500);
        } finally {
          setProcessing(false);
        }
      };

      mediaRecorder.start();
      setRecording(true);
    } catch {
      // Microphone access denied
      setResult({ text: "Нет доступа к микрофону", correct: false });
    }
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
    setRecording(false);
  };

  const playReference = () => {
    audioRef.current?.play();
  };

  return (
    <div className="flex flex-col items-center gap-6 w-full max-w-md mx-auto">
      {/* Word to pronounce */}
      <p className="text-3xl font-bold text-text">{step.word}</p>
      {step.phonetic && (
        <p className="text-lg text-text-secondary font-mono">{step.phonetic}</p>
      )}

      {/* Reference audio */}
      {step.audioUrl && (
        <>
          <audio ref={audioRef} src={step.audioUrl} />
          <button
            onClick={playReference}
            className="flex items-center gap-2 px-4 py-2 rounded-xl bg-surface border border-border text-text-secondary text-sm cursor-pointer hover:border-white/20 transition-colors"
          >
            <Volume2 size={16} />
            Прослушать эталон
          </button>
        </>
      )}

      {/* Record button */}
      {!result && !processing && (
        <motion.button
          whileTap={{ scale: 0.95 }}
          onClick={recording ? stopRecording : startRecording}
          className={`w-20 h-20 rounded-full flex items-center justify-center cursor-pointer transition-colors ${
            recording
              ? "bg-red-500 text-white animate-pulse"
              : "bg-primary/20 text-primary hover:bg-primary/30"
          }`}
        >
          {recording ? <Square size={28} /> : <Mic size={28} />}
        </motion.button>
      )}

      {recording && (
        <p className="text-sm text-red-400 animate-pulse">Запись... нажмите чтобы остановить</p>
      )}

      {!recording && !result && !processing && (
        <p className="text-sm text-text-secondary">Нажмите на микрофон и произнесите слово</p>
      )}

      {/* Processing */}
      {processing && (
        <div className="flex items-center gap-2 text-text-secondary text-sm">
          <Loader2 size={16} className="animate-spin" />
          Распознаём речь...
        </div>
      )}

      {/* Result */}
      {result && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className={`w-full rounded-xl p-4 border text-center ${
            result.correct
              ? "border-green-500/30 bg-green-500/10"
              : "border-red-500/30 bg-red-500/10"
          }`}
        >
          <p className="text-sm text-text-secondary mb-1">Распознано:</p>
          <p className={`text-lg font-semibold ${result.correct ? "text-green-400" : "text-red-400"}`}>
            "{result.text}"
          </p>
          <p className={`mt-2 font-medium ${result.correct ? "text-green-400" : "text-red-400"}`}>
            {result.correct ? "Отлично!" : `Ожидалось: "${step.word}"`}
          </p>
        </motion.div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/courses/steps/PronunciationStep.tsx
git commit -m "feat: add PronunciationStep component"
```

---

### Task 7: Wire new steps into CourseStepPlayer

**Files:**
- Modify: `src/components/courses/CourseStepPlayer.tsx:1-33` (imports)
- Modify: `src/components/courses/CourseStepPlayer.tsx:2670-2678` (renderStep switch)

- [ ] **Step 1: Add imports at top of CourseStepPlayer.tsx**

After the existing type imports (line 33), add:

```typescript
import WordBuilderStep from "./steps/WordBuilderStep";
import ClozePassageStep from "./steps/ClozePassageStep";
import ListeningComprehensionStep from "./steps/ListeningComprehensionStep";
import SentenceTranslationStep from "./steps/SentenceTranslationStep";
import PronunciationStep from "./steps/PronunciationStep";
```

Also add to the type imports from `@/services/courseApi`:

```typescript
import type {
  // ... existing imports ...
  StepListeningComprehension,
  StepPronunciation,
  StepWordBuilder,
  StepSentenceTranslation,
  StepClozePassage,
} from "@/services/courseApi";
```

- [ ] **Step 2: Add 5 new cases to renderStep switch**

In the `renderStep` function, before the `default: return null;` (line ~2678), add:

```typescript
      case "listening-comprehension":
        return (
          <ListeningComprehensionStep
            step={step as StepListeningComprehension}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "pronunciation":
        return (
          <PronunciationStep
            step={step as StepPronunciation}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "word-builder":
        return (
          <WordBuilderStep
            step={step as StepWordBuilder}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "sentence-translation":
        return (
          <SentenceTranslationStep
            step={step as StepSentenceTranslation}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "cloze-passage":
        return (
          <ClozePassageStep
            step={step as StepClozePassage}
            onAnswer={handleInteractiveAnswer}
          />
        );
```

- [ ] **Step 3: Commit**

```bash
git add src/components/courses/CourseStepPlayer.tsx
git commit -m "feat: wire 5 new language steps into CourseStepPlayer"
```

---

### Task 8: Add defaults and forms to StepEditor

**Files:**
- Modify: `src/components/courses/StepEditor.tsx:31` (imports)
- Modify: `src/components/courses/StepEditor.tsx:77-178` (defaultStep)
- Modify: `src/components/courses/StepEditor.tsx:181-203` (STEP_TYPES)
- Modify: `src/components/courses/StepEditor.tsx:1897-1902` (form rendering)

- [ ] **Step 1: Add type imports**

In `StepEditor.tsx`, add to the imports from `@/services/courseApi` (lines 34-60):

```typescript
  type StepListeningComprehension,
  type StepPronunciation,
  type StepWordBuilder,
  type StepSentenceTranslation,
  type StepClozePassage,
```

Add new icons to lucide-react imports:

```typescript
  Headphones, // already imported
  Mic,
  BookOpen,
  Languages,
  TextCursorInput,
```

- [ ] **Step 2: Add default steps in defaultStep function (after line 177)**

Before the closing `}` of the `defaultStep` function, add:

```typescript
    case "listening-comprehension":
      return {
        type: "listening-comprehension",
        audioUrl: "",
        transcript: "",
        questions: [
          {
            question: "",
            options: [
              { id: nanoid(), text: "", correct: true },
              { id: nanoid(), text: "", correct: false },
            ],
          },
        ],
      };
    case "pronunciation":
      return {
        type: "pronunciation",
        word: "",
        audioUrl: "",
        phonetic: "",
        acceptedForms: [""],
      };
    case "word-builder":
      return { type: "word-builder", hint: "", word: "", image: "" };
    case "sentence-translation":
      return {
        type: "sentence-translation",
        sentence: "",
        sourceLanguage: "ru",
        targetLanguage: "en",
        acceptedAnswers: [""],
        aiCheck: true,
      };
    case "cloze-passage":
      return {
        type: "cloze-passage",
        instruction: "",
        segments: [
          { type: "text", value: "The cat " },
          { type: "blank", answer: "sat" },
          { type: "text", value: " on the " },
          { type: "blank", answer: "mat", options: ["mat", "hat", "bat"] },
          { type: "text", value: "." },
        ],
      };
```

- [ ] **Step 3: Add to STEP_TYPES array (after line 202)**

```typescript
  { type: "listening-comprehension", label: "Аудирование", icon: <Headphones size={14} />, color: "#06B6D4" },
  { type: "pronunciation", label: "Произношение", icon: <Mic size={14} />, color: "#F43F5E" },
  { type: "word-builder", label: "Собери слово", icon: <BookOpen size={14} />, color: "#10B981" },
  { type: "sentence-translation", label: "Перевод", icon: <Languages size={14} />, color: "#A855F7" },
  { type: "cloze-passage", label: "Текст с пропусками", icon: <TextCursorInput size={14} />, color: "#F59E0B" },
```

- [ ] **Step 4: Add 5 editor forms**

After the last form (`SnippetOrderForm`, around line 1690), add these 5 forms:

```tsx
function ListeningComprehensionForm({
  step,
  onChange,
}: {
  step: StepListeningComprehension & { _id: string };
  onChange: (patch: Partial<StepListeningComprehension>) => void;
}) {
  const updateQuestion = (qIdx: number, patch: any) => {
    const questions = [...step.questions];
    questions[qIdx] = { ...questions[qIdx], ...patch };
    onChange({ questions });
  };

  const updateOption = (qIdx: number, oIdx: number, patch: any) => {
    const questions = [...step.questions];
    const options = [...questions[qIdx].options];
    options[oIdx] = { ...options[oIdx], ...patch };
    questions[qIdx] = { ...questions[qIdx], options };
    onChange({ questions });
  };

  const addQuestion = () => {
    onChange({
      questions: [
        ...step.questions,
        {
          question: "",
          options: [
            { id: nanoid(), text: "", correct: true },
            { id: nanoid(), text: "", correct: false },
          ],
        },
      ],
    });
  };

  const removeQuestion = (qIdx: number) => {
    onChange({ questions: step.questions.filter((_, i) => i !== qIdx) });
  };

  const addOption = (qIdx: number) => {
    const questions = [...step.questions];
    questions[qIdx] = {
      ...questions[qIdx],
      options: [...questions[qIdx].options, { id: nanoid(), text: "", correct: false }],
    };
    onChange({ questions });
  };

  return (
    <div className="space-y-3">
      <Input label="URL аудио" value={step.audioUrl} onChange={(e) => onChange({ audioUrl: e.target.value })} placeholder="https://..." />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Транскрипт (опц.)</label>
        <textarea value={step.transcript || ""} onChange={(e) => onChange({ transcript: e.target.value })} rows={3} className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm" placeholder="Текст аудиозаписи..." />
      </div>
      {step.questions.map((q, qi) => (
        <div key={qi} className="p-3 rounded-lg bg-white/4 border border-white/6 space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs text-text-secondary">Вопрос {qi + 1}</span>
            {step.questions.length > 1 && (
              <button onClick={() => removeQuestion(qi)} className="text-red-400 cursor-pointer"><Trash2 size={14} /></button>
            )}
          </div>
          <Input value={q.question} onChange={(e) => updateQuestion(qi, { question: e.target.value })} placeholder="Вопрос..." />
          {q.options.map((opt, oi) => (
            <div key={opt.id} className="flex items-center gap-2">
              <input type="radio" name={`lc-q-${qi}`} checked={opt.correct} onChange={() => {
                const options = q.options.map((o, i) => ({ ...o, correct: i === oi }));
                updateQuestion(qi, { options });
              }} className="cursor-pointer" />
              <Input value={opt.text} onChange={(e) => updateOption(qi, oi, { text: e.target.value })} placeholder="Вариант..." className="flex-1" />
            </div>
          ))}
          <button onClick={() => addOption(qi)} className="text-xs text-primary cursor-pointer">+ Вариант</button>
        </div>
      ))}
      <button onClick={addQuestion} className="text-xs text-primary cursor-pointer">+ Вопрос</button>
    </div>
  );
}

function PronunciationForm({
  step,
  onChange,
}: {
  step: StepPronunciation & { _id: string };
  onChange: (patch: Partial<StepPronunciation>) => void;
}) {
  return (
    <div className="space-y-3">
      <Input label="Слово / фраза" value={step.word} onChange={(e) => onChange({ word: e.target.value })} placeholder="Hello" />
      <Input label="Транскрипция" value={step.phonetic || ""} onChange={(e) => onChange({ phonetic: e.target.value })} placeholder="/həˈloʊ/" />
      <Input label="URL эталонного аудио (опц.)" value={step.audioUrl || ""} onChange={(e) => onChange({ audioUrl: e.target.value })} placeholder="https://..." />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Допустимые формы (по строке)</label>
        <textarea value={step.acceptedForms.join("\n")} onChange={(e) => onChange({ acceptedForms: e.target.value.split("\n") })} rows={3} className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono" placeholder={"hello\nHello"} />
      </div>
    </div>
  );
}

function WordBuilderForm({
  step,
  onChange,
}: {
  step: StepWordBuilder & { _id: string };
  onChange: (patch: Partial<StepWordBuilder>) => void;
}) {
  return (
    <div className="space-y-3">
      <Input label="Подсказка / перевод" value={step.hint} onChange={(e) => onChange({ hint: e.target.value })} placeholder="Привет" />
      <Input label="Правильное слово" value={step.word} onChange={(e) => onChange({ word: e.target.value })} placeholder="hello" />
      <Input label="URL картинки (опц.)" value={step.image || ""} onChange={(e) => onChange({ image: e.target.value })} placeholder="https://..." />
    </div>
  );
}

function SentenceTranslationForm({
  step,
  onChange,
}: {
  step: StepSentenceTranslation & { _id: string };
  onChange: (patch: Partial<StepSentenceTranslation>) => void;
}) {
  return (
    <div className="space-y-3">
      <Input label="Исходная фраза" value={step.sentence} onChange={(e) => onChange({ sentence: e.target.value })} placeholder="Я иду домой" />
      <div className="grid grid-cols-2 gap-3">
        <div>
          <label className="block text-sm text-text-secondary mb-1.5">Исходный язык</label>
          <select value={step.sourceLanguage} onChange={(e) => onChange({ sourceLanguage: e.target.value })} className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text outline-none text-sm">
            <option value="ru">Русский</option>
            <option value="en">Английский</option>
            <option value="kz">Казахский</option>
            <option value="de">Немецкий</option>
            <option value="fr">Французский</option>
          </select>
        </div>
        <div>
          <label className="block text-sm text-text-secondary mb-1.5">Целевой язык</label>
          <select value={step.targetLanguage} onChange={(e) => onChange({ targetLanguage: e.target.value })} className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text outline-none text-sm">
            <option value="en">Английский</option>
            <option value="ru">Русский</option>
            <option value="kz">Казахский</option>
            <option value="de">Немецкий</option>
            <option value="fr">Французский</option>
          </select>
        </div>
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Допустимые ответы (по строке)</label>
        <textarea value={step.acceptedAnswers.join("\n")} onChange={(e) => onChange({ acceptedAnswers: e.target.value.split("\n") })} rows={3} className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono" placeholder={"I'm going home\nI am going home"} />
      </div>
      <label className="flex items-center gap-2 text-sm text-text cursor-pointer">
        <input type="checkbox" checked={step.aiCheck} onChange={(e) => onChange({ aiCheck: e.target.checked })} className="cursor-pointer" />
        Проверять через AI если нет точного совпадения
      </label>
    </div>
  );
}

function ClozePassageForm({
  step,
  onChange,
}: {
  step: StepClozePassage & { _id: string };
  onChange: (patch: Partial<StepClozePassage>) => void;
}) {
  // Serialize segments back to markup
  const toMarkup = (): string => {
    return step.segments
      .map((s) => {
        if (s.type === "text") return s.value;
        if (s.options && s.options.length > 0) return `{${s.answer}|${s.options.join(",")}}`;
        return `{${s.answer}}`;
      })
      .join("");
  };

  // Parse markup into segments
  const parseMarkup = (text: string) => {
    const segments: StepClozePassage["segments"] = [];
    const regex = /\{([^}]+)\}/g;
    let lastIndex = 0;
    let match;
    while ((match = regex.exec(text)) !== null) {
      if (match.index > lastIndex) {
        segments.push({ type: "text", value: text.slice(lastIndex, match.index) });
      }
      const inner = match[1];
      const pipeIdx = inner.indexOf("|");
      if (pipeIdx >= 0) {
        segments.push({
          type: "blank",
          answer: inner.slice(0, pipeIdx),
          options: inner.slice(pipeIdx + 1).split(",").map((s) => s.trim()),
        });
      } else {
        segments.push({ type: "blank", answer: inner });
      }
      lastIndex = regex.lastIndex;
    }
    if (lastIndex < text.length) {
      segments.push({ type: "text", value: text.slice(lastIndex) });
    }
    return segments;
  };

  return (
    <div className="space-y-3">
      <Input label="Инструкция" value={step.instruction} onChange={(e) => onChange({ instruction: e.target.value })} placeholder="Заполните пропуски в тексте" />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Текст с пропусками — <code className="text-xs px-1 py-0.5 bg-white/8 rounded">{"{answer}"}</code> для ввода, <code className="text-xs px-1 py-0.5 bg-white/8 rounded">{"{answer|opt1,opt2}"}</code> для dropdown
        </label>
        <textarea
          value={toMarkup()}
          onChange={(e) => onChange({ segments: parseMarkup(e.target.value) })}
          rows={5}
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono"
          placeholder={"The cat {sat} on the {mat|mat,hat,bat}."}
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 5: Add form rendering in StepCard (after line ~1902)**

After the `snippet-order` conditional, before `</div>`, add:

```tsx
              {step.type === "listening-comprehension" && (
                <ListeningComprehensionForm
                  step={step as StepListeningComprehension & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "pronunciation" && (
                <PronunciationForm
                  step={step as StepPronunciation & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "word-builder" && (
                <WordBuilderForm
                  step={step as StepWordBuilder & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "sentence-translation" && (
                <SentenceTranslationForm
                  step={step as StepSentenceTranslation & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "cloze-passage" && (
                <ClozePassageForm
                  step={step as StepClozePassage & { _id: string }}
                  onChange={onUpdate}
                />
              )}
```

- [ ] **Step 6: Commit**

```bash
git add src/components/courses/StepEditor.tsx
git commit -m "feat: add editor forms for 5 new language step types"
```

---

### Task 9: Backend — add OPENAI_API_KEY to config

**Files:**
- Modify: `backend/app/config.py`
- Modify: `backend/requirements.txt`
- Modify: `backend/.env`

- [ ] **Step 1: Add OPENAI_API_KEY to Settings**

In `backend/app/config.py`, add to the `Settings` class:

```python
class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://redis:6379/0"
    ANTHROPIC_API_KEY: str
    OPENAI_API_KEY: str = ""
    JWT_SECRET: str
    JWT_ACCESS_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_EXPIRE_DAYS: int = 7
    CORS_ORIGINS: str = "http://localhost:5173"
```

- [ ] **Step 2: Add openai to requirements.txt**

Append to `backend/requirements.txt`:

```
openai==1.82.0
```

- [ ] **Step 3: Add OPENAI_API_KEY to .env**

Add to `backend/.env`:

```
OPENAI_API_KEY=sk-your-openai-key-here
```

- [ ] **Step 4: Install dependency**

```bash
cd backend && source venv/bin/activate && pip install openai==1.82.0
```

- [ ] **Step 5: Commit**

```bash
git add backend/app/config.py backend/requirements.txt
git commit -m "feat: add OpenAI dependency and config for Whisper"
```

---

### Task 10: Backend — add transcribe endpoint

**Files:**
- Modify: `backend/app/schemas/ai.py`
- Modify: `backend/app/services/ai_service.py`
- Modify: `backend/app/routers/ai.py`

- [ ] **Step 1: Add schemas**

In `backend/app/schemas/ai.py`, add at the end:

```python
class TranscribeResponse(BaseModel):
    text: str
    confidence: float


class CheckTranslationRequest(BaseModel):
    sentence: str = Field(min_length=1)
    user_answer: str = Field(min_length=1)
    source_language: str = Field(min_length=2, max_length=5)
    target_language: str = Field(min_length=2, max_length=5)


class CheckTranslationResponse(BaseModel):
    correct: bool
    feedback: str
    suggested: str
```

- [ ] **Step 2: Add transcribe function to ai_service.py**

At the end of `backend/app/services/ai_service.py`, add:

```python
async def transcribe(audio_bytes: bytes, filename: str = "recording.webm") -> dict:
    """Send audio to OpenAI Whisper and return transcription."""
    from openai import AsyncOpenAI
    import io

    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = filename

    response = await client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="verbose_json",
    )

    return {
        "text": response.text,
        "confidence": getattr(response, "confidence", 0.9),
    }
```

- [ ] **Step 3: Add check_translation function to ai_service.py**

At the end of `backend/app/services/ai_service.py`, add:

```python
LANG_NAMES = {"ru": "Russian", "en": "English", "kz": "Kazakh", "de": "German", "fr": "French"}


async def check_translation(
    sentence: str,
    user_answer: str,
    source_language: str,
    target_language: str,
) -> dict:
    """Use Claude to evaluate a translation."""
    src = LANG_NAMES.get(source_language, source_language)
    tgt = LANG_NAMES.get(target_language, target_language)

    system = (
        f"You are a language teacher evaluating a student's translation from {src} to {tgt}. "
        "Respond in JSON with keys: correct (bool), feedback (string in Russian, 1-2 sentences), "
        "suggested (the best translation). Accept semantically correct translations even if wording differs. "
        "Only output valid JSON, no markdown."
    )
    content = f"Original ({src}): {sentence}\nStudent's translation ({tgt}): {user_answer}"

    raw = await _call_claude(system, [{"role": "user", "content": content}], max_tokens=256)

    try:
        data = json.loads(raw)
        return {
            "correct": bool(data.get("correct", False)),
            "feedback": str(data.get("feedback", "")),
            "suggested": str(data.get("suggested", "")),
        }
    except (json.JSONDecodeError, KeyError):
        return {"correct": False, "feedback": "Ошибка проверки.", "suggested": ""}
```

- [ ] **Step 4: Add routes to ai.py**

In `backend/app/routers/ai.py`, add the imports at the top:

```python
from fastapi import APIRouter, Depends, Request, UploadFile, File
```

Then update the schemas import:

```python
from app.schemas.ai import (
    ChatRequest, ChatResponse,
    AssessRequest, AssessResponse,
    TipRequest, TipResponse,
    ScoreRequest, ScoreResponse,
    TranscribeResponse,
    CheckTranslationRequest, CheckTranslationResponse,
)
```

Then add the two endpoints at the end of the file:

```python
@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe(
    audio: UploadFile = File(...),
    request: Request = None,
    user_id: uuid.UUID = Depends(get_current_user_id),
):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    audio_bytes = await audio.read()
    result = await ai_service.transcribe(audio_bytes, audio.filename or "recording.webm")
    return TranscribeResponse(**result)


@router.post("/check-translation", response_model=CheckTranslationResponse)
async def check_translation(
    body: CheckTranslationRequest,
    request: Request,
    user_id: uuid.UUID = Depends(get_current_user_id),
):
    request.state.user_id = str(user_id)
    await rate_limit(request)
    result = await ai_service.check_translation(
        body.sentence, body.user_answer, body.source_language, body.target_language
    )
    return CheckTranslationResponse(**result)
```

- [ ] **Step 5: Commit**

```bash
git add backend/app/schemas/ai.py backend/app/services/ai_service.py backend/app/routers/ai.py
git commit -m "feat: add /api/ai/transcribe and /api/ai/check-translation endpoints"
```

---

### Task 11: Smoke test all 5 step types

**Files:** None (manual verification)

- [ ] **Step 1: Start backend and frontend**

```bash
npm run dev:all
```

- [ ] **Step 2: Open the course editor, create a test lesson, add each of the 5 new step types**

Verify each type:
1. **word-builder** — create with hint "Привет", word "hello". Open the lesson, verify letters appear shuffled, tapping works, check validates correctly.
2. **cloze-passage** — create with markup `The {cat} sat on the {mat|mat,hat,bat}`. Verify "cat" shows as input, "mat" shows as dropdown.
3. **listening-comprehension** — create with an audio URL and one question. Verify player plays, question appears, answer checking works.
4. **sentence-translation** — create with sentence "Привет", target "en", accepted "Hello,Hi". Type "hello" — should pass fast check. Type "Greetings" — should trigger AI check if aiCheck is on.
5. **pronunciation** — create with word "hello". Click mic, speak, verify Whisper transcription and result display.

- [ ] **Step 3: Fix any issues found**

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "fix: address issues found during smoke testing"
```
