import { useState, useMemo, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, ArrowLeft, ArrowRight, CheckCircle2, RotateCcw, Play, Copy, Check } from "lucide-react";
import { Highlight, themes } from "prism-react-renderer";
import CodeMirror from "@uiw/react-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { html } from "@codemirror/lang-html";
import { css } from "@codemirror/lang-css";
import { Button } from "@/components/ui/Button";
import type {
  LessonStep,
  StepInfo,
  StepQuiz,
  StepDragOrder,
  StepCodePuzzle,
  StepFillBlank,
  StepMatching,
  StepTrueFalse,
  StepFlashcards,
  StepTypeAnswer,
  StepImageHotspot,
  StepCodeEditor,
  StepTimeline,
  StepCategorySort,
  StepVideo,
  StepAudio,
  StepEmbed,
  StepTerminalSim,
  StepMultiSelect,
  StepConversationSim,
  StepHighlightText,
  StepSnippetOrder,
  StepListeningComprehension,
  StepPronunciation,
  StepWordBuilder,
  StepSentenceTranslation,
  StepClozePassage,
} from "@/services/courseApi";

import WordBuilderStep from "./steps/WordBuilderStep";
import ClozePassageStep from "./steps/ClozePassageStep";
import ListeningComprehensionStep from "./steps/ListeningComprehensionStep";
import SentenceTranslationStep from "./steps/SentenceTranslationStep";
import PronunciationStep from "./steps/PronunciationStep";

// ─── Helpers ───────────────────────────────────────────────────────────────

/** Fisher-Yates shuffle — returns a new array. */
function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** Render inline markdown: **bold**, `inline code` */
function renderInline(text: string): React.ReactNode[] {
  const parts: React.ReactNode[] = [];
  const tokens = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  tokens.forEach((token, i) => {
    if (token.startsWith("**") && token.endsWith("**")) {
      parts.push(<strong key={i} className="text-text font-semibold">{token.slice(2, -2)}</strong>);
    } else if (token.startsWith("`") && token.endsWith("`")) {
      parts.push(
        <code key={i} className="px-1.5 py-0.5 rounded-md bg-white/8 font-mono text-[#F97316] text-[0.85em] border border-white/6">
          {token.slice(1, -1)}
        </code>
      );
    } else {
      parts.push(token);
    }
  });
  return parts;
}

/** Syntax-highlighted code block with copy button */
function CodeBlock({ code, language }: { code: string; language: string }) {
  const [copied, setCopied] = useState(false);
  const langMap: Record<string, string> = {
    ts: "typescript", js: "javascript", tsx: "tsx", jsx: "jsx",
    py: "python", sh: "bash", yml: "yaml", md: "markdown",
  };
  const lang = langMap[language] || language || "typescript";

  const handleCopy = () => {
    navigator.clipboard.writeText(code).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  return (
    <div className="rounded-xl overflow-hidden border border-white/6 bg-[#0A0A0A]">
      {/* Header bar */}
      <div className="flex items-center justify-between px-4 py-2 bg-white/[0.03] border-b border-white/6">
        <span className="text-[11px] font-mono text-white/30 uppercase tracking-wider">{lang}</span>
        <button
          type="button"
          onClick={handleCopy}
          className="flex items-center gap-1.5 text-[11px] text-white/30 hover:text-white/60 transition-colors cursor-pointer"
        >
          {copied ? <Check size={12} className="text-[#4ADE80]" /> : <Copy size={12} />}
          {copied ? "Скопировано" : "Копировать"}
        </button>
      </div>
      {/* Code */}
      <Highlight theme={themes.nightOwl} code={code.trim()} language={lang as any}>
        {({ tokens, getLineProps, getTokenProps }) => (
          <pre className="overflow-x-auto p-4 text-[13px] leading-relaxed font-mono">
            {tokens.map((line, i) => (
              <div key={i} {...getLineProps({ line })} className="table-row">
                <span className="table-cell pr-4 text-right text-white/15 select-none w-8 text-[12px]">
                  {i + 1}
                </span>
                <span className="table-cell">
                  {line.map((token, j) => (
                    <span key={j} {...getTokenProps({ token })} />
                  ))}
                </span>
              </div>
            ))}
          </pre>
        )}
      </Highlight>
    </div>
  );
}

/** Parse markdown into blocks, then render with code highlighting */
function MarkdownBlock({ markdown }: { markdown: string }) {
  // Split markdown into blocks: code blocks vs text blocks
  const blocks: { type: "text" | "code"; content: string; lang?: string }[] = [];
  const codeBlockRegex = /```(\w*)\n([\s\S]*?)```/g;
  let lastIndex = 0;
  let match;

  while ((match = codeBlockRegex.exec(markdown)) !== null) {
    // Text before code block
    if (match.index > lastIndex) {
      blocks.push({ type: "text", content: markdown.slice(lastIndex, match.index) });
    }
    blocks.push({ type: "code", content: match[2], lang: match[1] || "typescript" });
    lastIndex = match.index + match[0].length;
  }
  // Remaining text after last code block
  if (lastIndex < markdown.length) {
    blocks.push({ type: "text", content: markdown.slice(lastIndex) });
  }

  return (
    <div className="space-y-4 text-sm leading-relaxed text-white/50">
      {blocks.map((block, bi) => {
        if (block.type === "code") {
          return <CodeBlock key={bi} code={block.content} language={block.lang || "typescript"} />;
        }
        // Render text lines
        const lines = block.content.split("\n");
        return (
          <div key={bi} className="space-y-2.5">
            {lines.map((line, i) => {
              const h3 = line.match(/^### (.+)/);
              const h2 = line.match(/^## (.+)/);
              const h1 = line.match(/^# (.+)/);
              const li = line.match(/^[-*] (.+)/);
              if (h1) return <h2 key={i} className="text-lg font-bold text-text mt-2">{h1[1]}</h2>;
              if (h2) return <h3 key={i} className="text-base font-semibold text-text mt-1">{h2[1]}</h3>;
              if (h3) return <h4 key={i} className="text-sm font-semibold text-text">{h3[1]}</h4>;
              if (li) {
                return (
                  <div key={i} className="flex gap-2.5 pl-1">
                    <span className="mt-2 flex-shrink-0 w-1.5 h-1.5 rounded-full bg-[#F97316]" />
                    <span className="text-white/50">{renderInline(li[1])}</span>
                  </div>
                );
              }
              if (line.trim() === "") return <div key={i} className="h-1" />;
              return <p key={i} className="text-white/50">{renderInline(line)}</p>;
            })}
          </div>
        );
      })}
    </div>
  );
}

// ─── Step renderers ────────────────────────────────────────────────────────

function InfoStep({ step }: { step: StepInfo }) {
  return (
    <div className="space-y-4">
      {step.title && (
        <h2 className="text-xl font-bold text-text">{step.title}</h2>
      )}
      <MarkdownBlock markdown={step.markdown} />
    </div>
  );
}

// ── Quiz ──────────────────────────────────────────────────────────────────

type QuizState = "idle" | "correct" | "wrong";

function QuizStep({
  step,
  onAnswer,
}: {
  step: StepQuiz;
  onAnswer: (correct: boolean) => void;
}) {
  const [selected, setSelected] = useState<string | null>(null);
  const [state, setState] = useState<QuizState>("idle");

  const handleSelect = (id: string) => {
    if (state !== "idle") return;
    const option = step.options.find((o) => o.id === id)!;
    setSelected(id);
    const correct = option.correct;
    setState(correct ? "correct" : "wrong");
    if (correct) {
      // Advance after a brief moment so the user sees the green highlight
      setTimeout(() => onAnswer(true), 900);
    } else {
      // Show wrong feedback (including which option was correct), then reset for retry
      setTimeout(() => {
        setSelected(null);
        setState("idle");
      }, 1500);
    }
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        {step.question}
      </p>
      <div className="space-y-2.5">
        {step.options.map((option) => {
          const isSelected = selected === option.id;
          const isCorrect = option.correct;

          let borderClass = "border-white/10 hover:border-white/25";
          let bgClass = "bg-white/5 hover:bg-white/8";
          let textClass = "text-text";

          if (isSelected && state === "correct") {
            borderClass = "border-success/60";
            bgClass = "bg-success/10";
            textClass = "text-success";
          } else if (isSelected && state === "wrong") {
            borderClass = "border-red-500/60";
            bgClass = "bg-red-500/10";
            textClass = "text-red-400";
          } else if (state !== "idle" && isCorrect) {
            // Show the correct answer after a wrong attempt
            borderClass = "border-success/40";
            bgClass = "bg-success/5";
            textClass = "text-success/80";
          }

          return (
            <button
              key={option.id}
              type="button"
              onClick={() => handleSelect(option.id)}
              disabled={state !== "idle"}
              className={`
                w-full text-left px-4 py-3 rounded-xl border transition-all duration-200 cursor-pointer
                disabled:cursor-default text-sm font-medium
                ${borderClass} ${bgClass} ${textClass}
              `}
            >
              {option.text}
            </button>
          );
        })}
      </div>
    </div>
  );
}

// ── Drag Order ─────────────────────────────────────────────────────────────

function DragOrderStep({
  step,
  onAnswer,
}: {
  step: StepDragOrder;
  onAnswer: (correct: boolean) => void;
}) {
  // Shuffle once on mount
  const shuffled = useMemo(() => shuffle(step.items), [step]);
  const [order, setOrder] = useState<string[]>(shuffled);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  // Track which item is being dragged via tap-to-select approach
  const [selected, setSelected] = useState<number | null>(null);

  const handleTap = (index: number) => {
    if (checked) return;
    if (selected === null) {
      setSelected(index);
    } else {
      // Swap selected and tapped
      const next = [...order];
      [next[selected], next[index]] = [next[index], next[selected]];
      setOrder(next);
      setSelected(null);
    }
  };

  const handleCheck = () => {
    const correct = order.every((item, i) => item === step.items[i]);
    setIsCorrect(correct);
    setChecked(true);
  };

  const handleRetry = () => {
    setOrder(shuffle(step.items));
    setChecked(false);
    setIsCorrect(false);
    setSelected(null);
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        Расставьте элементы в правильном порядке
      </p>
      <p className="text-xs text-text-secondary">
        Нажмите на элемент, затем на то место, куда его переместить
      </p>

      <div className="space-y-2">
        {order.map((item, i) => {
          const isSelected = selected === i;
          let borderClass = "border-white/10";
          let bgClass = "bg-white/5";

          if (checked) {
            const correct = item === step.items[i];
            borderClass = correct ? "border-success/50" : "border-red-500/50";
            bgClass = correct ? "bg-success/8" : "bg-red-500/8";
          } else if (isSelected) {
            borderClass = "border-[#F97316]/60";
            bgClass = "bg-[#F97316]/10";
          }

          return (
            <motion.button
              key={`${item}-${i}`}
              type="button"
              onClick={() => handleTap(i)}
              disabled={checked}
              layout
              className={`
                w-full flex items-center gap-3 px-4 py-3 rounded-xl border
                transition-colors duration-200 cursor-pointer disabled:cursor-default text-sm
                ${borderClass} ${bgClass}
              `}
            >
              <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-xs font-mono text-text-secondary">
                {i + 1}
              </span>
              <span className="text-text text-left">{item}</span>
              {isSelected && (
                <span className="ml-auto text-[#F97316] text-xs">выбрано</span>
              )}
            </motion.button>
          );
        })}
      </div>

      {!checked ? (
        <Button className="w-full" onClick={handleCheck} disabled={selected !== null}>
          Проверить порядок
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {isCorrect ? (
              <>
                <CheckCircle2 size={16} /> Правильный порядок!
              </>
            ) : (
              <>
                Неправильно. Попробуйте ещё раз.
              </>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Code Puzzle ────────────────────────────────────────────────────────────

function CodePuzzleStep({
  step,
  onAnswer,
}: {
  step: StepCodePuzzle;
  onAnswer: (correct: boolean) => void;
}) {
  const shuffled = useMemo(() => shuffle(step.fragments), [step]);
  const [assembled, setAssembled] = useState<string[]>([]);
  const [available, setAvailable] = useState<string[]>(shuffled);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const addFragment = (frag: string) => {
    if (checked) return;
    setAssembled((prev) => [...prev, frag]);
    setAvailable((prev) => {
      const idx = prev.indexOf(frag);
      const next = [...prev];
      next.splice(idx, 1);
      return next;
    });
  };

  const removeFragment = (index: number) => {
    if (checked) return;
    const frag = assembled[index];
    setAssembled((prev) => prev.filter((_, i) => i !== index));
    setAvailable((prev) => [...prev, frag]);
  };

  const handleCheck = () => {
    const correct = assembled.every((f, i) => f === step.fragments[i]) && assembled.length === step.fragments.length;
    setIsCorrect(correct);
    setChecked(true);
  };

  const handleRetry = () => {
    setAssembled([]);
    setAvailable(shuffle(step.fragments));
    setChecked(false);
    setIsCorrect(false);
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text">
        Соберите правильный код
      </p>

      {/* Assembly zone */}
      <div>
        <p className="text-xs text-text-secondary mb-2">Ваш код:</p>
        <div className="min-h-[56px] rounded-xl border border-white/6 bg-[#0A0A0A] p-3 space-y-1.5">
          {assembled.length === 0 ? (
            <p className="text-xs text-text-secondary/50 italic">
              Нажмите на фрагменты ниже, чтобы добавить их сюда
            </p>
          ) : (
            assembled.map((frag, i) => {
              const correct = checked ? frag === step.fragments[i] : null;
              return (
                <button
                  key={`${frag}-${i}`}
                  type="button"
                  onClick={() => removeFragment(i)}
                  disabled={checked}
                  className={`
                    block w-full text-left px-3 py-1.5 rounded-lg border text-xs font-mono
                    transition-colors cursor-pointer disabled:cursor-default
                    ${
                      checked
                        ? correct
                          ? "border-success/40 bg-success/8 text-success"
                          : "border-red-500/40 bg-red-500/8 text-red-400"
                        : "border-[#F97316]/30 bg-[#F97316]/8 text-[#F97316] hover:bg-[#F97316]/15"
                    }
                  `}
                >
                  {frag}
                </button>
              );
            })
          )}
        </div>
      </div>

      {/* Available fragments */}
      {!checked && (
        <div>
          <p className="text-xs text-text-secondary mb-2">Доступные фрагменты:</p>
          <div className="flex flex-wrap gap-2">
            {available.map((frag, i) => (
              <button
                key={`avail-${frag}-${i}`}
                type="button"
                onClick={() => addFragment(frag)}
                className="px-3 py-1.5 rounded-lg border border-white/15 bg-white/5 text-xs font-mono text-text hover:bg-white/10 hover:border-white/25 transition-colors cursor-pointer"
              >
                {frag}
              </button>
            ))}
          </div>
        </div>
      )}

      {!checked ? (
        <Button
          className="w-full"
          onClick={handleCheck}
          disabled={assembled.length !== step.fragments.length}
        >
          Проверить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {isCorrect ? (
              <>
                <CheckCircle2 size={16} /> Отлично! Код собран правильно.
              </>
            ) : (
              <>Порядок неверный. Попробуйте снова.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Fill Blank ─────────────────────────────────────────────────────────────

function FillBlankStep({
  step,
  onAnswer,
}: {
  step: StepFillBlank;
  onAnswer: (correct: boolean) => void;
}) {
  // Count blanks in the text
  const blanks = (step.text.match(/___/g) || []).length;
  const [values, setValues] = useState<string[]>(Array(blanks).fill(""));
  const [checked, setChecked] = useState(false);
  const [results, setResults] = useState<boolean[]>([]);

  const updateValue = (index: number, val: string) => {
    setValues((prev) => {
      const next = [...prev];
      next[index] = val;
      return next;
    });
  };

  const handleCheck = () => {
    const res = values.map((v, i) =>
      v.trim().toLowerCase() === (step.answers[i] ?? "").trim().toLowerCase()
    );
    setResults(res);
    setChecked(true);
  };

  const handleRetry = () => {
    setValues(Array(blanks).fill(""));
    setResults([]);
    setChecked(false);
  };

  const allCorrect = results.length > 0 && results.every(Boolean);

  // Render the text with input fields inline
  const parts = step.text.split("___");
  let inputIdx = 0;

  const renderedText = parts.map((part, i) => {
    const nodes: React.ReactNode[] = [<span key={`p-${i}`}>{part}</span>];
    if (i < parts.length - 1) {
      const idx = inputIdx++;
      const isCorrect = checked ? results[idx] : null;
      nodes.push(
        <input
          key={`inp-${idx}`}
          value={values[idx] ?? ""}
          onChange={(e) => updateValue(idx, e.target.value)}
          disabled={checked}
          className={`
            inline-block w-28 mx-1 px-2 py-0.5 rounded-lg border text-sm font-medium
            bg-white/5 outline-none transition-colors
            disabled:cursor-default
            ${
              isCorrect === null
                ? "border-white/20 text-text focus:border-[#F97316]/50"
                : isCorrect
                ? "border-success/60 bg-success/10 text-success"
                : "border-red-500/60 bg-red-500/10 text-red-400"
            }
          `}
          placeholder="..."
        />
      );
    }
    return nodes;
  });

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text">Заполните пропуски</p>

      <div className="bg-[#0A0A0A] border border-white/6 rounded-xl p-4 text-sm text-text leading-loose">
        {renderedText}
      </div>

      {checked && !allCorrect && (
        <div className="space-y-1">
          <p className="text-xs text-text-secondary">Правильные ответы:</p>
          {step.answers.map((ans, i) => (
            <p key={i} className="text-xs text-success font-medium">
              Пропуск {i + 1}: {ans}
            </p>
          ))}
        </div>
      )}

      {!checked ? (
        <Button
          className="w-full"
          onClick={handleCheck}
          disabled={values.some((v) => v.trim() === "")}
        >
          Проверить ответы
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              allCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {allCorrect ? (
              <>
                <CheckCircle2 size={16} /> Все ответы верны!
              </>
            ) : (
              <>Не все ответы правильны.</>
            )}
          </div>
          {allCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Matching ───────────────────────────────────────────────────────────────

function MatchingStep({
  step,
  onAnswer,
}: {
  step: StepMatching;
  onAnswer: (correct: boolean) => void;
}) {
  // Shuffle right column once on mount
  const shuffledRight = useMemo(
    () => shuffle(step.pairs.map((p) => p.right)),
    [step]
  );

  // selectedLeft: index into pairs (left side), connections: leftIdx -> rightValue
  const [selectedLeft, setSelectedLeft] = useState<number | null>(null);
  const [connections, setConnections] = useState<Record<number, string>>({});
  const [checked, setChecked] = useState(false);
  const [results, setResults] = useState<Record<number, boolean>>({});

  const handleLeftTap = (idx: number) => {
    if (checked) return;
    setSelectedLeft((prev) => (prev === idx ? null : idx));
  };

  const handleRightTap = (rightValue: string) => {
    if (checked || selectedLeft === null) return;
    setConnections((prev) => ({ ...prev, [selectedLeft]: rightValue }));
    setSelectedLeft(null);
  };

  const handleCheck = () => {
    const res: Record<number, boolean> = {};
    step.pairs.forEach((pair, i) => {
      res[i] = connections[i] === pair.right;
    });
    setResults(res);
    setChecked(true);
  };

  const handleRetry = () => {
    setConnections({});
    setSelectedLeft(null);
    setChecked(false);
    setResults({});
  };

  const allConnected = step.pairs.every((_, i) => connections[i] !== undefined);
  const allCorrect = checked && step.pairs.every((_, i) => results[i]);

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        Соедините пары
      </p>
      <p className="text-xs text-text-secondary">
        Нажмите левый элемент, затем правый, чтобы соединить их
      </p>

      <div className="grid grid-cols-2 gap-3">
        {/* Left column */}
        <div className="space-y-2">
          {step.pairs.map((pair, i) => {
            const isActive = selectedLeft === i;
            const isConnected = connections[i] !== undefined;
            const isCorrect = checked ? results[i] : null;

            let cls = "border-white/10 bg-white/5 text-text";
            if (isActive) cls = "border-[#F97316]/60 bg-[#F97316]/10 text-[#F97316]";
            else if (checked && isCorrect) cls = "border-success/50 bg-success/10 text-success";
            else if (checked && !isCorrect) cls = "border-red-500/50 bg-red-500/10 text-red-400";
            else if (isConnected) cls = "border-white/30 bg-white/10 text-text";

            return (
              <button
                key={i}
                type="button"
                onClick={() => handleLeftTap(i)}
                disabled={checked}
                className={`w-full text-left px-3 py-2.5 rounded-xl border text-xs font-medium transition-all duration-200 cursor-pointer disabled:cursor-default ${cls}`}
              >
                {pair.left}
              </button>
            );
          })}
        </div>

        {/* Right column */}
        <div className="space-y-2">
          {shuffledRight.map((rightValue, i) => {
            // Find which left this right value is connected to
            const connectedLeftIdx = Object.entries(connections).find(
              ([, v]) => v === rightValue
            )?.[0];
            const isConnectedLeft =
              connectedLeftIdx !== undefined
                ? parseInt(connectedLeftIdx, 10)
                : null;
            const isCorrectPair =
              checked && isConnectedLeft !== null
                ? results[isConnectedLeft]
                : null;

            let cls = "border-white/10 bg-white/5 text-text hover:border-white/25 hover:bg-white/10";
            if (selectedLeft !== null && isConnectedLeft === null)
              cls = "border-[#F97316]/30 bg-[#F97316]/5 text-text hover:border-[#F97316]/60 hover:bg-[#F97316]/10";
            else if (checked && isCorrectPair) cls = "border-success/50 bg-success/10 text-success";
            else if (checked && isCorrectPair === false) cls = "border-red-500/50 bg-red-500/10 text-red-400";
            else if (isConnectedLeft !== null) cls = "border-white/30 bg-white/10 text-text";

            return (
              <button
                key={`r-${i}`}
                type="button"
                onClick={() => handleRightTap(rightValue)}
                disabled={checked}
                className={`w-full text-left px-3 py-2.5 rounded-xl border text-xs font-medium transition-all duration-200 cursor-pointer disabled:cursor-default ${cls}`}
              >
                {rightValue}
              </button>
            );
          })}
        </div>
      </div>

      {!checked ? (
        <Button className="w-full" onClick={handleCheck} disabled={!allConnected}>
          Проверить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              allCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {allCorrect ? (
              <><CheckCircle2 size={16} /> Все пары верны!</>
            ) : (
              <>Не все пары совпадают.</>
            )}
          </div>
          {allCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── True / False ────────────────────────────────────────────────────────────

function TrueFalseStep({
  step,
  onAnswer,
}: {
  step: StepTrueFalse;
  onAnswer: (correct: boolean) => void;
}) {
  const [answered, setAnswered] = useState<boolean | null>(null);

  const handleChoice = (choice: boolean) => {
    if (answered !== null) return;
    setAnswered(choice);
    const correct = choice === step.correct;
    if (correct) {
      // Advance after a brief moment so the user sees the green highlight
      setTimeout(() => onAnswer(true), 800);
    } else {
      // Show wrong feedback (with correct answer hint already in JSX below), then reset for retry
      setTimeout(() => {
        setAnswered(null);
      }, 2000);
    }
  };

  const isCorrect = answered !== null && answered === step.correct;
  const isWrong = answered !== null && answered !== step.correct;

  return (
    <div className="space-y-6">
      <div className="bg-[#0A0A0A] border border-white/6 rounded-xl p-5 text-center">
        <p className="text-lg font-semibold text-text leading-snug">
          {step.statement}
        </p>
      </div>

      {answered !== null && (
        <motion.div
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className={`flex items-center justify-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
            isCorrect
              ? "bg-success/10 border-success/40 text-success"
              : "bg-red-500/10 border-red-500/40 text-red-400"
          }`}
        >
          {isCorrect ? (
            <><CheckCircle2 size={16} /> Правильно!</>
          ) : (
            <>Неверно. Правильный ответ: {step.correct ? "Верно" : "Неверно"}</>
          )}
        </motion.div>
      )}

      <div className="grid grid-cols-2 gap-3">
        <button
          type="button"
          onClick={() => handleChoice(true)}
          disabled={answered !== null}
          className={`
            py-4 rounded-xl border text-base font-bold transition-all duration-200 cursor-pointer disabled:cursor-default
            ${
              answered === true
                ? isCorrect
                  ? "bg-success/15 border-success/40 text-success"
                  : "bg-red-500/15 border-red-500/40 text-red-400"
                : "bg-[#4ADE80]/8 border-[#4ADE80]/20 text-[#4ADE80] hover:bg-[#4ADE80]/15 hover:border-[#4ADE80]/40"
            }
          `}
        >
          Верно
        </button>
        <button
          type="button"
          onClick={() => handleChoice(false)}
          disabled={answered !== null}
          className={`
            py-4 rounded-xl border text-base font-bold transition-all duration-200 cursor-pointer disabled:cursor-default
            ${
              answered === false
                ? isWrong
                  ? "bg-red-500/15 border-red-500/40 text-red-400"
                  : "bg-success/15 border-success/40 text-success"
                : "bg-[#F87171]/8 border-[#F87171]/20 text-[#F87171] hover:bg-[#F87171]/15 hover:border-[#F87171]/40"
            }
          `}
        >
          Неверно
        </button>
      </div>
    </div>
  );
}

// ── Flashcards ──────────────────────────────────────────────────────────────

function FlashcardsStep({
  step,
  onAnswer,
}: {
  step: StepFlashcards;
  onAnswer: (correct: boolean) => void;
}) {
  const [cardIndex, setCardIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [seen, setSeen] = useState<Set<number>>(new Set());

  const card = step.cards[cardIndex];
  const allSeen = seen.size === step.cards.length;

  const handleFlip = () => setFlipped((f) => !f);

  const handleNext = () => {
    setSeen((prev) => new Set(prev).add(cardIndex));
    if (cardIndex < step.cards.length - 1) {
      setCardIndex((i) => i + 1);
      setFlipped(false);
    }
    // On the last card "handleNext" is not wired to the button — "Готово" calls onAnswer directly
  };

  return (
    <div className="space-y-5">
      <div className="flex items-center justify-between">
        <p className="text-base font-semibold text-text">Карточки</p>
        <span className="text-xs text-text-secondary">
          {cardIndex + 1} / {step.cards.length}
        </span>
      </div>

      {/* Flip card */}
      <div
        className="relative w-full cursor-pointer"
        style={{ perspective: 1000 }}
        onClick={handleFlip}
      >
        <motion.div
          animate={{ rotateY: flipped ? 180 : 0 }}
          transition={{ duration: 0.45, ease: "easeInOut" }}
          style={{ transformStyle: "preserve-3d" }}
          className="relative w-full"
        >
          {/* Front */}
          <div
            style={{ backfaceVisibility: "hidden" }}
            className="w-full min-h-[160px] bg-[#0A0A0A] border border-white/6 rounded-2xl p-6 flex flex-col items-center justify-center text-center"
          >
            <span className="text-xs text-text-secondary mb-3 uppercase tracking-widest">
              Вопрос
            </span>
            <p className="text-base font-semibold text-text">{card.front}</p>
            <span className="mt-4 text-xs text-text-secondary/50">
              Нажмите, чтобы перевернуть
            </span>
          </div>

          {/* Back */}
          <div
            style={{
              backfaceVisibility: "hidden",
              transform: "rotateY(180deg)",
              position: "absolute",
              inset: 0,
            }}
            className="w-full min-h-[160px] bg-[#F97316]/8 border border-[#F97316]/20 rounded-2xl p-6 flex flex-col items-center justify-center text-center"
          >
            <span className="text-xs text-[#F97316]/70 mb-3 uppercase tracking-widest">
              Ответ
            </span>
            <p className="text-base font-semibold text-text">{card.back}</p>
          </div>
        </motion.div>
      </div>

      {/* Progress dots */}
      <div className="flex justify-center gap-1.5">
        {step.cards.map((_, i) => (
          <div
            key={i}
            className={`h-1.5 rounded-full transition-all duration-300 ${
              i === cardIndex
                ? "w-4 bg-[#F97316]"
                : seen.has(i)
                ? "w-1.5 bg-success/60"
                : "w-1.5 bg-white/15"
            }`}
          />
        ))}
      </div>

      {/* When all non-last cards are seen and we're on the last card flipped — show Готово directly */}
      {flipped && cardIndex === step.cards.length - 1 ? (
        <Button className="w-full" onClick={() => onAnswer(true)}>
          <CheckCircle2 size={16} /> Готово
        </Button>
      ) : allSeen ? (
        <Button className="w-full" onClick={() => onAnswer(true)}>
          <CheckCircle2 size={16} /> Готово
        </Button>
      ) : (
        <div className="flex gap-2">
          {flipped && (
            <Button className="flex-1" onClick={handleNext}>
              Следующая <ArrowRight size={15} />
            </Button>
          )}
          {!flipped && (
            <Button variant="secondary" className="flex-1" onClick={handleFlip}>
              Перевернуть
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Type Answer ─────────────────────────────────────────────────────────────

function TypeAnswerStep({
  step,
  onAnswer,
}: {
  step: StepTypeAnswer;
  onAnswer: (correct: boolean) => void;
}) {
  const [value, setValue] = useState("");
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleCheck = () => {
    const trimmed = value.trim().toLowerCase();
    const correct = step.acceptedAnswers.some(
      (a) => a.trim().toLowerCase() === trimmed
    );
    setIsCorrect(correct);
    setChecked(true);
  };

  const handleRetry = () => {
    setValue("");
    setChecked(false);
    setIsCorrect(false);
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        {step.question}
      </p>

      <div className="space-y-2">
        <input
          type="text"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !checked && value.trim() && handleCheck()}
          disabled={checked}
          placeholder="Введите ответ..."
          className={`
            w-full px-4 py-3 rounded-xl border text-sm bg-white/5 outline-none transition-colors
            disabled:cursor-default
            ${
              checked
                ? isCorrect
                  ? "border-success/60 bg-success/10 text-success"
                  : "border-red-500/60 bg-red-500/10 text-red-400"
                : "border-white/15 text-text focus:border-[#F97316]/50"
            }
          `}
        />
      </div>

      {checked && !isCorrect && (
        <div className="space-y-1">
          <p className="text-xs text-text-secondary">Правильные варианты:</p>
          {step.acceptedAnswers.map((ans, i) => (
            <p key={i} className="text-xs text-success font-medium">
              {ans}
            </p>
          ))}
        </div>
      )}

      {!checked ? (
        <Button
          className="w-full"
          onClick={handleCheck}
          disabled={value.trim() === ""}
        >
          Проверить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {isCorrect ? (
              <><CheckCircle2 size={16} /> Правильно!</>
            ) : (
              <>Неверно. Попробуйте ещё раз.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Image Hotspot ───────────────────────────────────────────────────────────

function ImageHotspotStep({
  step,
  onAnswer,
}: {
  step: StepImageHotspot;
  onAnswer: (correct: boolean) => void;
}) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [click, setClick] = useState<{ x: number; y: number } | null>(null);
  const [correct, setCorrect] = useState<boolean | null>(null);

  const handleImageClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (correct !== null) return;
    const rect = containerRef.current!.getBoundingClientRect();
    // Convert to percentage
    const xPct = ((e.clientX - rect.left) / rect.width) * 100;
    const yPct = ((e.clientY - rect.top) / rect.height) * 100;

    const dx = xPct - step.hotspot.x;
    const dy = yPct - step.hotspot.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const isHit = distance <= step.hotspot.radius;

    setClick({ x: xPct, y: yPct });
    setCorrect(isHit);
    if (isHit) {
      // Advance after a brief moment so the user sees the hit marker
      setTimeout(() => onAnswer(true), 1200);
    } else {
      // Show miss feedback, then reset so the user can try again
      setTimeout(() => {
        setClick(null);
        setCorrect(null);
      }, 1500);
    }
  };

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text leading-snug">
        {step.question}
      </p>
      <p className="text-xs text-text-secondary">
        Нажмите на правильное место на изображении
      </p>

      <div
        ref={containerRef}
        onClick={handleImageClick}
        className={`relative w-full rounded-xl overflow-hidden border ${
          correct !== null ? "cursor-default" : "cursor-crosshair"
        } border-white/10`}
      >
        <img
          src={step.imageUrl}
          alt="hotspot"
          className="w-full h-auto block"
          draggable={false}
        />

        {/* Click feedback circle */}
        {click && (
          <motion.div
            initial={{ scale: 0, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ type: "spring", stiffness: 300, damping: 18 }}
            style={{
              position: "absolute",
              left: `${click.x}%`,
              top: `${click.y}%`,
              transform: "translate(-50%, -50%)",
            }}
            className={`w-8 h-8 rounded-full border-2 ${
              correct
                ? "bg-[#4ADE80]/40 border-[#4ADE80]"
                : "bg-[#F87171]/40 border-[#F87171]"
            }`}
          />
        )}
      </div>

      {correct !== null && (
        <motion.div
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
            correct
              ? "bg-[#4ADE80]/15 border-[#4ADE80]/30 text-[#4ADE80]"
              : "bg-[#F87171]/15 border-[#F87171]/30 text-[#F87171]"
          }`}
        >
          {correct ? (
            <><CheckCircle2 size={16} /> Точное попадание!</>
          ) : (
            <>Мимо. Попробуйте ещё раз.</>
          )}
        </motion.div>
      )}
    </div>
  );
}

// ── Code Editor ─────────────────────────────────────────────────────────────

function CodeEditorStep({
  step,
  onAnswer,
}: {
  step: StepCodeEditor;
  onAnswer: (correct: boolean) => void;
}) {
  const [code, setCode] = useState(step.starterCode);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const extensions = useMemo(() => {
    const lang = step.language || "typescript";
    if (lang === "javascript" || lang === "js") return [javascript()];
    if (lang === "typescript" || lang === "ts") return [javascript({ typescript: true })];
    if (lang === "tsx" || lang === "jsx") return [javascript({ typescript: lang === "tsx", jsx: true })];
    if (lang === "html") return [html()];
    if (lang === "css") return [css()];
    return [javascript({ typescript: true })];
  }, [step.language]);

  const handleRun = () => {
    const correct = code.includes(step.expectedOutput);
    setIsCorrect(correct);
    setChecked(true);
  };

  const handleRetry = () => {
    setCode(step.starterCode);
    setChecked(false);
    setIsCorrect(false);
  };

  return (
    <div className="space-y-4">
      <p className="text-base font-semibold text-text leading-snug">
        {step.prompt}
      </p>

      {/* Code Editor */}
      <div className="rounded-xl overflow-hidden border border-white/6 bg-[#0A0A0A]">
        {/* Editor header */}
        <div className="flex items-center justify-between px-4 py-2 bg-white/[0.03] border-b border-white/6">
          <div className="flex items-center gap-2">
            <span className="w-3 h-3 rounded-full bg-[#FF5F57]" />
            <span className="w-3 h-3 rounded-full bg-[#FEBC2E]" />
            <span className="w-3 h-3 rounded-full bg-[#28C840]" />
          </div>
          <span className="text-[11px] font-mono text-white/30 uppercase tracking-wider">
            {step.language || "typescript"}
          </span>
        </div>

        <CodeMirror
          value={code}
          onChange={(val) => setCode(val)}
          editable={!checked}
          extensions={extensions}
          theme="dark"
          basicSetup={{
            lineNumbers: true,
            highlightActiveLineGutter: true,
            highlightActiveLine: true,
            foldGutter: false,
            autocompletion: false,
          }}
          style={{ fontSize: "13px" }}
          className="[&_.cm-editor]:!bg-[#0A0A0A] [&_.cm-gutters]:!bg-[#0A0A0A] [&_.cm-gutters]:!border-r [&_.cm-gutters]:!border-white/6 [&_.cm-activeLineGutter]:!bg-white/[0.04] [&_.cm-activeLine]:!bg-white/[0.03] [&_.cm-cursor]:!border-[#F97316] [&_.cm-selectionBackground]:!bg-[#F97316]/20 [&_.cm-focused]:!outline-none"
          minHeight="160px"
        />
      </div>

      {/* Expected output hint on failure */}
      {checked && !isCorrect && (
        <div className="space-y-1.5">
          <p className="text-xs text-white/30">Ожидаемый фрагмент в вашем решении:</p>
          <div className="rounded-xl overflow-hidden border border-white/6 bg-[#0A0A0A]">
            <div className="px-4 py-2 bg-white/[0.03] border-b border-white/6">
              <span className="text-[11px] font-mono text-white/30">expected</span>
            </div>
            <pre className="px-4 py-3 text-[13px] font-mono text-[#F97316] overflow-x-auto">
              {step.expectedOutput}
            </pre>
          </div>
        </div>
      )}

      {/* Actions */}
      {!checked ? (
        <Button className="w-full" onClick={handleRun}>
          <Play size={14} /> Запустить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-[#4ADE80]/10 border-[#4ADE80]/30 text-[#4ADE80]"
                : "bg-[#F87171]/10 border-[#F87171]/30 text-[#F87171]"
            }`}
          >
            {isCorrect ? (
              <><CheckCircle2 size={16} /> Тест пройден!</>
            ) : (
              <>Результат не совпадает. Попробуйте ещё раз.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Timeline ────────────────────────────────────────────────────────────────

function TimelineStep({
  step,
  onAnswer,
}: {
  step: StepTimeline;
  onAnswer: (correct: boolean) => void;
}) {
  const shuffled = useMemo(
    () => shuffle(step.events.map((e) => e.label)),
    [step]
  );
  const [order, setOrder] = useState<string[]>(shuffled);
  const [selected, setSelected] = useState<number | null>(null);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleTap = (index: number) => {
    if (checked) return;
    if (selected === null) {
      setSelected(index);
    } else {
      const next = [...order];
      [next[selected], next[index]] = [next[index], next[selected]];
      setOrder(next);
      setSelected(null);
    }
  };

  const handleCheck = () => {
    const correct = order.every((label, i) => label === step.events[i].label);
    setIsCorrect(correct);
    setChecked(true);
  };

  const handleRetry = () => {
    setOrder(shuffle(step.events.map((e) => e.label)));
    setChecked(false);
    setIsCorrect(false);
    setSelected(null);
  };

  // Build a lookup: label -> year (shown only after checking)
  const yearByLabel = Object.fromEntries(
    step.events.map((e) => [e.label, e.year])
  );

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        Расставьте события в хронологическом порядке
      </p>
      <p className="text-xs text-text-secondary">
        Нажмите на событие, затем на место, куда его переместить
      </p>

      <div className="space-y-2">
        {order.map((label, i) => {
          const isSelected = selected === i;
          const correctLabel = step.events[i]?.label;
          const isItemCorrect = checked ? label === correctLabel : null;

          let borderClass = "border-white/10";
          let bgClass = "bg-white/5";
          if (checked && isItemCorrect) {
            borderClass = "border-success/50";
            bgClass = "bg-success/8";
          } else if (checked && !isItemCorrect) {
            borderClass = "border-red-500/50";
            bgClass = "bg-red-500/8";
          } else if (isSelected) {
            borderClass = "border-[#F97316]/60";
            bgClass = "bg-[#F97316]/10";
          }

          return (
            <motion.button
              key={`${label}-${i}`}
              type="button"
              onClick={() => handleTap(i)}
              disabled={checked}
              layout
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl border transition-colors duration-200 cursor-pointer disabled:cursor-default text-sm ${borderClass} ${bgClass}`}
            >
              <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-xs font-mono text-text-secondary">
                {i + 1}
              </span>
              <span className="text-text text-left flex-1">{label}</span>
              {checked && (
                <span className={`text-xs font-mono ${isItemCorrect ? "text-success/80" : "text-red-400/80"}`}>
                  {yearByLabel[label]}
                </span>
              )}
              {isSelected && !checked && (
                <span className="ml-auto text-[#F97316] text-xs">выбрано</span>
              )}
            </motion.button>
          );
        })}
      </div>

      {!checked ? (
        <Button className="w-full" onClick={handleCheck} disabled={selected !== null}>
          Проверить порядок
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {isCorrect ? (
              <><CheckCircle2 size={16} /> Хронология верна!</>
            ) : (
              <>Порядок неверный. Попробуйте ещё раз.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Category Sort ───────────────────────────────────────────────────────────

function CategorySortStep({
  step,
  onAnswer,
}: {
  step: StepCategorySort;
  onAnswer: (correct: boolean) => void;
}) {
  // placements: itemText -> categoryName
  const [placements, setPlacements] = useState<Record<string, string>>({});
  const [selectedItem, setSelectedItem] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);
  const [results, setResults] = useState<Record<string, boolean>>({});

  const unplacedItems = step.items.filter((item) => !placements[item.text]);

  const handleItemTap = (itemText: string) => {
    if (checked) return;
    setSelectedItem((prev) => (prev === itemText ? null : itemText));
  };

  const handleCategoryTap = (category: string) => {
    if (!selectedItem || checked) return;
    setPlacements((prev) => ({ ...prev, [selectedItem]: category }));
    setSelectedItem(null);
  };

  const handleCheck = () => {
    const res: Record<string, boolean> = {};
    step.items.forEach((item) => {
      res[item.text] = placements[item.text] === item.category;
    });
    setResults(res);
    setChecked(true);
  };

  const handleRetry = () => {
    setPlacements({});
    setSelectedItem(null);
    setChecked(false);
    setResults({});
  };

  const allPlaced = step.items.every((item) => placements[item.text]);
  const allCorrect = checked && step.items.every((item) => results[item.text]);

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        Распределите по категориям
      </p>
      <p className="text-xs text-text-secondary">
        Выберите элемент, затем нажмите на категорию
      </p>

      {/* Category columns */}
      <div className="grid gap-3" style={{ gridTemplateColumns: `repeat(${step.categories.length}, 1fr)` }}>
        {step.categories.map((cat) => {
          const itemsInCat = step.items.filter(
            (item) => placements[item.text] === cat
          );
          const isTargetable = selectedItem !== null && !checked;

          return (
            <div key={cat} className="space-y-2">
              <button
                type="button"
                onClick={() => handleCategoryTap(cat)}
                disabled={!isTargetable}
                className={`w-full text-center px-3 py-2 rounded-xl border text-xs font-semibold uppercase tracking-wider transition-all duration-200
                  ${
                    isTargetable
                      ? "border-[#F97316]/50 bg-[#F97316]/10 text-[#F97316] cursor-pointer hover:bg-[#F97316]/20"
                      : "border-white/10 bg-white/5 text-text-secondary cursor-default"
                  }`}
              >
                {cat}
              </button>

              <div className="min-h-[48px] rounded-xl border border-dashed border-white/10 p-2 space-y-1.5">
                {itemsInCat.map((item) => {
                  const isCorrectItem = checked ? results[item.text] : null;
                  return (
                    <div
                      key={item.text}
                      className={`px-2.5 py-1.5 rounded-lg border text-xs font-medium text-center transition-colors ${
                        checked && isCorrectItem
                          ? "border-success/40 bg-success/10 text-success"
                          : checked && !isCorrectItem
                          ? "border-red-500/40 bg-red-500/10 text-red-400"
                          : "border-white/15 bg-white/8 text-text"
                      }`}
                    >
                      {item.text}
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>

      {/* Unplaced item chips */}
      {unplacedItems.length > 0 && (
        <div>
          <p className="text-xs text-text-secondary mb-2">Элементы:</p>
          <div className="flex flex-wrap gap-2">
            {unplacedItems.map((item) => {
              const isActive = selectedItem === item.text;
              return (
                <button
                  key={item.text}
                  type="button"
                  onClick={() => handleItemTap(item.text)}
                  disabled={checked}
                  className={`px-3 py-1.5 rounded-lg border text-xs font-medium transition-all cursor-pointer disabled:cursor-default ${
                    isActive
                      ? "border-[#F97316]/60 bg-[#F97316]/15 text-[#F97316]"
                      : "border-white/15 bg-white/5 text-text hover:bg-white/10 hover:border-white/25"
                  }`}
                >
                  {item.text}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {!checked ? (
        <Button className="w-full" onClick={handleCheck} disabled={!allPlaced}>
          Проверить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              allCorrect
                ? "bg-success/10 border-success/40 text-success"
                : "bg-red-500/10 border-red-500/40 text-red-400"
            }`}
          >
            {allCorrect ? (
              <><CheckCircle2 size={16} /> Все элементы на своих местах!</>
            ) : (
              <>Некоторые элементы не там. Попробуйте снова.</>
            )}
          </div>
          {allCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Video ───────────────────────────────────────────────────────────────────

function VideoStep({ step, onNext }: { step: StepVideo; onNext: () => void }) {
  const isYouTube =
    step.url.includes("youtube.com") || step.url.includes("youtu.be");

  // Convert watch URLs to embed URLs if needed
  const embedUrl = isYouTube
    ? step.url
        .replace("watch?v=", "embed/")
        .replace("youtu.be/", "www.youtube.com/embed/")
    : step.url;

  return (
    <div className="space-y-4">
      {step.title && (
        <h2 className="text-xl font-bold text-text">{step.title}</h2>
      )}

      <div className="w-full rounded-xl overflow-hidden border border-white/10 bg-[#0A0A0A]">
        {isYouTube ? (
          <iframe
            src={embedUrl}
            title={step.title}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            className="w-full aspect-video"
          />
        ) : (
          // eslint-disable-next-line jsx-a11y/media-has-caption
          <video
            src={step.url}
            controls
            className="w-full aspect-video"
            preload="metadata"
          />
        )}
      </div>

      <Button className="w-full" onClick={onNext}>
        Далее <ArrowRight size={15} />
      </Button>
    </div>
  );
}

// ── Audio ───────────────────────────────────────────────────────────────────

function AudioStep({ step, onNext }: { step: StepAudio; onNext: () => void }) {
  return (
    <div className="space-y-4">
      {step.title && (
        <h2 className="text-xl font-bold text-text">{step.title}</h2>
      )}

      <div className="w-full rounded-xl border border-white/10 bg-[#0A0A0A] p-4">
        {/* eslint-disable-next-line jsx-a11y/media-has-caption */}
        <audio
          src={step.url}
          controls
          preload="metadata"
          className="w-full"
        />
      </div>

      {step.transcript && (
        <div className="rounded-xl border border-white/6 bg-white/3 p-4 max-h-40 overflow-y-auto">
          <p className="text-xs text-text-secondary mb-2 uppercase tracking-widest">
            Транскрипт
          </p>
          <p className="text-sm text-text-secondary leading-relaxed whitespace-pre-wrap">
            {step.transcript}
          </p>
        </div>
      )}

      <Button className="w-full" onClick={onNext}>
        Далее <ArrowRight size={15} />
      </Button>
    </div>
  );
}

// ── Embed ───────────────────────────────────────────────────────────────────

function EmbedStep({ step, onNext }: { step: StepEmbed; onNext: () => void }) {
  return (
    <div className="space-y-4">
      {step.title && (
        <h2 className="text-xl font-bold text-text">{step.title}</h2>
      )}

      <div
        className="w-full rounded-xl overflow-hidden border border-white/10 bg-[#0A0A0A]"
        style={{ height: step.height ?? 400 }}
      >
        <iframe
          src={step.url}
          title={step.title}
          className="w-full h-full"
          sandbox="allow-scripts allow-same-origin allow-popups allow-forms"
        />
      </div>

      <Button className="w-full" onClick={onNext}>
        Далее <ArrowRight size={15} />
      </Button>
    </div>
  );
}

// ── Terminal Sim ─────────────────────────────────────────────────────────────

function TerminalSimStep({
  step,
  onAnswer,
}: {
  step: StepTerminalSim;
  onAnswer: (correct: boolean) => void;
}) {
  const [command, setCommand] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const [outputVisible, setOutputVisible] = useState(false);

  const handleSubmit = () => {
    if (!command.trim()) return;
    const correct = command === step.expectedCommand;
    setIsCorrect(correct);
    setSubmitted(true);
    if (correct) {
      setOutputVisible(true);
      setTimeout(() => onAnswer(true), 1500);
    }
  };

  const handleRetry = () => {
    setCommand("");
    setSubmitted(false);
    setIsCorrect(false);
    setOutputVisible(false);
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        {step.prompt}
      </p>

      {/* Terminal container */}
      <div className="rounded-xl overflow-hidden border border-white/6 bg-[#0A0A0A]">
        {/* Terminal header */}
        <div className="flex items-center gap-2 px-4 py-2.5 bg-white/[0.03] border-b border-white/6">
          <span className="w-3 h-3 rounded-full bg-[#FF5F57]" />
          <span className="w-3 h-3 rounded-full bg-[#FEBC2E]" />
          <span className="w-3 h-3 rounded-full bg-[#28C840]" />
          <span className="ml-2 text-[11px] font-mono text-white/30 uppercase tracking-wider">terminal</span>
        </div>

        {/* Terminal body */}
        <div className="p-4 font-mono text-sm min-h-[100px]">
          {/* Command input line */}
          <div className="flex items-center gap-2">
            <span className="text-[#4ADE80] select-none flex-shrink-0">$</span>
            <input
              type="text"
              value={command}
              onChange={(e) => setCommand(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !submitted && command.trim()) handleSubmit();
              }}
              disabled={submitted}
              placeholder="Введите команду..."
              autoComplete="off"
              spellCheck={false}
              className="flex-1 bg-transparent outline-none text-[#4ADE80] placeholder:text-white/20 disabled:cursor-default caret-[#4ADE80]"
            />
          </div>

          {/* Output after correct command */}
          {outputVisible && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.3 }}
              className="mt-2 text-white/60 whitespace-pre-wrap"
            >
              {step.output}
            </motion.div>
          )}

          {/* Wrong command feedback */}
          {submitted && !isCorrect && (
            <p className="mt-2 text-[#F87171]">
              Неверная команда. Попробуйте снова.
            </p>
          )}
        </div>
      </div>

      {/* Hint */}
      {step.hint && (
        <div>
          {!showHint ? (
            <button
              type="button"
              onClick={() => setShowHint(true)}
              className="text-xs text-text-secondary hover:text-text transition-colors cursor-pointer underline underline-offset-2"
            >
              Показать подсказку
            </button>
          ) : (
            <div className="px-4 py-3 rounded-xl border border-[#F59E0B]/20 bg-[#F59E0B]/8 text-[#F59E0B] text-sm">
              {step.hint}
            </div>
          )}
        </div>
      )}

      {/* Actions */}
      {!submitted ? (
        <Button
          className="w-full"
          onClick={handleSubmit}
          disabled={!command.trim()}
        >
          Выполнить
        </Button>
      ) : !isCorrect ? (
        <Button variant="secondary" className="w-full" onClick={handleRetry}>
          <RotateCcw size={14} /> Попробовать снова
        </Button>
      ) : null}
    </div>
  );
}

// ── Multi-Select ─────────────────────────────────────────────────────────────

function MultiSelectStep({
  step,
  onAnswer,
}: {
  step: StepMultiSelect;
  onAnswer: (correct: boolean) => void;
}) {
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const toggleOption = (id: string) => {
    if (checked) return;
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const handleCheck = () => {
    const correctIds = new Set(
      step.options.filter((o) => o.correct).map((o) => o.id)
    );
    const allMatch =
      correctIds.size === selected.size &&
      [...selected].every((id) => correctIds.has(id));
    setIsCorrect(allMatch);
    setChecked(true);
  };

  const handleRetry = () => {
    setSelected(new Set());
    setChecked(false);
    setIsCorrect(false);
  };

  const correctIds = new Set(step.options.filter((o) => o.correct).map((o) => o.id));

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        {step.question}
      </p>
      <p className="text-xs text-text-secondary">
        Выберите все правильные ответы
      </p>

      <div className="space-y-2.5">
        {step.options.map((option) => {
          const isSelected = selected.has(option.id);
          const isOptionCorrect = option.correct;

          let borderClass = "border-white/10 hover:border-white/25";
          let bgClass = "bg-white/5 hover:bg-white/8";
          let textClass = "text-text";
          let checkboxClass = "border-white/30 bg-transparent";

          if (checked) {
            if (isSelected && isOptionCorrect) {
              borderClass = "border-[#4ADE80]/50";
              bgClass = "bg-[#4ADE80]/8";
              textClass = "text-[#4ADE80]";
              checkboxClass = "border-[#4ADE80] bg-[#4ADE80]";
            } else if (isSelected && !isOptionCorrect) {
              borderClass = "border-[#F87171]/50";
              bgClass = "bg-[#F87171]/8";
              textClass = "text-[#F87171]";
              checkboxClass = "border-[#F87171] bg-[#F87171]";
            } else if (!isSelected && isOptionCorrect) {
              // Missed a correct answer — highlight it
              borderClass = "border-[#4ADE80]/30";
              bgClass = "bg-[#4ADE80]/5";
              textClass = "text-[#4ADE80]/70";
              checkboxClass = "border-[#4ADE80]/50 bg-transparent";
            }
          } else if (isSelected) {
            borderClass = "border-[#F97316]/50";
            bgClass = "bg-[#F97316]/8";
            checkboxClass = "border-[#F97316] bg-[#F97316]";
          }

          return (
            <button
              key={option.id}
              type="button"
              onClick={() => toggleOption(option.id)}
              disabled={checked}
              className={`
                w-full flex items-center gap-3 px-4 py-3 rounded-xl border
                transition-all duration-200 cursor-pointer disabled:cursor-default text-sm font-medium text-left
                ${borderClass} ${bgClass} ${textClass}
              `}
            >
              <span
                className={`flex-shrink-0 w-5 h-5 rounded border-2 flex items-center justify-center transition-all ${checkboxClass}`}
              >
                {(isSelected || (checked && isOptionCorrect)) && (
                  <Check size={11} className="text-white" />
                )}
              </span>
              {option.text}
            </button>
          );
        })}
      </div>

      {!checked ? (
        <Button
          className="w-full"
          onClick={handleCheck}
          disabled={selected.size === 0}
        >
          Проверить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-[#4ADE80]/10 border-[#4ADE80]/30 text-[#4ADE80]"
                : "bg-[#F87171]/10 border-[#F87171]/30 text-[#F87171]"
            }`}
          >
            {isCorrect ? (
              <><CheckCircle2 size={16} /> Все правильные ответы выбраны!</>
            ) : (
              <>Не все ответы верны. Попробуйте снова.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Conversation Sim ─────────────────────────────────────────────────────────

function ConversationSimStep({
  step,
  onAnswer,
}: {
  step: StepConversationSim;
  onAnswer: (correct: boolean) => void;
}) {
  const [selectedChoiceId, setSelectedChoiceId] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<string | null>(null);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleChoice = (choice: StepConversationSim["choices"][number]) => {
    if (selectedChoiceId !== null) return;
    setSelectedChoiceId(choice.id);
    setFeedback(choice.feedback);
    setIsCorrect(choice.correct);
    if (choice.correct) {
      setTimeout(() => onAnswer(true), 1400);
    }
  };

  const handleRetry = () => {
    setSelectedChoiceId(null);
    setFeedback(null);
    setIsCorrect(false);
  };

  return (
    <div className="space-y-5">
      {/* Scenario context */}
      <div className="px-4 py-3 rounded-xl bg-white/[0.04] border border-white/8 text-xs text-text-secondary leading-relaxed">
        <span className="font-semibold text-white/50 uppercase tracking-wider text-[10px] block mb-1">
          Сценарий
        </span>
        {step.scenario}
      </div>

      {/* Chat messages */}
      <div className="space-y-3">
        {step.messages.map((msg, i) => (
          <div
            key={i}
            className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] px-4 py-2.5 rounded-2xl text-sm leading-relaxed ${
                msg.role === "user"
                  ? "bg-[#F97316]/15 border border-[#F97316]/25 text-text rounded-tr-sm"
                  : "bg-white/[0.06] border border-white/8 text-text-secondary rounded-tl-sm"
              }`}
            >
              {msg.text}
            </div>
          </div>
        ))}
      </div>

      {/* Feedback after selection */}
      {feedback && (
        <motion.div
          initial={{ opacity: 0, y: -6 }}
          animate={{ opacity: 1, y: 0 }}
          className={`px-4 py-3 rounded-xl border text-sm font-medium ${
            isCorrect
              ? "bg-[#4ADE80]/10 border-[#4ADE80]/30 text-[#4ADE80]"
              : "bg-[#F87171]/10 border-[#F87171]/30 text-[#F87171]"
          }`}
        >
          {feedback}
        </motion.div>
      )}

      {/* Choices */}
      {selectedChoiceId === null ? (
        <div className="space-y-2">
          <p className="text-xs text-text-secondary">Выберите лучший ответ:</p>
          {step.choices.map((choice) => (
            <button
              key={choice.id}
              type="button"
              onClick={() => handleChoice(choice)}
              className="w-full text-left px-4 py-3 rounded-xl border border-white/10 bg-white/5 text-text text-sm hover:border-[#F97316]/40 hover:bg-[#F97316]/8 transition-all duration-200 cursor-pointer"
            >
              {choice.text}
            </button>
          ))}
        </div>
      ) : !isCorrect ? (
        <Button variant="secondary" className="w-full" onClick={handleRetry}>
          <RotateCcw size={14} /> Попробовать снова
        </Button>
      ) : null}
    </div>
  );
}

// ── Highlight Text ───────────────────────────────────────────────────────────

function HighlightTextStep({
  step,
  onAnswer,
}: {
  step: StepHighlightText;
  onAnswer: (correct: boolean) => void;
}) {
  const [highlighted, setHighlighted] = useState<Set<number>>(new Set());
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const toggleSegment = (index: number) => {
    if (checked) return;
    setHighlighted((prev) => {
      const next = new Set(prev);
      if (next.has(index)) next.delete(index);
      else next.add(index);
      return next;
    });
  };

  const handleCheck = () => {
    const correctIndices = new Set(
      step.segments
        .map((s, i) => (s.correct ? i : -1))
        .filter((i) => i !== -1)
    );
    const allMatch =
      correctIndices.size === highlighted.size &&
      [...highlighted].every((i) => correctIndices.has(i));
    setIsCorrect(allMatch);
    setChecked(true);
  };

  const handleRetry = () => {
    setHighlighted(new Set());
    setChecked(false);
    setIsCorrect(false);
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        {step.instruction}
      </p>
      <p className="text-xs text-text-secondary">
        Нажмите на слова или фразы, которые нужно выделить
      </p>

      {/* Segments */}
      <div className="bg-[#0A0A0A] border border-white/6 rounded-xl p-4 leading-loose">
        {step.segments.map((seg, i) => {
          const isHighlighted = highlighted.has(i);
          const isSegCorrect = seg.correct;

          let cls = "cursor-pointer rounded px-0.5 transition-all duration-150";
          if (checked) {
            if (isHighlighted && isSegCorrect) {
              cls += " bg-[#4ADE80]/25 text-[#4ADE80]";
            } else if (isHighlighted && !isSegCorrect) {
              cls += " bg-[#F87171]/25 text-[#F87171]";
            } else if (!isHighlighted && isSegCorrect) {
              cls += " bg-[#F59E0B]/20 text-[#F59E0B]";
            } else {
              cls += " text-text";
            }
          } else if (isHighlighted) {
            cls += " bg-[#F97316]/25 text-[#F97316]";
          } else {
            cls += " text-text hover:bg-white/10";
          }

          return (
            <span
              key={i}
              onClick={() => toggleSegment(i)}
              className={cls}
            >
              {seg.text}
            </span>
          );
        })}
      </div>

      {!checked ? (
        <Button
          className="w-full"
          onClick={handleCheck}
          disabled={highlighted.size === 0}
        >
          Проверить
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-[#4ADE80]/10 border-[#4ADE80]/30 text-[#4ADE80]"
                : "bg-[#F87171]/10 border-[#F87171]/30 text-[#F87171]"
            }`}
          >
            {isCorrect ? (
              <><CheckCircle2 size={16} /> Правильно выделено!</>
            ) : (
              <>Не все выделения верны. Попробуйте снова.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ── Snippet Order ─────────────────────────────────────────────────────────────

function SnippetOrderStep({
  step,
  onAnswer,
}: {
  step: StepSnippetOrder;
  onAnswer: (correct: boolean) => void;
}) {
  const shuffled = useMemo(() => shuffle(step.fragments), [step]);
  const [order, setOrder] = useState<string[]>(shuffled);
  const [selected, setSelected] = useState<number | null>(null);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleTap = (index: number) => {
    if (checked) return;
    if (selected === null) {
      setSelected(index);
    } else {
      const next = [...order];
      [next[selected], next[index]] = [next[index], next[selected]];
      setOrder(next);
      setSelected(null);
    }
  };

  const handleCheck = () => {
    const correct = order.every((frag, i) => frag === step.fragments[i]);
    setIsCorrect(correct);
    setChecked(true);
  };

  const handleRetry = () => {
    setOrder(shuffle(step.fragments));
    setChecked(false);
    setIsCorrect(false);
    setSelected(null);
  };

  return (
    <div className="space-y-5">
      <p className="text-base font-semibold text-text leading-snug">
        {step.instruction || "Соберите фрагменты в правильном порядке"}
      </p>
      <p className="text-xs text-text-secondary">
        Нажмите на фрагмент, затем на место, куда его переместить
      </p>

      <div className="space-y-2">
        {order.map((frag, i) => {
          const isItemSelected = selected === i;
          const isItemCorrect = checked ? frag === step.fragments[i] : null;

          let borderClass = "border-white/10";
          let bgClass = "bg-white/5";

          if (checked) {
            borderClass = isItemCorrect ? "border-[#4ADE80]/50" : "border-[#F87171]/50";
            bgClass = isItemCorrect ? "bg-[#4ADE80]/8" : "bg-[#F87171]/8";
          } else if (isItemSelected) {
            borderClass = "border-[#F97316]/60";
            bgClass = "bg-[#F97316]/10";
          }

          return (
            <motion.button
              key={`${frag}-${i}`}
              type="button"
              onClick={() => handleTap(i)}
              disabled={checked}
              layout
              className={`
                w-full flex items-center gap-3 px-4 py-3 rounded-xl border
                transition-colors duration-200 cursor-pointer disabled:cursor-default text-sm
                ${borderClass} ${bgClass}
              `}
            >
              <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-xs font-mono text-text-secondary">
                {i + 1}
              </span>
              <span className="text-text text-left flex-1">{frag}</span>
              {isItemSelected && !checked && (
                <span className="ml-auto text-[#F97316] text-xs">выбрано</span>
              )}
            </motion.button>
          );
        })}
      </div>

      {!checked ? (
        <Button
          className="w-full"
          onClick={handleCheck}
          disabled={selected !== null}
        >
          Проверить порядок
        </Button>
      ) : (
        <div className="space-y-3">
          <div
            className={`flex items-center gap-2 px-4 py-3 rounded-xl border text-sm font-medium ${
              isCorrect
                ? "bg-[#4ADE80]/10 border-[#4ADE80]/30 text-[#4ADE80]"
                : "bg-[#F87171]/10 border-[#F87171]/30 text-[#F87171]"
            }`}
          >
            {isCorrect ? (
              <><CheckCircle2 size={16} /> Правильный порядок!</>
            ) : (
              <>Порядок неверный. Попробуйте ещё раз.</>
            )}
          </div>
          {isCorrect ? (
            <Button className="w-full" onClick={() => onAnswer(true)}>
              Продолжить <ArrowRight size={16} />
            </Button>
          ) : (
            <Button variant="secondary" className="w-full" onClick={handleRetry}>
              <RotateCcw size={14} /> Попробовать снова
            </Button>
          )}
        </div>
      )}
    </div>
  );
}

// ─── Congratulations screen ────────────────────────────────────────────────

function CongratsScreen({
  lessonTitle,
  onClose,
}: {
  lessonTitle: string;
  onClose: () => void;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.92 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
      className="flex flex-col items-center justify-center text-center px-6 py-10 space-y-6"
    >
      {/* Trophy icon */}
      <motion.div
        initial={{ scale: 0, rotate: -15 }}
        animate={{ scale: 1, rotate: 0 }}
        transition={{ delay: 0.15, type: "spring", stiffness: 220, damping: 14 }}
        className="w-24 h-24 rounded-full bg-[#F97316]/15 border border-[#F97316]/30 flex items-center justify-center text-5xl"
      >
        🏆
      </motion.div>

      <div className="space-y-2">
        <h2 className="text-2xl font-bold text-text">Урок завершён!</h2>
        <p className="text-text-secondary text-sm leading-relaxed max-w-xs">
          Вы успешно прошли урок{" "}
          <span className="text-text font-medium">«{lessonTitle}»</span>.
          XP начислены на ваш аккаунт.
        </p>
      </div>

      <div className="flex items-center gap-2 px-5 py-2.5 rounded-full bg-success/10 border border-success/30">
        <CheckCircle2 size={16} className="text-success" />
        <span className="text-success text-sm font-medium">+XP начислено</span>
      </div>

      <Button className="w-full max-w-xs" size="lg" onClick={onClose}>
        Вернуться к роадмапу
      </Button>
    </motion.div>
  );
}

// ─── Main component ────────────────────────────────────────────────────────

export interface CourseStepPlayerProps {
  steps: LessonStep[];
  lessonTitle: string;
  onComplete: () => void;
  onClose: () => void;
}

export function CourseStepPlayer({
  steps,
  lessonTitle,
  onComplete,
  onClose,
}: CourseStepPlayerProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [completed, setCompleted] = useState(false);
  const [showExitConfirm, setShowExitConfirm] = useState(false);
  // Direction for slide animation: 1 = forward, -1 = backward
  const [direction, setDirection] = useState(1);

  const currentStep = steps[currentIndex];
  const progress = ((currentIndex) / steps.length) * 100;
  const isLastStep = currentIndex === steps.length - 1;

  // Info step: shows "Далее" nav footer at the bottom of the card.
  // Video, audio, and embed render their own "Далее" button internally.
  const CONTENT_ONLY_TYPES = new Set(["info", "video", "audio", "embed"]);
  const isInfoStep = currentStep?.type === "info";
  // All content-only types (including info) never gate on a correct answer.
  const isContentOnly = CONTENT_ONLY_TYPES.has(currentStep?.type ?? "");

  const goForward = useCallback(() => {
    setDirection(1);
    if (isLastStep) {
      setCompleted(true);
      onComplete();
    } else {
      setCurrentIndex((i) => i + 1);
    }
  }, [isLastStep, onComplete]);

  const goBack = useCallback(() => {
    if (currentIndex === 0) return;
    setDirection(-1);
    setCurrentIndex((i) => i - 1);
  }, [currentIndex]);

  // Interactive steps call this when the user answers correctly
  const handleInteractiveAnswer = useCallback(
    (correct: boolean) => {
      if (correct) {
        goForward();
      }
      // Wrong answers are handled inside the step component with retry UI
    },
    [goForward]
  );

  const slideVariants = {
    enter: (dir: number) => ({
      x: dir > 0 ? 48 : -48,
      opacity: 0,
    }),
    center: { x: 0, opacity: 1 },
    exit: (dir: number) => ({
      x: dir > 0 ? -48 : 48,
      opacity: 0,
    }),
  };

  const renderStep = (step: LessonStep) => {
    switch (step.type) {
      case "info":
        return <InfoStep step={step as StepInfo} />;
      case "quiz":
        return (
          <QuizStep
            step={step as StepQuiz}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "drag-order":
        return (
          <DragOrderStep
            step={step as StepDragOrder}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "code-puzzle":
        return (
          <CodePuzzleStep
            step={step as StepCodePuzzle}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "fill-blank":
        return (
          <FillBlankStep
            step={step as StepFillBlank}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "matching":
        return (
          <MatchingStep
            step={step as StepMatching}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "true-false":
        return (
          <TrueFalseStep
            step={step as StepTrueFalse}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "flashcards":
        return (
          <FlashcardsStep
            step={step as StepFlashcards}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "type-answer":
        return (
          <TypeAnswerStep
            step={step as StepTypeAnswer}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "image-hotspot":
        return (
          <ImageHotspotStep
            step={step as StepImageHotspot}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "code-editor":
        return (
          <CodeEditorStep
            step={step as StepCodeEditor}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "timeline":
        return (
          <TimelineStep
            step={step as StepTimeline}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "category-sort":
        return (
          <CategorySortStep
            step={step as StepCategorySort}
            onAnswer={handleInteractiveAnswer}
          />
        );
      // Content-only steps — "Далее" footer handles navigation
      case "video":
        return <VideoStep step={step as StepVideo} onNext={goForward} />;
      case "audio":
        return <AudioStep step={step as StepAudio} onNext={goForward} />;
      case "embed":
        return <EmbedStep step={step as StepEmbed} onNext={goForward} />;
      case "terminal-sim":
        return (
          <TerminalSimStep
            step={step as StepTerminalSim}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "multi-select":
        return (
          <MultiSelectStep
            step={step as StepMultiSelect}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "conversation-sim":
        return (
          <ConversationSimStep
            step={step as StepConversationSim}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "highlight-text":
        return (
          <HighlightTextStep
            step={step as StepHighlightText}
            onAnswer={handleInteractiveAnswer}
          />
        );
      case "snippet-order":
        return (
          <SnippetOrderStep
            step={step as StepSnippetOrder}
            onAnswer={handleInteractiveAnswer}
          />
        );
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
      default:
        return null;
    }
  };

  return (
    <div className="fixed inset-0 z-50 bg-black flex flex-col">
      {/* ── Header ── */}
      <div className="flex items-center gap-4 px-4 sm:px-6 py-4 flex-shrink-0">
        <button
          type="button"
          onClick={() => (completed ? onClose() : setShowExitConfirm(true))}
          className="w-8 h-8 rounded-full flex items-center justify-center hover:bg-white/8 transition-colors cursor-pointer"
        >
          <X size={18} className="text-text-secondary" />
        </button>

        {/* Progress bar */}
        <div className="flex-1 h-2.5 bg-white/8 rounded-full overflow-hidden">
          <motion.div
            className="h-full rounded-full bg-[#F97316]"
            animate={{ width: `${completed ? 100 : progress}%` }}
            transition={{ duration: 0.4, ease: "easeOut" }}
          />
        </div>

        <span className="text-xs text-text-secondary min-w-[40px] text-right">
          {completed ? steps.length : currentIndex + 1}/{steps.length}
        </span>
      </div>

      {/* ── Content ── */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-xl mx-auto px-4 sm:px-6 py-6">
          {completed ? (
            <CongratsScreen lessonTitle={lessonTitle} onClose={onClose} />
          ) : (
            <AnimatePresence mode="wait" custom={direction}>
              <motion.div
                key={currentIndex}
                custom={direction}
                variants={slideVariants}
                initial="enter"
                animate="center"
                exit="exit"
                transition={{ duration: 0.25, ease: "easeInOut" }}
                className="bg-[#111111] border border-white/6 rounded-2xl p-5 sm:p-6"
              >
                {currentStep && renderStep(currentStep)}

                {/* Navigation footer — only for plain info steps (video/audio/embed have their own button) */}
                {isInfoStep && (
                  <div className="flex items-center justify-between mt-6 pt-5 border-t border-white/6">
                    <button
                      type="button"
                      onClick={goBack}
                      disabled={currentIndex === 0}
                      className="flex items-center gap-1.5 text-sm text-text-secondary hover:text-text transition-colors cursor-pointer disabled:opacity-30 disabled:cursor-not-allowed"
                    >
                      <ArrowLeft size={15} /> Назад
                    </button>

                    <Button onClick={goForward} size="md">
                      {isLastStep ? "Завершить" : "Далее"}
                      <ArrowRight size={15} />
                    </Button>
                  </div>
                )}

                {/* Back nav for interactive steps and media steps (they control their own flow) */}
                {!isContentOnly && currentIndex > 0 && (
                  <div className="mt-4 pt-4 border-t border-white/6">
                    <button
                      type="button"
                      onClick={goBack}
                      className="flex items-center gap-1.5 text-sm text-text-secondary hover:text-text transition-colors cursor-pointer"
                    >
                      <ArrowLeft size={15} /> Назад
                    </button>
                  </div>
                )}
              </motion.div>
            </AnimatePresence>
          )}
        </div>
      </div>

      {/* ── Exit confirmation modal ── */}
      <AnimatePresence>
        {showExitConfirm && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[60] bg-black/60 flex items-end sm:items-center justify-center p-4 sm:p-6"
            onClick={() => setShowExitConfirm(false)}
          >
            <motion.div
              initial={{ y: 40, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              exit={{ y: 40, opacity: 0 }}
              transition={{ duration: 0.2 }}
              onClick={(e) => e.stopPropagation()}
              className="w-full max-w-sm bg-[#111111] border border-white/6 rounded-2xl p-6 text-center space-y-4"
            >
              <h3 className="text-base font-bold text-text">Выйти из урока?</h3>
              <p className="text-sm text-text-secondary">
                Ваш прогресс по этому уроку не будет сохранён.
              </p>
              <div className="flex gap-3">
                <button
                  type="button"
                  onClick={() => setShowExitConfirm(false)}
                  className="flex-1 py-2.5 rounded-xl border border-white/10 text-sm font-medium text-text hover:bg-white/5 transition-colors cursor-pointer"
                >
                  Остаться
                </button>
                <button
                  type="button"
                  onClick={onClose}
                  className="flex-1 py-2.5 rounded-xl bg-red-500/15 border border-red-500/30 text-red-400 text-sm font-medium hover:bg-red-500/25 transition-colors cursor-pointer"
                >
                  Выйти
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
