import { motion } from "framer-motion";
import { Plus, Trash2 } from "lucide-react";
import type { Session } from "@/services/mentorApi";

interface SessionListProps {
  sessions: Session[];
  activeSession: Session | null;
  onSelect: (session: Session) => void;
  onCreate: () => void;
  onDelete: (sessionId: string) => void;
}

export function SessionList({
  sessions,
  activeSession,
  onSelect,
  onCreate,
  onDelete,
}: SessionListProps) {
  return (
    <div className="flex flex-col h-full bg-surface/80 border-r border-border">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-border">
        <p className="text-sm font-semibold text-text">Сессии</p>
        <motion.button
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          onClick={onCreate}
          className="w-8 h-8 rounded-lg bg-primary/15 text-primary flex items-center justify-center hover:bg-primary/25 transition-colors cursor-pointer"
        >
          <Plus size={16} />
        </motion.button>
      </div>

      {/* Session list */}
      <div className="flex-1 overflow-y-auto py-2">
        {sessions.length === 0 && (
          <p className="text-xs text-text-secondary text-center px-4 py-6">
            Нет сессий. Начните новую!
          </p>
        )}

        {sessions.map((session) => {
          const isActive = activeSession?.id === session.id;
          const date = new Date(session.updated_at);
          const dateStr = date.toLocaleDateString("ru-RU", {
            day: "numeric",
            month: "short",
          });

          return (
            <motion.div
              key={session.id}
              whileHover={{ x: 2 }}
              onClick={() => onSelect(session)}
              className={`group flex items-center gap-3 px-4 py-3 mx-2 rounded-xl cursor-pointer transition-colors ${
                isActive
                  ? "bg-primary/10 border border-primary/20"
                  : "hover:bg-white/5"
              }`}
            >
              <div className="flex-1 min-w-0">
                <p
                  className={`text-sm truncate ${
                    isActive ? "text-primary font-medium" : "text-text"
                  }`}
                >
                  {session.title}
                </p>
                <p className="text-xs text-text-secondary mt-0.5">{dateStr}</p>
              </div>

              <button
                onClick={(e) => {
                  e.stopPropagation();
                  onDelete(session.id);
                }}
                className="opacity-0 group-hover:opacity-100 p-1.5 rounded-lg text-text-secondary hover:text-red-400 hover:bg-red-400/10 transition-all cursor-pointer"
              >
                <Trash2 size={14} />
              </button>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
