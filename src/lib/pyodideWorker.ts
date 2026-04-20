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
