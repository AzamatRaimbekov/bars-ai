import { motion, AnimatePresence } from "framer-motion";
import { Mic, MicOff, X, Volume2, Loader2, MessageSquare } from "lucide-react";
import { WaveformVisualizer } from "./WaveformVisualizer";
import { useTranslation } from "@/hooks/useTranslation";
import type { VoiceState } from "@/hooks/useVoice";

interface VoiceModeOverlayProps {
  active: boolean;
  voiceState: VoiceState;
  mentorAvatar: string;
  mentorName: string;
  transcript: string;
  lastAIMessage: string;
  isLoading: boolean;
  onMicToggle: () => void;
  onClose: () => void;
  onSwitchToText: () => void;
}

const stateColors: Record<VoiceState, string> = {
  idle: "rgba(255,255,255,0.3)",
  listening: "#FF4444",
  thinking: "#F97316",
  speaking: "#FB923C",
};

export function VoiceModeOverlay({
  active,
  voiceState,
  mentorAvatar,
  mentorName,
  transcript,
  lastAIMessage,
  isLoading,
  onMicToggle,
  onClose,
  onSwitchToText,
}: VoiceModeOverlayProps) {
  const { t } = useTranslation();
  const effectiveState = isLoading ? "thinking" : voiceState;
  const color = stateColors[effectiveState];

  const stateLabels: Record<VoiceState, string> = {
    idle: t("voice.idle"),
    listening: t("voice.listening"),
    thinking: t("voice.thinking"),
    speaking: t("voice.speaking"),
  };

  return (
    <AnimatePresence>
      {active && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="absolute inset-0 z-50 flex flex-col bg-bg/95 backdrop-blur-2xl"
        >
          {/* Top bar */}
          <div className="flex items-center justify-between px-6 py-4">
            <button
              onClick={onSwitchToText}
              className="flex items-center gap-2 px-3 py-2 rounded-xl text-xs text-text-secondary hover:text-text hover:bg-surface transition-all cursor-pointer"
            >
              <MessageSquare size={14} />
              {t("mentor.textMode")}
            </button>

            <div className="flex items-center gap-2">
              <span className="text-xl">{mentorAvatar}</span>
              <span className="text-sm font-medium">{mentorName}</span>
            </div>

            <button
              onClick={onClose}
              className="p-2 rounded-xl text-text-secondary hover:text-text hover:bg-surface transition-all cursor-pointer"
            >
              <X size={18} />
            </button>
          </div>

          {/* Center area */}
          <div className="flex-1 flex flex-col items-center justify-center px-6">
            {/* AI Avatar with state ring */}
            <motion.div
              className="relative mb-8"
              animate={
                effectiveState === "speaking"
                  ? { scale: [1, 1.05, 1] }
                  : effectiveState === "thinking"
                  ? { rotate: [0, 5, -5, 0] }
                  : {}
              }
              transition={{ repeat: Infinity, duration: 2 }}
            >
              <div
                className="w-28 h-28 rounded-full flex items-center justify-center text-5xl border-4 transition-colors duration-500"
                style={{
                  borderColor: color,
                  boxShadow: `0 0 40px ${color}30, 0 0 80px ${color}10`,
                  backgroundColor: `${color}08`,
                }}
              >
                {mentorAvatar}
              </div>

              {/* Animated rings */}
              {effectiveState === "speaking" && (
                <>
                  <motion.div
                    className="absolute inset-0 rounded-full border-2"
                    style={{ borderColor: `${color}40` }}
                    animate={{ scale: [1, 1.6], opacity: [0.6, 0] }}
                    transition={{ repeat: Infinity, duration: 1.5, ease: "easeOut" }}
                  />
                  <motion.div
                    className="absolute inset-0 rounded-full border-2"
                    style={{ borderColor: `${color}30` }}
                    animate={{ scale: [1, 2], opacity: [0.4, 0] }}
                    transition={{ repeat: Infinity, duration: 2, ease: "easeOut", delay: 0.3 }}
                  />
                </>
              )}

              {effectiveState === "thinking" && (
                <motion.div
                  className="absolute -bottom-1 -right-1 w-8 h-8 rounded-full bg-surface border-2 flex items-center justify-center"
                  style={{ borderColor: color }}
                >
                  <Loader2 size={14} className="animate-spin" style={{ color }} />
                </motion.div>
              )}
            </motion.div>

            {/* Waveform */}
            {effectiveState === "speaking" && (
              <div className="mb-6">
                <WaveformVisualizer active color={color} />
              </div>
            )}

            {/* State label */}
            <motion.p
              key={effectiveState}
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              className="text-sm font-medium mb-4"
              style={{ color }}
            >
              {stateLabels[effectiveState]}
            </motion.p>

            {/* Live transcript (while listening) */}
            <AnimatePresence mode="wait">
              {effectiveState === "listening" && transcript && (
                <motion.div
                  key="transcript"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0 }}
                  className="max-w-md text-center px-6 py-4 rounded-2xl bg-surface/50 border border-border"
                >
                  <p className="text-sm text-text italic">{transcript}</p>
                </motion.div>
              )}

              {effectiveState === "speaking" && lastAIMessage && (
                <motion.div
                  key="ai-response"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0 }}
                  className="max-w-md text-center px-6 py-4 rounded-2xl bg-surface/50 border border-accent/20"
                >
                  <p className="text-sm text-text-secondary leading-relaxed line-clamp-4">
                    {lastAIMessage}
                  </p>
                </motion.div>
              )}

              {effectiveState === "thinking" && (
                <motion.div
                  key="thinking"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="flex gap-1.5"
                >
                  {[0, 1, 2].map((i) => (
                    <motion.div
                      key={i}
                      className="w-2.5 h-2.5 rounded-full bg-primary"
                      animate={{ y: [0, -8, 0] }}
                      transition={{
                        repeat: Infinity,
                        duration: 0.8,
                        delay: i * 0.2,
                      }}
                    />
                  ))}
                </motion.div>
              )}
            </AnimatePresence>
          </div>

          {/* Bottom mic button */}
          <div className="flex flex-col items-center gap-4 pb-10">
            <motion.button
              whileTap={{ scale: 0.9 }}
              onClick={onMicToggle}
              className="relative cursor-pointer"
            >
              {/* Outer pulse ring when listening */}
              {effectiveState === "listening" && (
                <motion.div
                  className="absolute inset-0 rounded-full bg-red-500/10"
                  animate={{ scale: [1, 1.8], opacity: [0.5, 0] }}
                  transition={{ repeat: Infinity, duration: 1.5 }}
                  style={{ margin: "-16px" }}
                />
              )}

              <div
                className={`w-20 h-20 rounded-full flex items-center justify-center transition-all duration-300 ${
                  effectiveState === "listening"
                    ? "bg-red-500 text-white shadow-lg shadow-red-500/30"
                    : effectiveState === "speaking"
                    ? "bg-[#FB923C]/20 text-[#FB923C] border-2 border-[#FB923C]/50"
                    : "bg-surface border-2 border-border text-text hover:border-[#F97316]/50 hover:text-[#F97316]"
                }`}
              >
                {effectiveState === "listening" ? (
                  <MicOff size={28} />
                ) : effectiveState === "speaking" ? (
                  <Volume2 size={28} />
                ) : (
                  <Mic size={28} />
                )}
              </div>
            </motion.button>

            <p className="text-xs text-text-secondary">
              {effectiveState === "listening"
                ? t("voice.tapToStop")
                : effectiveState === "speaking"
                ? t("voice.tapToInterrupt")
                : t("voice.tapToSpeak")}
            </p>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
