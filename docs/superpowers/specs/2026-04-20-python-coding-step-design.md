# Python Coding Step — Pyodide Integration

## Summary

Add a `python-coding` step type to the lesson system that lets students write and run Python code directly in the browser using Pyodide. Code output is compared against expected output for validation.

## Architecture

- **Pyodide** loads Python 3.12 WASM runtime in a Web Worker (one-time load, cached by browser)
- **PythonCodingStep** component: CodeMirror editor (Python syntax) + console output + validation
- **No backend changes** — all execution happens client-side

## Step JSON Format

```json
{
  "type": "python-coding",
  "prompt": "Напишите программу которая выводит сумму 2 + 3",
  "starterCode": "# Ваш код здесь\n",
  "expectedOutput": "5",
  "hint": "Используйте print() и оператор +"
}
```

## Components

### 1. Pyodide Worker (`src/lib/pyodideWorker.ts`)

Web Worker that:
- Loads Pyodide from CDN (`https://cdn.jsdelivr.net/pyodide/v0.27.0/full/`)
- Exposes `runPython(code: string)` → `{ stdout: string, stderr: string, error?: string }`
- Captures stdout/stderr via Pyodide's `io` redirect
- Enforces 5-second timeout (terminates and recreates worker on timeout)
- Singleton — one worker for the entire app session

### 2. `usePyodide` Hook (`src/hooks/usePyodide.ts`)

```typescript
const { runCode, isLoading, isReady } = usePyodide()
// runCode(code) → Promise<{ stdout, stderr, error? }>
```

- Initializes worker on first use
- Shows loading state while Pyodide downloads (~10MB, cached after first load)
- Handles timeouts and worker crashes

### 3. `PythonCodingStep` Component (`src/components/courses/steps/PythonCodingStep.tsx`)

UI layout:
1. **Prompt** — задание в markdown
2. **CodeMirror editor** — Python syntax highlighting, line numbers, starter code
3. **Button bar** — "Запустить" (▶) and "Сбросить" buttons
4. **Console** — dark terminal-style output area
5. **Result** — green checkmark + XP on success, red "Expected X, got Y" on failure
6. **Hint** — collapsible hint button (if hint provided)

States:
- `idle` — editor ready, no output
- `running` — spinner on Run button, editor disabled
- `success` — green border, checkmark, XP awarded
- `error` — red border, diff shown
- `timeout` — "Code took too long (5s limit)"

### 4. Integration into `CourseStepPlayer.tsx`

Add `case "python-coding"` to the renderStep switch, render `PythonCodingStep`.

### 5. CodeMirror Python Support

Add `@codemirror/lang-python` package for syntax highlighting. Already have JS/HTML/CSS extensions.

## Validation Logic

```
stdout = pyodide.runPython(code).stdout
result = stdout.trim() === expectedOutput.trim()
```

- Comparison is exact string match after trimming whitespace
- Multi-line output supported (compare line by line)
- Empty expectedOutput means any output is accepted (free-form exercises)

## Python Course Content

Update `seed_python_course.py` to include `python-coding` steps in lessons. Example progression:

**Section 1 (Basics):**
- print("Hello, World!")
- Variables: name = "Азамат"; print(name)
- Math: print(2 + 3 * 4)

**Section 2 (Strings):**
- String concatenation
- f-strings
- .upper(), .lower()

**Section 3 (Conditions):**
- if/else
- Comparison operators

**Section 4 (Loops):**
- for i in range(5)
- while loops
- List iteration

**Section 5+ (Functions, Lists, Dicts):**
- def sum(a, b): return a + b; print(sum(2, 3))
- List operations
- Dictionary access

Each lesson mixes `info` steps (theory) with `python-coding` steps (practice) — roughly 50/50.

## Performance

- Pyodide WASM: ~10MB first load, cached by service worker (PWA already configured)
- Worker initialization: ~2-3 seconds first time
- Code execution: <100ms for simple programs
- Loading state shown with skeleton while Pyodide initializes

## Security

- Pyodide runs in Web Worker sandbox — no access to DOM, cookies, localStorage
- Network access blocked by Worker scope
- 5-second timeout kills infinite loops
- No file system access

## Files to Create/Modify

| File | Action |
|---|---|
| `src/lib/pyodideWorker.ts` | Create — Web Worker for Pyodide |
| `src/hooks/usePyodide.ts` | Create — React hook |
| `src/components/courses/steps/PythonCodingStep.tsx` | Create — UI component |
| `src/components/courses/CourseStepPlayer.tsx` | Modify — add case |
| `src/services/courseApi.ts` | Modify — add type |
| `backend/seed_python_course.py` | Modify — add coding steps |
| `package.json` | Modify — add @codemirror/lang-python |
| `index.html` | Optionally preload Pyodide |
