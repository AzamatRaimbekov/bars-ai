import type { LessonStep } from "@/services/courseApi";
import type { TDQuestion } from "./types";
import { QUESTIONS_PER_WAVE } from "./config";

export function extractQuestions(steps: LessonStep[]): TDQuestion[] {
  const questions: TDQuestion[] = [];
  for (const step of steps) {
    if (step.type === "tower-defense") continue;
    if (step.type === "quiz") {
      questions.push({ type: "quiz", question: step.question, options: step.options });
    } else if (step.type === "true-false") {
      questions.push({ type: "true-false", question: step.statement, statement: step.statement, correct: step.correct });
    } else if (step.type === "type-answer") {
      questions.push({ type: "type-answer", question: step.question, acceptedAnswers: step.acceptedAnswers });
    } else if (step.type === "fill-blank") {
      questions.push({ type: "fill-blank", question: "Заполните пропуск", text: step.text, answers: step.answers });
    }
  }
  return questions;
}

export function splitIntoWaves(questions: TDQuestion[]): TDQuestion[][] {
  const shuffled = [...questions];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  const waves: TDQuestion[][] = [];
  for (let i = 0; i < shuffled.length; i += QUESTIONS_PER_WAVE) {
    waves.push(shuffled.slice(i, i + QUESTIONS_PER_WAVE));
  }
  if (waves.length === 0) waves.push([]);
  return waves;
}
