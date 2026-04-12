import { useState, useCallback, useRef, useEffect } from "react";
import { motion, AnimatePresence, Reorder } from "framer-motion";
import {
  X,
  Plus,
  Trash2,
  GripVertical,
  Save,
  ChevronDown,
  Check,
  FileText,
  HelpCircle,
  ListOrdered,
  Code2,
  Type,
  Link,
  ToggleLeft,
  Layers,
  Keyboard,
  MousePointerClick,
  Terminal,
  Clock,
  FolderTree,
  Play,
  Headphones,
  Globe,
  CheckSquare,
  MessageSquare,
  Highlighter,
  Puzzle,
  Mic,
  BookOpen,
  Languages,
  TextCursorInput,
  Shield,
} from "lucide-react";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import {
  courseApi,
  type LessonStep,
  type StepType,
  type StepInfo,
  type StepQuiz,
  type StepDragOrder,
  type StepCodePuzzle,
  type StepFillBlank,
  type StepQuizOption,
  type StepMatching,
  type StepTrueFalse,
  type StepFlashcards,
  type StepTypeAnswer,
  type StepImageHotspot,
  type StepCodeEditor,
  type StepTimeline,
  type StepCategorySort,
  type StepVideo,
  type StepAudio,
  type StepEmbed,
  type StepTerminalSim,
  type StepMultiSelect,
  type StepConversationSim,
  type StepHighlightText,
  type StepSnippetOrder,
  type StepListeningComprehension,
  type StepPronunciation,
  type StepWordBuilder,
  type StepSentenceTranslation,
  type StepClozePassage,
  type StepTowerDefense,
} from "@/services/courseApi";

// ─── Types ─────────────────────────────────────────────────────────────────

interface StepWithId extends Record<string, unknown> {
  _id: string;
  type: StepType;
}

type EditorStep = (LessonStep & { _id: string });

// ─── Helpers ───────────────────────────────────────────────────────────────

function nanoid() {
  return Math.random().toString(36).slice(2, 10);
}

function defaultStep(type: StepType): LessonStep {
  switch (type) {
    case "info":
      return { type: "info", title: "", markdown: "" };
    case "quiz":
      return {
        type: "quiz",
        question: "",
        options: [
          { id: nanoid(), text: "", correct: true },
          { id: nanoid(), text: "", correct: false },
        ],
      };
    case "drag-order":
      return { type: "drag-order", items: ["", ""] };
    case "code-puzzle":
      return { type: "code-puzzle", fragments: ["", ""] };
    case "fill-blank":
      return { type: "fill-blank", text: "", answers: [""] };
    case "matching":
      return { type: "matching", pairs: [{ left: "", right: "" }, { left: "", right: "" }] };
    case "true-false":
      return { type: "true-false", statement: "", correct: true };
    case "flashcards":
      return { type: "flashcards", cards: [{ front: "", back: "" }] };
    case "type-answer":
      return { type: "type-answer", question: "", acceptedAnswers: [""] };
    case "image-hotspot":
      return {
        type: "image-hotspot",
        imageUrl: "",
        question: "",
        hotspot: { x: 50, y: 50, radius: 10 },
      };
    case "code-editor":
      return {
        type: "code-editor",
        language: "javascript",
        prompt: "",
        starterCode: "",
        expectedOutput: "",
      };
    case "timeline":
      return {
        type: "timeline",
        events: [
          { label: "", year: "" },
          { label: "", year: "" },
        ],
      };
    case "category-sort":
      return {
        type: "category-sort",
        categories: ["Категория 1", "Категория 2"],
        items: [{ text: "", category: "Категория 1" }],
      };
    case "video":
      return { type: "video", title: "", url: "" };
    case "audio":
      return { type: "audio", title: "", url: "", transcript: "" };
    case "embed":
      return { type: "embed", title: "", url: "", height: 400 };
    case "terminal-sim":
      return {
        type: "terminal-sim",
        prompt: "",
        expectedCommand: "",
        output: "",
        hint: "",
      };
    case "multi-select":
      return {
        type: "multi-select",
        question: "",
        options: [
          { id: nanoid(), text: "", correct: true },
          { id: nanoid(), text: "", correct: false },
          { id: nanoid(), text: "", correct: false },
        ],
      };
    case "conversation-sim":
      return {
        type: "conversation-sim",
        scenario: "",
        messages: [{ role: "assistant", text: "" }],
        choices: [
          { id: nanoid(), text: "", correct: true, feedback: "" },
          { id: nanoid(), text: "", correct: false, feedback: "" },
        ],
      };
    case "highlight-text":
      return {
        type: "highlight-text",
        instruction: "",
        segments: [
          { text: "", correct: false },
          { text: "", correct: true },
        ],
      };
    case "snippet-order":
      return { type: "snippet-order", instruction: "", fragments: ["", ""] };
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
    case "tower-defense":
      return { type: "tower-defense" };
  }
}

const STEP_TYPES: { type: StepType; label: string; icon: React.ReactNode; color: string }[] = [
  { type: "info", label: "Информация", icon: <FileText size={14} />, color: "#F97316" },
  { type: "quiz", label: "Квиз", icon: <HelpCircle size={14} />, color: "#FFB800" },
  { type: "drag-order", label: "Порядок", icon: <ListOrdered size={14} />, color: "#4ADE80" },
  { type: "code-puzzle", label: "Код-пазл", icon: <Code2 size={14} />, color: "#22C55E" },
  { type: "fill-blank", label: "Заполни пропуск", icon: <Type size={14} />, color: "#FF6B6B" },
  { type: "matching", label: "Соответствие", icon: <Link size={14} />, color: "#3B82F6" },
  { type: "true-false", label: "Верно/Неверно", icon: <ToggleLeft size={14} />, color: "#EF4444" },
  { type: "flashcards", label: "Карточки", icon: <Layers size={14} />, color: "#8B5CF6" },
  { type: "type-answer", label: "Введи ответ", icon: <Keyboard size={14} />, color: "#EC4899" },
  { type: "image-hotspot", label: "Хотспот", icon: <MousePointerClick size={14} />, color: "#14B8A6" },
  { type: "code-editor", label: "Редактор кода", icon: <Terminal size={14} />, color: "#22C55E" },
  { type: "timeline", label: "Хронология", icon: <Clock size={14} />, color: "#6366F1" },
  { type: "category-sort", label: "Сортировка", icon: <FolderTree size={14} />, color: "#F59E0B" },
  { type: "video", label: "Видео", icon: <Play size={14} />, color: "#EF4444" },
  { type: "audio", label: "Аудио", icon: <Headphones size={14} />, color: "#06B6D4" },
  { type: "embed", label: "Встроить", icon: <Globe size={14} />, color: "#8B5CF6" },
  { type: "terminal-sim", label: "Терминал", icon: <Terminal size={14} />, color: "#22C55E" },
  { type: "multi-select", label: "Мульти-выбор", icon: <CheckSquare size={14} />, color: "#3B82F6" },
  { type: "conversation-sim", label: "Диалог", icon: <MessageSquare size={14} />, color: "#8B5CF6" },
  { type: "highlight-text", label: "Выделение", icon: <Highlighter size={14} />, color: "#F59E0B" },
  { type: "snippet-order", label: "Фрагменты", icon: <Puzzle size={14} />, color: "#EC4899" },
  { type: "listening-comprehension", label: "Аудирование", icon: <Headphones size={14} />, color: "#06B6D4" },
  { type: "pronunciation", label: "Произношение", icon: <Mic size={14} />, color: "#F43F5E" },
  { type: "word-builder", label: "Собери слово", icon: <BookOpen size={14} />, color: "#10B981" },
  { type: "sentence-translation", label: "Перевод", icon: <Languages size={14} />, color: "#A855F7" },
  { type: "cloze-passage", label: "Текст с пропусками", icon: <TextCursorInput size={14} />, color: "#F59E0B" },
  { type: "tower-defense", label: "Tower Defense", icon: <Shield size={14} />, color: "#ef4444" },
];

// ─── Sub-forms ─────────────────────────────────────────────────────────────

function InfoForm({
  step,
  onChange,
}: {
  step: StepInfo & { _id: string };
  onChange: (patch: Partial<StepInfo>) => void;
}) {
  return (
    <div className="space-y-3">
      <Input
        label="Заголовок"
        value={step.title}
        onChange={(e) => onChange({ title: e.target.value })}
        placeholder="Заголовок слайда..."
      />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Контент (Markdown)</label>
        <textarea
          value={step.markdown}
          onChange={(e) => onChange({ markdown: e.target.value })}
          rows={6}
          placeholder="# Heading&#10;&#10;Write your content here..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono"
        />
      </div>
    </div>
  );
}

function QuizForm({
  step,
  onChange,
}: {
  step: StepQuiz & { _id: string };
  onChange: (patch: Partial<StepQuiz>) => void;
}) {
  const addOption = () => {
    onChange({
      options: [...step.options, { id: nanoid(), text: "", correct: false }],
    });
  };

  const removeOption = (id: string) => {
    onChange({ options: step.options.filter((o) => o.id !== id) });
  };

  const updateOption = (id: string, patch: Partial<StepQuizOption>) => {
    onChange({
      options: step.options.map((o) => (o.id === id ? { ...o, ...patch } : o)),
    });
  };

  const toggleCorrect = (id: string) => {
    onChange({
      options: step.options.map((o) => (o.id === id ? { ...o, correct: !o.correct } : o)),
    });
  };

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Вопрос</label>
        <textarea
          value={step.question}
          onChange={(e) => onChange({ question: e.target.value })}
          rows={2}
          placeholder="Какой вопрос?"
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Варианты{" "}
          <span className="text-xs text-text-secondary/60">(нажмите на галочку для правильного ответа)</span>
        </label>
        <div className="space-y-2">
          {step.options.map((option) => (
            <div key={option.id} className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => toggleCorrect(option.id)}
                className={`flex-shrink-0 w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all cursor-pointer ${
                  option.correct
                    ? "bg-green-500 border-green-500"
                    : "border-border hover:border-green-500/50"
                }`}
              >
                {option.correct && <Check size={10} className="text-white" />}
              </button>
              <input
                value={option.text}
                onChange={(e) => updateOption(option.id, { text: e.target.value })}
                placeholder="Текст варианта..."
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeOption(option.id)}
                disabled={step.options.length <= 2}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addOption}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить вариант
        </button>
      </div>
    </div>
  );
}

function DragOrderForm({
  step,
  onChange,
}: {
  step: StepDragOrder & { _id: string };
  onChange: (patch: Partial<StepDragOrder>) => void;
}) {
  const updateItem = (index: number, value: string) => {
    const items = [...step.items];
    items[index] = value;
    onChange({ items });
  };

  const addItem = () => onChange({ items: [...step.items, ""] });

  const removeItem = (index: number) => {
    onChange({ items: step.items.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <p className="text-xs text-text-secondary">
        Перечислите элементы в правильном порядке. Студенты будут перетаскивать их.
      </p>
      <div className="space-y-2">
        {step.items.map((item, i) => (
          <div key={i} className="flex items-center gap-2">
            <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-xs text-text-secondary font-mono">
              {i + 1}
            </span>
            <input
              value={item}
              onChange={(e) => updateItem(i, e.target.value)}
              placeholder={`Элемент ${i + 1}...`}
              className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
            <button
              type="button"
              onClick={() => removeItem(i)}
              disabled={step.items.length <= 2}
              className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
            >
              <Trash2 size={14} />
            </button>
          </div>
        ))}
      </div>
      <button
        type="button"
        onClick={addItem}
        className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
      >
        <Plus size={12} />
        Добавить элемент
      </button>
    </div>
  );
}

function CodePuzzleForm({
  step,
  onChange,
}: {
  step: StepCodePuzzle & { _id: string };
  onChange: (patch: Partial<StepCodePuzzle>) => void;
}) {
  const updateFragment = (index: number, value: string) => {
    const fragments = [...step.fragments];
    fragments[index] = value;
    onChange({ fragments });
  };

  const addFragment = () => onChange({ fragments: [...step.fragments, ""] });

  const removeFragment = (index: number) => {
    onChange({ fragments: step.fragments.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <p className="text-xs text-text-secondary">
        Введите фрагменты кода в правильном порядке. Студенты будут собирать их.
      </p>
      <div className="space-y-2">
        {step.fragments.map((fragment, i) => (
          <div key={i} className="flex items-center gap-2">
            <span className="flex-shrink-0 w-6 h-6 rounded flex items-center justify-center text-xs text-text-secondary font-mono bg-white/5">
              {i + 1}
            </span>
            <input
              value={fragment}
              onChange={(e) => updateFragment(i, e.target.value)}
              placeholder={`Фрагмент ${i + 1}...`}
              className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm font-mono"
            />
            <button
              type="button"
              onClick={() => removeFragment(i)}
              disabled={step.fragments.length <= 2}
              className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
            >
              <Trash2 size={14} />
            </button>
          </div>
        ))}
      </div>
      <button
        type="button"
        onClick={addFragment}
        className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
      >
        <Plus size={12} />
        Добавить фрагмент
      </button>
    </div>
  );
}

function FillBlankForm({
  step,
  onChange,
}: {
  step: StepFillBlank & { _id: string };
  onChange: (patch: Partial<StepFillBlank>) => void;
}) {
  const addAnswer = () => onChange({ answers: [...step.answers, ""] });

  const updateAnswer = (index: number, value: string) => {
    const answers = [...step.answers];
    answers[index] = value;
    onChange({ answers });
  };

  const removeAnswer = (index: number) => {
    onChange({ answers: step.answers.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Текст с пропусками{" "}
          <span className="text-xs text-text-secondary/60">(используйте ___ для пропусков)</span>
        </label>
        <textarea
          value={step.text}
          onChange={(e) => onChange({ text: e.target.value })}
          rows={3}
          placeholder="Столица Франции — ___."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Правильные ответы{" "}
          <span className="text-xs text-text-secondary/60">(в порядке пропусков)</span>
        </label>
        <div className="space-y-2">
          {step.answers.map((answer, i) => (
            <div key={i} className="flex items-center gap-2">
              <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-xs text-text-secondary">
                {i + 1}
              </span>
              <input
                value={answer}
                onChange={(e) => updateAnswer(i, e.target.value)}
                placeholder={`Ответ ${i + 1}...`}
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeAnswer(i)}
                disabled={step.answers.length <= 1}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addAnswer}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить ответ
        </button>
      </div>
    </div>
  );
}

function MatchingForm({
  step,
  onChange,
}: {
  step: StepMatching & { _id: string };
  onChange: (patch: Partial<StepMatching>) => void;
}) {
  const updatePair = (
    index: number,
    side: "left" | "right",
    value: string
  ) => {
    const pairs = step.pairs.map((p, i) =>
      i === index ? { ...p, [side]: value } : p
    );
    onChange({ pairs });
  };

  const addPair = () =>
    onChange({ pairs: [...step.pairs, { left: "", right: "" }] });

  const removePair = (index: number) => {
    onChange({ pairs: step.pairs.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <p className="text-xs text-text-secondary">
        Добавьте пары. Студенты будут соединять левую колонку с правой.
      </p>
      <div className="space-y-2">
        {step.pairs.map((pair, i) => (
          <div key={i} className="flex items-center gap-2">
            <input
              value={pair.left}
              onChange={(e) => updatePair(i, "left", e.target.value)}
              placeholder="Левая сторона..."
              className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
            <span className="flex-shrink-0 text-text-secondary text-xs">↔</span>
            <input
              value={pair.right}
              onChange={(e) => updatePair(i, "right", e.target.value)}
              placeholder="Правая сторона..."
              className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
            <button
              type="button"
              onClick={() => removePair(i)}
              disabled={step.pairs.length <= 2}
              className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
            >
              <Trash2 size={14} />
            </button>
          </div>
        ))}
      </div>
      <button
        type="button"
        onClick={addPair}
        className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
      >
        <Plus size={12} />
        Добавить пару
      </button>
    </div>
  );
}

function TrueFalseForm({
  step,
  onChange,
}: {
  step: StepTrueFalse & { _id: string };
  onChange: (patch: Partial<StepTrueFalse>) => void;
}) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Утверждение</label>
        <textarea
          value={step.statement}
          onChange={(e) => onChange({ statement: e.target.value })}
          rows={3}
          placeholder="Введите утверждение, которое студент должен оценить..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">Правильный ответ</label>
        <div className="flex gap-3">
          <button
            type="button"
            onClick={() => onChange({ correct: true })}
            className={`flex-1 py-2.5 rounded-xl text-sm font-medium border transition-all cursor-pointer ${
              step.correct
                ? "bg-green-500/20 border-green-500/50 text-green-400"
                : "border-border text-text-secondary hover:border-green-500/30 hover:text-green-400/70"
            }`}
          >
            Верно
          </button>
          <button
            type="button"
            onClick={() => onChange({ correct: false })}
            className={`flex-1 py-2.5 rounded-xl text-sm font-medium border transition-all cursor-pointer ${
              !step.correct
                ? "bg-red-500/20 border-red-500/50 text-red-400"
                : "border-border text-text-secondary hover:border-red-500/30 hover:text-red-400/70"
            }`}
          >
            Неверно
          </button>
        </div>
      </div>
    </div>
  );
}

function FlashcardsForm({
  step,
  onChange,
}: {
  step: StepFlashcards & { _id: string };
  onChange: (patch: Partial<StepFlashcards>) => void;
}) {
  const updateCard = (
    index: number,
    side: "front" | "back",
    value: string
  ) => {
    const cards = step.cards.map((c, i) =>
      i === index ? { ...c, [side]: value } : c
    );
    onChange({ cards });
  };

  const addCard = () =>
    onChange({ cards: [...step.cards, { front: "", back: "" }] });

  const removeCard = (index: number) => {
    onChange({ cards: step.cards.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <p className="text-xs text-text-secondary">
        Студенты будут переворачивать карточки, чтобы увидеть обратную сторону.
      </p>
      <div className="space-y-3">
        {step.cards.map((card, i) => (
          <div
            key={i}
            className="rounded-xl border border-border bg-white/[0.02] p-3 space-y-2"
          >
            <div className="flex items-center justify-between mb-1">
              <span className="text-xs text-text-secondary font-medium">Карточка {i + 1}</span>
              <button
                type="button"
                onClick={() => removeCard(i)}
                disabled={step.cards.length <= 1}
                className="text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={13} />
              </button>
            </div>
            <input
              value={card.front}
              onChange={(e) => updateCard(i, "front", e.target.value)}
              placeholder="Лицевая сторона..."
              className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
            <input
              value={card.back}
              onChange={(e) => updateCard(i, "back", e.target.value)}
              placeholder="Обратная сторона..."
              className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
          </div>
        ))}
      </div>
      <button
        type="button"
        onClick={addCard}
        className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
      >
        <Plus size={12} />
        Добавить карточку
      </button>
    </div>
  );
}

function TypeAnswerForm({
  step,
  onChange,
}: {
  step: StepTypeAnswer & { _id: string };
  onChange: (patch: Partial<StepTypeAnswer>) => void;
}) {
  const addAnswer = () =>
    onChange({ acceptedAnswers: [...step.acceptedAnswers, ""] });

  const updateAnswer = (index: number, value: string) => {
    const acceptedAnswers = [...step.acceptedAnswers];
    acceptedAnswers[index] = value;
    onChange({ acceptedAnswers });
  };

  const removeAnswer = (index: number) => {
    onChange({
      acceptedAnswers: step.acceptedAnswers.filter((_, i) => i !== index),
    });
  };

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Вопрос</label>
        <textarea
          value={step.question}
          onChange={(e) => onChange({ question: e.target.value })}
          rows={2}
          placeholder="Что нужно ввести студенту?"
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Принимаемые ответы{" "}
          <span className="text-xs text-text-secondary/60">(без учёта регистра)</span>
        </label>
        <div className="space-y-2">
          {step.acceptedAnswers.map((answer, i) => (
            <div key={i} className="flex items-center gap-2">
              <input
                value={answer}
                onChange={(e) => updateAnswer(i, e.target.value)}
                placeholder={`Вариант ответа ${i + 1}...`}
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeAnswer(i)}
                disabled={step.acceptedAnswers.length <= 1}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addAnswer}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить вариант
        </button>
      </div>
    </div>
  );
}

function ImageHotspotForm({
  step,
  onChange,
}: {
  step: StepImageHotspot & { _id: string };
  onChange: (patch: Partial<StepImageHotspot>) => void;
}) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">URL изображения</label>
        <input
          value={step.imageUrl}
          onChange={(e) => onChange({ imageUrl: e.target.value })}
          placeholder="https://example.com/image.png"
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Вопрос</label>
        <input
          value={step.question}
          onChange={(e) => onChange({ question: e.target.value })}
          placeholder="Нажмите на правильную область..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Область хотспота{" "}
          <span className="text-xs text-text-secondary/60">(в % от размера изображения)</span>
        </label>
        <div className="grid grid-cols-3 gap-2">
          <div>
            <label className="block text-xs text-text-secondary mb-1">X (%)</label>
            <input
              type="number"
              min={0}
              max={100}
              value={step.hotspot.x}
              onChange={(e) =>
                onChange({ hotspot: { ...step.hotspot, x: Number(e.target.value) } })
              }
              className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm"
            />
          </div>
          <div>
            <label className="block text-xs text-text-secondary mb-1">Y (%)</label>
            <input
              type="number"
              min={0}
              max={100}
              value={step.hotspot.y}
              onChange={(e) =>
                onChange({ hotspot: { ...step.hotspot, y: Number(e.target.value) } })
              }
              className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm"
            />
          </div>
          <div>
            <label className="block text-xs text-text-secondary mb-1">Радиус (%)</label>
            <input
              type="number"
              min={1}
              max={50}
              value={step.hotspot.radius}
              onChange={(e) =>
                onChange({ hotspot: { ...step.hotspot, radius: Number(e.target.value) } })
              }
              className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

function CodeEditorForm({
  step,
  onChange,
}: {
  step: StepCodeEditor & { _id: string };
  onChange: (patch: Partial<StepCodeEditor>) => void;
}) {
  const languages = ["html", "css", "javascript", "typescript"];

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Язык</label>
        <select
          value={step.language}
          onChange={(e) => onChange({ language: e.target.value })}
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm"
        >
          {languages.map((lang) => (
            <option key={lang} value={lang}>
              {lang}
            </option>
          ))}
        </select>
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Задание</label>
        <textarea
          value={step.prompt}
          onChange={(e) => onChange({ prompt: e.target.value })}
          rows={2}
          placeholder="Что должен сделать студент?"
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Стартовый код</label>
        <textarea
          value={step.starterCode}
          onChange={(e) => onChange({ starterCode: e.target.value })}
          rows={4}
          placeholder="// Начальный код для студента..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Ожидаемый вывод{" "}
          <span className="text-xs text-text-secondary/60">(подстрока в результате)</span>
        </label>
        <textarea
          value={step.expectedOutput}
          onChange={(e) => onChange({ expectedOutput: e.target.value })}
          rows={2}
          placeholder="Текст, который должен присутствовать в результате..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono"
        />
      </div>
    </div>
  );
}

function TimelineForm({
  step,
  onChange,
}: {
  step: StepTimeline & { _id: string };
  onChange: (patch: Partial<StepTimeline>) => void;
}) {
  const updateEvent = (
    index: number,
    field: "label" | "year",
    value: string
  ) => {
    const events = step.events.map((e, i) =>
      i === index ? { ...e, [field]: value } : e
    );
    onChange({ events });
  };

  const addEvent = () =>
    onChange({ events: [...step.events, { label: "", year: "" }] });

  const removeEvent = (index: number) => {
    onChange({ events: step.events.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <p className="text-xs text-text-secondary">
        Добавьте события в правильном хронологическом порядке. Студенты будут их сортировать.
      </p>
      <div className="space-y-2">
        {step.events.map((event, i) => (
          <div key={i} className="flex items-center gap-2">
            <span className="flex-shrink-0 w-6 h-6 rounded-full bg-white/10 flex items-center justify-center text-xs text-text-secondary font-mono">
              {i + 1}
            </span>
            <input
              value={event.year}
              onChange={(e) => updateEvent(i, "year", e.target.value)}
              placeholder="Год..."
              className="w-20 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
            <input
              value={event.label}
              onChange={(e) => updateEvent(i, "label", e.target.value)}
              placeholder="Событие..."
              className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
            />
            <button
              type="button"
              onClick={() => removeEvent(i)}
              disabled={step.events.length <= 2}
              className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
            >
              <Trash2 size={14} />
            </button>
          </div>
        ))}
      </div>
      <button
        type="button"
        onClick={addEvent}
        className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
      >
        <Plus size={12} />
        Добавить событие
      </button>
    </div>
  );
}

function CategorySortForm({
  step,
  onChange,
}: {
  step: StepCategorySort & { _id: string };
  onChange: (patch: Partial<StepCategorySort>) => void;
}) {
  const updateCategory = (index: number, value: string) => {
    const oldName = step.categories[index];
    const categories = step.categories.map((c, i) =>
      i === index ? value : c
    );
    // Rename matching category in items
    const items = step.items.map((item) =>
      item.category === oldName ? { ...item, category: value } : item
    );
    onChange({ categories, items });
  };

  const addCategory = () =>
    onChange({ categories: [...step.categories, `Категория ${step.categories.length + 1}`] });

  const removeCategory = (index: number) => {
    const removed = step.categories[index];
    const categories = step.categories.filter((_, i) => i !== index);
    const fallback = categories[0] ?? "";
    const items = step.items.map((item) =>
      item.category === removed ? { ...item, category: fallback } : item
    );
    onChange({ categories, items });
  };

  const updateItem = (index: number, field: "text" | "category", value: string) => {
    const items = step.items.map((item, i) =>
      i === index ? { ...item, [field]: value } : item
    );
    onChange({ items });
  };

  const addItem = () =>
    onChange({
      items: [...step.items, { text: "", category: step.categories[0] ?? "" }],
    });

  const removeItem = (index: number) => {
    onChange({ items: step.items.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-4">
      {/* Categories */}
      <div>
        <label className="block text-sm text-text-secondary mb-2">Категории</label>
        <div className="space-y-2">
          {step.categories.map((cat, i) => (
            <div key={i} className="flex items-center gap-2">
              <input
                value={cat}
                onChange={(e) => updateCategory(i, e.target.value)}
                placeholder={`Категория ${i + 1}...`}
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeCategory(i)}
                disabled={step.categories.length <= 2}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addCategory}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить категорию
        </button>
      </div>

      {/* Items */}
      <div>
        <label className="block text-sm text-text-secondary mb-2">Элементы для сортировки</label>
        <div className="space-y-2">
          {step.items.map((item, i) => (
            <div key={i} className="flex items-center gap-2">
              <input
                value={item.text}
                onChange={(e) => updateItem(i, "text", e.target.value)}
                placeholder="Текст элемента..."
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <select
                value={item.category}
                onChange={(e) => updateItem(i, "category", e.target.value)}
                className="w-36 rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm"
              >
                {step.categories.map((cat) => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
              <button
                type="button"
                onClick={() => removeItem(i)}
                disabled={step.items.length <= 1}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addItem}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить элемент
        </button>
      </div>
    </div>
  );
}

function VideoForm({
  step,
  onChange,
}: {
  step: StepVideo & { _id: string };
  onChange: (patch: Partial<StepVideo>) => void;
}) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Заголовок</label>
        <input
          value={step.title}
          onChange={(e) => onChange({ title: e.target.value })}
          placeholder="Название видео..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">URL видео</label>
        <input
          value={step.url}
          onChange={(e) => onChange({ url: e.target.value })}
          placeholder="https://www.youtube.com/embed/... или прямая ссылка"
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
    </div>
  );
}

function AudioForm({
  step,
  onChange,
}: {
  step: StepAudio & { _id: string };
  onChange: (patch: Partial<StepAudio>) => void;
}) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Заголовок</label>
        <input
          value={step.title}
          onChange={(e) => onChange({ title: e.target.value })}
          placeholder="Название аудио..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">URL аудио</label>
        <input
          value={step.url}
          onChange={(e) => onChange({ url: e.target.value })}
          placeholder="https://example.com/audio.mp3"
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Транскрипция{" "}
          <span className="text-xs text-text-secondary/60">(необязательно)</span>
        </label>
        <textarea
          value={step.transcript ?? ""}
          onChange={(e) => onChange({ transcript: e.target.value })}
          rows={4}
          placeholder="Текст аудио для доступности..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
    </div>
  );
}

function EmbedForm({
  step,
  onChange,
}: {
  step: StepEmbed & { _id: string };
  onChange: (patch: Partial<StepEmbed>) => void;
}) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Заголовок</label>
        <input
          value={step.title}
          onChange={(e) => onChange({ title: e.target.value })}
          placeholder="Название встроенного контента..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">URL (iframe src)</label>
        <input
          value={step.url}
          onChange={(e) => onChange({ url: e.target.value })}
          placeholder="https://example.com/embed"
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Высота (px){" "}
          <span className="text-xs text-text-secondary/60">(необязательно, по умолчанию 400)</span>
        </label>
        <input
          type="number"
          min={100}
          max={2000}
          value={step.height ?? 400}
          onChange={(e) => onChange({ height: Number(e.target.value) })}
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
    </div>
  );
}

function TerminalSimForm({
  step,
  onChange,
}: {
  step: StepTerminalSim & { _id: string };
  onChange: (patch: Partial<StepTerminalSim>) => void;
}) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Инструкция для студента</label>
        <textarea
          value={step.prompt}
          onChange={(e) => onChange({ prompt: e.target.value })}
          rows={2}
          placeholder="Что должен сделать студент в терминале?"
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Ожидаемая команда{" "}
          <span className="text-xs text-text-secondary/60">(с учётом регистра)</span>
        </label>
        <input
          value={step.expectedCommand}
          onChange={(e) => onChange({ expectedCommand: e.target.value })}
          placeholder="npm install"
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm font-mono"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Вывод после правильной команды</label>
        <textarea
          value={step.output}
          onChange={(e) => onChange({ output: e.target.value })}
          rows={3}
          placeholder="added 42 packages in 3s"
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm font-mono"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Подсказка{" "}
          <span className="text-xs text-text-secondary/60">(необязательно)</span>
        </label>
        <input
          value={step.hint ?? ""}
          onChange={(e) => onChange({ hint: e.target.value })}
          placeholder="Попробуйте команду npm..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
    </div>
  );
}

function MultiSelectForm({
  step,
  onChange,
}: {
  step: StepMultiSelect & { _id: string };
  onChange: (patch: Partial<StepMultiSelect>) => void;
}) {
  const addOption = () => {
    onChange({
      options: [...step.options, { id: nanoid(), text: "", correct: false }],
    });
  };

  const removeOption = (id: string) => {
    onChange({ options: step.options.filter((o) => o.id !== id) });
  };

  const updateOption = (id: string, text: string) => {
    onChange({
      options: step.options.map((o) => (o.id === id ? { ...o, text } : o)),
    });
  };

  const toggleCorrect = (id: string) => {
    onChange({
      options: step.options.map((o) => (o.id === id ? { ...o, correct: !o.correct } : o)),
    });
  };

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Вопрос</label>
        <textarea
          value={step.question}
          onChange={(e) => onChange({ question: e.target.value })}
          rows={2}
          placeholder="Выберите все правильные ответы..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Варианты{" "}
          <span className="text-xs text-text-secondary/60">(можно отмечать несколько правильных)</span>
        </label>
        <div className="space-y-2">
          {step.options.map((option) => (
            <div key={option.id} className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => toggleCorrect(option.id)}
                className={`flex-shrink-0 w-5 h-5 rounded border-2 flex items-center justify-center transition-all cursor-pointer ${
                  option.correct
                    ? "bg-green-500 border-green-500"
                    : "border-border hover:border-green-500/50"
                }`}
              >
                {option.correct && <Check size={10} className="text-white" />}
              </button>
              <input
                value={option.text}
                onChange={(e) => updateOption(option.id, e.target.value)}
                placeholder="Текст варианта..."
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeOption(option.id)}
                disabled={step.options.length <= 2}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addOption}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить вариант
        </button>
      </div>
    </div>
  );
}

function ConversationSimForm({
  step,
  onChange,
}: {
  step: StepConversationSim & { _id: string };
  onChange: (patch: Partial<StepConversationSim>) => void;
}) {
  const updateMessage = (index: number, field: "role" | "text", value: string) => {
    const messages = step.messages.map((m, i) =>
      i === index ? { ...m, [field]: value } : m
    ) as StepConversationSim["messages"];
    onChange({ messages });
  };

  const addMessage = () =>
    onChange({
      messages: [...step.messages, { role: "assistant", text: "" }],
    });

  const removeMessage = (index: number) => {
    onChange({ messages: step.messages.filter((_, i) => i !== index) });
  };

  const updateChoice = (
    id: string,
    field: "text" | "correct" | "feedback",
    value: string | boolean
  ) => {
    onChange({
      choices: step.choices.map((c) =>
        c.id === id ? { ...c, [field]: value } : c
      ),
    });
  };

  const addChoice = () =>
    onChange({
      choices: [...step.choices, { id: nanoid(), text: "", correct: false, feedback: "" }],
    });

  const removeChoice = (id: string) => {
    onChange({ choices: step.choices.filter((c) => c.id !== id) });
  };

  const toggleChoiceCorrect = (id: string) => {
    onChange({
      choices: step.choices.map((c) =>
        c.id === id ? { ...c, correct: !c.correct } : c
      ),
    });
  };

  return (
    <div className="space-y-4">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Сценарий (контекст)</label>
        <textarea
          value={step.scenario}
          onChange={(e) => onChange({ scenario: e.target.value })}
          rows={2}
          placeholder="Опишите ситуацию диалога..."
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>

      <div>
        <label className="block text-sm text-text-secondary mb-2">Диалог</label>
        <div className="space-y-2">
          {step.messages.map((msg, i) => (
            <div key={i} className="flex items-start gap-2">
              <select
                value={msg.role}
                onChange={(e) => updateMessage(i, "role", e.target.value)}
                className="flex-shrink-0 w-28 rounded-xl border border-border bg-bg px-2 py-2 text-text outline-none transition-colors focus:border-primary/50 text-xs"
              >
                <option value="assistant">Ассистент</option>
                <option value="user">Пользователь</option>
              </select>
              <input
                value={msg.text}
                onChange={(e) => updateMessage(i, "text", e.target.value)}
                placeholder="Текст сообщения..."
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeMessage(i)}
                disabled={step.messages.length <= 1}
                className="flex-shrink-0 mt-1 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addMessage}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить сообщение
        </button>
      </div>

      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Варианты ответа{" "}
          <span className="text-xs text-text-secondary/60">(отметьте правильный)</span>
        </label>
        <div className="space-y-3">
          {step.choices.map((choice) => (
            <div key={choice.id} className="rounded-xl border border-border bg-white/[0.02] p-3 space-y-2">
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => toggleChoiceCorrect(choice.id)}
                  className={`flex-shrink-0 w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all cursor-pointer ${
                    choice.correct
                      ? "bg-green-500 border-green-500"
                      : "border-border hover:border-green-500/50"
                  }`}
                >
                  {choice.correct && <Check size={10} className="text-white" />}
                </button>
                <input
                  value={choice.text}
                  onChange={(e) => updateChoice(choice.id, "text", e.target.value)}
                  placeholder="Текст варианта..."
                  className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
                />
                <button
                  type="button"
                  onClick={() => removeChoice(choice.id)}
                  disabled={step.choices.length <= 2}
                  className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
                >
                  <Trash2 size={14} />
                </button>
              </div>
              <input
                value={choice.feedback}
                onChange={(e) => updateChoice(choice.id, "feedback", e.target.value)}
                placeholder="Обратная связь (что покажется после выбора)..."
                className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-xs"
              />
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addChoice}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить вариант
        </button>
      </div>
    </div>
  );
}

function HighlightTextForm({
  step,
  onChange,
}: {
  step: StepHighlightText & { _id: string };
  onChange: (patch: Partial<StepHighlightText>) => void;
}) {
  const updateSegment = (index: number, field: "text" | "correct", value: string | boolean) => {
    const segments = step.segments.map((s, i) =>
      i === index ? { ...s, [field]: value } : s
    );
    onChange({ segments });
  };

  const addSegment = () =>
    onChange({ segments: [...step.segments, { text: "", correct: false }] });

  const removeSegment = (index: number) => {
    onChange({ segments: step.segments.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Инструкция</label>
        <input
          value={step.instruction}
          onChange={(e) => onChange({ instruction: e.target.value })}
          placeholder="Выделите все ключевые термины..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-2">
          Сегменты текста{" "}
          <span className="text-xs text-text-secondary/60">(отметьте правильные для выделения)</span>
        </label>
        <div className="space-y-2">
          {step.segments.map((seg, i) => (
            <div key={i} className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => updateSegment(i, "correct", !seg.correct)}
                className={`flex-shrink-0 w-5 h-5 rounded border-2 flex items-center justify-center transition-all cursor-pointer ${
                  seg.correct
                    ? "bg-amber-500 border-amber-500"
                    : "border-border hover:border-amber-500/50"
                }`}
              >
                {seg.correct && <Check size={10} className="text-white" />}
              </button>
              <input
                value={seg.text}
                onChange={(e) => updateSegment(i, "text", e.target.value)}
                placeholder={`Сегмент ${i + 1}...`}
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeSegment(i)}
                disabled={step.segments.length <= 2}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addSegment}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить сегмент
        </button>
      </div>
    </div>
  );
}

function SnippetOrderForm({
  step,
  onChange,
}: {
  step: StepSnippetOrder & { _id: string };
  onChange: (patch: Partial<StepSnippetOrder>) => void;
}) {
  const updateFragment = (index: number, value: string) => {
    const fragments = [...step.fragments];
    fragments[index] = value;
    onChange({ fragments });
  };

  const addFragment = () => onChange({ fragments: [...step.fragments, ""] });

  const removeFragment = (index: number) => {
    onChange({ fragments: step.fragments.filter((_, i) => i !== index) });
  };

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Инструкция</label>
        <input
          value={step.instruction}
          onChange={(e) => onChange({ instruction: e.target.value })}
          placeholder="Соберите запрос в правильном порядке..."
          className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
        />
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1">
          Фрагменты{" "}
          <span className="text-xs text-text-secondary/60">(в правильном порядке)</span>
        </label>
        <div className="space-y-2">
          {step.fragments.map((fragment, i) => (
            <div key={i} className="flex items-center gap-2">
              <span className="flex-shrink-0 w-6 h-6 rounded flex items-center justify-center text-xs text-text-secondary font-mono bg-white/5">
                {i + 1}
              </span>
              <input
                value={fragment}
                onChange={(e) => updateFragment(i, e.target.value)}
                placeholder={`Фрагмент ${i + 1}...`}
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeFragment(i)}
                disabled={step.fragments.length <= 2}
                className="flex-shrink-0 text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </div>
        <button
          type="button"
          onClick={addFragment}
          className="mt-2 flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
        >
          <Plus size={12} />
          Добавить фрагмент
        </button>
      </div>
    </div>
  );
}

function ListeningComprehensionForm({
  step,
  onChange,
}: {
  step: StepListeningComprehension & { _id: string };
  onChange: (patch: Partial<StepListeningComprehension>) => void;
}) {
  const updateQuestion = (qIdx: number, field: string, value: string) => {
    const questions = step.questions.map((q, i) =>
      i === qIdx ? { ...q, [field]: value } : q
    );
    onChange({ questions });
  };

  const updateOption = (qIdx: number, oIdx: number, text: string) => {
    const questions = step.questions.map((q, qi) =>
      qi === qIdx
        ? { ...q, options: q.options.map((o, oi) => (oi === oIdx ? { ...o, text } : o)) }
        : q
    );
    onChange({ questions });
  };

  const setCorrectOption = (qIdx: number, oIdx: number) => {
    const questions = step.questions.map((q, qi) =>
      qi === qIdx
        ? {
            ...q,
            options: q.options.map((o, oi) => ({ ...o, correct: oi === oIdx })),
          }
        : q
    );
    onChange({ questions });
  };

  const addOption = (qIdx: number) => {
    const questions = step.questions.map((q, qi) =>
      qi === qIdx
        ? { ...q, options: [...q.options, { id: nanoid(), text: "", correct: false }] }
        : q
    );
    onChange({ questions });
  };

  const removeOption = (qIdx: number, oIdx: number) => {
    const questions = step.questions.map((q, qi) =>
      qi === qIdx
        ? { ...q, options: q.options.filter((_, oi) => oi !== oIdx) }
        : q
    );
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

  return (
    <div className="space-y-3">
      <Input
        label="URL аудио"
        value={step.audioUrl}
        onChange={(e) => onChange({ audioUrl: e.target.value })}
        placeholder="https://example.com/audio.mp3"
      />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Транскрипт</label>
        <textarea
          value={step.transcript}
          onChange={(e) => onChange({ transcript: e.target.value })}
          placeholder="Текст аудио..."
          rows={3}
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      {step.questions.map((q, qIdx) => (
        <div key={qIdx} className="border border-border rounded-xl p-3 space-y-2">
          <div className="flex items-center justify-between">
            <label className="text-sm text-text-secondary font-medium">Вопрос {qIdx + 1}</label>
            <button
              type="button"
              onClick={() => removeQuestion(qIdx)}
              disabled={step.questions.length <= 1}
              className="text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
            >
              <Trash2 size={14} />
            </button>
          </div>
          <input
            value={q.question}
            onChange={(e) => updateQuestion(qIdx, "question", e.target.value)}
            placeholder="Вопрос по аудио..."
            className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
          />
          {q.options.map((opt, oIdx) => (
            <div key={opt.id} className="flex items-center gap-2">
              <input
                type="radio"
                name={`lc-q-${qIdx}`}
                checked={opt.correct}
                onChange={() => setCorrectOption(qIdx, oIdx)}
                className="accent-primary cursor-pointer"
              />
              <input
                value={opt.text}
                onChange={(e) => updateOption(qIdx, oIdx, e.target.value)}
                placeholder={`Вариант ${oIdx + 1}`}
                className="flex-1 rounded-xl border border-border bg-bg px-3 py-2 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <button
                type="button"
                onClick={() => removeOption(qIdx, oIdx)}
                disabled={q.options.length <= 2}
                className="text-text-secondary hover:text-red-400 transition-colors disabled:opacity-30 cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </div>
          ))}
          <button
            type="button"
            onClick={() => addOption(qIdx)}
            className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
          >
            <Plus size={12} />
            Вариант
          </button>
        </div>
      ))}
      <button
        type="button"
        onClick={addQuestion}
        className="flex items-center gap-1.5 text-xs text-primary hover:text-primary/80 transition-colors cursor-pointer"
      >
        <Plus size={12} />
        Вопрос
      </button>
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
      <Input
        label="Слово"
        value={step.word}
        onChange={(e) => onChange({ word: e.target.value })}
        placeholder="Hello"
      />
      <Input
        label="Фонетика"
        value={step.phonetic}
        onChange={(e) => onChange({ phonetic: e.target.value })}
        placeholder="/həˈloʊ/"
      />
      <Input
        label="URL аудио"
        value={step.audioUrl}
        onChange={(e) => onChange({ audioUrl: e.target.value })}
        placeholder="https://example.com/audio.mp3"
      />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Допустимые формы <span className="text-xs text-text-secondary/60">(по одной на строку)</span>
        </label>
        <textarea
          value={step.acceptedForms.join("\n")}
          onChange={(e) =>
            onChange({ acceptedForms: e.target.value.split("\n") })
          }
          placeholder={"hello\nhello!"}
          rows={3}
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
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
      <Input
        label="Подсказка"
        value={step.hint}
        onChange={(e) => onChange({ hint: e.target.value })}
        placeholder="Составьте слово из букв..."
      />
      <Input
        label="Слово"
        value={step.word}
        onChange={(e) => onChange({ word: e.target.value })}
        placeholder="algorithm"
      />
      <Input
        label="URL изображения"
        value={step.image || ""}
        onChange={(e) => onChange({ image: e.target.value })}
        placeholder="https://example.com/image.png"
      />
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
  const languages = [
    { value: "ru", label: "Русский" },
    { value: "en", label: "English" },
    { value: "kz", label: "Қазақша" },
    { value: "de", label: "Deutsch" },
    { value: "fr", label: "Français" },
  ];

  return (
    <div className="space-y-3">
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">Предложение</label>
        <textarea
          value={step.sentence}
          onChange={(e) => onChange({ sentence: e.target.value })}
          placeholder="Введите предложение для перевода..."
          rows={2}
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <div className="grid grid-cols-2 gap-3">
        <div>
          <label className="block text-sm text-text-secondary mb-1.5">Язык оригинала</label>
          <select
            value={step.sourceLanguage}
            onChange={(e) => onChange({ sourceLanguage: e.target.value })}
            className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm cursor-pointer"
          >
            {languages.map((l) => (
              <option key={l.value} value={l.value}>{l.label}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="block text-sm text-text-secondary mb-1.5">Язык перевода</label>
          <select
            value={step.targetLanguage}
            onChange={(e) => onChange({ targetLanguage: e.target.value })}
            className="w-full rounded-xl border border-border bg-bg px-3 py-2 text-text outline-none transition-colors focus:border-primary/50 text-sm cursor-pointer"
          >
            {languages.map((l) => (
              <option key={l.value} value={l.value}>{l.label}</option>
            ))}
          </select>
        </div>
      </div>
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Принятые ответы <span className="text-xs text-text-secondary/60">(по одному на строку)</span>
        </label>
        <textarea
          value={step.acceptedAnswers.join("\n")}
          onChange={(e) =>
            onChange({ acceptedAnswers: e.target.value.split("\n") })
          }
          placeholder={"The cat sat on the mat\nA cat sat on a mat"}
          rows={3}
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
      <label className="flex items-center gap-2 cursor-pointer">
        <input
          type="checkbox"
          checked={step.aiCheck}
          onChange={(e) => onChange({ aiCheck: e.target.checked })}
          className="accent-primary"
        />
        <span className="text-sm text-text-secondary">Проверка с помощью AI</span>
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
  // Convert segments to markup string
  const segmentsToMarkup = (segments: StepClozePassage["segments"]): string => {
    return segments
      .map((seg) => {
        if (seg.type === "text") return seg.value;
        if (seg.options && seg.options.length > 0) {
          return `{${seg.answer}|${seg.options.join(",")}}`;
        }
        return `{${seg.answer}}`;
      })
      .join("");
  };

  // Parse markup string back to segments
  const markupToSegments = (markup: string): StepClozePassage["segments"] => {
    const segments: StepClozePassage["segments"] = [];
    const regex = /\{([^}]+)\}/g;
    let lastIndex = 0;
    let match;

    while ((match = regex.exec(markup)) !== null) {
      if (match.index > lastIndex) {
        segments.push({ type: "text", value: markup.slice(lastIndex, match.index) });
      }
      const inner = match[1];
      const pipeIdx = inner.indexOf("|");
      if (pipeIdx >= 0) {
        const answer = inner.slice(0, pipeIdx);
        const options = inner.slice(pipeIdx + 1).split(",").map((s) => s.trim());
        segments.push({ type: "blank", answer, options });
      } else {
        segments.push({ type: "blank", answer: inner });
      }
      lastIndex = regex.lastIndex;
    }

    if (lastIndex < markup.length) {
      segments.push({ type: "text", value: markup.slice(lastIndex) });
    }

    return segments.length > 0 ? segments : [{ type: "text", value: "" }];
  };

  const [markup, setMarkup] = useState(() => segmentsToMarkup(step.segments));

  const handleMarkupChange = (value: string) => {
    setMarkup(value);
    onChange({ segments: markupToSegments(value) });
  };

  return (
    <div className="space-y-3">
      <Input
        label="Инструкция"
        value={step.instruction}
        onChange={(e) => onChange({ instruction: e.target.value })}
        placeholder="Заполните пропуски в тексте..."
      />
      <div>
        <label className="block text-sm text-text-secondary mb-1.5">
          Текст с пропусками{" "}
          <span className="text-xs text-text-secondary/60">
            {"Синтаксис: {ответ} — ввод, {ответ|вар1,вар2,вар3} — выбор"}
          </span>
        </label>
        <textarea
          value={markup}
          onChange={(e) => handleMarkupChange(e.target.value)}
          placeholder={"The cat {sat} on the {mat|mat,hat,bat}."}
          rows={5}
          className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
        />
      </div>
    </div>
  );
}

// ─── Step Card ──────────────────────────────────────────────────────────────

function StepCard({
  step,
  index,
  onUpdate,
  onDelete,
}: {
  step: EditorStep;
  index: number;
  onUpdate: (patch: Partial<LessonStep>) => void;
  onDelete: () => void;
}) {
  const [collapsed, setCollapsed] = useState(false);
  const meta = STEP_TYPES.find((t) => t.type === step.type)!;

  return (
    <Reorder.Item
      value={step}
      id={step._id}
      className="rounded-2xl border border-white/6 bg-[#0A0A0A] overflow-hidden"
    >
      {/* Card header */}
      <div className="flex items-center gap-3 px-4 py-3 border-b border-white/6">
        {/* Drag handle */}
        <div className="cursor-grab active:cursor-grabbing text-text-secondary hover:text-text transition-colors">
          <GripVertical size={16} />
        </div>

        {/* Type badge */}
        <div
          className="flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium"
          style={{ backgroundColor: `${meta.color}20`, color: meta.color }}
        >
          {meta.icon}
          {meta.label}
        </div>

        <span className="text-xs text-text-secondary">Шаг {index + 1}</span>

        <div className="ml-auto flex items-center gap-2">
          <button
            type="button"
            onClick={() => setCollapsed((v) => !v)}
            className="text-text-secondary hover:text-text transition-colors cursor-pointer"
          >
            <motion.div animate={{ rotate: collapsed ? -90 : 0 }} transition={{ duration: 0.2 }}>
              <ChevronDown size={16} />
            </motion.div>
          </button>
          <button
            type="button"
            onClick={onDelete}
            className="text-text-secondary hover:text-red-400 transition-colors cursor-pointer"
          >
            <Trash2 size={15} />
          </button>
        </div>
      </div>

      {/* Form body */}
      <AnimatePresence initial={false}>
        {!collapsed && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <div className="p-4">
              {step.type === "info" && (
                <InfoForm
                  step={step as StepInfo & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "quiz" && (
                <QuizForm
                  step={step as StepQuiz & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "drag-order" && (
                <DragOrderForm
                  step={step as StepDragOrder & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "code-puzzle" && (
                <CodePuzzleForm
                  step={step as StepCodePuzzle & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "fill-blank" && (
                <FillBlankForm
                  step={step as StepFillBlank & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "matching" && (
                <MatchingForm
                  step={step as StepMatching & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "true-false" && (
                <TrueFalseForm
                  step={step as StepTrueFalse & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "flashcards" && (
                <FlashcardsForm
                  step={step as StepFlashcards & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "type-answer" && (
                <TypeAnswerForm
                  step={step as StepTypeAnswer & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "image-hotspot" && (
                <ImageHotspotForm
                  step={step as StepImageHotspot & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "code-editor" && (
                <CodeEditorForm
                  step={step as StepCodeEditor & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "timeline" && (
                <TimelineForm
                  step={step as StepTimeline & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "category-sort" && (
                <CategorySortForm
                  step={step as StepCategorySort & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "video" && (
                <VideoForm
                  step={step as StepVideo & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "audio" && (
                <AudioForm
                  step={step as StepAudio & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "embed" && (
                <EmbedForm
                  step={step as StepEmbed & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "terminal-sim" && (
                <TerminalSimForm
                  step={step as StepTerminalSim & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "multi-select" && (
                <MultiSelectForm
                  step={step as StepMultiSelect & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "conversation-sim" && (
                <ConversationSimForm
                  step={step as StepConversationSim & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "highlight-text" && (
                <HighlightTextForm
                  step={step as StepHighlightText & { _id: string }}
                  onChange={onUpdate}
                />
              )}
              {step.type === "snippet-order" && (
                <SnippetOrderForm
                  step={step as StepSnippetOrder & { _id: string }}
                  onChange={onUpdate}
                />
              )}
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
              {step.type === "tower-defense" && (
                <div className="text-sm text-text-secondary px-1">
                  Игра Tower Defense. Вопросы берутся автоматически из других шагов этого урока.
                  Убедитесь что в уроке есть quiz, true-false или type-answer шаги.
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </Reorder.Item>
  );
}

// ─── Add Step Dropdown ─────────────────────────────────────────────────────

function AddStepButton({ onAdd }: { onAdd: (type: StepType) => void }) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  // Close on outside click
  const handleDocClick = useCallback(
    (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    },
    []
  );

  return (
    <div ref={ref} className="relative">
      <button
        type="button"
        onClick={() => {
          setOpen((v) => !v);
          if (!open) document.addEventListener("click", handleDocClick, { once: true });
        }}
        className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-primary/10 border border-primary/30 text-primary text-sm font-medium hover:bg-primary/20 transition-all cursor-pointer"
      >
        <Plus size={15} />
        Добавить шаг
        <ChevronDown size={13} />
      </button>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, y: -8, scale: 0.96 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -8, scale: 0.96 }}
            transition={{ duration: 0.15 }}
            className="absolute left-0 top-full mt-2 z-50 w-48 rounded-xl bg-[#111111] border border-white/6 shadow-2xl overflow-hidden"
          >
            {STEP_TYPES.map((t) => (
              <button
                key={t.type}
                type="button"
                onClick={() => {
                  onAdd(t.type);
                  setOpen(false);
                }}
                className="w-full flex items-center gap-2.5 px-4 py-2.5 text-sm text-text-secondary hover:text-text hover:bg-white/5 transition-colors cursor-pointer"
              >
                <span style={{ color: t.color }}>{t.icon}</span>
                {t.label}
              </button>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

// ─── Main Component ─────────────────────────────────────────────────────────

interface StepEditorProps {
  lessonId: string;
  lessonTitle: string;
  onClose: () => void;
  onSaved?: () => void;
}

export function StepEditor({
  lessonId,
  lessonTitle,
  onClose,
  onSaved,
}: StepEditorProps) {
  const [steps, setSteps] = useState<EditorStep[]>([]);
  const [loadingSteps, setLoadingSteps] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch steps from the API on mount so we always have the latest saved state
  useEffect(() => {
    setLoadingSteps(true);
    courseApi
      .getLessonSteps(lessonId)
      .then((res) => {
        setSteps(res.steps.map((s) => ({ ...s, _id: nanoid() })));
      })
      .catch(() => {
        setError("Не удалось загрузить шаги урока.");
      })
      .finally(() => setLoadingSteps(false));
  }, [lessonId]);

  const handleAdd = (type: StepType) => {
    setSteps((prev) => [...prev, { ...defaultStep(type), _id: nanoid() } as EditorStep]);
  };

  const handleUpdate = (id: string, patch: Partial<LessonStep>) => {
    setSteps((prev) =>
      prev.map((s) => (s._id === id ? ({ ...s, ...patch } as EditorStep) : s))
    );
  };

  const handleDelete = (id: string) => {
    setSteps((prev) => prev.filter((s) => s._id !== id));
  };

  const handleSave = async () => {
    setSaving(true);
    setError(null);
    try {
      // Strip internal _id before sending to API
      const payload = steps.map(({ _id, ...rest }) => rest as LessonStep);
      await courseApi.saveLessonSteps(lessonId, payload);
      onSaved?.();
      onClose();
    } catch {
      setError("Не удалось сохранить шаги. Попробуйте снова.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 z-50 bg-black flex flex-col"
    >
      {/* Header */}
      <div className="flex items-center gap-4 px-4 lg:px-6 py-4 border-b border-white/6 bg-[#111111]">
        <button
          type="button"
          onClick={onClose}
          className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-white/10 text-text-secondary hover:text-text transition-all cursor-pointer"
        >
          <X size={18} />
        </button>
        <div className="flex-1 min-w-0">
          <p className="text-xs text-text-secondary">Редактор шагов</p>
          <h2 className="text-sm font-semibold truncate">{lessonTitle}</h2>
        </div>
        <div className="flex items-center gap-3">
          <span className="text-xs text-text-secondary hidden sm:block">
            {steps.length} {steps.length === 1 ? "шаг" : "шагов"}
          </span>
          <Button onClick={handleSave} disabled={saving} size="sm">
            <Save size={14} />
            {saving ? "Сохранение..." : "Сохранить шаги"}
          </Button>
        </div>
      </div>

      {/* Error banner */}
      <AnimatePresence>
        {error && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            className="bg-red-500/10 border-b border-red-500/20 px-6 py-2.5 text-sm text-red-400"
          >
            {error}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Content */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-2xl mx-auto px-4 lg:px-0 py-6 space-y-3">
          {loadingSteps ? (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: [0.4, 1, 0.4] }}
              transition={{ repeat: Infinity, duration: 1.4 }}
              className="text-center py-16 text-sm text-text-secondary"
            >
              Загрузка шагов...
            </motion.div>
          ) : steps.length === 0 ? (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="text-center py-16 text-text-secondary"
            >
              <FileText size={40} className="mx-auto mb-3 opacity-30" />
              <p className="text-sm">Шагов пока нет.</p>
              <p className="text-xs mt-1 text-text-secondary/60">Добавьте первый шаг ниже.</p>
            </motion.div>
          ) : (
            <Reorder.Group
              axis="y"
              values={steps}
              onReorder={setSteps}
              className="space-y-3"
            >
              {steps.map((step, index) => (
                <StepCard
                  key={step._id}
                  step={step}
                  index={index}
                  onUpdate={(patch) => handleUpdate(step._id, patch)}
                  onDelete={() => handleDelete(step._id)}
                />
              ))}
            </Reorder.Group>
          )}

          {/* Add step button — hidden while initial load is in progress */}
          {!loadingSteps && (
            <div className="flex justify-center pt-2">
              <AddStepButton onAdd={handleAdd} />
            </div>
          )}
        </div>
      </div>

      {/* Footer save */}
      <div className="border-t border-white/6 bg-[#111111] px-4 lg:px-6 py-4 flex items-center justify-between">
        <button
          type="button"
          onClick={onClose}
          className="text-sm text-text-secondary hover:text-text transition-colors cursor-pointer"
        >
          Отменить изменения
        </button>
        <Button onClick={handleSave} disabled={saving}>
          <Save size={15} />
          {saving ? "Сохранение..." : "Сохранить шаги"}
        </Button>
      </div>
    </motion.div>
  );
}
