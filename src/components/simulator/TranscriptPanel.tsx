import { motion } from "framer-motion";
import { useTranslation } from "@/hooks/useTranslation";

interface TranscriptPanelProps {
  entries: Array<{ role: "interviewer" | "candidate"; text: string }>;
}

export function TranscriptPanel({ entries }: TranscriptPanelProps) {
  const { t, lang } = useTranslation();
  return (
    <div className="space-y-3 max-h-60 overflow-y-auto">
      {entries.map((entry, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className={`text-sm ${entry.role === "interviewer" ? "text-[#FB923C]" : "text-text"}`}
        >
          <span className="text-xs text-white/40 uppercase">
            {entry.role === "interviewer" ? t("sim.interviewer") : (lang === "ru" ? "Вы" : "You")}:
          </span>{" "}
          {entry.text}
        </motion.div>
      ))}
    </div>
  );
}
