import type { ChatMessage } from "@/types/chat";

const API_KEY = import.meta.env.VITE_ANTHROPIC_API_KEY;
const API_URL = "https://api.anthropic.com/v1/messages";

interface ClaudeResponse {
  content: Array<{ type: string; text: string }>;
}

export async function sendMessage(
  systemPrompt: string,
  messages: ChatMessage[]
): Promise<string> {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": API_KEY,
      "anthropic-version": "2023-06-01",
      "anthropic-dangerous-direct-browser-access": "true",
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 1024,
      system: systemPrompt,
      messages: messages.map((m) => ({
        role: m.role,
        content: m.content,
      })),
    }),
  });

  if (!response.ok) {
    throw new Error(`Claude API error: ${response.status}`);
  }

  const data: ClaudeResponse = await response.json();
  return data.content[0]?.text ?? "No response";
}

export async function assessLevel(
  direction: string,
  answers: string[]
): Promise<"beginner" | "intermediate" | "advanced"> {
  const systemPrompt = `You are assessing a student's level in ${direction}. Based on their answers to assessment questions, classify them as exactly one of: beginner, intermediate, advanced. Respond with ONLY that single word.`;

  const messages: ChatMessage[] = [
    {
      id: "assess",
      role: "user",
      content: `Here are the student's answers to assessment questions:\n${answers.map((a, i) => `Q${i + 1}: ${a}`).join("\n")}\n\nWhat is their level? Respond with only: beginner, intermediate, or advanced`,
      timestamp: Date.now(),
    },
  ];

  const result = await sendMessage(systemPrompt, messages);
  const level = result.trim().toLowerCase();
  if (level === "beginner" || level === "intermediate" || level === "advanced") {
    return level;
  }
  return "beginner";
}

export async function generateTip(
  direction: string,
  level: string
): Promise<string> {
  const messages: ChatMessage[] = [
    {
      id: "tip",
      role: "user",
      content: `Give me one short, actionable tip of the day for a ${level} ${direction} student. Max 2 sentences.`,
      timestamp: Date.now(),
    },
  ];

  return sendMessage(
    `You are a helpful ${direction} mentor. Be concise and practical.`,
    messages
  );
}

export async function scoreAnswer(
  question: string,
  answer: string,
  direction: string
): Promise<{ score: number; feedback: string; modelAnswer: string }> {
  const systemPrompt = `You are an expert interviewer for ${direction} positions. Score the candidate's answer on a scale of 1-10. Respond in this exact JSON format: {"score": <number>, "feedback": "<string>", "modelAnswer": "<string>"}`;

  const messages: ChatMessage[] = [
    {
      id: "score",
      role: "user",
      content: `Question: ${question}\n\nCandidate's answer: ${answer}\n\nScore this answer. Respond ONLY with JSON.`,
      timestamp: Date.now(),
    },
  ];

  const result = await sendMessage(systemPrompt, messages);
  try {
    return JSON.parse(result);
  } catch {
    return { score: 5, feedback: result, modelAnswer: "Could not parse response" };
  }
}
