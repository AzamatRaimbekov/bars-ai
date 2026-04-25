# Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a one-page marketing landing at `/` for unauthenticated users with 7 scroll sections that funnel visitors to free registration.

**Architecture:** New `Landing.tsx` page composed of 7 section components in `src/components/landing/`. Route `/` shows Landing for guests, Onboarding for authenticated users without onboarding, Dashboard redirect for onboarded users. Each section uses Framer Motion `whileInView` for scroll-triggered animations.

**Tech Stack:** React 19, React Router 7, Tailwind CSS 4, Framer Motion 12, Lucide React icons, existing Button/Input UI components.

---

## File Structure

| Action | Path | Responsibility |
|--------|------|---------------|
| Create | `src/pages/Landing.tsx` | Page shell: nav + 7 sections + smooth scroll |
| Create | `src/components/landing/LandingNav.tsx` | Fixed top navigation with anchor links |
| Create | `src/components/landing/HeroSection.tsx` | Hero: headline, subtitle, CTA, floating badges |
| Create | `src/components/landing/FeaturesSection.tsx` | 2×2 grid of feature cards |
| Create | `src/components/landing/HowItWorksSection.tsx` | 3-step vertical list |
| Create | `src/components/landing/SprintsSection.tsx` | Sprint mockup with prizes |
| Create | `src/components/landing/CreateCoursesSection.tsx` | Author CTA with 3 benefit rows |
| Create | `src/components/landing/FAQSection.tsx` | Accordion-style FAQ |
| Create | `src/components/landing/FinalCTASection.tsx` | Closing CTA block |
| Modify | `src/App.tsx:28-75` | Route `/` logic: guest→Landing, auth→Onboarding/Dashboard |

---

### Task 1: Route `/` to Landing for Guests

**Files:**
- Create: `src/pages/Landing.tsx`
- Modify: `src/App.tsx:28-75`

- [ ] **Step 1: Create a minimal Landing page placeholder**

```tsx
// src/pages/Landing.tsx
import { Link } from 'react-router-dom'

export default function Landing() {
  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-extrabold mb-4">
          Bars<span className="text-[#F97316]"> AI</span>
        </h1>
        <p className="text-white/40 mb-6">Landing page coming soon</p>
        <Link
          to="/register"
          className="inline-block bg-[#F97316] text-black font-bold px-6 py-3 rounded-xl"
        >
          Начать бесплатно
        </Link>
      </div>
    </div>
  )
}
```

- [ ] **Step 2: Update App.tsx routing — add LandingOrOnboarding wrapper**

Replace the current `/` route (lines 68-75) and AuthGuard logic. The full updated `App.tsx`:

```tsx
// Add import at top of App.tsx (line 5 area)
import Landing from '@/pages/Landing'

// Replace the AuthGuard component (lines 28-52) with:
function AuthGuard({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading, user } = useAuthStore()
  const location = useLocation()

  if (isLoading) {
    return <LoadingScreen />
  }

  if (!isAuthenticated) return <Navigate to="/login" replace />

  const onboardingComplete = !!user?.onboarding_complete

  if (!onboardingComplete && location.pathname !== '/onboarding') {
    return <Navigate to="/onboarding" replace />
  }

  if (onboardingComplete && location.pathname === '/onboarding') {
    return <Navigate to="/dashboard" replace />
  }

  return <>{children}</>
}

// New component to handle `/` route:
function RootRoute() {
  const { isAuthenticated, isLoading, user } = useAuthStore()

  if (isLoading) {
    return <LoadingScreen />
  }

  if (!isAuthenticated) {
    return <Landing />
  }

  if (!user?.onboarding_complete) {
    return <Navigate to="/onboarding" replace />
  }

  return <Navigate to="/dashboard" replace />
}
```

Then update routes inside `<Routes>`:
- Change the `/` route from `<AuthGuard><Onboarding /></AuthGuard>` to `<RootRoute />`
- Add new route: `<Route path="/onboarding" element={<AuthGuard><Onboarding /></AuthGuard>} />`
- Update AuthGuard onboarding checks to reference `/onboarding` instead of `/`

- [ ] **Step 3: Verify routing works**

Run: `npm run dev`

Test manually:
- Open `/` in incognito → should show Landing placeholder
- Login → should redirect to `/dashboard` (if onboarding complete) or `/onboarding`
- Visiting `/` when logged in → should redirect appropriately

- [ ] **Step 4: Commit**

```bash
git add src/pages/Landing.tsx src/App.tsx
git commit -m "feat: add landing page route for unauthenticated users"
```

---

### Task 2: LandingNav — Fixed Top Navigation

**Files:**
- Create: `src/components/landing/LandingNav.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create LandingNav component**

```tsx
// src/components/landing/LandingNav.tsx
import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

const navLinks = [
  { label: 'Фичи', href: '#features' },
  { label: 'Спринты', href: '#sprints' },
  { label: 'Авторам', href: '#create' },
  { label: 'FAQ', href: '#faq' },
]

export function LandingNav() {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const scrollTo = (href: string) => {
    const el = document.querySelector(href)
    el?.scrollIntoView({ behavior: 'smooth' })
  }

  return (
    <motion.nav
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled
          ? 'bg-black/80 backdrop-blur-xl border-b border-white/6'
          : 'bg-transparent'
      }`}
    >
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        {/* Logo */}
        <Link to="/" className="text-xl font-bold text-white">
          Bars<span className="text-[#F97316]"> AI</span>
        </Link>

        {/* Center links — hidden on mobile */}
        <div className="hidden md:flex items-center gap-6">
          {navLinks.map((link) => (
            <button
              key={link.href}
              onClick={() => scrollTo(link.href)}
              className="text-sm text-white/50 hover:text-white transition-colors"
            >
              {link.label}
            </button>
          ))}
        </div>

        {/* Right side */}
        <div className="flex items-center gap-3">
          <Link
            to="/login"
            className="text-sm text-white/60 hover:text-white transition-colors"
          >
            Войти
          </Link>
          <Link
            to="/register"
            className="text-sm font-semibold text-black bg-[#F97316] hover:bg-[#FB923C] px-4 py-2 rounded-xl transition-colors"
          >
            Начать бесплатно
          </Link>
        </div>
      </div>
    </motion.nav>
  )
}
```

- [ ] **Step 2: Update Landing.tsx to use LandingNav**

```tsx
// src/pages/Landing.tsx
import { LandingNav } from '@/components/landing/LandingNav'

export default function Landing() {
  return (
    <div className="min-h-screen bg-black">
      <LandingNav />
      <main>
        {/* Sections will be added in subsequent tasks */}
        <div className="pt-16 flex items-center justify-center min-h-screen text-white">
          <p className="text-white/40">Sections coming next...</p>
        </div>
      </main>
    </div>
  )
}
```

- [ ] **Step 3: Verify nav renders and scroll behavior works**

Run: `npm run dev`
- Open `/` → nav bar should appear at top
- Scroll down → nav should gain blur background
- "Войти" → navigates to `/login`
- "Начать бесплатно" → navigates to `/register`

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/LandingNav.tsx src/pages/Landing.tsx
git commit -m "feat: add landing page navigation bar"
```

---

### Task 3: HeroSection

**Files:**
- Create: `src/components/landing/HeroSection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create HeroSection component**

```tsx
// src/components/landing/HeroSection.tsx
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

const floatingBadges = [
  { text: '+250 XP', delay: 0 },
  { text: 'Level 5', delay: 0.1 },
  { text: '7 streak', delay: 0.2 },
]

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center px-4 pt-16 overflow-hidden">
      {/* Background glow */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 800,
          height: 800,
          background: 'radial-gradient(circle, rgba(249,115,22,0.08), transparent 70%)',
          top: '-10%',
          right: '-10%',
        }}
      />

      <div className="relative z-10 text-center max-w-2xl mx-auto">
        {/* Subtitle badge */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-xs uppercase tracking-[3px] text-[#F97316] font-semibold mb-6"
        >
          Bars AI Platform
        </motion.div>

        {/* Main headline */}
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="text-5xl md:text-7xl font-extrabold text-white leading-[1.1] mb-5"
        >
          Учись. Играй.
          <br />
          <span className="text-[#F97316]">Побеждай.</span>
        </motion.h1>

        {/* Subtitle */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="text-lg text-white/45 mb-8 max-w-md mx-auto"
        >
          AI-ментор, интерактивные курсы и геймификация — всё в одном месте
        </motion.p>

        {/* CTA button */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          <Link
            to="/register"
            className="inline-block text-lg font-bold text-black px-8 py-4 rounded-2xl transition-all hover:scale-105"
            style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
          >
            Начать бесплатно
          </Link>
        </motion.div>

        {/* Floating badges */}
        <div className="flex justify-center gap-3 mt-8">
          {floatingBadges.map((badge) => (
            <motion.div
              key={badge.text}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5 + badge.delay }}
              className="bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-2 text-xs text-white/50"
            >
              {badge.text}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

- [ ] **Step 2: Add HeroSection to Landing.tsx**

```tsx
// src/pages/Landing.tsx
import { LandingNav } from '@/components/landing/LandingNav'
import { HeroSection } from '@/components/landing/HeroSection'

export default function Landing() {
  return (
    <div className="min-h-screen bg-black">
      <LandingNav />
      <main>
        <HeroSection />
      </main>
    </div>
  )
}
```

- [ ] **Step 3: Verify hero renders correctly**

Run: `npm run dev`
- Open `/` → should show hero with animated headline, subtitle, CTA button, floating badges
- CTA button → navigates to `/register`
- Background glow visible in top-right

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/HeroSection.tsx src/pages/Landing.tsx
git commit -m "feat: add hero section to landing page"
```

---

### Task 4: FeaturesSection

**Files:**
- Create: `src/components/landing/FeaturesSection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create FeaturesSection component**

```tsx
// src/components/landing/FeaturesSection.tsx
import { motion } from 'framer-motion'
import { Bot, Code, Trophy, BookOpen } from 'lucide-react'

const features = [
  {
    icon: Bot,
    title: 'AI-ментор',
    description: 'Персональный помощник 24/7',
  },
  {
    icon: Code,
    title: 'Python в браузере',
    description: 'Пиши код без установки',
  },
  {
    icon: Trophy,
    title: 'Геймификация',
    description: 'XP, лиги, бейджи, стрики',
  },
  {
    icon: BookOpen,
    title: '44+ курсов',
    description: 'AI-рекомендации под тебя',
  },
]

export function FeaturesSection() {
  return (
    <section id="features" className="py-24 px-4">
      <div className="max-w-4xl mx-auto">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-3xl font-bold text-white text-center mb-12"
        >
          Почему Bars AI?
        </motion.h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {features.map((feature, i) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className="bg-white/[0.03] border border-white/[0.06] rounded-2xl p-6 text-center"
            >
              <div className="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#F97316]/10 mb-4">
                <feature.icon className="w-6 h-6 text-[#F97316]" />
              </div>
              <h3 className="text-base font-semibold text-white mb-1">{feature.title}</h3>
              <p className="text-sm text-white/40">{feature.description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

- [ ] **Step 2: Add FeaturesSection to Landing.tsx**

Add import and place after `<HeroSection />`:

```tsx
import { FeaturesSection } from '@/components/landing/FeaturesSection'
// ... inside <main>:
<HeroSection />
<FeaturesSection />
```

- [ ] **Step 3: Verify**

Run: `npm run dev`
- Scroll down from hero → features section appears with staggered animation
- 2×2 grid on desktop, 1-column on mobile
- Anchor link "Фичи" in nav scrolls to this section

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/FeaturesSection.tsx src/pages/Landing.tsx
git commit -m "feat: add features section to landing page"
```

---

### Task 5: HowItWorksSection

**Files:**
- Create: `src/components/landing/HowItWorksSection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create HowItWorksSection component**

```tsx
// src/components/landing/HowItWorksSection.tsx
import { motion } from 'framer-motion'

const steps = [
  {
    number: '1',
    title: 'Зарегистрируйся бесплатно',
    description: 'Барсбек подберёт курсы по твоим интересам',
  },
  {
    number: '2',
    title: 'Проходи курсы и набирай XP',
    description: 'Интерактивные уроки, код в браузере, AI-помощник',
  },
  {
    number: '3',
    title: 'Соревнуйся и зарабатывай',
    description: 'Лиги, спринты с призами, рейтинги',
  },
]

export function HowItWorksSection() {
  return (
    <section className="py-24 px-4">
      <div className="max-w-2xl mx-auto">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-3xl font-bold text-white text-center mb-12"
        >
          Как это работает
        </motion.h2>

        <div className="flex flex-col gap-6">
          {steps.map((step, i) => (
            <motion.div
              key={step.number}
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.15 }}
              className="flex items-start gap-4"
            >
              <div className="w-10 h-10 min-w-10 rounded-xl bg-[#F97316]/15 border border-[#F97316]/30 flex items-center justify-center text-[#F97316] font-extrabold text-base">
                {step.number}
              </div>
              <div>
                <h3 className="text-base font-semibold text-white">{step.title}</h3>
                <p className="text-sm text-white/40 mt-1">{step.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

- [ ] **Step 2: Add HowItWorksSection to Landing.tsx**

Add import and place after `<FeaturesSection />`:

```tsx
import { HowItWorksSection } from '@/components/landing/HowItWorksSection'
// ... inside <main>:
<FeaturesSection />
<HowItWorksSection />
```

- [ ] **Step 3: Verify**

Run: `npm run dev`
- Scroll → 3 steps appear with slide-in animation
- Numbers in orange boxes, text aligned right of numbers

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/HowItWorksSection.tsx src/pages/Landing.tsx
git commit -m "feat: add how-it-works section to landing page"
```

---

### Task 6: SprintsSection

**Files:**
- Create: `src/components/landing/SprintsSection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create SprintsSection component**

```tsx
// src/components/landing/SprintsSection.tsx
import { motion } from 'framer-motion'
import { Star } from 'lucide-react'

const prizes = [
  { place: '1st', amount: '50 000 ₸', highlight: true },
  { place: '2nd', amount: '30 000 ₸', highlight: false },
  { place: '3rd', amount: '15 000 ₸', highlight: false },
]

export function SprintsSection() {
  return (
    <section id="sprints" className="py-24 px-4 relative overflow-hidden">
      {/* Yellow glow */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 500,
          height: 500,
          background: 'radial-gradient(circle, rgba(251,191,36,0.08), transparent 70%)',
          bottom: '-10%',
          right: '-5%',
        }}
      />

      <div className="max-w-2xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-10"
        >
          <h2 className="text-3xl font-bold text-white mb-3">
            Спринты — учись и зарабатывай
          </h2>
          <p className="text-white/45">Регулярные соревнования с реальными призами</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: 0.15 }}
          className="bg-white/[0.03] border border-white/[0.06] rounded-2xl p-6"
        >
          {/* Sprint header */}
          <div className="flex items-center justify-between mb-5">
            <span className="text-base font-semibold text-white">Весенний спринт</span>
            <span className="text-sm text-[#FBBF24] font-semibold">3 дня осталось</span>
          </div>

          {/* Prize cards */}
          <div className="grid grid-cols-3 gap-3 mb-5">
            {prizes.map((prize) => (
              <div
                key={prize.place}
                className={`text-center rounded-xl p-4 border ${
                  prize.highlight
                    ? 'bg-[#FBBF24]/10 border-[#FBBF24]/20'
                    : 'bg-white/[0.03] border-white/[0.06]'
                }`}
              >
                <Star className={`w-5 h-5 mx-auto mb-2 ${prize.highlight ? 'text-[#FBBF24]' : 'text-white/30'}`} />
                <div className={`text-lg font-extrabold ${prize.highlight ? 'text-[#FBBF24]' : 'text-white/50'}`}>
                  {prize.place}
                </div>
                <div className="text-xs text-white/40 mt-1">{prize.amount}</div>
              </div>
            ))}
          </div>

          {/* Explanation */}
          <p className="text-xs text-white/35 text-center">
            Набирай звёзды за выполнение уроков → поднимайся в рейтинге → забирай приз
          </p>
        </motion.div>
      </div>
    </section>
  )
}
```

- [ ] **Step 2: Add SprintsSection to Landing.tsx**

Add import and place after `<HowItWorksSection />`:

```tsx
import { SprintsSection } from '@/components/landing/SprintsSection'
// ... inside <main>:
<HowItWorksSection />
<SprintsSection />
```

- [ ] **Step 3: Verify**

Run: `npm run dev`
- Scroll → sprints section with prize cards
- Yellow glow in background
- Nav anchor "Спринты" scrolls here

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/SprintsSection.tsx src/pages/Landing.tsx
git commit -m "feat: add sprints section to landing page"
```

---

### Task 7: CreateCoursesSection

**Files:**
- Create: `src/components/landing/CreateCoursesSection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create CreateCoursesSection component**

```tsx
// src/components/landing/CreateCoursesSection.tsx
import { motion } from 'framer-motion'
import { PenLine, Bot, DollarSign } from 'lucide-react'

const benefits = [
  {
    icon: PenLine,
    title: 'Удобный редактор',
    description: 'Создавай уроки с видео, кодом и квизами',
    accent: false,
  },
  {
    icon: Bot,
    title: 'AI генерирует за тебя',
    description: 'Опиши тему — AI создаст структуру курса',
    accent: false,
  },
  {
    icon: DollarSign,
    title: 'Зарабатывай',
    description: 'Устанавливай цену и получай доход',
    accent: true,
  },
]

export function CreateCoursesSection() {
  return (
    <section id="create" className="py-24 px-4 relative overflow-hidden">
      {/* Green glow */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 400,
          height: 400,
          background: 'radial-gradient(circle, rgba(74,222,128,0.06), transparent 70%)',
          top: '-5%',
          left: '-5%',
        }}
      />

      <div className="max-w-2xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-10"
        >
          <h2 className="text-3xl font-bold text-white mb-3">
            Создавай курсы. Зарабатывай.
          </h2>
          <p className="text-white/45">Стань автором и получай доход с каждого ученика</p>
        </motion.div>

        <div className="flex flex-col gap-3">
          {benefits.map((item, i) => (
            <motion.div
              key={item.title}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className={`flex items-center gap-4 rounded-2xl p-4 border ${
                item.accent
                  ? 'bg-[#4ADE80]/[0.06] border-[#4ADE80]/15'
                  : 'bg-white/[0.03] border-white/[0.06]'
              }`}
            >
              <div
                className={`w-10 h-10 min-w-10 rounded-xl flex items-center justify-center ${
                  item.accent ? 'bg-[#4ADE80]/15' : 'bg-white/[0.06]'
                }`}
              >
                <item.icon className={`w-5 h-5 ${item.accent ? 'text-[#4ADE80]' : 'text-white/50'}`} />
              </div>
              <div>
                <h3 className={`text-sm font-semibold ${item.accent ? 'text-[#4ADE80]' : 'text-white'}`}>
                  {item.title}
                </h3>
                <p className="text-xs text-white/40 mt-0.5">{item.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

- [ ] **Step 2: Add CreateCoursesSection to Landing.tsx**

Add import and place after `<SprintsSection />`:

```tsx
import { CreateCoursesSection } from '@/components/landing/CreateCoursesSection'
// ... inside <main>:
<SprintsSection />
<CreateCoursesSection />
```

- [ ] **Step 3: Verify**

Run: `npm run dev`
- Scroll → 3 benefit rows with green accent on "Зарабатывай"
- Nav anchor "Авторам" scrolls here

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/CreateCoursesSection.tsx src/pages/Landing.tsx
git commit -m "feat: add create-courses section to landing page"
```

---

### Task 8: FAQSection

**Files:**
- Create: `src/components/landing/FAQSection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create FAQSection component**

```tsx
// src/components/landing/FAQSection.tsx
import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronDown } from 'lucide-react'

const faqs = [
  {
    question: 'Это бесплатно?',
    answer: 'Да, регистрация и большинство курсов бесплатны.',
  },
  {
    question: 'Нужно устанавливать что-то?',
    answer: 'Нет, всё работает в браузере — включая Python.',
  },
  {
    question: 'Как заработать на спринтах?',
    answer: 'Проходи уроки, набирай звёзды, попади в топ рейтинга — забирай приз.',
  },
]

function FAQItem({ question, answer }: { question: string; answer: string }) {
  const [open, setOpen] = useState(false)

  return (
    <button
      onClick={() => setOpen(!open)}
      className="w-full text-left bg-white/[0.03] border border-white/[0.06] rounded-2xl p-5 transition-colors hover:border-white/10"
    >
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-white">{question}</span>
        <ChevronDown
          className={`w-4 h-4 text-white/30 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
        />
      </div>
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <p className="text-sm text-white/40 mt-3">{answer}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </button>
  )
}

export function FAQSection() {
  return (
    <section id="faq" className="py-24 px-4">
      <div className="max-w-2xl mx-auto">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-3xl font-bold text-white text-center mb-12"
        >
          Частые вопросы
        </motion.h2>

        <div className="flex flex-col gap-3">
          {faqs.map((faq, i) => (
            <motion.div
              key={faq.question}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
            >
              <FAQItem {...faq} />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
```

- [ ] **Step 2: Add FAQSection to Landing.tsx**

Add import and place after `<CreateCoursesSection />`:

```tsx
import { FAQSection } from '@/components/landing/FAQSection'
// ... inside <main>:
<CreateCoursesSection />
<FAQSection />
```

- [ ] **Step 3: Verify**

Run: `npm run dev`
- Scroll → FAQ section with 3 expandable items
- Click question → smoothly expands answer with chevron rotation
- Nav anchor "FAQ" scrolls here

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/FAQSection.tsx src/pages/Landing.tsx
git commit -m "feat: add FAQ section to landing page"
```

---

### Task 9: FinalCTASection

**Files:**
- Create: `src/components/landing/FinalCTASection.tsx`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Create FinalCTASection component**

```tsx
// src/components/landing/FinalCTASection.tsx
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

export function FinalCTASection() {
  return (
    <section className="py-24 px-4 relative overflow-hidden">
      {/* Orange glow */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 600,
          height: 600,
          background: 'radial-gradient(circle, rgba(249,115,22,0.08), transparent 60%)',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        className="max-w-xl mx-auto text-center relative z-10 border border-[#F97316]/20 rounded-2xl py-16 px-6"
      >
        <h2 className="text-3xl font-extrabold text-white mb-4">Готов начать?</h2>
        <p className="text-base text-white/45 mb-8">Присоединяйся — это бесплатно</p>
        <Link
          to="/register"
          className="inline-block text-lg font-bold text-black px-10 py-4 rounded-2xl transition-all hover:scale-105"
          style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
        >
          Создать аккаунт
        </Link>
      </motion.div>
    </section>
  )
}
```

- [ ] **Step 2: Update Landing.tsx — add FinalCTASection and finalize page**

Final version of Landing.tsx:

```tsx
// src/pages/Landing.tsx
import { LandingNav } from '@/components/landing/LandingNav'
import { HeroSection } from '@/components/landing/HeroSection'
import { FeaturesSection } from '@/components/landing/FeaturesSection'
import { HowItWorksSection } from '@/components/landing/HowItWorksSection'
import { SprintsSection } from '@/components/landing/SprintsSection'
import { CreateCoursesSection } from '@/components/landing/CreateCoursesSection'
import { FAQSection } from '@/components/landing/FAQSection'
import { FinalCTASection } from '@/components/landing/FinalCTASection'

export default function Landing() {
  return (
    <div className="min-h-screen bg-black">
      <LandingNav />
      <main>
        <HeroSection />
        <FeaturesSection />
        <HowItWorksSection />
        <SprintsSection />
        <CreateCoursesSection />
        <FAQSection />
        <FinalCTASection />
      </main>
    </div>
  )
}
```

- [ ] **Step 3: Verify full landing page end-to-end**

Run: `npm run dev`
- Full scroll through all 7 sections
- All animations trigger on scroll
- All anchor links work
- Both CTA buttons → `/register`
- "Войти" → `/login`
- Mobile responsive: stack to single column
- Authenticated user visiting `/` → redirects to dashboard

- [ ] **Step 4: Commit**

```bash
git add src/components/landing/FinalCTASection.tsx src/pages/Landing.tsx
git commit -m "feat: add final CTA section, complete landing page"
```

---

### Task 10: SEO Meta Tags and Semantic Markup

**Files:**
- Modify: `index.html`
- Modify: `src/pages/Landing.tsx`

- [ ] **Step 1: Update index.html with meta tags**

Add/update the following inside `<head>` in `index.html`:

```html
<title>Bars AI — Учись. Играй. Побеждай.</title>
<meta name="description" content="AI-ментор, интерактивные курсы и геймификация — всё в одном месте. Бесплатная регистрация." />
<meta property="og:title" content="Bars AI — Учись. Играй. Побеждай." />
<meta property="og:description" content="AI-ментор, интерактивные курсы и геймификация. 44+ курсов, Python в браузере, спринты с призами." />
<meta property="og:type" content="website" />
```

- [ ] **Step 2: Add semantic HTML to Landing.tsx sections**

Ensure Landing.tsx uses semantic elements (already done — `<main>`, `<section>` with ids). Add `<footer>` after FinalCTASection:

```tsx
// At the bottom of Landing.tsx, after </main>:
<footer className="py-8 px-4 border-t border-white/[0.06]">
  <div className="max-w-6xl mx-auto text-center text-xs text-white/25">
    © 2026 Bars AI. Все права защищены.
  </div>
</footer>
```

- [ ] **Step 3: Verify**

Run: `npm run dev`
- Check page title in browser tab
- View page source → meta tags present
- Footer visible at bottom

- [ ] **Step 4: Commit**

```bash
git add index.html src/pages/Landing.tsx
git commit -m "feat: add SEO meta tags and footer to landing page"
```

---

### Task 11: Update Documentation

**Files:**
- Modify: `docs/фронтенд/Роутинг.md`

- [ ] **Step 1: Update routing documentation**

Add the landing page to the routing docs. Open `docs/фронтенд/Роутинг.md` and add an entry for:

- `/` — Landing page (unauthenticated) / redirect to dashboard (authenticated)
- `/onboarding` — Onboarding (moved from `/`)

Note the new `RootRoute` component that handles the conditional rendering.

- [ ] **Step 2: Commit**

```bash
git add docs/
git commit -m "docs: update routing docs for landing page"
```
