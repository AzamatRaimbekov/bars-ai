import { FRONTEND_LESSONS } from "./lessons/frontend";
import { ENGLISH_LESSONS } from "./lessons/english";
import { CALLCENTER_LESSONS } from "./lessons/callcenter";
import { CIB_LESSONS } from "./lessons/cib";
import { FRONTEND_LESSONS_V2 } from "./lessons/frontend-v2";
import { FRONTEND_V2_JUNIOR_HTML } from "./lessons/frontend-v2-junior-html";
import { FRONTEND_V2_JUNIOR_CSS } from "./lessons/frontend-v2-junior-css";
import { FRONTEND_V2_MIDDLE_JS } from "./lessons/frontend-v2-middle-js";
import { FRONTEND_V2_MIDDLE_REACT } from "./lessons/frontend-v2-middle-react";
import { FRONTEND_V2_SENIOR } from "./lessons/frontend-v2-senior";
import type { LessonContentV2 } from "@/types/lesson";

export interface VideoResource {
  title: string;
  url: string;
  duration?: string;
}

export interface FlashCardData {
  front: string;
  back: string;
}

export interface MatchPairData {
  term: string;
  definition: string;
}

export interface LessonContent {
  id: string;
  title: string;
  content: string;
  videos?: VideoResource[];
  codeExamples?: Array<{ language: string; code: string }>;
  quiz?: Array<{ question: string; options: string[]; correct: number }>;
  flashCards?: FlashCardData[];
  matchGame?: MatchPairData[];
}

export const LESSONS: Record<string, LessonContent> = {
  ...FRONTEND_LESSONS,
  ...ENGLISH_LESSONS,
  ...CALLCENTER_LESSONS,
  ...CIB_LESSONS,
};

export const LESSONS_V2: Record<string, LessonContentV2> = {
  ...FRONTEND_LESSONS_V2,
  ...FRONTEND_V2_JUNIOR_HTML,
  ...FRONTEND_V2_JUNIOR_CSS,
  ...FRONTEND_V2_MIDDLE_JS,
  ...FRONTEND_V2_MIDDLE_REACT,
  ...FRONTEND_V2_SENIOR,
};
