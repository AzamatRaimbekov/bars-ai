import { motion } from "framer-motion";
import { Card } from "@/components/ui/Card";

interface ScoreCardProps {
  score: number;
  feedback: string;
  modelAnswer: string;
}

export function ScoreCard({ score, feedback, modelAnswer }: ScoreCardProps) {
  const color = score >= 7 ? "#00FF94" : score >= 4 ? "#FFB800" : "#FF4444";

  return (
    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
      <Card className="space-y-4">
        <div className="flex items-center gap-4">
          <div
            className="w-16 h-16 rounded-full flex items-center justify-center text-2xl font-bold border-4"
            style={{ borderColor: color, color }}
          >
            {score}
          </div>
          <div>
            <p className="text-sm font-semibold">Score</p>
            <p className="text-xs text-text-secondary">out of 10</p>
          </div>
        </div>
        <div>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-1">Feedback</p>
          <p className="text-sm leading-relaxed">{feedback}</p>
        </div>
        <div>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-1">Model Answer</p>
          <p className="text-sm text-text-secondary leading-relaxed">{modelAnswer}</p>
        </div>
      </Card>
    </motion.div>
  );
}
