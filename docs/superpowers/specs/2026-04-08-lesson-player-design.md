# Lesson Player (Duolingo-style) — Design Spec

**Date:** 2026-04-08
**Status:** Approved

---

## 1. Overview

Replace the current basic Lesson page with a Duolingo-style lesson player. When a user clicks "Start" on a roadmap node, they enter an immersive linear lesson flow: theory slides followed by auto-mixed mini-games. After completing all steps, a result screen shows stars, XP, and unlocks the next node.

---

## 2. User Flow

```
Roadmap → Click node → NodePanel → "Start" button
→ LessonPlayer:
  [Progress bar at top, close button]
  Step 1: Theory slide (card with text/code/image)
  Step 2: Theory slide
  Step 3-7: Auto-mixed mini-games (4-5 from pool)
→ ResultScreen:
  Stars (1-3 based on errors)
  XP earned (base 50 + bonus)
  Next node unlock animation
  Buttons: "Back to Map" / "Retry"
→ Return to Roadmap (node marked complete)
```

---

## 3. Components

### 3.1 LessonPlayer (main container)

- Full-screen overlay (covers roadmap)
- Progress bar at top — fills as user completes each step
- Close button (top-left) with confirmation dialog: "Progress will be lost. Exit?"
- Renders current step component based on step type
- Tracks: current step index, errors count, total score
- On final step completion → shows ResultScreen

### 3.2 Theory Slides

- 2-3 slides per lesson
- Card layout: title, markdown content, optional code block, optional image
- "Continue" button at bottom
- No interaction required — just read and proceed

### 3.3 Mini-Games (8 types)

| Type | Component | Description | Interaction |
|------|-----------|-------------|-------------|
| quiz | QuizGame | Question + 4 answer options | Click correct option |
| flash_cards | FlashCardGame | Show term, guess definition | Flip card + self-assess (knew/didn't know) |
| match | MatchGame | 5 pairs (term ↔ definition) | Click term then click matching definition |
| fill_blanks | FillBlanksGame | Text/code with `___` gaps | Select correct word from options for each blank |
| drag_order | DragOrderGame | Put steps in correct order | Drag-and-drop to reorder |
| true_false | TrueFalseGame | Statement — true or false | Click True or False |
| code_puzzle | CodePuzzleGame | Assemble code from shuffled blocks | Drag blocks into correct order |
| type_answer | TypeAnswerGame | Question requiring typed answer | Text input, fuzzy match for correctness |

### 3.4 Auto-Mix System

For each lesson:
1. Take the question pool from lesson data
2. Group questions by type
3. Select 4-5 questions ensuring type variety (no two same types in a row if possible)
4. Randomize order within constraints
5. Prepend 2-3 theory slides
6. Total session: 6-8 steps

### 3.5 ResultScreen

- Stars: 0 errors = 3★, 1-2 errors = 2★, 3+ errors = 1★
- XP: base 50 + star bonus (3★ = +50, 2★ = +25, 1★ = +0)
- Animated star reveal (one by one)
- XP counter animation (counting up)
- Node unlock animation (green pulse on next node)
- Badge reveal if earned
- Buttons: "Back to Map" (primary), "Retry" (secondary)
- On "Back to Map": marks lesson complete, marks node complete if all lessons done, adds XP

### 3.6 Feedback System

After each game answer:
- **Correct:** Green flash, checkmark animation, encouraging text ("Great!", "Perfect!", "Correct!")
- **Wrong:** Red flash, shake animation, show correct answer, error counter increments
- 1-second delay before auto-advancing to next step

---

## 4. Data Model

### 4.1 LessonContent (updated)

```typescript
interface LessonContent {
  id: string;
  title: { en: string; ru: string };
  slides: Slide[];
  questions: GameQuestion[];
}

interface Slide {
  title: { en: string; ru: string };
  content: { en: string; ru: string };
  code?: { language: string; code: string };
  image?: string;
}

interface GameQuestion {
  type: "quiz" | "match" | "fill_blanks" | "drag_order" | "true_false" | "code_puzzle" | "type_answer" | "flash_cards";
  question: { en: string; ru: string };
  // Type-specific fields:
  options?: { en: string; ru: string }[];     // quiz, fill_blanks
  correct?: number;                            // quiz (index into options)
  correctText?: { en: string; ru: string };    // type_answer
  pairs?: { term: { en: string; ru: string }; definition: { en: string; ru: string } }[];  // match, flash_cards
  items?: { en: string; ru: string }[];        // drag_order, code_puzzle (correct order)
  statement?: { en: string; ru: string };      // true_false
  answer?: boolean;                            // true_false
  blanks?: { text: { en: string; ru: string }; answers: { en: string; ru: string }[]; correctIndex: number }[];  // fill_blanks
}
```

### 4.2 Session State

```typescript
interface LessonSession {
  lessonId: string;
  steps: LessonStep[];
  currentStepIndex: number;
  errors: number;
  score: number;
  startedAt: number;
}

type LessonStep =
  | { type: "slide"; data: Slide }
  | { type: "game"; gameType: GameQuestion["type"]; data: GameQuestion };
```

---

## 5. File Structure

### New files

```
src/components/lesson/
  ├── LessonPlayer.tsx        # Main container, step management, progress bar
  ├── LessonSlide.tsx         # Theory slide card
  ├── ResultScreen.tsx        # Stars, XP, unlock animation
  ├── FeedbackOverlay.tsx     # Correct/wrong flash after each answer
  ├── games/
  │   ├── QuizGame.tsx        # Multiple choice
  │   ├── FlashCardGame.tsx   # Flip card self-assessment
  │   ├── MatchGame.tsx       # Pair matching (click-click)
  │   ├── FillBlanksGame.tsx  # Fill in the blanks
  │   ├── DragOrderGame.tsx   # Drag to reorder
  │   ├── TrueFalseGame.tsx   # True/False
  │   ├── CodePuzzleGame.tsx  # Assemble code blocks
  │   └── TypeAnswerGame.tsx  # Type the answer
  └── utils/
      └── autoMix.ts          # Session builder (select & order games)
```

### Modified files

```
src/pages/Lesson.tsx          # Replace with LessonPlayer integration
src/data/lessons/             # Update lesson data to new format with slides + questions
src/types/index.ts            # Add new types (LessonContent, Slide, GameQuestion, etc.)
```

### Unchanged files

```
src/components/roadmap/       # NodePanel already has "Start Lesson" button
src/pages/Roadmap.tsx         # No changes needed
```

---

## 6. Lesson Data Strategy

Each direction has 25 nodes with 1-2 lessons each. Each lesson needs:
- 2-3 theory slides
- 8-15 questions across different game types

For MVP: create rich lesson data for the first 3-4 lessons of the frontend direction. Remaining lessons get placeholder data that can be expanded later.

---

## 7. Visual Design

- **LessonPlayer:** Full-screen dark overlay, centered content card (max-w-2xl)
- **Progress bar:** Top of screen, direction color, smooth animation
- **Slides:** Clean card with large text, syntax-highlighted code blocks
- **Games:** Each game fills the content area, big touch-friendly buttons/targets
- **Feedback:** Full-width banner sliding in from bottom (green/red)
- **ResultScreen:** Centered, stars animate in sequence, confetti particles for 3★
- **Transitions:** Framer Motion slide-left between steps

---

## 8. Scoring & Rewards

| Stars | Errors | XP |
|-------|--------|----|
| 3★    | 0      | 100 (50 base + 50 bonus) |
| 2★    | 1-2    | 75 (50 base + 25 bonus) |
| 1★    | 3+     | 50 (50 base + 0 bonus) |

- Perfect score (3★) on first attempt → triggers "perfectQuiz" XP reward (100 XP from constants)
- Completing all lessons in a node → node marked complete, next node unlocked
- Badge checks run after each lesson completion
