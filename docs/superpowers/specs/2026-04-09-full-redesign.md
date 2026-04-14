># PathMind Full Redesign Spec

**Date:** 2026-04-09
**Style:** Black + Warm Orange (Apple/Stripe inspired)
**Scope:** All pages, all UI components, layout system

---

## 1. Design Tokens

### Colors

```
--bg:              #000000
--surface:         #0A0A0A
--surface-elevated:#111111
--border:          rgba(255,255,255,0.06)
--border-hover:    rgba(255,255,255,0.12)
--primary:         #F97316
--primary-light:   #FB923C
--primary-bg:      rgba(249,115,22,0.1)
--primary-border:  rgba(249,115,22,0.2)
--success:         #4ADE80
--success-bg:      rgba(74,222,128,0.1)
--error:           #F87171
--error-bg:        rgba(248,113,113,0.1)
--warning:         #FBBF24
--warning-bg:      rgba(251,191,36,0.1)
--text:            #FAFAFA
--text-secondary:  rgba(255,255,255,0.4)
--text-muted:      rgba(255,255,255,0.25)
```

### Typography
- Font: Inter (unchanged)
- Mono: JetBrains Mono (unchanged)
- Headings: font-weight 700, letter-spacing -0.5px, color #FAFAFA
- Body: font-weight 400, color rgba(255,255,255,0.4)
- Sizes: text-2xl for page titles, text-sm for body, text-xs for meta

### Radii & Spacing
- Cards: rounded-2xl (16px)
- Buttons: rounded-xl (12px)
- Inputs: rounded-xl (12px)
- Chips/badges: rounded-full
- Card padding: p-5 (20px)
- Section gaps: space-y-4 to space-y-6

### Effects
- No box-shadows — use border only
- Primary elements get subtle radial glow: `radial-gradient(circle, rgba(249,115,22,0.08), transparent 70%)`
- Hover: border color transitions to --border-hover
- Active/focus: border transitions to --primary-border

---

## 2. UI Components (src/components/ui/)

### Button.tsx
- **Primary:** bg-[#F97316] text-white rounded-xl, hover:bg-[#EA580C]
- **Secondary:** bg-transparent border border-white/6 text-white/40 rounded-xl, hover:border-white/12 hover:text-white
- **Ghost:** bg-transparent text-white/40, hover:bg-white/4 hover:text-white
- Remove shadow/glow from primary variant
- Keep framer-motion scale animations

### Card.tsx
- bg-[#0A0A0A] border border-white/6 rounded-2xl
- Remove backdrop-blur (not needed on solid black bg)
- Hover: border-white/12 transition
- Remove glow prop (no glows in new design)

### Input.tsx
- bg-transparent border border-white/6 rounded-xl
- Focus: border-[#F97316]/30
- Placeholder: text-white/25
- Label: text-xs text-white/40 uppercase tracking-wider

### ProgressBar.tsx
- Track: bg-white/4 rounded-full h-1.5 (thinner)
- Fill: bg-gradient-to-r from-[#F97316] to-[#FB923C]
- Remove glow effect

### Modal.tsx
- Backdrop: bg-black/80 (darker)
- Content: bg-[#111111] border border-white/6 rounded-2xl
- Remove backdrop-blur

### Chip.tsx
- Active: bg-[#F97316]/10 border-[#F97316]/20 text-[#FB923C]
- Inactive: bg-white/4 border-white/6 text-white/40

### Badge.tsx
- Keep rarity color system but adapt to new palette
- Use orange glow for legendary instead of yellow

### ProgressRing.tsx
- Stroke color: #F97316
- Track: rgba(255,255,255,0.04)

---

## 3. Layout Components

### Sidebar.tsx (desktop, w-64)
- bg-[#0A0A0A] border-r border-white/6
- Remove backdrop-blur
- Logo: "PathMind" — white text, no split colors
- Nav items: text-white/40, hover:text-white hover:bg-white/4 rounded-xl
- Active item: text-[#FB923C] bg-[#F97316]/8
- Active indicator: 2px left bar bg-[#F97316] rounded-full
- Footer: version text in text-white/20

### TopBar.tsx
- bg-[#0A0A0A]/80 backdrop-blur-xl border-b border-white/6
- Greeting: text-white/40 text-sm
- Stats (XP, streak): compact pills with bg-white/4

### TabBar.tsx (mobile bottom)
- bg-[#0A0A0A]/90 backdrop-blur-xl border-t border-white/6
- Remove gradient background, floating capsule shape → simpler flat bar
- Icons: text-white/30 inactive, text-[#FB923C] active
- Active dot indicator: 4px circle bg-[#F97316] below icon
- No background fill on active tab

### PageWrapper.tsx
- bg-[#000000] min-h-screen
- Content max-width stays as is
- Padding: keep current responsive padding

---

## 4. Pages Redesign

### Dashboard.tsx
- Welcome section: large greeting, today's stats in horizontal row
- Stats: XP, Streak, Level — clean pills with bg-[#0A0A0A] border
- Active course card: prominent, shows progress bar
- Daily quests section
- Remove mascot images (cleaner look)

### Login.tsx / Register.tsx
- Centered card on pure black bg
- Subtle orange radial glow behind card
- Minimal form: email, password, submit
- Brand name at top in large font

### Courses.tsx (catalog)
- Search bar: bg-[#0A0A0A] border border-white/6
- Category pills: rounded-full, active = orange
- Course cards: gradient thumbnails kept, info below
- Remove price badge styling — just text

### CourseDetail.tsx
- Hero: large title, stats row, no background gradient
- Curriculum: clean expandable sections with thin borders
- Reviews: minimal cards
- CTA bar: sticky bottom, bg-[#0A0A0A]/90 backdrop-blur

### CourseEditor.tsx
- Tab bar: bg-[#0A0A0A] border, active tab underline orange
- Forms: clean inputs on black bg
- Toast: top-center, bg-[#111111] border

### CourseLearn / StepPlayer
- Full-screen black bg
- Step content in centered card (max-w-lg)
- Progress bar at very top (thin orange line)
- Clean navigation buttons at bottom

### Roadmap.tsx
- Keep snake-pattern layout
- Node colors: completed=#4ADE80, current=#F97316, locked=white/10
- Connection lines: white/6
- Section headers: text-xs uppercase tracking-wider text-white/30

### CourseRoadmap.tsx
- Same approach as Roadmap
- Drawer: slide from bottom, bg-[#111111]

### Profile.tsx
- Avatar area: large initials circle with orange border
- Stats grid: clean bordered cards
- Settings sections: simple list with borders

### Mentor.tsx (AI Chat)
- Messages: user = bg-[#0A0A0A], bot = bg-transparent
- Input: bottom fixed, bg-[#0A0A0A] border
- Remove heavy backgrounds

### Simulator.tsx (Interview)
- Clean dark interface
- Score indicators: orange accent
- Transcript: clean text on black

### Achievements.tsx
- Grid of badge cards
- Locked: grayscale + opacity
- Unlocked: subtle orange border for legendary

### Leaderboard.tsx
- Table/list with alternating bg-[#0A0A0A] rows
- Top 3: orange accent numbers
- Current user row: highlighted with orange left border

### Teach.tsx
- Course cards with gradient thumbnails
- Draft/Published badge
- Clean grid layout

### Onboarding.tsx
- Step-by-step on black bg
- Progress dots at bottom
- Orange primary buttons

---

## 5. Gamification Components

### XPBar.tsx
- Thin progress bar, #F97316 fill
- Text: current/next level in text-white/40

### StreakCounter.tsx
- Fire emoji + count
- bg-[#F97316]/8 text-[#FB923C] rounded-full pill

### LevelUpModal.tsx
- Clean centered modal on black backdrop
- Level name in large text
- Orange confetti/particles (optional)
- Remove mascot image

### BadgeReveal.tsx
- Centered modal
- Badge icon large, name below
- Rarity-colored border ring
- Remove mascot

### DailyQuests.tsx
- Checklist style
- Progress: orange fill
- Reward pill: bg-[#F97316]/10 text-[#FB923C]

---

## 6. Global CSS Changes (src/index.css)

- Change @theme color values to new palette
- bg: #000000
- surface: #0A0A0A
- border: rgba(255,255,255,0.06)
- primary: #F97316
- accent: #FB923C (was cyan, now orange light)
- success: #4ADE80
- warning: #FBBF24
- text: #FAFAFA
- text-secondary: rgba(255,255,255,0.4)
- Scrollbar: thumb rgba(255,255,255,0.08), track transparent
- Remove fractal noise overlay

---

## 7. What NOT to Change

- React Router structure
- API layer (courseApi, api.ts)
- State management (Zustand stores)
- Data files (lessons, roadmaps, achievements)
- Backend (no changes)
- Core business logic in components
- Framer Motion animation patterns (keep, just update colors)
- Icon library (Lucide — keep)
- Font families (Inter + JetBrains Mono — keep)
