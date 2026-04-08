import type { LessonContentV2, LessonStep, LessonSession } from "@/types/lesson";

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function buildSession(lesson: LessonContentV2): LessonSession {
  const slideSteps: LessonStep[] = lesson.slides.map((s) => ({
    type: "slide",
    data: s,
  }));

  const shuffled = shuffle(lesson.questions);
  const count = Math.min(shuffled.length, Math.max(4, Math.min(5, shuffled.length)));

  const picked: typeof shuffled = [];
  const remaining = [...shuffled];

  while (picked.length < count && remaining.length > 0) {
    const lastType = picked.length > 0 ? picked[picked.length - 1].type : null;
    const differentIdx = remaining.findIndex((q) => q.type !== lastType);
    const idx = differentIdx !== -1 ? differentIdx : 0;
    picked.push(remaining.splice(idx, 1)[0]);
  }

  const gameSteps: LessonStep[] = picked.map((q) => ({
    type: "game",
    gameType: q.type,
    data: q,
  }));

  return {
    lessonId: lesson.id,
    steps: [...slideSteps, ...gameSteps],
    currentStepIndex: 0,
    errors: 0,
    startedAt: Date.now(),
  };
}

export function calculateStars(errors: number): number {
  if (errors === 0) return 3;
  if (errors <= 2) return 2;
  return 1;
}

export function calculateXP(stars: number): number {
  const base = 50;
  const bonus = stars === 3 ? 50 : stars === 2 ? 25 : 0;
  return base + bonus;
}
