import { motion } from "framer-motion";
import { Mic, MicOff, Volume2 } from "lucide-react";
import { cn } from "@/lib/cn";

interface VoiceButtonProps {
  isListening: boolean;
  isSpeaking: boolean;
  onToggle: () => void;
  className?: string;
}

export function VoiceButton({ isListening, isSpeaking, onToggle, className }: VoiceButtonProps) {
  return (
    <motion.button
      whileTap={{ scale: 0.9 }}
      onClick={onToggle}
      className={cn(
        "relative w-12 h-12 rounded-full flex items-center justify-center transition-all cursor-pointer",
        isListening
          ? "bg-red-500/20 text-red-400 border-2 border-red-500/50"
          : isSpeaking
          ? "bg-accent/20 text-accent border-2 border-accent/50"
          : "bg-surface border-2 border-border text-text-secondary hover:border-primary/50 hover:text-primary",
        className
      )}
    >
      {isListening && (
        <motion.div
          className="absolute inset-0 rounded-full border-2 border-red-500/30"
          animate={{ scale: [1, 1.4, 1], opacity: [0.5, 0, 0.5] }}
          transition={{ repeat: Infinity, duration: 1.5 }}
        />
      )}
      {isListening ? <MicOff size={20} /> : isSpeaking ? <Volume2 size={20} /> : <Mic size={20} />}
    </motion.button>
  );
}
