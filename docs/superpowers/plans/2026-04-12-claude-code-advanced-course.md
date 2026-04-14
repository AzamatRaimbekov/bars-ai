# Claude Code Advanced Course — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a massive 89-lesson advanced Claude Code course as a Python seed file following existing patterns.

**Architecture:** Single Python seed file `backend/seed_claude_code_advanced.py` containing all 18 sections, 89 lessons + 4 module projects (~93 total lessons, ~1570 steps). Follows the exact pattern of existing `seed_claude_code_full.py` — Python dict structure with async seed function. Content in Russian (primary language, matching existing seed files). Trilingual support (en/ky) is a separate platform task outside this plan.

**Tech Stack:** Python, SQLAlchemy async, existing Course/CourseSection/CourseLesson models.

**Spec:** `docs/superpowers/specs/2026-04-12-claude-code-advanced-course-design.md`

---

## File Structure

- **Create:** `backend/seed_claude_code_advanced.py` — the main seed file (~5000+ lines)

The seed file structure follows the exact pattern from `backend/seed_claude_code_full.py`:

```python
"""Seed: Claude Code Advanced Mastery — 18 sections, 89+ lessons."""
import asyncio, uuid
from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.models.course import Course, CourseSection, CourseLesson

SNAKE_X = [0.50, 0.75, 0.50, 0.25, 0.50]
CANVAS_W, ROW_H, V_PAD = 500, 148, 90
T = "Claude Code Advanced Mastery"

S = [
  # ... all sections with lessons and steps ...
]

async def main():
    # ... same pattern as seed_claude_code_full.py ...
```

Each section is a dict: `{"title": "...", "pos": N, "lessons": [...]}`
Each lesson is a dict: `{"t": "...", "xp": N, "steps": [...]}`
Each step is a dict with `type` and type-specific fields.

### Step type reference (from existing seed files):

```python
# info
{"type":"info","title":"Title","markdown":"## Content"}

# quiz
{"type":"quiz","question":"Q?","options":[{"id":"a","text":"A","correct":True},{"id":"b","text":"B","correct":False}]}

# terminal-sim
{"type":"terminal-sim","prompt":"Do X","expectedCommand":"command","output":"output","hint":"Hint"}

# code-puzzle
{"type":"code-puzzle","question":"Arrange","items":["line1","line2","line3"]}

# matching
{"type":"matching","pairs":[{"left":"A","right":"B"}]}

# flashcards
{"type":"flashcards","cards":[{"front":"Term","back":"Definition"}]}

# drag-order
{"type":"drag-order","items":["First","Second","Third"]}

# snippet-order
{"type":"snippet-order","instruction":"Order fragments","fragments":["frag1","frag2"]}

# category-sort
{"type":"category-sort","categories":["Cat1","Cat2"],"items":[{"text":"Item","category":"Cat1"}]}

# multi-select
{"type":"multi-select","question":"Select all","options":[{"id":"a","text":"A","correct":True}]}

# true-false
{"type":"true-false","statement":"Statement","correct":True}

# fill_blanks / fill-blank
{"type":"fill-blank","text":"The ___ command...","answers":["answer"]}

# highlight-text
{"type":"highlight-text","instruction":"Select correct","segments":[{"text":"Word","correct":True}]}

# type-answer
{"type":"type-answer","question":"What is?","acceptedAnswers":["a1","a2"]}

# conversation-sim
{"type":"conversation-sim","scenario":"Scenario","messages":[],"choices":[{"id":"a","text":"Choice","correct":True,"feedback":"Why"}]}
```

---

## Tasks

Due to the massive size (~1570 steps), the seed file is built incrementally — one module at a time. Each task creates one module's worth of sections with ALL lessons and ALL steps fully written out. The agent MUST follow the spec exactly for lesson titles, step counts, XP values, and step types.

### Task 1: Create seed file scaffold + Module 1 (Sections 1-4 + Project)

**Files:**
- Create: `backend/seed_claude_code_advanced.py`

**Context:** The spec defines Module 1 with sections 1-4 (21 lessons) + 1 module project. Each lesson has 15-25 steps. See spec file `docs/superpowers/specs/2026-04-12-claude-code-advanced-course-design.md` for the full breakdown.

- [ ] **Step 1: Create the seed file with scaffold and Module 1 content**

Create `backend/seed_claude_code_advanced.py` with:
1. The imports and constants (copy pattern from `seed_claude_code_full.py`)
2. `T = "Claude Code Advanced Mastery"`
3. Course description string
4. `S = [...]` with ALL sections from Module 1:
   - Section 1: "Быстрый старт и CLI" (5 lessons, pos=0)
   - Section 2: "Навигация и чтение кодовых баз" (5 lessons, pos=1)
   - Section 3: "Редактирование и рефакторинг" (5 lessons, pos=2)
   - Section 4: "Git-интеграция" (5 lessons, pos=3)
   - Section 5: "Проект: Исследуй и отрефактори open-source проект" (1 lesson, pos=4)
5. The `async def main()` function (copy from seed_claude_code_full.py, update course metadata: category="AI-Assisted Development", difficulty="Advanced")

**CRITICAL:** Every lesson must have ALL steps from the spec fully written out with real educational content. Do NOT use placeholders. Each step must have complete, accurate content about Claude Code.

Reference files for step format: `backend/seed_claude_code_full.py` (lines 17-22 show info/quiz/matching/flashcards/true-false step formats, lines 26-30 show terminal-sim/multi-select/drag-order formats).

- [ ] **Step 2: Verify the file is valid Python**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи" && python3 -c "import ast; ast.parse(open('backend/seed_claude_code_advanced.py').read()); print('Valid Python')"`
Expected: "Valid Python"

- [ ] **Step 3: Commit**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи" && git add backend/seed_claude_code_advanced.py && git commit -m "feat: add Claude Code Advanced course seed — Module 1 (sections 1-4)"
```

---

### Task 2: Add Module 2 (Sections 5-9 + Project)

**Files:**
- Modify: `backend/seed_claude_code_advanced.py`

**Context:** Append Module 2 sections to the `S` list. The spec defines sections 5-9 (23 lessons) + 1 module project.

- [ ] **Step 1: Add Module 2 sections to the S list**

Append to the `S` list in `seed_claude_code_advanced.py`:
- Section 6: "CLAUDE.md — конфигурация проекта" (5 lessons, pos=5)
- Section 7: "Permissions и безопасность" (4 lessons, pos=6)
- Section 8: "Хуки (Hooks)" (5 lessons, pos=7)
- Section 9: "Промпт-инжиниринг для Claude Code" (5 lessons, pos=8)
- Section 10: "Оптимизация контекстного окна" (4 lessons, pos=9)
- Section 11: "Проект: Настрой идеальное окружение" (1 lesson, pos=10)

**CRITICAL:** Every lesson must have ALL steps from the spec fully written out. Follow exact step types and counts from the spec. All content must be accurate Claude Code educational material.

- [ ] **Step 2: Verify valid Python**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи" && python3 -c "import ast; ast.parse(open('backend/seed_claude_code_advanced.py').read()); print('Valid Python')"`
Expected: "Valid Python"

- [ ] **Step 3: Commit**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи" && git add backend/seed_claude_code_advanced.py && git commit -m "feat: add Claude Code Advanced course — Module 2 (sections 5-9)"
```

---

### Task 3: Add Module 3 (Sections 10-14 + Project)

**Files:**
- Modify: `backend/seed_claude_code_advanced.py`

**Context:** Append Module 3 sections to the `S` list. The spec defines sections 10-14 (25 lessons) + 1 module project.

- [ ] **Step 1: Add Module 3 sections to the S list**

Append to the `S` list in `seed_claude_code_advanced.py`:
- Section 12: "MCP серверы" (6 lessons, pos=11)
- Section 13: "Custom Slash Commands и Skills" (5 lessons, pos=12)
- Section 14: "Мультиагентность" (5 lessons, pos=13)
- Section 15: "Claude Code SDK" (5 lessons, pos=14)
- Section 16: "IDE интеграции" (4 lessons, pos=15)
- Section 17: "Проект: Построй свою инфраструктуру" (1 lesson, pos=16)

**CRITICAL:** Every lesson must have ALL steps from the spec fully written out. IDE section covers VS Code, Cursor, Zed, Antigravity (NOT JetBrains). All MCP/SDK/skills content must be technically accurate.

- [ ] **Step 2: Verify valid Python**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи" && python3 -c "import ast; ast.parse(open('backend/seed_claude_code_advanced.py').read()); print('Valid Python')"`
Expected: "Valid Python"

- [ ] **Step 3: Commit**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи" && git add backend/seed_claude_code_advanced.py && git commit -m "feat: add Claude Code Advanced course — Module 3 (sections 10-14)"
```

---

### Task 4: Add Module 4 (Sections 15-18 + Final Project)

**Files:**
- Modify: `backend/seed_claude_code_advanced.py`

**Context:** Append Module 4 sections to the `S` list. The spec defines sections 15-18 (20 lessons) + 1 final project.

- [ ] **Step 1: Add Module 4 sections to the S list**

Append to the `S` list in `seed_claude_code_advanced.py`:
- Section 18: "Работа с тестами и TDD" (5 lessons, pos=17)
- Section 19: "Отладка и debugging" (5 lessons, pos=18)
- Section 20: "CI/CD интеграция" (4 lessons, pos=19)
- Section 21: "Реальные проекты и кейсы" (6 lessons, pos=20)
- Section 22: "Финальный проект: Full-stack от идеи до деплоя" (1 lesson, pos=21)

**CRITICAL:** Every lesson must have ALL steps. The "Реальные проекты и кейсы" section has 6 case-study lessons with heavy terminal-sim usage. Final project has 25 steps.

- [ ] **Step 2: Verify valid Python**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи" && python3 -c "import ast; ast.parse(open('backend/seed_claude_code_advanced.py').read()); print('Valid Python')"`
Expected: "Valid Python"

- [ ] **Step 3: Commit**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи" && git add backend/seed_claude_code_advanced.py && git commit -m "feat: add Claude Code Advanced course — Module 4 (sections 15-18, final project)"
```

---

### Task 5: Validate and run seed

**Files:**
- Read: `backend/seed_claude_code_advanced.py`

- [ ] **Step 1: Count total sections and lessons**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи" && python3 -c "
exec(open('backend/seed_claude_code_advanced.py').read().split('async def')[0])
total_lessons = sum(len(s['lessons']) for s in S)
total_steps = sum(len(l['steps']) for s in S for l in s['lessons'])
print(f'Sections: {len(S)}, Lessons: {total_lessons}, Steps: {total_steps}')
"`

Expected: Sections: 22, Lessons: ~93, Steps: ~1570+

- [ ] **Step 2: Validate step types**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи" && python3 -c "
exec(open('backend/seed_claude_code_advanced.py').read().split('async def')[0])
from collections import Counter
types = Counter(step['type'] for s in S for l in s['lessons'] for step in l['steps'])
for t, c in types.most_common():
    print(f'  {t}: {c}')
print(f'Total unique types: {len(types)}')
"`

Expected: 14+ unique step types with terminal-sim and code-puzzle being the most frequent.

- [ ] **Step 3: Run the seed against the database**

Run: `cd "/Users/azamat/Desktop/платформа обучнеи/backend" && python3 -m seed_claude_code_advanced`

Expected: "Created 'Claude Code Advanced Mastery': 22 sections, ~93 lessons."

- [ ] **Step 4: Final commit**

```bash
cd "/Users/azamat/Desktop/платформа обучнеи" && git add -A && git commit -m "feat: complete Claude Code Advanced Mastery course — 22 sections, 93 lessons, 1570+ steps"
```
