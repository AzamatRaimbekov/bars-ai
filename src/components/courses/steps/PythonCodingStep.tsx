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

    if (!expected || got === expected) {
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
      <div className="text-white/90 text-sm leading-relaxed whitespace-pre-wrap">
        {step.prompt}
      </div>

      {isLoading && (
        <div className="flex items-center gap-2 text-white/50 text-sm py-4">
          <Loader2 className="animate-spin" size={16} />
          Загрузка Python... (первый раз может занять несколько секунд)
        </div>
      )}

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

      <div className="flex gap-2">
        <button
          onClick={handleRun}
          disabled={isLoading || isRunning || status === "success"}
          className="flex items-center gap-2 px-4 py-2 rounded-lg bg-green-600 hover:bg-green-500 disabled:opacity-40 disabled:cursor-not-allowed text-white text-sm font-medium transition-colors"
        >
          {isRunning ? <Loader2 className="animate-spin" size={16} /> : <Play size={16} />}
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

      {showHint && step.hint && (
        <div className="px-3 py-2 rounded-lg bg-yellow-500/10 border border-yellow-500/20 text-yellow-200/80 text-sm">
          {step.hint}
        </div>
      )}

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
