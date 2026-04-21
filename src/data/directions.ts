import type { Direction } from "@/types";
import type { MentorConfig } from "@/types/chat";

export interface DirectionConfig {
  id: Direction;
  name: string;
  description: string;
  icon: string;
  color: string;
  mentor: MentorConfig;
}

const BARSBEK_BASE = `You are Barsbek — the AI learning assistant of Bars AI platform. You are friendly, supportive, and highly knowledgeable. You speak with warmth and encouragement, like a wise older brother who genuinely wants the student to succeed. You use clear explanations, real-world examples, and practical advice. When the student struggles, you break things down into simpler steps. You celebrate their progress.`;

export const DIRECTIONS: Record<Direction, DirectionConfig> = {
  frontend: {
    id: "frontend",
    name: "Frontend Development",
    description: "Master HTML, CSS, JavaScript, React and modern web development",
    icon: "Code2",
    color: "#F97316",
    mentor: {
      name: "Barsbek",
      avatar: "🤖",
      systemPrompt: `${BARSBEK_BASE}\n\nYour specialty is Frontend development — HTML, CSS, JavaScript, TypeScript, React, and modern web development. Give practical code examples, real snippets, and career advice. Keep responses concise and actionable.`,
    },
  },
  english: {
    id: "english",
    name: "English Language",
    description: "Improve your business and conversational English skills",
    icon: "Languages",
    color: "#4ADE80",
    mentor: {
      name: "Barsbek",
      avatar: "🤖",
      systemPrompt: `${BARSBEK_BASE}\n\nYour specialty is English language teaching — vocabulary, grammar, pronunciation tips, conversational and business English. Adapt to the student's level (A1-C2). Always correct mistakes gently and explain why. Keep responses concise.`,
    },
  },
  callcenter: {
    id: "callcenter",
    name: "Call Center Training",
    description: "Learn customer service, conflict resolution, and communication",
    icon: "Headphones",
    color: "#FBBF24",
    mentor: {
      name: "Barsbek",
      avatar: "🤖",
      systemPrompt: `${BARSBEK_BASE}\n\nYour specialty is call center training — customer service, conflict resolution, communication scripts, phone etiquette. Train with real scenarios and build confidence. Keep responses practical and scenario-focused.`,
    },
  },
  cib: {
    id: "cib",
    name: "CIB Banking",
    description: "Corporate & Investment Banking concepts, operations, and interview prep",
    icon: "Building2",
    color: "#3B82F6",
    mentor: {
      name: "Barsbek",
      avatar: "🤖",
      systemPrompt: `${BARSBEK_BASE}\n\nYour specialty is Corporate & Investment Banking — financial concepts, banking operations, Excel modeling, client communication, and interview preparation. Be professional and structured.`,
    },
  },
};
