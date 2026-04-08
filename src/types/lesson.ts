export interface Slide {
  title: { en: string; ru: string };
  content: { en: string; ru: string };
  code?: { language: string; code: string };
  image?: string;
}

export type GameType =
  | "quiz"
  | "match"
  | "fill_blanks"
  | "drag_order"
  | "true_false"
  | "code_puzzle"
  | "type_answer"
  | "flash_cards";

export interface GameQuestion {
  type: GameType;
  question: { en: string; ru: string };
  options?: { en: string; ru: string }[];
  correct?: number;
  correctText?: { en: string; ru: string };
  pairs?: { term: { en: string; ru: string }; definition: { en: string; ru: string } }[];
  items?: { en: string; ru: string }[];
  statement?: { en: string; ru: string };
  answer?: boolean;
  blanks?: {
    text: { en: string; ru: string };
    options: { en: string; ru: string }[];
    correctIndex: number;
  }[];
}

export interface LessonContentV2 {
  id: string;
  title: { en: string; ru: string };
  slides: Slide[];
  questions: GameQuestion[];
}

export type LessonStep =
  | { type: "slide"; data: Slide }
  | { type: "game"; gameType: GameType; data: GameQuestion };

export interface LessonSession {
  lessonId: string;
  steps: LessonStep[];
  currentStepIndex: number;
  errors: number;
  startedAt: number;
}
