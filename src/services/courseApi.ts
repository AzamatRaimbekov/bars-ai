import { apiFetch } from "./api";

export interface CourseCard {
  id: string;
  title: string;
  slug: string;
  description: string;
  thumbnail_url: string | null;
  author_name: string;
  author_id: string;
  category: string;
  difficulty: string;
  price: number;
  currency: string;
  status: string;
  total_enrolled: number;
  rating_avg: number;
  rating_count: number;
}

export interface CourseLesson {
  id: string;
  title: string;
  position: number;
  content_type: string;
  xp_reward: number;
  steps?: LessonStep[] | null;
  step_count?: number;
}

export interface CourseSection {
  id: string;
  title: string;
  position: number;
  lessons: CourseLesson[];
}

export interface CourseDetail extends CourseCard {
  status: string;
  sections: CourseSection[];
  reviews: {
    id: string;
    user_name: string;
    rating: number;
    comment: string;
    created_at: string;
  }[];
  is_enrolled: boolean;
  is_author: boolean;
  roadmap_nodes?: { id: string; x: number; y: number }[] | null;
  roadmap_edges?: { id: string; source: string; target: string }[] | null;
}

export interface CourseProgress {
  completed_lesson_ids: string[];
  total_lessons: number;
  completed_count: number;
}

// Step types used in the step editor
export type StepType =
  | "info"
  | "quiz"
  | "drag-order"
  | "code-puzzle"
  | "fill-blank"
  | "matching"
  | "true-false"
  | "flashcards"
  | "type-answer"
  | "image-hotspot"
  | "code-editor"
  | "timeline"
  | "category-sort"
  | "video"
  | "audio"
  | "embed"
  | "terminal-sim"
  | "multi-select"
  | "conversation-sim"
  | "highlight-text"
  | "snippet-order"
  | "listening-comprehension"
  | "pronunciation"
  | "word-builder"
  | "sentence-translation"
  | "cloze-passage"
  | "tower-defense";

export interface StepInfo {
  type: "info";
  title: string;
  markdown: string;
}

export interface StepQuizOption {
  id: string;
  text: string;
  correct: boolean;
}

export interface StepQuiz {
  type: "quiz";
  question: string;
  options: StepQuizOption[];
}

export interface StepDragOrder {
  type: "drag-order";
  items: string[];
}

export interface StepCodePuzzle {
  type: "code-puzzle";
  fragments: string[];
}

export interface StepFillBlank {
  type: "fill-blank";
  text: string;
  answers: string[];
}

export interface StepMatching {
  type: "matching";
  pairs: { left: string; right: string }[];
}

export interface StepTrueFalse {
  type: "true-false";
  statement: string;
  correct: boolean;
}

export interface StepFlashcards {
  type: "flashcards";
  cards: { front: string; back: string }[];
}

export interface StepTypeAnswer {
  type: "type-answer";
  question: string;
  acceptedAnswers: string[]; // case-insensitive match
}

export interface StepImageHotspot {
  type: "image-hotspot";
  imageUrl: string;
  question: string;
  hotspot: { x: number; y: number; radius: number }; // percentage-based coords
}

export interface StepCodeEditor {
  type: "code-editor";
  language: string; // "html" | "css" | "javascript" | "typescript"
  prompt: string;
  starterCode: string;
  expectedOutput: string; // substring that must be in the result
}

export interface StepTimeline {
  type: "timeline";
  events: { label: string; year: string }[]; // correct order
}

export interface StepCategorySort {
  type: "category-sort";
  categories: string[]; // e.g. ["CSS", "JavaScript"]
  items: { text: string; category: string }[]; // category matches one of categories
}

export interface StepVideo {
  type: "video";
  title: string;
  url: string; // YouTube embed URL or direct video URL
}

export interface StepAudio {
  type: "audio";
  title: string;
  url: string;
  transcript?: string;
}

export interface StepEmbed {
  type: "embed";
  title: string;
  url: string; // iframe src
  height?: number;
}

export interface StepTerminalSim {
  type: "terminal-sim";
  prompt: string; // instruction for the user
  expectedCommand: string; // exact command to type (case-sensitive)
  output: string; // what to show after correct command
  hint?: string; // optional hint
}

export interface StepMultiSelect {
  type: "multi-select";
  question: string;
  options: { id: string; text: string; correct: boolean }[];
}

export interface StepConversationSim {
  type: "conversation-sim";
  scenario: string; // context description
  messages: { role: "user" | "assistant"; text: string }[]; // dialogue so far
  choices: { id: string; text: string; correct: boolean; feedback: string }[]; // user picks one
}

export interface StepHighlightText {
  type: "highlight-text";
  instruction: string;
  segments: { text: string; correct: boolean }[]; // text split into clickable segments
}

export interface StepSnippetOrder {
  type: "snippet-order";
  instruction: string;
  fragments: string[]; // correct order
}

export interface StepListeningComprehension {
  type: "listening-comprehension";
  audioUrl: string;
  transcript?: string;
  questions: {
    question: string;
    options: { id: string; text: string; correct: boolean }[];
  }[];
}

export interface StepPronunciation {
  type: "pronunciation";
  word: string;
  audioUrl?: string;
  phonetic?: string;
  acceptedForms: string[];
}

export interface StepWordBuilder {
  type: "word-builder";
  hint: string;
  word: string;
  image?: string;
}

export interface StepSentenceTranslation {
  type: "sentence-translation";
  sentence: string;
  sourceLanguage: string;
  targetLanguage: string;
  acceptedAnswers: string[];
  aiCheck: boolean;
}

export type ClozeSegment =
  | { type: "text"; value: string }
  | { type: "blank"; answer: string; options?: string[] };

export interface StepClozePassage {
  type: "cloze-passage";
  instruction: string;
  segments: ClozeSegment[];
}

export interface StepTowerDefense {
  type: "tower-defense";
}

export type LessonStep =
  | StepInfo
  | StepQuiz
  | StepDragOrder
  | StepCodePuzzle
  | StepFillBlank
  | StepMatching
  | StepTrueFalse
  | StepFlashcards
  | StepTypeAnswer
  | StepImageHotspot
  | StepCodeEditor
  | StepTimeline
  | StepCategorySort
  | StepVideo
  | StepAudio
  | StepEmbed
  | StepTerminalSim
  | StepMultiSelect
  | StepConversationSim
  | StepHighlightText
  | StepSnippetOrder
  | StepListeningComprehension
  | StepPronunciation
  | StepWordBuilder
  | StepSentenceTranslation
  | StepClozePassage
  | StepTowerDefense;

export interface LessonStepsResponse {
  steps: LessonStep[];
}

export const courseApi = {
  list: async (params?: Record<string, string>) => {
    const query = params ? "?" + new URLSearchParams(params).toString() : "";
    try {
      return await apiFetch<{ items: CourseCard[]; total: number }>(`/courses${query}`);
    } catch {
      // Public endpoint — fallback if not authenticated
      const resp = await fetch(`/api/courses${query}`);
      if (!resp.ok) return { items: [], total: 0 };
      return resp.json();
    }
  },
  get: (id: string) => apiFetch<CourseDetail>(`/courses/${id}`),
  getMy: () => apiFetch<CourseCard[]>("/courses/my"),
  getEnrolled: () => apiFetch<CourseCard[]>("/courses/enrolled"),
  create: (data: any) =>
    apiFetch<{ id: string }>("/courses", {
      method: "POST",
      body: JSON.stringify(data),
    }),
  update: (id: string, data: any) =>
    apiFetch<any>(`/courses/${id}`, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),
  publish: (id: string, published: boolean) =>
    apiFetch<any>(`/courses/${id}`, {
      method: "PATCH",
      body: JSON.stringify({ status: published ? "published" : "draft" }),
    }),
  addSection: (courseId: string, title: string, position?: number) =>
    apiFetch<any>(`/courses/${courseId}/sections`, {
      method: "POST",
      body: JSON.stringify({ title, position: position ?? 0 }),
    }),
  updateSection: (sectionId: string, data: { title?: string; position?: number }) =>
    apiFetch<any>(`/courses/sections/${sectionId}`, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),
  deleteSection: (sectionId: string) =>
    apiFetch<any>(`/courses/sections/${sectionId}`, { method: "DELETE" }),
  addLesson: (sectionId: string, data: any) =>
    apiFetch<any>(`/courses/sections/${sectionId}/lessons`, {
      method: "POST",
      body: JSON.stringify(data),
    }),
  updateLesson: (lessonId: string, data: any) =>
    apiFetch<any>(`/courses/lessons/${lessonId}`, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),
  deleteLesson: (lessonId: string) =>
    apiFetch<any>(`/courses/lessons/${lessonId}`, { method: "DELETE" }),
  getLessonSteps: async (lessonId: string): Promise<LessonStepsResponse> => {
    const lesson = await apiFetch<{ steps: LessonStep[] | null }>(`/courses/lessons/${lessonId}`);
    return { steps: lesson.steps ?? [] };
  },
  saveLessonSteps: (lessonId: string, steps: LessonStep[]) =>
    apiFetch<any>(`/courses/lessons/${lessonId}`, {
      method: "PATCH",
      body: JSON.stringify({ steps }),
    }),
  enroll: (id: string) =>
    apiFetch<any>(`/courses/${id}/enroll`, { method: "POST" }),
  review: (id: string, rating: number, comment: string) =>
    apiFetch<any>(`/courses/${id}/review`, {
      method: "POST",
      body: JSON.stringify({ rating, comment }),
    }),
  completeLesson: (lessonId: string) =>
    apiFetch<any>(`/courses/lessons/${lessonId}/complete`, { method: "POST" }),
  getProgress: (id: string) =>
    apiFetch<CourseProgress>(`/courses/${id}/progress`),
  getLesson: (lessonId: string) =>
    apiFetch<{
      id: string;
      title: string;
      content_markdown: string;
      xp_reward: number;
      steps?: LessonStep[] | null;
    }>(`/courses/lessons/${lessonId}`),
};

export async function transcribeAudio(audioBlob: Blob): Promise<{ text: string; confidence: number }> {
  const formData = new FormData();
  formData.append("audio", audioBlob, "recording.webm");
  const token = sessionStorage.getItem("pathmind_access_token");
  const resp = await fetch("/api/ai/transcribe", {
    method: "POST",
    headers: token ? { Authorization: `Bearer ${token}` } : {},
    credentials: "include",
    body: formData,
  });
  if (!resp.ok) throw new Error("Transcription failed");
  return resp.json();
}

export async function checkTranslation(data: {
  sentence: string;
  user_answer: string;
  source_language: string;
  target_language: string;
}): Promise<{ correct: boolean; feedback: string; suggested: string }> {
  return apiFetch("/ai/check-translation", {
    method: "POST",
    body: JSON.stringify(data),
  });
}
