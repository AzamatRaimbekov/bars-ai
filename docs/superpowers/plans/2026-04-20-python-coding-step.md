# Python Coding Step — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `python-coding` step type that runs Python code in the browser via Pyodide, validates output, and integrate into the Python course.

**Architecture:** Pyodide WASM runtime loaded in a Web Worker. New `PythonCodingStep` component with CodeMirror (Python) + console. Steps stored as JSON in existing `steps` column. No backend changes.

**Tech Stack:** Pyodide 0.27, @codemirror/lang-python, Web Workers, existing CourseStepPlayer

---

## File Structure

| File | Action | Responsibility |
|---|---|---|
| `src/lib/pyodideWorker.ts` | Create | Web Worker: load Pyodide, run code, capture stdout |
| `src/hooks/usePyodide.ts` | Create | React hook: init worker, run code, handle timeout |
| `src/components/courses/steps/PythonCodingStep.tsx` | Create | UI: editor + console + validation |
| `src/services/courseApi.ts` | Modify | Add `StepPythonCoding` interface and type |
| `src/components/courses/CourseStepPlayer.tsx` | Modify | Add import + case for `python-coding` |
| `backend/seed_python_course.py` | Replace | Full Python course with coding exercises |
| `package.json` | Modify | Add @codemirror/lang-python |

---

### Task 1: Install @codemirror/lang-python

**Files:**
- Modify: `package.json`

- [ ] **Step 1: Install the package**

```bash
npm install @codemirror/lang-python
```

- [ ] **Step 2: Verify it installed**

```bash
node -e "require('@codemirror/lang-python')" 2>&1 || echo "ESM module, OK"
ls node_modules/@codemirror/lang-python/package.json
```

- [ ] **Step 3: Commit**

```bash
git add package.json package-lock.json
git commit -m "chore: add @codemirror/lang-python"
```

---

### Task 2: Add StepPythonCoding type to courseApi.ts

**Files:**
- Modify: `src/services/courseApi.ts:61-88` (StepType union)
- Modify: `src/services/courseApi.ts` (add interface after StepCodeEditor ~line 159)

- [ ] **Step 1: Add "python-coding" to StepType union**

In `src/services/courseApi.ts`, add `"python-coding"` to the StepType union (before the closing semicolon at line 88):

```typescript
  | "tower-defense"
  | "python-coding";
```

- [ ] **Step 2: Add StepPythonCoding interface**

After the `StepCodeEditor` interface (~line 159), add:

```typescript
export interface StepPythonCoding {
  type: "python-coding";
  prompt: string;
  starterCode: string;
  expectedOutput: string;
  hint?: string;
}
```

- [ ] **Step 3: Add StepPythonCoding to LessonStep union**

Find the `LessonStep` type union and add `| StepPythonCoding`.

- [ ] **Step 4: Commit**

```bash
git add src/services/courseApi.ts
git commit -m "feat: add StepPythonCoding type definition"
```

---

### Task 3: Create Pyodide Web Worker

**Files:**
- Create: `src/lib/pyodideWorker.ts`

- [ ] **Step 1: Create the worker file**

```typescript
// src/lib/pyodideWorker.ts
// This file runs as a Web Worker — no DOM access

declare const self: DedicatedWorkerGlobalScope;

let pyodide: any = null;

async function loadPyodideRuntime() {
  if (pyodide) return pyodide;
  importScripts("https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js");
  pyodide = await (self as any).loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.27.0/full/",
  });
  return pyodide;
}

self.onmessage = async (e: MessageEvent) => {
  const { id, code } = e.data;

  try {
    const py = await loadPyodideRuntime();

    // Capture stdout
    py.runPython(`
import sys, io
_stdout_capture = io.StringIO()
_stderr_capture = io.StringIO()
sys.stdout = _stdout_capture
sys.stderr = _stderr_capture
`);

    try {
      py.runPython(code);
    } catch (err: any) {
      const stderr = py.runPython("_stderr_capture.getvalue()");
      // Reset stdio
      py.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__");
      self.postMessage({
        id,
        stdout: "",
        stderr: stderr || String(err.message || err),
        error: String(err.message || err),
      });
      return;
    }

    const stdout = py.runPython("_stdout_capture.getvalue()");
    const stderr = py.runPython("_stderr_capture.getvalue()");

    // Reset stdio for next run
    py.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__");

    self.postMessage({ id, stdout, stderr, error: null });
  } catch (err: any) {
    self.postMessage({
      id,
      stdout: "",
      stderr: String(err.message || err),
      error: String(err.message || err),
    });
  }
};
```

- [ ] **Step 2: Commit**

```bash
git add src/lib/pyodideWorker.ts
git commit -m "feat: Pyodide Web Worker for Python execution"
```

---

### Task 4: Create usePyodide hook

**Files:**
- Create: `src/hooks/usePyodide.ts`

- [ ] **Step 1: Create the hook**

```typescript
// src/hooks/usePyodide.ts
import { useState, useRef, useCallback, useEffect } from "react";

interface RunResult {
  stdout: string;
  stderr: string;
  error: string | null;
}

let sharedWorker: Worker | null = null;
let workerReady = false;
let pendingCallbacks = new Map<string, (result: RunResult) => void>();
let initPromise: Promise<void> | null = null;

function getWorker(): Promise<Worker> {
  if (sharedWorker && workerReady) return Promise.resolve(sharedWorker);

  if (!initPromise) {
    initPromise = new Promise((resolve) => {
      sharedWorker = new Worker(
        new URL("../lib/pyodideWorker.ts", import.meta.url),
        { type: "classic" }
      );
      sharedWorker.onmessage = (e) => {
        workerReady = true;
        const { id, ...result } = e.data;
        const cb = pendingCallbacks.get(id);
        if (cb) {
          pendingCallbacks.delete(id);
          cb(result);
        }
        resolve();
      };
      // Send a warmup message to trigger Pyodide load
      const warmupId = "warmup-" + Date.now();
      pendingCallbacks.set(warmupId, () => {});
      sharedWorker.postMessage({ id: warmupId, code: "print('ready')" });
    });
  }

  return initPromise.then(() => sharedWorker!);
}

export function usePyodide() {
  const [isLoading, setIsLoading] = useState(true);
  const [isRunning, setIsRunning] = useState(false);
  const timeoutRef = useRef<ReturnType<typeof setTimeout>>();

  useEffect(() => {
    getWorker().then(() => setIsLoading(false));
  }, []);

  const runCode = useCallback(
    async (code: string): Promise<RunResult> => {
      setIsRunning(true);
      const worker = await getWorker();
      const id = "run-" + Date.now() + "-" + Math.random();

      return new Promise<RunResult>((resolve) => {
        timeoutRef.current = setTimeout(() => {
          pendingCallbacks.delete(id);
          setIsRunning(false);
          resolve({
            stdout: "",
            stderr: "Превышено время выполнения (5 сек). Возможно бесконечный цикл?",
            error: "timeout",
          });
        }, 5000);

        pendingCallbacks.set(id, (result) => {
          clearTimeout(timeoutRef.current);
          setIsRunning(false);
          resolve(result);
        });

        worker.postMessage({ id, code });
      });
    },
    []
  );

  return { runCode, isLoading, isRunning, isReady: !isLoading };
}
```

- [ ] **Step 2: Commit**

```bash
git add src/hooks/usePyodide.ts
git commit -m "feat: usePyodide hook with shared worker and timeout"
```

---

### Task 5: Create PythonCodingStep component

**Files:**
- Create: `src/components/courses/steps/PythonCodingStep.tsx`

- [ ] **Step 1: Create the component**

```tsx
// src/components/courses/steps/PythonCodingStep.tsx
import { useState, useCallback } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { Play, RotateCcw, CheckCircle2, XCircle, Lightbulb, Loader2 } from "lucide-react";
import { usePyodide } from "@/hooks/usePyodide";
import type { StepPythonCoding } from "@/services/courseApi";

interface Props {
  step: StepPythonCoding;
  onComplete: () => void;
}

export default function PythonCodingStep({ step, onComplete }: Props) {
  const { runCode, isLoading, isRunning } = usePyodide();
  const [code, setCode] = useState(step.starterCode || "");
  const [output, setOutput] = useState("");
  const [status, setStatus] = useState<"idle" | "success" | "error" | "timeout">("idle");
  const [showHint, setShowHint] = useState(false);

  const handleRun = useCallback(async () => {
    setOutput("");
    setStatus("idle");
    const result = await runCode(code);

    if (result.error === "timeout") {
      setOutput("⏱ Превышено время выполнения (5 сек)");
      setStatus("timeout");
      return;
    }

    if (result.error) {
      setOutput(result.stderr || result.error);
      setStatus("error");
      return;
    }

    const got = result.stdout.trim();
    const expected = step.expectedOutput.trim();
    setOutput(got || "(нет вывода)");

    if (got === expected) {
      setStatus("success");
      onComplete();
    } else {
      setStatus("error");
    }
  }, [code, runCode, step.expectedOutput, onComplete]);

  const handleReset = () => {
    setCode(step.starterCode || "");
    setOutput("");
    setStatus("idle");
  };

  return (
    <div className="flex flex-col gap-4">
      {/* Prompt */}
      <div className="text-white/90 text-sm leading-relaxed whitespace-pre-wrap">
        {step.prompt}
      </div>

      {/* Loading Pyodide */}
      {isLoading && (
        <div className="flex items-center gap-2 text-white/50 text-sm py-4">
          <Loader2 className="animate-spin" size={16} />
          Загрузка Python... (первый раз может занять несколько секунд)
        </div>
      )}

      {/* Code Editor */}
      <div className={`rounded-xl overflow-hidden border ${
        status === "success" ? "border-green-500/50" :
        status === "error" || status === "timeout" ? "border-red-500/50" :
        "border-white/10"
      }`}>
        <div className="bg-[#1e1e2e] px-3 py-1.5 flex items-center justify-between border-b border-white/5">
          <span className="text-xs text-white/40 font-mono">Python</span>
          <div className="flex gap-1.5">
            <div className="w-2.5 h-2.5 rounded-full bg-red-500/60" />
            <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/60" />
            <div className="w-2.5 h-2.5 rounded-full bg-green-500/60" />
          </div>
        </div>
        <CodeMirror
          value={code}
          onChange={setCode}
          extensions={[python()]}
          theme="dark"
          basicSetup={{
            lineNumbers: true,
            highlightActiveLineGutter: true,
            foldGutter: false,
          }}
          editable={status !== "success"}
          className="text-sm"
          minHeight="120px"
          maxHeight="300px"
        />
      </div>

      {/* Buttons */}
      <div className="flex gap-2">
        <button
          onClick={handleRun}
          disabled={isLoading || isRunning || status === "success"}
          className="flex items-center gap-2 px-4 py-2 rounded-lg bg-green-600 hover:bg-green-500 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium transition-colors"
        >
          {isRunning ? (
            <Loader2 className="animate-spin" size={16} />
          ) : (
            <Play size={16} />
          )}
          {isRunning ? "Выполняется..." : "Запустить"}
        </button>
        <button
          onClick={handleReset}
          disabled={status === "success"}
          className="flex items-center gap-2 px-3 py-2 rounded-lg bg-white/5 hover:bg-white/10 disabled:opacity-40 text-white/60 text-sm transition-colors"
        >
          <RotateCcw size={14} />
          Сбросить
        </button>
        {step.hint && (
          <button
            onClick={() => setShowHint(!showHint)}
            className="flex items-center gap-2 px-3 py-2 rounded-lg bg-yellow-500/10 hover:bg-yellow-500/20 text-yellow-400 text-sm transition-colors ml-auto"
          >
            <Lightbulb size={14} />
            Подсказка
          </button>
        )}
      </div>

      {/* Hint */}
      {showHint && step.hint && (
        <div className="px-3 py-2 rounded-lg bg-yellow-500/10 border border-yellow-500/20 text-yellow-200/80 text-sm">
          {step.hint}
        </div>
      )}

      {/* Console Output */}
      {output && (
        <div className="rounded-xl overflow-hidden border border-white/10">
          <div className="bg-[#0d0d14] px-3 py-1.5 border-b border-white/5">
            <span className="text-xs text-white/40 font-mono">Консоль</span>
          </div>
          <pre className="bg-[#0d0d14] p-3 text-sm font-mono text-white/80 whitespace-pre-wrap min-h-[40px] max-h-[200px] overflow-auto">
            {output}
          </pre>
        </div>
      )}

      {/* Result */}
      {status === "success" && (
        <div className="flex items-center gap-2 text-green-400 text-sm">
          <CheckCircle2 size={18} />
          Верно! Отличная работа!
        </div>
      )}
      {status === "error" && output && !output.startsWith("⏱") && (
        <div className="flex items-start gap-2 text-red-400 text-sm">
          <XCircle size={18} className="mt-0.5 shrink-0" />
          <div>
            <span>Не совпадает. </span>
            <span className="text-white/40">Ожидалось: </span>
            <code className="text-green-400">{step.expectedOutput}</code>
          </div>
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add src/components/courses/steps/PythonCodingStep.tsx
git commit -m "feat: PythonCodingStep component with Pyodide execution"
```

---

### Task 6: Integrate into CourseStepPlayer

**Files:**
- Modify: `src/components/courses/CourseStepPlayer.tsx:1-59` (imports)
- Modify: `src/components/courses/CourseStepPlayer.tsx:~2680` (switch case)

- [ ] **Step 1: Add import at top of CourseStepPlayer.tsx**

After the existing step imports (around line 59), add:

```typescript
import PythonCodingStep from "./steps/PythonCodingStep";
```

Also add to the type import from courseApi:

```typescript
import type { ..., StepPythonCoding } from "@/services/courseApi";
```

- [ ] **Step 2: Add case in renderStep switch**

Find the switch statement that handles step types (around line 2615). After the last `case`, before `default:`, add:

```typescript
      case "python-coding":
        return (
          <PythonCodingStep
            step={step as StepPythonCoding}
            onComplete={() => setStepDone(true)}
          />
        );
```

- [ ] **Step 3: Verify it builds**

```bash
npm run build
```

- [ ] **Step 4: Commit**

```bash
git add src/components/courses/CourseStepPlayer.tsx
git commit -m "feat: integrate python-coding step into CourseStepPlayer"
```

---

### Task 7: Rewrite Python course with coding exercises

**Files:**
- Replace: `backend/seed_python_course.py`

- [ ] **Step 1: Rewrite seed_python_course.py**

Replace the entire file with a Python course that mixes `info` steps (theory) and `python-coding` steps (practice). The course should have 8 sections progressing from basics to functions.

Each section has 4-6 lessons. Each lesson has ~4-6 steps mixing theory and coding. Example lesson structure:

```python
{
    "title": "Привет, мир!",
    "steps": [
        {"type": "info", "title": "Ваша первая программа", "markdown": "## print()\n\nФункция `print()` выводит текст на экран...\n\n```python\nprint(\"Hello, World!\")\n```"},
        {"type": "python-coding", "prompt": "Напишите программу, которая выводит: Hello, World!", "starterCode": "# Напишите ваш код здесь\n", "expectedOutput": "Hello, World!", "hint": "Используйте print(\"Hello, World!\")"},
        {"type": "python-coding", "prompt": "Выведите своё имя с помощью print()", "starterCode": "# Выведите любое имя\n", "expectedOutput": "", "hint": "print(\"Азамат\") — подойдёт любое имя"},
        {"type": "quiz", "question": "Что выведет print(2 + 3)?", "options": [{"id": "a", "text": "23", "correct": False}, {"id": "b", "text": "5", "correct": True}, {"id": "c", "text": "2 + 3", "correct": False}]},
    ]
}
```

Note: When `expectedOutput` is empty string `""`, any output is accepted (free-form exercise).

Full course sections:
1. **Основы: print() и комментарии** (3 lessons, ~15 steps)
2. **Переменные и типы данных** (4 lessons, ~20 steps)
3. **Строки** (3 lessons, ~15 steps)
4. **Условия: if/elif/else** (3 lessons, ~15 steps)
5. **Циклы: for и while** (4 lessons, ~20 steps)
6. **Списки** (3 lessons, ~15 steps)
7. **Функции** (4 lessons, ~20 steps)
8. **Словари и финальный проект** (3 lessons, ~15 steps)

Total: ~27 lessons, ~135 steps, roughly 50% coding / 30% info / 20% quiz.

- [ ] **Step 2: Commit**

```bash
git add backend/seed_python_course.py
git commit -m "feat: Python course with real coding exercises (Pyodide)"
```

---

### Task 8: Deploy and verify

- [ ] **Step 1: Push to GitHub**

```bash
git push origin main
```

- [ ] **Step 2: Deploy to Railway**

```bash
railway up
```

- [ ] **Step 3: Wait for deploy and verify**

```bash
railway service status
curl -s https://app-production-ebd5.up.railway.app/api/health
```

- [ ] **Step 4: Test Python coding step**

Open https://app-production-ebd5.up.railway.app, navigate to Python course, open a lesson with a coding step. Type `print("Hello, World!")` and click Run. Should see green checkmark.

- [ ] **Step 5: Final commit with any fixes**

```bash
git add -A
git commit -m "fix: deploy adjustments for python-coding"
git push origin main
```
