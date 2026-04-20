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
