# Course Constructor Design

## Overview
Full-featured course constructor where users create courses with visual roadmap editor, step-based interactive lessons, and AI-powered generation from uploaded materials.

## Pages & Tabs

### `/teach/:id/edit` — Constructor (4 tabs)

**Tab 1: Info** — Course metadata
- Title, description, category, difficulty, thumbnail URL, price
- Publish / Unpublish toggle

**Tab 2: Structure** — Sections → Nodes → Lessons
- Collapsible tree: Section > Node > Lesson
- Drag & drop reordering at all levels
- Add/edit/delete at each level
- Each lesson has "Edit steps" button → opens step editor
- Each lesson has "AI: Generate" button → generates steps from course context
- XP reward per lesson (0–500)

**Tab 3: Roadmap** — Visual canvas editor
- `@xyflow/react` canvas with course nodes
- Auto-layout from Tab 2 structure (sections as columns, nodes as rows)
- Drag nodes to reposition, positions saved as x/y
- Draw edges (connections) between nodes
- "Auto Layout" button resets to computed positions
- Preview mode (read-only, as student sees it)

**Tab 4: AI Generation**
- File upload zone (PDF, Word, images, plain text)
- "Generate Full Course" → AI creates sections, nodes, lessons with steps
- "Generate Structure Only" → AI creates sections + nodes, no lesson content
- Results populate Tab 2 and Tab 3
- Per-lesson "AI Generate" button in Tab 2

### Step Editor (full-screen overlay)
Opens when clicking "Edit steps" on a lesson.

**Step types:**
- `info` — markdown text block (title, content)
- `quiz` — question + options array + correctIndex (single choice) or correctIndices (multi)
- `drag-order` — items array, correctOrder array
- `code-puzzle` — code fragments array, correctOrder array
- `fill-blank` — text with `___` placeholders, answers array

**UI:** Vertical list of step cards, each with type-specific form fields. Add step button with type selector. Drag to reorder. Delete button per step.

## Data Model Changes

### Backend: New fields on CourseLesson
- `steps: JSON` — array of step objects (replaces markdown content for interactive lessons)
- `content_type: str` — "markdown" | "steps"

### Backend: New fields on Course
- `roadmap_nodes: JSON` — array of `{ nodeId, x, y, sectionIndex, nodeIndex }`
- `roadmap_edges: JSON` — array of `{ source, target }`

### Frontend types
```typescript
interface CourseRoadmapNode {
  id: string;
  title: string;
  description: string;
  sectionId: string;
  x: number;
  y: number;
  sectionIndex: number;
  nodeIndex: number;
  lessonIds: string[];
}

interface CourseRoadmapEdge {
  source: string;
  target: string;
}

type StepType = "info" | "quiz" | "drag-order" | "code-puzzle" | "fill-blank";

interface LessonStep {
  id: string;
  type: StepType;
  data: InfoStepData | QuizStepData | DragOrderStepData | CodePuzzleStepData | FillBlankStepData;
}
```

## API Changes

### Existing endpoints (modified)
- `PATCH /api/courses/:id` — accepts `roadmap_nodes` and `roadmap_edges`
- `POST /api/courses/sections/:id/lessons` — accepts `steps` JSON array
- `PATCH /api/courses/lessons/:id` — update lesson steps

### New endpoints
- `POST /api/courses/:id/generate` — AI full course generation from files
- `POST /api/courses/lessons/:id/ai-generate` — AI single lesson generation
- `POST /api/courses/:id/auto-layout` — compute auto layout positions

## Implementation Scope (Constructor Only — no AI yet)

Phase 1 (this task):
1. Backend: Add roadmap_nodes, roadmap_edges, steps fields to models
2. Backend: Update/add endpoints for lesson steps CRUD
3. Frontend: Rewrite CourseEditor with 4-tab layout
4. Frontend: Structure tab with collapsible tree + CRUD
5. Frontend: Step editor overlay with all 5 step types
6. Frontend: Roadmap canvas tab with @xyflow/react
7. Frontend: Auto-layout algorithm
8. Frontend: Info and Settings tabs (polish existing)

Phase 2 (next task):
- AI generation from uploaded files
- File upload handling
- AI endpoints integration
