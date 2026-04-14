import { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowLeft,
  Save,
  Info,
  Layers,
  Map,
  Sparkles,
  Upload,
  Zap,
  Eye,
  EyeOff,
  Image as ImageIcon,
  Tag,
  BarChart3,
  DollarSign,
} from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { StepEditor } from "@/components/courses/StepEditor";
import { StructureTree } from "@/components/courses/StructureTree";
import { RoadmapEditor, type NodePosition, type RoadmapEdge } from "@/components/courses/RoadmapEditor";
import {
  courseApi,
  type CourseDetail,
  type CourseLesson,
} from "@/services/courseApi";

// ─── Constants ──────────────────────────────────────────────────────────────

const CATEGORIES = ["Frontend", "English", "Call Center", "CIB", "Other"];
const DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"];

// ─── Tab definition ──────────────────────────────────────────────────────────

type Tab = "info" | "structure" | "roadmap" | "ai";

interface TabMeta {
  key: Tab;
  label: string;
  icon: React.ReactNode;
}

const TABS: TabMeta[] = [
  { key: "info", label: "Информация", icon: <Info size={15} /> },
  { key: "structure", label: "Структура", icon: <Layers size={15} /> },
  { key: "roadmap", label: "Роадмап", icon: <Map size={15} /> },
  { key: "ai", label: "AI Генератор", icon: <Sparkles size={15} /> },
];

// ─── Animation variants ──────────────────────────────────────────────────────

const pageVariants = {
  hidden: { opacity: 0, y: 12 },
  show: { opacity: 1, y: 0, transition: { duration: 0.3 } },
  exit: { opacity: 0, y: -8, transition: { duration: 0.2 } },
};

// ─── Info Tab ────────────────────────────────────────────────────────────────

interface InfoTabProps {
  title: string;
  description: string;
  category: string;
  difficulty: string;
  thumbnailUrl: string;
  price: number;
  isPublished: boolean;
  saving: boolean;
  hasUnsavedChanges: boolean;
  onSave: () => void;
  onChange: (field: string, value: string | number | boolean) => void;
}

function InfoTab({
  title,
  description,
  category,
  difficulty,
  thumbnailUrl,
  price,
  isPublished,
  saving,
  hasUnsavedChanges,
  onSave,
  onChange,
}: InfoTabProps) {
  return (
    <motion.div variants={pageVariants} initial="hidden" animate="show" exit="exit" className="space-y-5">
      {/* Publish toggle */}
      <div className="flex items-center justify-between p-4 rounded-2xl bg-[#0A0A0A] border border-white/6">
        <div>
          <p className="text-sm font-semibold">Статус курса</p>
          <p className="text-xs text-text-secondary mt-0.5">
            {isPublished ? "Опубликован — виден студентам" : "Черновик — не виден студентам"}
          </p>
        </div>
        <button
          type="button"
          onClick={() => onChange("is_published", !isPublished)}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium transition-all cursor-pointer border ${
            isPublished
              ? "bg-[#4ADE80]/10 border-[#4ADE80]/30 text-[#4ADE80] hover:bg-[#4ADE80]/20"
              : "bg-white/5 border-white/6 text-text-secondary hover:border-white/20 hover:text-text"
          }`}
        >
          {isPublished ? <Eye size={14} /> : <EyeOff size={14} />}
          {isPublished ? "Опубликован" : "Черновик"}
        </button>
      </div>

      {/* Metadata form */}
      <div className="rounded-2xl bg-[#0A0A0A] border border-white/6 overflow-hidden">
        <div className="px-5 py-4 border-b border-white/5">
          <h3 className="text-sm font-semibold">Детали курса</h3>
        </div>
        <div className="p-5 space-y-4">
          <Input
            label="Название"
            value={title}
            onChange={(e) => onChange("title", e.target.value)}
            placeholder="Например: Введение в Frontend разработку"
          />

          <div>
            <div className="flex items-center justify-between mb-1.5">
              <label className="block text-sm text-text-secondary">Описание</label>
              <span className="text-xs text-text-secondary/60">{description.length} симв.</span>
            </div>
            <textarea
              value={description}
              onChange={(e) => onChange("description", e.target.value)}
              rows={4}
              placeholder="Опишите, чему научатся студенты..."
              className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
            />
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="flex items-center gap-1.5 text-sm text-text-secondary mb-1.5">
                <Tag size={12} />
                Категория
              </label>
              <select
                value={category}
                onChange={(e) => onChange("category", e.target.value)}
                className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text outline-none transition-colors focus:border-primary/50 text-sm cursor-pointer"
              >
                {CATEGORIES.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="flex items-center gap-1.5 text-sm text-text-secondary mb-1.5">
                <BarChart3 size={12} />
                Сложность
              </label>
              <select
                value={difficulty}
                onChange={(e) => onChange("difficulty", e.target.value)}
                className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text outline-none transition-colors focus:border-primary/50 text-sm cursor-pointer"
              >
                {DIFFICULTIES.map((d) => (
                  <option key={d} value={d}>
                    {d}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div>
            <label className="flex items-center gap-1.5 text-sm text-text-secondary mb-1.5">
              <ImageIcon size={12} />
              Обложка (URL)
            </label>
            <div className="flex gap-3">
              <input
                value={thumbnailUrl}
                onChange={(e) => onChange("thumbnail_url", e.target.value)}
                placeholder="https://example.com/thumbnail.jpg"
                className="flex-1 rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 text-sm"
              />
              {thumbnailUrl && (
                <div className="w-10 h-10 rounded-lg overflow-hidden border border-white/10 flex-shrink-0">
                  <img
                    src={thumbnailUrl}
                    alt="thumbnail preview"
                    className="w-full h-full object-cover"
                    onError={(e) => {
                      (e.target as HTMLImageElement).style.display = "none";
                    }}
                  />
                </div>
              )}
            </div>
          </div>

          <div>
            <label className="flex items-center gap-1.5 text-sm text-text-secondary mb-1.5">
              <DollarSign size={12} />
              Цена (в центах, 0 = бесплатно)
            </label>
            <div className="flex items-center gap-3">
              <input
                type="number"
                min={0}
                value={price}
                onChange={(e) => onChange("price", parseInt(e.target.value) || 0)}
                className="w-32 rounded-xl border border-border bg-bg px-4 py-2.5 text-text outline-none transition-colors focus:border-primary/50 text-sm"
              />
              <span className="text-sm text-text-secondary">
                {price === 0
                  ? "Бесплатно"
                  : `$${(price / 100).toFixed(2)} USD`}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between">
        <AnimatePresence>
          {hasUnsavedChanges && (
            <motion.span
              key="unsaved"
              initial={{ opacity: 0, x: -8 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -8 }}
              className="text-xs text-yellow-400/80"
            >
              Есть несохранённые изменения
            </motion.span>
          )}
        </AnimatePresence>
        <Button onClick={onSave} disabled={saving}>
          <Save size={15} />
          {saving ? "Сохранение..." : "Сохранить"}
        </Button>
      </div>
    </motion.div>
  );
}

// ─── AI Tab (placeholder) ────────────────────────────────────────────────────

function AiTab() {
  return (
    <motion.div variants={pageVariants} initial="hidden" animate="show" exit="exit" className="space-y-5">
      <div className="rounded-2xl bg-[#0A0A0A] border border-white/6 overflow-hidden">
        <div className="px-5 py-4 border-b border-white/5 flex items-center gap-2">
          <Sparkles size={16} className="text-warning" />
          <h3 className="text-sm font-semibold">AI Генератор курсов</h3>
          <span className="ml-auto px-2.5 py-0.5 rounded-full text-[10px] font-semibold bg-warning/10 text-warning border border-warning/20">
            Скоро
          </span>
        </div>
        <div className="p-6 space-y-5">
          {/* Upload zone */}
          <div className="border-2 border-dashed border-white/15 rounded-2xl p-10 text-center hover:border-white/25 transition-colors">
            <Upload size={32} className="mx-auto mb-3 text-text-secondary/50" />
            <p className="text-sm font-medium text-text-secondary">
              Перетащите документы, слайды или PDF сюда
            </p>
            <p className="text-xs text-text-secondary/50 mt-1">
              PDF, PPTX, DOCX, TXT — до 50МБ
            </p>
            <button
              type="button"
              disabled
              className="mt-4 px-4 py-2 rounded-xl bg-white/5 border border-white/10 text-sm text-text-secondary cursor-not-allowed opacity-50"
            >
              Выбрать файлы
            </button>
          </div>

          {/* Config options */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {[
              { label: "Язык", value: "Русский" },
              { label: "Шагов в уроке", value: "5" },
              { label: "Частота квизов", value: "Каждая секция" },
            ].map((opt) => (
              <div key={opt.label} className="p-3 rounded-xl bg-[#0A0A0A] border border-white/6">
                <p className="text-xs text-text-secondary mb-1">{opt.label}</p>
                <p className="text-sm font-medium opacity-50">{opt.value}</p>
              </div>
            ))}
          </div>

          {/* Generate button */}
          <div className="flex justify-center">
            <button
              type="button"
              disabled
              className="flex items-center gap-2.5 px-8 py-3.5 rounded-2xl bg-[#F97316]/20 border border-[#F97316]/30 text-[#F97316] font-semibold text-sm cursor-not-allowed opacity-50"
            >
              <Zap size={16} />
              Сгенерировать структуру курса
            </button>
          </div>

          <p className="text-center text-xs text-text-secondary/50">
            AI автоматически создаст секции, уроки и интерактивные шаги из ваших материалов.
          </p>
        </div>
      </div>
    </motion.div>
  );
}

// ─── Main Page ───────────────────────────────────────────────────────────────

export default function CourseEditor() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const [tab, setTab] = useState<Tab>("info");
  const [course, setCourse] = useState<CourseDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [toast, setToast] = useState<{ message: string; type: "success" | "error" } | null>(null);

  // Auto-dismiss the toast after 3 s
  useEffect(() => {
    if (!toast) return;
    const timer = setTimeout(() => setToast(null), 3000);
    return () => clearTimeout(timer);
  }, [toast]);

  // Info form state
  const [formState, setFormState] = useState({
    title: "",
    description: "",
    category: "Other",
    difficulty: "Beginner",
    thumbnail_url: "",
    price: 0,
    is_published: false,
  });

  // Roadmap layout persistence
  const [roadmapPositions, setRoadmapPositions] = useState<NodePosition[]>([]);
  const [roadmapEdges, setRoadmapEdges] = useState<RoadmapEdge[]>([]);

  // Step editor state
  const [stepEditorLesson, setStepEditorLesson] = useState<CourseLesson | null>(null);

  // Stable load function — called on mount and after mutations
  const loadCourse = useCallback(() => {
    if (!id) return;
    setLoading(true);
    courseApi
      .get(id)
      .then((data) => {
        setCourse(data);
        setFormState({
          title: data.title,
          description: data.description,
          category: data.category,
          difficulty: data.difficulty,
          thumbnail_url: data.thumbnail_url ?? "",
          price: data.price,
          is_published: data.status === "published",
        });
        if (data.roadmap_nodes) setRoadmapPositions(data.roadmap_nodes as NodePosition[]);
        if (data.roadmap_edges) setRoadmapEdges(data.roadmap_edges as RoadmapEdge[]);
      })
      .catch(() => navigate("/teach"))
      .finally(() => setLoading(false));
  }, [id, navigate]);

  useEffect(() => {
    loadCourse();
  }, [loadCourse]);

  const handleFieldChange = useCallback((field: string, value: string | number | boolean) => {
    setFormState((prev) => ({ ...prev, [field]: value }));
  }, []);

  const handleSaveInfo = async () => {
    if (!id) return;
    setSaving(true);
    try {
      await courseApi.update(id, {
        title: formState.title,
        description: formState.description,
        category: formState.category,
        difficulty: formState.difficulty,
        thumbnail_url: formState.thumbnail_url || null,
        price: formState.price,
        status: formState.is_published ? "published" : "draft",
      });
      const updated = await courseApi.get(id);
      setCourse(updated);
      setToast({ message: "Изменения сохранены", type: "success" });
    } catch {
      setToast({ message: "Не удалось сохранить изменения", type: "error" });
    } finally {
      setSaving(false);
    }
  };

  // Derived: detect unsaved changes by comparing formState against the last-loaded course
  const hasUnsavedChanges = course !== null && (
    formState.title !== course.title ||
    formState.description !== course.description ||
    formState.category !== course.category ||
    formState.difficulty !== course.difficulty ||
    formState.thumbnail_url !== (course.thumbnail_url ?? "") ||
    formState.price !== course.price ||
    formState.is_published !== (course.status === "published")
  );

  const handleRoadmapSave = async (positions: NodePosition[], edges: RoadmapEdge[]) => {
    setRoadmapPositions(positions);
    setRoadmapEdges(edges);
    if (id) {
      await courseApi.update(id, {
        roadmap_nodes: positions,
        roadmap_edges: edges,
      }).catch(() => {});
    }
  };

  if (loading) {
    return (
      <PageWrapper>
        <div className="flex items-center justify-center py-20">
          <motion.div
            animate={{ opacity: [0.4, 1, 0.4] }}
            transition={{ repeat: Infinity, duration: 1.4 }}
            className="text-sm text-text-secondary"
          >
            Загрузка...
          </motion.div>
        </div>
      </PageWrapper>
    );
  }

  if (!course) return null;

  // Roadmap tab needs full-height container so we break out of PageWrapper padding
  if (tab === "roadmap") {
    return (
      <>
        {/* Step editor overlay */}
        <AnimatePresence>
          {stepEditorLesson && (
            <StepEditor
              lessonId={stepEditorLesson.id}
              lessonTitle={stepEditorLesson.title}
              onClose={() => setStepEditorLesson(null)}
              onSaved={loadCourse}
            />
          )}
        </AnimatePresence>

        <PageWrapper>
          <div className="flex flex-col" style={{ height: "calc(100vh - 8rem)" }}>
            {/* Page header */}
            <div className="flex-shrink-0 space-y-4 mb-4">
              <EditorHeader
                title={course.title}
                onBack={() => navigate("/teach")}
                tab={tab}
                onTabChange={setTab}
              />
            </div>

            {/* Full-height canvas */}
            <div className="flex-1 min-h-0 rounded-2xl border border-white/6 overflow-hidden">
              <RoadmapEditor
                sections={course.sections}
                initialPositions={roadmapPositions}
                initialEdges={roadmapEdges}
                onSave={handleRoadmapSave}
              />
            </div>
          </div>
        </PageWrapper>
      </>
    );
  }

  return (
    <>
      {/* Step editor overlay — rendered outside PageWrapper to be truly full-screen */}
      <AnimatePresence>
        {stepEditorLesson && (
          <StepEditor
            lessonId={stepEditorLesson.id}
            lessonTitle={stepEditorLesson.title}
            onClose={() => setStepEditorLesson(null)}
            onSaved={loadCourse}
          />
        )}
      </AnimatePresence>

      {/* Toast notification */}
      <AnimatePresence>
        {toast && (
          <motion.div
            key="toast"
            initial={{ opacity: 0, y: -12 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -12 }}
            transition={{ duration: 0.2 }}
            className={`fixed top-4 left-1/2 -translate-x-1/2 z-[100] px-5 py-2.5 rounded-xl text-sm font-medium shadow-2xl border ${
              toast.type === "success"
                ? "bg-[#111111] border-white/6 text-[#4ADE80]"
                : "bg-[#111111] border-white/6 text-red-400"
            }`}
          >
            {toast.message}
          </motion.div>
        )}
      </AnimatePresence>

      <PageWrapper>
        <div className="max-w-3xl mx-auto space-y-5 pb-12">
          <EditorHeader
            title={course.title}
            onBack={() => navigate("/teach")}
            tab={tab}
            onTabChange={setTab}
          />

          {/* Tab content */}
          <AnimatePresence mode="wait">
            {tab === "info" && (
              <motion.div key="info">
                <InfoTab
                  title={formState.title}
                  description={formState.description}
                  category={formState.category}
                  difficulty={formState.difficulty}
                  thumbnailUrl={formState.thumbnail_url}
                  price={formState.price}
                  isPublished={formState.is_published}
                  saving={saving}
                  hasUnsavedChanges={hasUnsavedChanges}
                  onSave={handleSaveInfo}
                  onChange={handleFieldChange}
                />
              </motion.div>
            )}

            {tab === "structure" && (
              <motion.div
                key="structure"
                variants={pageVariants}
                initial="hidden"
                animate="show"
                exit="exit"
              >
                <StructureTree
                  courseId={course.id}
                  sections={course.sections}
                  onRefresh={loadCourse}
                  onEditSteps={(lesson) => setStepEditorLesson(lesson)}
                />
              </motion.div>
            )}

            {tab === "ai" && (
              <motion.div key="ai">
                <AiTab />
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </PageWrapper>
    </>
  );
}

// ─── Shared Header ────────────────────────────────────────────────────────────

function EditorHeader({
  title,
  onBack,
  tab,
  onTabChange,
}: {
  title: string;
  onBack: () => void;
  tab: Tab;
  onTabChange: (t: Tab) => void;
}) {
  return (
    <div className="space-y-4">
      {/* Back + title row */}
      <div className="flex items-center gap-3">
        <button
          type="button"
          onClick={onBack}
          className="flex items-center gap-1.5 text-sm text-text-secondary hover:text-text transition-colors cursor-pointer"
        >
          <ArrowLeft size={15} />
          <span className="hidden sm:inline">Назад</span>
        </button>
        <div className="h-4 w-px bg-white/10" />
        <h1 className="text-base lg:text-lg font-bold truncate flex-1">{title}</h1>
      </div>

      {/* Tab bar */}
      <div className="flex gap-1 bg-white/5 border border-white/10 rounded-2xl p-1">
        {TABS.map((t) => (
          <button
            key={t.key}
            type="button"
            onClick={() => onTabChange(t.key)}
            className={`flex-1 flex items-center justify-center gap-1.5 py-2 px-2 rounded-xl text-xs sm:text-sm font-medium transition-all cursor-pointer ${
              tab === t.key
                ? "bg-[#F97316]/10 text-[#F97316] shadow-sm"
                : "text-text-secondary hover:text-text hover:bg-white/5"
            }`}
          >
            <span className={tab === t.key ? "text-[#F97316]" : "text-text-secondary"}>
              {t.icon}
            </span>
            <span className="hidden sm:inline">{t.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
