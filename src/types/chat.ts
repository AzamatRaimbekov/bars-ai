export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: number;
}

export interface MentorConfig {
  name: string;
  avatar: string;
  systemPrompt: string;
  voiceName?: string;
}
