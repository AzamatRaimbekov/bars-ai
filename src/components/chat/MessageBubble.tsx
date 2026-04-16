import { motion } from "framer-motion";
import type { ChatMessage } from "@/types/chat";

interface MessageBubbleProps {
  message: ChatMessage;
  mentorAvatar?: string;
}

export function MessageBubble({ message, mentorAvatar }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`flex gap-2 sm:gap-3 ${isUser ? "flex-row-reverse" : ""}`}
    >
      <div className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-surface border border-border flex items-center justify-center text-xs sm:text-sm shrink-0">
        {isUser ? "👤" : mentorAvatar || "🤖"}
      </div>
      <div
        className={`max-w-[85%] sm:max-w-[70%] px-3 sm:px-4 py-2 sm:py-3 rounded-2xl text-[13px] sm:text-sm leading-relaxed ${
          isUser
            ? "bg-primary text-white rounded-tr-md"
            : "bg-surface border border-border text-text rounded-tl-md"
        }`}
      >
        <div className="whitespace-pre-wrap break-words">{message.content}</div>
      </div>
    </motion.div>
  );
}
