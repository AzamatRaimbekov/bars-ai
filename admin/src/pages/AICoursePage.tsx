import { useState, useRef } from "react";
import { Sparkles, Loader2, CheckCircle, BookOpen, ArrowRight, Upload, X, FileText } from "lucide-react";
import { apiFetchRaw } from "../lib/api";
import PageTransition from "../components/PageTransition";

interface GenerateResult {
  course_id: string;
  title: string;
  sections_count: number;
  lessons_count: number;
  status: string;
}

export default function AICoursePage() {
  const [topic, setTopic] = useState("");
  const [prompt, setPrompt] = useState("");
  const [language, setLanguage] = useState("ru");
  const [difficulty, setDifficulty] = useState("intermediate");
  const [sectionsCount, setSectionsCount] = useState(5);
  const [files, setFiles] = useState<File[]>([]);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<GenerateResult | null>(null);
  const [error, setError] = useState("");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFiles = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFiles((prev) => [...prev, ...Array.from(e.target.files!)]);
    }
  };

  const removeFile = (index: number) => {
    setFiles((prev) => prev.filter((_, i) => i !== index));
  };

  const handleGenerate = async () => {
    if (!topic.trim()) return;
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const formData = new FormData();
      formData.append("topic", topic.trim());
      formData.append("language", language);
      formData.append("difficulty", difficulty);
      formData.append("sections_count", String(sectionsCount));
      formData.append("prompt", prompt);
      for (const file of files) {
        formData.append("files", file);
      }
      const data = await apiFetchRaw<GenerateResult>("/api/ai/generate-course", {
        method: "POST",
        body: formData,
      });
      setResult(data);
    } catch (err: any) {
      setError(err.message || "Ошибка генерации курса");
    } finally {
      setLoading(false);
    }
  };

  return (
    <PageTransition>
      <div className="flex items-center gap-3 mb-6">
        <Sparkles size={20} className="text-orange-400" />
        <h1 className="text-xl font-bold text-white">AI Генератор курсов</h1>
      </div>

      <div className="max-w-2xl">
        <div className="bg-[var(--surface)] border border-white/8 rounded-xl p-6 space-y-5">
          {/* Topic */}
          <div>
            <label className="text-sm text-zinc-400 mb-2 block">Тема курса</label>
            <input
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="Например: Delivery Management, UX Research, Python для аналитиков..."
              className="w-full px-4 py-3 bg-white/5 border border-white/8 rounded-lg text-white placeholder-zinc-600 focus:outline-none focus:border-orange-500/50 transition-colors"
              disabled={loading}
            />
          </div>

          {/* Prompt */}
          <div>
            <label className="text-sm text-zinc-400 mb-2 block">
              Промпт / Инструкции для AI
              <span className="text-zinc-600 ml-1">(опционально)</span>
            </label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Опишите подробнее содержание курса, целевую аудиторию, какие темы включить, на что сделать акцент..."
              rows={4}
              className="w-full px-4 py-3 bg-white/5 border border-white/8 rounded-lg text-white placeholder-zinc-600 focus:outline-none focus:border-orange-500/50 transition-colors resize-none"
              disabled={loading}
            />
          </div>

          {/* File upload */}
          <div>
            <label className="text-sm text-zinc-400 mb-2 block">
              Файлы-источники
              <span className="text-zinc-600 ml-1">(PDF, Word, Excel, TXT — опционально)</span>
            </label>
            <input
              ref={fileInputRef}
              type="file"
              multiple
              accept=".pdf,.doc,.docx,.xls,.xlsx,.txt,.md,.csv"
              onChange={handleFiles}
              className="hidden"
            />
            <button
              onClick={() => fileInputRef.current?.click()}
              disabled={loading}
              className="flex items-center gap-2 px-4 py-2.5 bg-white/5 border border-dashed border-white/15 rounded-lg text-sm text-zinc-400 hover:border-orange-500/40 hover:text-zinc-300 transition-colors disabled:opacity-40 cursor-pointer"
            >
              <Upload size={16} />
              Загрузить файлы
            </button>

            {files.length > 0 && (
              <div className="mt-3 space-y-2">
                {files.map((file, i) => (
                  <div
                    key={`${file.name}-${i}`}
                    className="flex items-center gap-3 px-3 py-2 bg-white/3 border border-white/6 rounded-lg"
                  >
                    <FileText size={14} className="text-orange-400 shrink-0" />
                    <span className="text-sm text-zinc-300 truncate flex-1">{file.name}</span>
                    <span className="text-xs text-zinc-600 shrink-0">
                      {(file.size / 1024).toFixed(0)} KB
                    </span>
                    <button
                      onClick={() => removeFile(i)}
                      className="text-zinc-600 hover:text-red-400 transition-colors cursor-pointer"
                    >
                      <X size={14} />
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Settings row */}
          <div className="grid grid-cols-3 gap-4">
            <div>
              <label className="text-sm text-zinc-400 mb-2 block">Язык</label>
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="w-full px-3 py-2.5 bg-white/5 border border-white/8 rounded-lg text-white text-sm focus:outline-none focus:border-orange-500/50 transition-colors"
                disabled={loading}
              >
                <option value="ru">Русский</option>
                <option value="en">English</option>
              </select>
            </div>

            <div>
              <label className="text-sm text-zinc-400 mb-2 block">Сложность</label>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="w-full px-3 py-2.5 bg-white/5 border border-white/8 rounded-lg text-white text-sm focus:outline-none focus:border-orange-500/50 transition-colors"
                disabled={loading}
              >
                <option value="beginner">Начинающий</option>
                <option value="intermediate">Средний</option>
                <option value="advanced">Продвинутый</option>
              </select>
            </div>

            <div>
              <label className="text-sm text-zinc-400 mb-2 block">Секций</label>
              <select
                value={sectionsCount}
                onChange={(e) => setSectionsCount(Number(e.target.value))}
                className="w-full px-3 py-2.5 bg-white/5 border border-white/8 rounded-lg text-white text-sm focus:outline-none focus:border-orange-500/50 transition-colors"
                disabled={loading}
              >
                {[3, 4, 5, 6, 7, 8, 9, 10].map((n) => (
                  <option key={n} value={n}>{n} секций</option>
                ))}
              </select>
            </div>
          </div>

          {/* Generate button */}
          <button
            onClick={handleGenerate}
            disabled={loading || !topic.trim()}
            className="w-full flex items-center justify-center gap-2 py-3 px-4 rounded-lg font-semibold text-sm text-white transition-all disabled:opacity-40 cursor-pointer"
            style={{ background: loading ? "#333" : "linear-gradient(135deg, #F97316, #FB923C)" }}
          >
            {loading ? (
              <>
                <Loader2 size={18} className="animate-spin" />
                Генерация курса... (30-60 сек)
              </>
            ) : (
              <>
                <Sparkles size={18} />
                Сгенерировать курс
              </>
            )}
          </button>

          {error && (
            <div className="p-3 rounded-lg bg-red-500/10 border border-red-500/20 text-red-400 text-sm">
              {error}
            </div>
          )}

          {result && (
            <div className="p-4 rounded-lg bg-emerald-500/10 border border-emerald-500/20 space-y-3">
              <div className="flex items-center gap-2 text-emerald-400">
                <CheckCircle size={18} />
                <span className="font-semibold text-sm">Курс создан!</span>
              </div>
              <div className="space-y-1 text-sm">
                <p className="text-white font-medium">{result.title}</p>
                <p className="text-zinc-400">
                  {result.sections_count} секций, {result.lessons_count} уроков
                </p>
                <p className="text-zinc-500">
                  Статус: <span className="text-yellow-400">Черновик</span> — просмотрите и опубликуйте
                </p>
              </div>
              <a
                href="/courses"
                className="inline-flex items-center gap-1.5 text-xs text-orange-400 hover:text-orange-300 transition-colors"
              >
                <BookOpen size={14} />
                Перейти к курсам
                <ArrowRight size={12} />
              </a>
            </div>
          )}
        </div>

        <div className="mt-6 p-4 rounded-lg bg-white/3 border border-white/5 text-xs text-zinc-500 space-y-1">
          <p>AI генерирует полный курс с секциями, уроками и интерактивными шагами (тесты, карточки, matching и т.д.)</p>
          <p>Загрузите PDF, Word или Excel файлы — AI извлечёт текст и использует как основу для курса.</p>
          <p>Курс создаётся как черновик — просмотрите содержание и опубликуйте когда будете готовы.</p>
        </div>
      </div>
    </PageTransition>
  );
}
