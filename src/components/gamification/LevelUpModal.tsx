import { Modal } from "@/components/ui/Modal";
import { motion } from "framer-motion";
import type { Level } from "@/types";

interface LevelUpModalProps {
  open: boolean;
  onClose: () => void;
  level: Level;
}

export function LevelUpModal({ open, onClose, level }: LevelUpModalProps) {
  return (
    <Modal open={open} onClose={onClose}>
      <div className="flex flex-col items-center gap-4 py-4">
        <motion.div
          animate={{ rotate: [0, 10, -10, 0], scale: [1, 1.2, 1] }}
          transition={{ repeat: 2, duration: 0.5 }}
          className="text-6xl"
        >
          🎉
        </motion.div>
        <h2 className="text-2xl font-bold">Level Up!</h2>
        <p className="text-lg text-primary font-semibold">{level}</p>
        <p className="text-sm text-text-secondary text-center">
          Keep going — you're making amazing progress!
        </p>
      </div>
    </Modal>
  );
}
