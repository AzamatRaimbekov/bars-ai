import type { LessonStep } from "@/services/courseApi";
import type { TDQuestion } from "./types";
import { QUESTIONS_PER_WAVE, MIN_WAVES } from "./config";

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** Extract answerable questions from lesson steps. */
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

/** Shuffle and split into waves. Guarantees at least MIN_WAVES waves by recycling questions. */
export function splitIntoWaves(questions: TDQuestion[]): TDQuestion[][] {
  if (questions.length === 0) return [[]];

  const totalQuestionsNeeded = MIN_WAVES * QUESTIONS_PER_WAVE;

  // Recycle questions if not enough for MIN_WAVES
  let pool = shuffle(questions);
  while (pool.length < totalQuestionsNeeded) {
    pool = [...pool, ...shuffle(questions)];
  }
  pool = pool.slice(0, totalQuestionsNeeded);

  const waves: TDQuestion[][] = [];
  for (let i = 0; i < pool.length; i += QUESTIONS_PER_WAVE) {
    waves.push(pool.slice(i, i + QUESTIONS_PER_WAVE));
  }

  return waves;
}
