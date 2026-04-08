import { motion } from "framer-motion";
import { Star, ArrowRight, RotateCcw } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { calculateStars, calculateXP } from "./autoMix";

interface ResultScreenProps {
  errors: number;
  onBackToMap: () => void;
  onRetry: () => void;
}

export function ResultScreen({ errors, onBackToMap, onRetry }: ResultScreenProps) {
  const stars = calculateStars(errors);
  const xp = calculateXP(stars);

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      className="flex flex-col items-center justify-center min-h-[60vh] gap-6 text-center"
    >
      <div className="flex items-end gap-3">
        {[1, 2, 3].map((i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 30, scale: 0 }}
            animate={{ opacity: i <= stars ? 1 : 0.2, y: 0, scale: i === 2 ? 1.3 : 1 }}
            transition={{ delay: 0.3 + i * 0.25, type: "spring", stiffness: 200 }}
          >
            <Star
              size={i === 2 ? 56 : 44}
              fill={i <= stars ? "#FFD700" : "transparent"}
              stroke={i <= stars ? "#FFD700" : "#4B5563"}
              strokeWidth={2}
              style={i <= stars ? { filter: "drop-shadow(0 0 12px rgba(255,215,0,0.5))" } : {}}
            />
          </motion.div>
        ))}
      </div>

      <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 1.2 }}>
        <h2 className="text-2xl font-bold mb-1">
          {stars === 3 ? "Perfect!" : stars === 2 ? "Great Job!" : "Lesson Complete!"}
        </h2>
        <p className="text-text-secondary text-sm">
          {errors === 0 ? "No mistakes — flawless!" : `${errors} mistake${errors > 1 ? "s" : ""}`}
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 1.5, type: "spring" }}
        className="px-6 py-3 rounded-2xl bg-primary/15 border-2 border-primary/30"
      >
        <span className="text-2xl font-bold text-primary">+{xp} XP</span>
      </motion.div>

      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 2 }} className="flex gap-3 mt-4">
        <Button variant="ghost" onClick={onRetry}><RotateCcw size={16} /> Retry</Button>
        <Button onClick={onBackToMap}>Back to Map <ArrowRight size={16} /></Button>
      </motion.div>
    </motion.div>
  );
}
