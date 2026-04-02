import { create } from "zustand";
import type { ChatMessage } from "@/types/chat";

interface ChatState {
  messages: ChatMessage[];
  isLoading: boolean;
  addMessage: (message: ChatMessage) => void;
  setLoading: (loading: boolean) => void;
  clearMessages: () => void;
}

export const useChatStore = create<ChatState>()((set) => ({
  messages: [],
  isLoading: false,
  addMessage: (message) =>
    set((s) => ({ messages: [...s.messages, message] })),
  setLoading: (loading) => set({ isLoading: loading }),
  clearMessages: () => set({ messages: [] }),
}));
