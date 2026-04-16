import { useState, useRef, useEffect, type ReactNode } from "react";
import { Send, Loader2, Mic } from "lucide-react";
import { motion } from "framer-motion";
import { MessageBubble } from "./MessageBubble";
import { VoiceButton } from "./VoiceButton";
import { WaveformVisualizer } from "./WaveformVisualizer";
import { Chip } from "@/components/ui/Chip";
import { useTranslation } from "@/hooks/useTranslation";
import type { ChatMessage } from "@/types/chat";
import type { VoiceState } from "@/hooks/useVoice";

interface ChatWindowProps {
  messages: ChatMessage[];
  isLoading: boolean;
  onSend: (text: string) => void;
  mentorAvatar: string;
  mentorName: string;
  voiceEnabled?: boolean;
  isListening?: boolean;
  isSpeaking?: boolean;
  transcript?: string;
  onVoiceToggle?: () => void;
  suggestions?: string[];
  voiceMode?: boolean;
  voiceState?: VoiceState;
  onVoiceModeToggle?: () => void;
  renderMessage?: (msg: ChatMessage) => ReactNode | undefined;
}

export function ChatWindow({
  messages,
  isLoading,
  onSend,
  mentorAvatar,
  mentorName,
  voiceEnabled,
  isListening,
  isSpeaking,
  transcript,
  onVoiceToggle,
  suggestions = [],
  voiceMode,
  voiceState,
  onVoiceModeToggle,
  renderMessage,
}: ChatWindowProps) {
  const { t } = useTranslation();
  const [input, setInput] = useState("");
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages, isLoading]);

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input.trim());
    setInput("");
  };

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="flex items-center justify-between px-3 sm:px-6 py-2.5 sm:py-4 border-b border-border">
        <div className="flex items-center gap-2 sm:gap-3 pl-9 lg:pl-0">
          <span className="text-xl sm:text-2xl">{mentorAvatar}</span>
          <div>
            <p className="font-semibold text-xs sm:text-sm">{mentorName}</p>
            <p className="text-[10px] sm:text-xs text-text-secondary">{t("mentor.aiMentor")}</p>
          </div>
          {isSpeaking && !voiceMode && <WaveformVisualizer active color="#F97316" />}
        </div>

        {/* Voice Mode Toggle */}
        {voiceEnabled && onVoiceModeToggle && (
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={onVoiceModeToggle}
            className={`flex items-center gap-1.5 sm:gap-2 px-2.5 sm:px-4 py-1.5 sm:py-2 rounded-xl text-[10px] sm:text-xs font-medium transition-all cursor-pointer ${
              voiceMode
                ? "bg-accent/15 text-accent border border-accent/30"
                : "bg-surface border border-border text-text-secondary hover:text-text hover:border-primary/30"
            }`}
          >
            <Mic size={12} className="sm:w-3.5 sm:h-3.5" />
            <span className="hidden sm:inline">{voiceMode ? t("mentor.voiceModeOn") : t("mentor.voiceModeOff")}</span>
            <span className="sm:hidden"><Mic size={14} /></span>
          </motion.button>
        )}
      </div>

      {/* Messages */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-3 sm:p-6 space-y-3 sm:space-y-4">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center gap-4 opacity-60">
            <motion.img
              src="/images/mascot-thinking.png"
              alt="Mentor mascot"
              className="w-44 h-44 object-contain drop-shadow-2xl"
              animate={{ y: [0, -10, 0] }}
              transition={{ repeat: Infinity, duration: 3, ease: "easeInOut" }}
            />
            <p className="text-sm text-text-secondary max-w-xs">
              {t("mentor.greeting", { name: mentorName })}
            </p>
          </div>
        )}

        {messages.map((msg) => {
          const custom = renderMessage?.(msg);
          if (custom !== undefined) {
            return (
              <div key={msg.id} className="flex gap-3">
                <div className="w-8 h-8 rounded-full bg-surface border border-border flex items-center justify-center text-sm shrink-0">
                  {msg.role === "user" ? "👤" : mentorAvatar}
                </div>
                <div className="max-w-[85%] sm:max-w-[70%] px-3 sm:px-4 py-2.5 sm:py-3 rounded-2xl text-sm leading-relaxed bg-surface border border-border text-text rounded-tl-md">
                  {custom}
                </div>
              </div>
            );
          }
          return <MessageBubble key={msg.id} message={msg} mentorAvatar={mentorAvatar} />;
        })}
        {isLoading && (
          <div className="flex gap-3">
            <div className="w-8 h-8 rounded-full bg-surface border border-border flex items-center justify-center text-sm">
              {mentorAvatar}
            </div>
            <div className="px-4 py-3 rounded-2xl bg-surface border border-border rounded-tl-md">
              <Loader2 className="animate-spin" size={16} />
            </div>
          </div>
        )}
      </div>

      {/* Transcript */}
      {isListening && transcript && !voiceMode && (
        <div className="px-3 sm:px-6 py-1.5 sm:py-2 text-xs sm:text-sm text-accent italic border-t border-border/50">
          {transcript}
        </div>
      )}

      {/* Suggestions */}
      {suggestions.length > 0 && messages.length < 3 && (
        <div className="flex gap-1.5 sm:gap-2 px-3 sm:px-6 py-1.5 sm:py-2 overflow-x-auto scrollbar-hide">
          {suggestions.map((s) => (
            <Chip key={s} label={s} onClick={() => onSend(s)} />
          ))}
        </div>
      )}

      {/* Input */}
      <div className="flex items-center gap-2 sm:gap-3 px-3 sm:px-6 py-2.5 sm:py-4 border-t border-border">
        {voiceEnabled && onVoiceToggle && !voiceMode && (
          <VoiceButton
            isListening={isListening || false}
            isSpeaking={isSpeaking || false}
            onToggle={onVoiceToggle}
          />
        )}

        {voiceMode && onVoiceModeToggle ? (
          <div className="flex-1 flex items-center justify-center gap-3 py-1">
            <motion.div
              animate={{ scale: [1, 1.1, 1] }}
              transition={{ repeat: Infinity, duration: 2 }}
            >
              <Mic size={18} className="text-accent" />
            </motion.div>
            <p className="text-sm text-accent">{t("mentor.voiceModeActive")}</p>
          </div>
        ) : (
          <>
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && handleSend()}
              placeholder={t("mentor.askAnything", { name: mentorName })}
              className="flex-1 min-w-0 bg-[#0A0A0A] border border-white/6 rounded-xl px-3 sm:px-4 py-2 sm:py-2.5 text-sm text-text outline-none focus:border-primary/40 placeholder:text-text-secondary/50"
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || isLoading}
              className="w-9 h-9 sm:w-10 sm:h-10 shrink-0 rounded-xl bg-primary flex items-center justify-center text-white disabled:opacity-50 cursor-pointer hover:bg-primary/90 transition-colors"
            >
              <Send size={16} />
            </button>
          </>
        )}
      </div>
    </div>
  );
}
