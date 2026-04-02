import { motion } from "framer-motion";

interface TranscriptPanelProps {
  entries: Array<{ role: "interviewer" | "candidate"; text: string }>;
}

export function TranscriptPanel({ entries }: TranscriptPanelProps) {
  return (
    <div className="space-y-3 max-h-60 overflow-y-auto">
      {entries.map((entry, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className={`text-sm ${entry.role === "interviewer" ? "text-accent" : "text-text"}`}
        >
          <span className="text-xs text-text-secondary uppercase">
            {entry.role === "interviewer" ? "Interviewer" : "You"}:
          </span>{" "}
          {entry.text}
        </motion.div>
      ))}
    </div>
  );
}
