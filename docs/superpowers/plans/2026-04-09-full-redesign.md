# PathMind Full Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the entire PathMind UI from dark purple theme to black + warm orange (Apple/Stripe inspired).

**Architecture:** CSS-first approach — update global theme tokens in index.css which cascade to most components, then update components that use hardcoded colors, then update pages with inline styles. No logic/API/state changes.

**Tech Stack:** Tailwind CSS v4 (via @theme in index.css), React, Framer Motion, Lucide icons

---

### Task 1: Global Theme Tokens

**Files:**
- Modify: `src/index.css`

Update the @theme block and global styles to new palette.

- [ ] **Step 1: Update @theme colors in index.css**

Replace the entire `@theme` color block:
```css
--color-bg: #000000;
--color-surface: #0A0A0A;
--color-border: rgba(255,255,255,0.06);
--color-primary: #F97316;
--color-accent: #FB923C;
--color-success: #4ADE80;
--color-warning: #FBBF24;
--color-text: #FAFAFA;
--color-text-secondary: rgba(255,255,255,0.4);
```

- [ ] **Step 2: Update scrollbar styles**

Scrollbar thumb: `rgba(255,255,255,0.08)`, track: `transparent`

- [ ] **Step 3: Remove fractal noise overlay if present**

Delete the `::after` pseudo-element that adds noise texture.

- [ ] **Step 4: Verify build compiles**

Run: `npx tsc --noEmit && npx vite build`

- [ ] **Step 5: Commit**

```
git add src/index.css
git commit -m "feat: update global theme tokens to black + orange palette"
```

---

### Task 2: UI Components

**Files:**
- Modify: `src/components/ui/Button.tsx`
- Modify: `src/components/ui/Card.tsx`
- Modify: `src/components/ui/Input.tsx`
- Modify: `src/components/ui/ProgressBar.tsx`
- Modify: `src/components/ui/ProgressRing.tsx`
- Modify: `src/components/ui/Modal.tsx`
- Modify: `src/components/ui/Chip.tsx`
- Modify: `src/components/ui/Badge.tsx`
- Modify: `src/components/ui/Tooltip.tsx`

- [ ] **Step 1: Update Button.tsx**

Primary variant: remove shadow/glow (`shadow-lg shadow-primary/25` → nothing). Colors will cascade from theme.

- [ ] **Step 2: Update Card.tsx**

Remove `backdrop-blur-xl`. Remove `glow` prop and its drop-shadow/inset-shadow rendering. Keep hover animation.

- [ ] **Step 3: Update Input.tsx**

Add `uppercase tracking-wider` to label. Ensure bg is `bg-transparent` not `bg-bg`.

- [ ] **Step 4: Update ProgressBar.tsx**

Change height from current to `h-1.5`. Remove glow/shadow effect on fill. Keep gradient (will use new primary/accent from theme).

- [ ] **Step 5: Update Modal.tsx**

Backdrop: `bg-black/80`. Remove `backdrop-blur-sm`. Content: `bg-[#111111]`.

- [ ] **Step 6: Update remaining components (Chip, Badge, ProgressRing, Tooltip)**

Chip active: ensure it uses theme primary colors.
Badge: adapt rarity colors, use orange for legendary.
ProgressRing: stroke color uses theme primary.
Tooltip: bg uses border color.

- [ ] **Step 7: Verify build**

Run: `npx tsc --noEmit`

- [ ] **Step 8: Commit**

```
git add src/components/ui/
git commit -m "feat: redesign all UI components to black + orange theme"
```

---

### Task 3: Layout Components

**Files:**
- Modify: `src/components/layout/Sidebar.tsx`
- Modify: `src/components/layout/TopBar.tsx`
- Modify: `src/components/layout/TabBar.tsx`
- Modify: `src/components/layout/PageWrapper.tsx`

- [ ] **Step 1: Update Sidebar.tsx**

- Background: `bg-[#0A0A0A] border-r border-white/6`
- Remove `backdrop-blur-xl`
- Logo text: plain white, no split primary/accent colors
- Nav items: `text-white/40 hover:text-white hover:bg-white/4 rounded-xl`
- Active item: `text-[#FB923C] bg-[#F97316]/8` + left 2px bar `bg-[#F97316]`
- Footer: `text-white/20` for version
- Remove mascot image from footer

- [ ] **Step 2: Update TopBar.tsx**

- Background: `bg-[#0A0A0A]/80 backdrop-blur-xl border-b border-white/6`
- Greeting text: `text-white/40`
- Stat pills: `bg-white/4 rounded-full`

- [ ] **Step 3: Update TabBar.tsx**

- Remove gradient bg and floating capsule shape
- Use: `bg-[#0A0A0A]/90 backdrop-blur-xl border-t border-white/6`
- Icons: `text-white/30` inactive, `text-[#FB923C]` active
- Remove background fill on active tab
- Add 4px dot indicator below active icon: `w-1 h-1 rounded-full bg-[#F97316]`

- [ ] **Step 4: Update PageWrapper.tsx**

- Root bg: `bg-black` (instead of bg-bg if it was different)
- Ensure sidebar offset works correctly

- [ ] **Step 5: Verify build**

Run: `npx tsc --noEmit`

- [ ] **Step 6: Commit**

```
git add src/components/layout/
git commit -m "feat: redesign layout components (sidebar, topbar, tabbar)"
```

---

### Task 4: Gamification Components

**Files:**
- Modify: `src/components/gamification/XPBar.tsx`
- Modify: `src/components/gamification/StreakCounter.tsx`
- Modify: `src/components/gamification/LevelUpModal.tsx`
- Modify: `src/components/gamification/BadgeReveal.tsx`
- Modify: `src/components/gamification/DailyQuests.tsx`

- [ ] **Step 1: Update XPBar.tsx**

Progress fill: theme primary gradient. Text: `text-white/40`.

- [ ] **Step 2: Update StreakCounter.tsx**

Pill style: `bg-[#F97316]/8 text-[#FB923C] rounded-full`.

- [ ] **Step 3: Update LevelUpModal.tsx**

Remove mascot image. Clean centered modal with level name in large text. Orange accent.

- [ ] **Step 4: Update BadgeReveal.tsx**

Remove mascot image. Clean centered badge display. Rarity-colored border ring.

- [ ] **Step 5: Update DailyQuests.tsx**

Progress fill: orange. Reward pill: `bg-[#F97316]/10 text-[#FB923C]`.

- [ ] **Step 6: Commit**

```
git add src/components/gamification/
git commit -m "feat: redesign gamification components to orange theme"
```

---

### Task 5: Auth Pages

**Files:**
- Modify: `src/pages/Login.tsx`
- Modify: `src/pages/Register.tsx`
- Modify: `src/pages/Onboarding.tsx`

- [ ] **Step 1: Update Login.tsx**

- Pure black bg
- Centered card: `bg-[#0A0A0A] border border-white/6 rounded-2xl`
- Subtle orange radial glow behind card
- Brand name "PathMind" at top in large white text
- Orange primary submit button
- Remove any mascot/illustration backgrounds

- [ ] **Step 2: Update Register.tsx**

Same approach as Login — centered card, black bg, orange CTA.

- [ ] **Step 3: Update Onboarding.tsx**

- Black bg, step-by-step flow
- Progress dots at bottom: active = `bg-[#F97316]`, inactive = `bg-white/10`
- Orange primary buttons
- Clean typography

- [ ] **Step 4: Commit**

```
git add src/pages/Login.tsx src/pages/Register.tsx src/pages/Onboarding.tsx
git commit -m "feat: redesign auth and onboarding pages"
```

---

### Task 6: Dashboard Page

**Files:**
- Modify: `src/pages/Dashboard.tsx`

- [ ] **Step 1: Update Dashboard.tsx**

- Welcome: large greeting text, clean sans-serif
- Stats row: XP, Streak, Level in horizontal pills with `bg-[#0A0A0A] border border-white/6`
- Active course card: prominent with orange progress bar
- Daily quests section below
- Remove mascot images
- Update all hardcoded colors to new palette
- Ensure card hovers use `border-white/12`

- [ ] **Step 2: Commit**

```
git add src/pages/Dashboard.tsx
git commit -m "feat: redesign dashboard page"
```

---

### Task 7: Course Pages

**Files:**
- Modify: `src/pages/Courses.tsx`
- Modify: `src/pages/CourseDetail.tsx`
- Modify: `src/pages/CourseEditor.tsx`
- Modify: `src/pages/CourseLearn.tsx`
- Modify: `src/pages/CourseRoadmap.tsx`
- Modify: `src/pages/Teach.tsx`
- Modify: `src/components/courses/StructureTree.tsx`
- Modify: `src/components/courses/StepEditor.tsx`
- Modify: `src/components/courses/RoadmapEditor.tsx`
- Modify: `src/components/courses/ReviewForm.tsx`
- Modify: `src/components/courses/StarRating.tsx`
- Modify: `src/components/courses/CourseStepPlayer.tsx`

- [ ] **Step 1: Update Courses.tsx (catalog)**

- Search bar: `bg-[#0A0A0A] border border-white/6`
- Category pills: active = orange, inactive = `bg-white/4`
- Course cards: keep gradient thumbnails, update text/border colors
- Sort dropdown: `bg-[#111111] border border-white/6`

- [ ] **Step 2: Update CourseDetail.tsx**

- Hero card: remove radial-gradient overlay, clean flat card
- Category/difficulty badges: orange for category, `bg-white/6` for difficulty
- Curriculum sections: `border border-white/6 rounded-xl`
- Reviews: minimal style with white/6 borders
- CTA bar: `bg-[#0A0A0A]/90 backdrop-blur-xl`

- [ ] **Step 3: Update CourseEditor.tsx**

- Tab bar: `bg-[#0A0A0A]`, active tab = orange underline/text
- Forms: transparent inputs on black bg
- Toast: `bg-[#111111] border border-white/6`
- Info tab publish toggle: orange when published

- [ ] **Step 4: Update Teach.tsx**

- Course cards: update borders, status badges
- Draft badge: `bg-white/6 text-white/40`
- Published badge: `bg-[#4ADE80]/10 text-[#4ADE80]`

- [ ] **Step 5: Update course components**

StructureTree: section borders `border-white/6`, lesson rows `bg-white/2`
StepEditor: header `bg-[#111111]`, step cards `bg-[#0A0A0A] border-white/6`
RoadmapEditor: update node colors
ReviewForm: update star colors
StarRating: keep yellow stars
CourseStepPlayer: update all bg/border colors, quiz feedback colors

- [ ] **Step 6: Update CourseLearn.tsx and CourseRoadmap.tsx**

CourseLearn: bg-black, loading text white/40
CourseRoadmap: node completed=#4ADE80, current=#F97316, locked=white/10, connections=white/6

- [ ] **Step 7: Verify build**

Run: `npx tsc --noEmit`

- [ ] **Step 8: Commit**

```
git add src/pages/Courses.tsx src/pages/CourseDetail.tsx src/pages/CourseEditor.tsx src/pages/CourseLearn.tsx src/pages/CourseRoadmap.tsx src/pages/Teach.tsx src/components/courses/
git commit -m "feat: redesign all course pages and components"
```

---

### Task 8: Remaining Pages

**Files:**
- Modify: `src/pages/Profile.tsx`
- Modify: `src/pages/Mentor.tsx`
- Modify: `src/pages/Simulator.tsx`
- Modify: `src/pages/Achievements.tsx`
- Modify: `src/pages/Leaderboard.tsx`
- Modify: `src/pages/Roadmap.tsx`
- Modify: `src/pages/Lesson.tsx`

- [ ] **Step 1: Update Profile.tsx**

- Avatar: large initials circle with `border-2 border-[#F97316]`
- Stats grid: `bg-[#0A0A0A] border border-white/6` cards
- Settings: list with `border-b border-white/6` dividers

- [ ] **Step 2: Update Mentor.tsx**

- User messages: `bg-[#0A0A0A] rounded-2xl`
- Bot messages: `bg-transparent` or very subtle bg
- Input bar: `bg-[#0A0A0A] border border-white/6` fixed bottom
- Remove heavy background gradients

- [ ] **Step 3: Update Simulator.tsx and related components**

- Update ScoreCard, TranscriptPanel, InterviewRoom colors
- Score indicators: orange accent
- Clean dark interface

- [ ] **Step 4: Update Achievements.tsx**

- Badge grid cards: `bg-[#0A0A0A] border border-white/6`
- Locked: `opacity-40 grayscale`
- Unlocked legendary: `border-[#F97316]/30`

- [ ] **Step 5: Update Leaderboard.tsx**

- Alternating rows: `bg-[#0A0A0A]` / `bg-transparent`
- Top 3: orange accent rank numbers
- Current user: `border-l-2 border-[#F97316] bg-[#F97316]/5`

- [ ] **Step 6: Update Roadmap.tsx and Lesson.tsx**

Roadmap: completed=#4ADE80, current=#F97316, locked=white/10
Lesson: update LessonPlayer wrapper colors

- [ ] **Step 7: Verify build**

Run: `npx tsc --noEmit && npx vite build`

- [ ] **Step 8: Commit**

```
git add src/pages/ src/components/
git commit -m "feat: redesign remaining pages (profile, mentor, simulator, achievements, leaderboard, roadmap)"
```

---

### Task 9: Chat & Voice Components

**Files:**
- Modify: `src/components/chat/ChatWindow.tsx`
- Modify: `src/components/chat/WaveformVisualizer.tsx`
- Modify: `src/components/chat/VoiceModeOverlay.tsx`
- Modify: `src/components/simulator/InterviewRoom.tsx`
- Modify: `src/components/simulator/ScoreCard.tsx`
- Modify: `src/components/simulator/TranscriptPanel.tsx`
- Modify: `src/components/lesson/LessonPlayer.tsx`
- Modify: `src/components/lesson/ResultScreen.tsx`
- Modify: `src/components/roadmap/NodePanel.tsx`
- Modify: `src/components/roadmap/RoadmapCanvas.tsx`
- Modify: `src/components/roadmap/RoadmapNode.tsx`

- [ ] **Step 1: Update chat components**

ChatWindow: message bubbles, input bar, background colors
WaveformVisualizer: use #F97316 for active waveform color
VoiceModeOverlay: dark bg, orange accent for recording indicator

- [ ] **Step 2: Update simulator components**

InterviewRoom: dark interface, orange accents for scores
ScoreCard: progress rings with #F97316
TranscriptPanel: clean text on black, speaker labels in white/40

- [ ] **Step 3: Update lesson components**

LessonPlayer: progress bar orange, step indicators, bg colors
ResultScreen: stars in #FBBF24, XP in orange, clean dark bg

- [ ] **Step 4: Update roadmap components**

RoadmapNode: completed=#4ADE80, current=#F97316, locked=white/10
RoadmapCanvas: connection lines white/6
NodePanel: slide-up drawer bg-[#111111]

- [ ] **Step 5: Verify full build**

Run: `npx tsc --noEmit && npx vite build`

- [ ] **Step 6: Commit**

```
git add src/components/chat/ src/components/simulator/ src/components/lesson/ src/components/roadmap/
git commit -m "feat: redesign chat, simulator, lesson, and roadmap components"
```

---

### Task 10: Direction Colors & Constants

**Files:**
- Modify: `src/lib/constants.ts`

- [ ] **Step 1: Update direction color palette**

```ts
frontend:  { primary: '#F97316', secondary: '#FB923C' }
english:   { primary: '#4ADE80', secondary: '#34D399' }
callcenter:{ primary: '#FBBF24', secondary: '#F59E0B' }
cib:       { primary: '#3B82F6', secondary: '#60A5FA' }
```

- [ ] **Step 2: Commit**

```
git add src/lib/constants.ts
git commit -m "feat: update direction color constants"
```

---

### Task 11: Final Verification

- [ ] **Step 1: Full TypeScript check**

Run: `npx tsc --noEmit`

- [ ] **Step 2: Full production build**

Run: `npx vite build`

- [ ] **Step 3: Visual smoke test**

Open http://localhost:5175 and navigate through:
- Login page
- Dashboard
- Courses catalog
- Course detail
- Course editor
- Profile
- Achievements

Verify no purple/cyan colors remain, all pages use black + orange.
