import { useState, useRef, useEffect } from "react";
import { Send, Loader2 } from "lucide-react";
import { MessageBubble } from "./MessageBubble";
import { VoiceButton } from "./VoiceButton";
import { WaveformVisualizer } from "./WaveformVisualizer";
import { Chip } from "@/components/ui/Chip";
import type { ChatMessage } from "@/types/chat";

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
}: ChatWindowProps) {
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
      <div className="flex items-center gap-3 px-6 py-4 border-b border-border">
        <span className="text-2xl">{mentorAvatar}</span>
        <div>
          <p className="font-semibold text-sm">{mentorName}</p>
          <p className="text-xs text-text-secondary">AI Mentor</p>
        </div>
        {isSpeaking && <WaveformVisualizer active color="#00D9FF" />}
      </div>

      {/* Messages */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} mentorAvatar={mentorAvatar} />
        ))}
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
      {isListening && transcript && (
        <div className="px-6 py-2 text-sm text-accent italic border-t border-border/50">
          {transcript}
        </div>
      )}

      {/* Suggestions */}
      {suggestions.length > 0 && messages.length < 3 && (
        <div className="flex gap-2 px-6 py-2 overflow-x-auto">
          {suggestions.map((s) => (
            <Chip key={s} label={s} onClick={() => onSend(s)} />
          ))}
        </div>
      )}

      {/* Input */}
      <div className="flex items-center gap-3 px-6 py-4 border-t border-border">
        {voiceEnabled && onVoiceToggle && (
          <VoiceButton
            isListening={isListening || false}
            isSpeaking={isSpeaking || false}
            onToggle={onVoiceToggle}
          />
        )}
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && handleSend()}
          placeholder={`Ask ${mentorName} anything...`}
          className="flex-1 bg-bg border border-border rounded-xl px-4 py-2.5 text-sm text-text outline-none focus:border-primary/50 placeholder:text-text-secondary/50"
        />
        <button
          onClick={handleSend}
          disabled={!input.trim() || isLoading}
          className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center text-white disabled:opacity-50 cursor-pointer hover:bg-primary/90 transition-colors"
        >
          <Send size={16} />
        </button>
      </div>
    </div>
  );
}
