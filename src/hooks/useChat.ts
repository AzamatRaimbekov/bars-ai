import { useCallback } from "react";
import { useChatStore } from "@/store/chatStore";
import { sendMessage } from "@/services/claudeApi";
import type { ChatMessage } from "@/types/chat";

export function useChat(systemPrompt: string) {
  const { messages, isLoading, addMessage, setLoading } = useChatStore();

  const send = useCallback(
    async (text: string) => {
      const userMsg: ChatMessage = {
        id: crypto.randomUUID(),
        role: "user",
        content: text,
        timestamp: Date.now(),
      };
      addMessage(userMsg);
      setLoading(true);

      try {
        const allMessages = [...messages, userMsg];
        const response = await sendMessage(systemPrompt, allMessages);
        const aiMsg: ChatMessage = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: response,
          timestamp: Date.now(),
        };
        addMessage(aiMsg);
        return response;
      } catch (error) {
        const errMsg: ChatMessage = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: "Sorry, I encountered an error. Please try again.",
          timestamp: Date.now(),
        };
        addMessage(errMsg);
        return null;
      } finally {
        setLoading(false);
      }
    },
    [messages, systemPrompt, addMessage, setLoading]
  );

  return { messages, isLoading, send };
}
