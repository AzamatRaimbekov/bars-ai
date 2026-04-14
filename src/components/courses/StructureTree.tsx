import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  ChevronRight,
  Plus,
  Trash2,
  GripVertical,
  Edit3,
  Check,
  X,
  BookOpen,
  Layers,
  Pencil,
  Zap,
} from "lucide-react";
import { Button } from "@/components/ui/Button";
import { courseApi, type CourseSection, type CourseLesson } from "@/services/courseApi";

// ─── Types ─────────────────────────────────────────────────────────────────

interface StructureTreeProps {
  courseId: string;
  sections: CourseSection[];
  onRefresh: () => void;
  onEditSteps: (lesson: CourseLesson, sectionTitle: string) => void;
}

// ─── Inline Edit Input ─────────────────────────────────────────────────────

function InlineEdit({
  value,
  onSave,
  onCancel,
  placeholder,
}: {
  value: string;
  onSave: (v: string) => void;
  onCancel: () => void;
  placeholder?: string;
}) {
  const [draft, setDraft] = useState(value);

  return (
    <div className="flex items-center gap-1.5 flex-1 min-w-0">
      <input
        autoFocus
        value={draft}
        onChange={(e) => setDraft(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") onSave(draft.trim());
          if (e.key === "Escape") onCancel();
        }}
        placeholder={placeholder}
        className="flex-1 min-w-0 rounded-lg border border-primary/40 bg-bg px-2.5 py-1 text-sm text-text outline-none focus:border-primary/70 transition-colors"
        onClick={(e) => e.stopPropagation()}
      />
      <button
        type="button"
        onClick={(e) => {
          e.stopPropagation();
          onSave(draft.trim());
        }}
        className="flex-shrink-0 text-green-400 hover:text-green-300 transition-colors cursor-pointer"
      >
        <Check size={14} />
      </button>
      <button
        type="button"
        onClick={(e) => {
          e.stopPropagation();
          onCancel();
        }}
        className="flex-shrink-0 text-text-secondary hover:text-text transition-colors cursor-pointer"
      >
        <X size={14} />
      </button>
    </div>
  );
}

// ─── Lesson Row ─────────────────────────────────────────────────────────────

function LessonRow({
  lesson,
  onEdit,
  onDelete,
  onEditSteps,
}: {
  lesson: CourseLesson;
  onEdit: (title: string) => void;
  onDelete: () => void;
  onEditSteps: () => void;
}) {
  const [editing, setEditing] = useState(false);
  const [deleting, setDeleting] = useState(false);

  const handleDelete = async () => {
    setDeleting(true);
    try {
      await courseApi.deleteLesson(lesson.id);
      onDelete();
    } catch {
      // silently fail
    } finally {
      setDeleting(false);
    }
  };

  return (
    <motion.div
      layout
      initial={{ opacity: 0, x: -8 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -8 }}
      className="flex items-center gap-2 px-3 py-2.5 rounded-xl bg-transparent border border-white/6 hover:border-white/12 transition-all group"
    >
      <GripVertical size={12} className="text-text-secondary flex-shrink-0 cursor-grab" />

      <BookOpen size={13} className="text-text-secondary flex-shrink-0" />

      {editing ? (
        <InlineEdit
          value={lesson.title}
          placeholder="Lesson title"
          onSave={async (v) => {
            if (v) await onEdit(v);
            setEditing(false);
          }}
          onCancel={() => setEditing(false)}
        />
      ) : (
        <span className="text-sm flex-1 min-w-0 truncate">{lesson.title}</span>
      )}

      {!editing && (
        <div className="flex items-center gap-2 ml-auto flex-shrink-0">
          {/* Metadata chips */}
          {lesson.xp_reward > 0 && (
            <span className="flex items-center gap-0.5 text-[10px] text-warning font-medium">
              <Zap size={9} />
              {lesson.xp_reward}
            </span>
          )}
          {(() => {
              const stepCount = lesson.steps?.length ?? lesson.step_count ?? 0;
              return stepCount > 0 ? (
                <span className="text-[10px] text-text-secondary">{stepCount} шагов</span>
              ) : null;
            })()}

          {/* Actions — visible on hover */}
          <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
            <button
              type="button"
              onClick={onEditSteps}
              className="flex items-center gap-1 px-2 py-1 rounded-lg bg-primary/10 text-primary text-[10px] font-medium hover:bg-primary/20 transition-all cursor-pointer"
            >
              <Pencil size={10} />
              Шаги
            </button>
            <button
              type="button"
              onClick={() => setEditing(true)}
              className="p-1 rounded-lg text-text-secondary hover:text-text hover:bg-white/10 transition-all cursor-pointer"
            >
              <Edit3 size={12} />
            </button>
            <button
              type="button"
              onClick={handleDelete}
              disabled={deleting}
              className="p-1 rounded-lg text-text-secondary hover:text-red-400 hover:bg-red-500/10 transition-all cursor-pointer disabled:opacity-40"
            >
              <Trash2 size={12} />
            </button>
          </div>
        </div>
      )}
    </motion.div>
  );
}

// ─── Add Lesson Form ────────────────────────────────────────────────────────

function AddLessonForm({
  sectionId,
  lessonCount,
  onAdded,
  onCancel,
}: {
  sectionId: string;
  lessonCount: number;
  onAdded: () => void;
  onCancel: () => void;
}) {
  const [title, setTitle] = useState("");
  const [xp, setXp] = useState("10");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!title.trim()) return;
    setLoading(true);
    try {
      await courseApi.addLesson(sectionId, {
        title: title.trim(),
        content_markdown: "",
        xp_reward: parseInt(xp) || 10,
        content_type: "interactive",
        position: lessonCount,
      });
      onAdded();
    } catch {
      // silently fail
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: -4 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -4 }}
      className="space-y-2 p-3 rounded-xl border border-primary/20 bg-primary/5"
    >
      <div className="flex gap-2">
        <input
          autoFocus
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
          placeholder="Название урока..."
          className="flex-1 rounded-lg border border-border bg-bg px-3 py-2 text-sm text-text placeholder:text-text-secondary/50 outline-none focus:border-primary/50 transition-colors"
        />
        <input
          type="number"
          value={xp}
          onChange={(e) => setXp(e.target.value)}
          placeholder="XP"
          className="w-16 rounded-lg border border-border bg-bg px-2 py-2 text-sm text-text outline-none focus:border-primary/50 transition-colors text-center"
        />
      </div>
      <div className="flex gap-2">
        <Button size="sm" onClick={handleSubmit} disabled={loading || !title.trim()}>
          {loading ? "Добавление..." : "Добавить"}
        </Button>
        <Button variant="ghost" size="sm" onClick={onCancel}>
          Отмена
        </Button>
      </div>
    </motion.div>
  );
}

// ─── Section Row ────────────────────────────────────────────────────────────

function SectionRow({
  section,
  onRefresh,
  onEditSteps,
}: {
  section: CourseSection;
  onRefresh: () => void;
  onEditSteps: (lesson: CourseLesson) => void;
}) {
  const [expanded, setExpanded] = useState(true);
  const [editing, setEditing] = useState(false);
  const [addingLesson, setAddingLesson] = useState(false);
  const [deleting, setDeleting] = useState(false);

  const sortedLessons = [...section.lessons].sort((a, b) => a.position - b.position);

  const handleRenameSection = async (title: string) => {
    if (!title) return;
    await courseApi.updateSection(section.id, { title }).catch(() => {});
    onRefresh();
  };

  const handleDeleteSection = async () => {
    if (!window.confirm(`Удалить секцию "${section.title}" и все её уроки?`)) return;
    setDeleting(true);
    try {
      await courseApi.deleteSection(section.id);
      onRefresh();
    } catch {
      // silently fail
    } finally {
      setDeleting(false);
    }
  };

  const handleEditLesson = async (lesson: CourseLesson, title: string) => {
    await courseApi.updateLesson(lesson.id, { title }).catch(() => {});
    onRefresh();
  };

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-white/6 bg-[#0A0A0A] overflow-hidden"
    >
      {/* Section header */}
      <div className="flex items-center gap-2 px-4 py-3">
        <GripVertical size={14} className="text-text-secondary flex-shrink-0 cursor-grab" />
        <button
          type="button"
          onClick={() => setExpanded((v) => !v)}
          className="flex-shrink-0 cursor-pointer text-text-secondary hover:text-text transition-colors"
        >
          <motion.div animate={{ rotate: expanded ? 90 : 0 }} transition={{ duration: 0.2 }}>
            <ChevronRight size={15} />
          </motion.div>
        </button>

        <Layers size={14} className="text-primary flex-shrink-0" />

        {editing ? (
          <InlineEdit
            value={section.title}
            placeholder="Section title"
            onSave={async (v) => {
              if (v) await handleRenameSection(v);
              setEditing(false);
            }}
            onCancel={() => setEditing(false)}
          />
        ) : (
          <>
            <button
              type="button"
              onClick={() => setExpanded((v) => !v)}
              className="flex-1 text-left text-sm font-semibold cursor-pointer hover:text-primary transition-colors min-w-0 truncate"
            >
              {section.title}
            </button>
            <span className="text-xs text-text-secondary flex-shrink-0">
              {sortedLessons.length} {sortedLessons.length === 1 ? "урок" : "уроков"}
            </span>
            <div className="flex items-center gap-1 flex-shrink-0">
              <button
                type="button"
                onClick={() => setEditing(true)}
                className="p-1 rounded-lg text-text-secondary hover:text-text hover:bg-white/10 transition-all cursor-pointer"
              >
                <Edit3 size={12} />
              </button>
              <button
                type="button"
                onClick={handleDeleteSection}
                disabled={deleting}
                className="p-1 rounded-lg text-text-secondary hover:text-red-400 hover:bg-red-500/10 transition-all cursor-pointer disabled:opacity-40"
              >
                <Trash2 size={12} />
              </button>
            </div>
          </>
        )}
      </div>

      {/* Lessons */}
      <AnimatePresence>
        {expanded && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="overflow-hidden"
          >
            <div className="px-4 pb-4 space-y-2 border-t border-white/5 pt-3">
              <AnimatePresence>
                {sortedLessons.map((lesson) => (
                  <LessonRow
                    key={lesson.id}
                    lesson={lesson}
                    onEdit={(title) => handleEditLesson(lesson, title)}
                    onDelete={onRefresh}
                    onEditSteps={() => onEditSteps(lesson)}
                  />
                ))}
              </AnimatePresence>

              {/* Add lesson */}
              <AnimatePresence>
                {addingLesson ? (
                  <AddLessonForm
                    sectionId={section.id}
                    lessonCount={sortedLessons.length}
                    onAdded={() => {
                      setAddingLesson(false);
                      onRefresh();
                    }}
                    onCancel={() => setAddingLesson(false)}
                  />
                ) : (
                  <motion.button
                    type="button"
                    onClick={() => setAddingLesson(true)}
                    className="w-full flex items-center gap-2 px-3 py-2 rounded-xl text-sm text-primary/70 hover:text-primary hover:bg-primary/10 transition-all cursor-pointer border border-dashed border-primary/20 hover:border-primary/40"
                  >
                    <Plus size={13} />
                    Добавить урок
                  </motion.button>
                )}
              </AnimatePresence>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}

// ─── Main Component ─────────────────────────────────────────────────────────

export function StructureTree({
  courseId,
  sections,
  onRefresh,
  onEditSteps,
}: StructureTreeProps) {
  const [newSectionTitle, setNewSectionTitle] = useState("");
  const [addingSection, setAddingSection] = useState(false);

  const sortedSections = [...sections].sort((a, b) => a.position - b.position);

  const handleAddSection = async () => {
    if (!newSectionTitle.trim()) return;
    setAddingSection(true);
    try {
      await courseApi.addSection(courseId, newSectionTitle.trim(), sortedSections.length);
      setNewSectionTitle("");
      onRefresh();
    } catch {
      // silently fail
    } finally {
      setAddingSection(false);
    }
  };

  return (
    <div className="space-y-3">
      {/* Sections list */}
      <AnimatePresence>
        {sortedSections.length === 0 ? (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-12 text-text-secondary"
          >
            <Layers size={36} className="mx-auto mb-3 opacity-30" />
            <p className="text-sm">Секций пока нет.</p>
            <p className="text-xs mt-1 opacity-60">Добавьте первую секцию ниже.</p>
          </motion.div>
        ) : (
          sortedSections.map((section) => (
            <SectionRow
              key={section.id}
              section={section}
              onRefresh={onRefresh}
              onEditSteps={(lesson) => onEditSteps(lesson, section.title)}
            />
          ))
        )}
      </AnimatePresence>

      {/* Add section */}
      <div className="rounded-2xl border border-dashed border-white/10 bg-[#0A0A0A] p-4">
        <p className="text-xs text-text-secondary mb-3 font-medium uppercase tracking-wider">
          Новая секция
        </p>
        <div className="flex gap-2">
          <input
            value={newSectionTitle}
            onChange={(e) => setNewSectionTitle(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAddSection()}
            placeholder="Название секции..."
            className="flex-1 rounded-xl border border-border bg-bg px-4 py-2.5 text-sm text-text placeholder:text-text-secondary/50 outline-none focus:border-primary/50 transition-colors"
          />
          <Button
            size="sm"
            onClick={handleAddSection}
            disabled={addingSection || !newSectionTitle.trim()}
          >
            <Plus size={14} />
            Добавить
          </Button>
        </div>
      </div>
    </div>
  );
}
