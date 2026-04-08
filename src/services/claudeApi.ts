import { apiFetch } from "./api";

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export async function sendMessage(
  systemPrompt: string,
  messages: ChatMessage[],
  direction: string = "frontend",
): Promise<string> {
  const data = await apiFetch<{ content: string }>("/ai/chat", {
    method: "POST",
    body: JSON.stringify({
      messages: messages.map((m) => ({ role: m.role, content: m.content })),
      direction,
    }),
  });
  return data.content;
}

export async function assessLevel(
  direction: string,
  answers: string[],
): Promise<"beginner" | "intermediate" | "advanced"> {
  const data = await apiFetch<{ level: string }>("/ai/assess", {
    method: "POST",
    body: JSON.stringify({ direction, answers }),
  });
  const level = data.level;
  if (level === "beginner" || level === "intermediate" || level === "advanced") {
    return level;
  }
  return "beginner";
}

export async function generateTip(
  direction: string,
  level: string,
): Promise<string> {
  const data = await apiFetch<{ tip: string }>("/ai/tip", {
    method: "POST",
    body: JSON.stringify({ direction, level }),
  });
  return data.tip;
}

export async function scoreAnswer(
  question: string,
  answer: string,
  direction: string,
): Promise<{ score: number; feedback: string; modelAnswer: string }> {
  const data = await apiFetch<{ score: number; feedback: string; model_answer: string }>("/ai/score", {
    method: "POST",
    body: JSON.stringify({ question, answer, direction }),
  });
  return { score: data.score, feedback: data.feedback, modelAnswer: data.model_answer };
}
