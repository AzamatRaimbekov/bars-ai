import { motion, AnimatePresence } from "framer-motion";
import { Check, X } from "lucide-react";

interface FeedbackOverlayProps {
  show: boolean;
  correct: boolean;
  message?: string;
}

const POSITIVE = ["Great!", "Perfect!", "Correct!", "Well done!", "Nailed it!"];
const NEGATIVE = ["Not quite", "Try to remember", "Incorrect", "Wrong answer"];

function randomFrom(arr: string[]) {
  return arr[Math.floor(Math.random() * arr.length)];
}

export function FeedbackOverlay({ show, correct, message }: FeedbackOverlayProps) {
  return (
    <AnimatePresence>
      {show && (
        <motion.div
          initial={{ y: 100, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: 100, opacity: 0 }}
          transition={{ type: "spring", stiffness: 300, damping: 25 }}
          className={`fixed bottom-0 left-0 right-0 z-50 px-6 py-5 flex items-center gap-4 ${
            correct ? "bg-green-500/95 text-white" : "bg-red-500/95 text-white"
          }`}
          style={{ backdropFilter: "blur(8px)" }}
        >
          <div className={`w-10 h-10 rounded-full flex items-center justify-center shrink-0 ${correct ? "bg-green-400/30" : "bg-red-400/30"}`}>
            {correct ? <Check size={22} strokeWidth={3} /> : <X size={22} strokeWidth={3} />}
          </div>
          <div>
            <p className="font-bold text-lg">{message || (correct ? randomFrom(POSITIVE) : randomFrom(NEGATIVE))}</p>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
