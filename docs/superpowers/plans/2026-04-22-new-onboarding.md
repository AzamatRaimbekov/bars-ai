# New Onboarding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the old direction-based onboarding with a 4-step hybrid wizard that recommends real courses from the DB based on user-selected interest tags, guided by the Barsbek mascot.

**Architecture:** Add `tags` JSON field to Course model, add `interests`/`onboarding_complete` fields to User model. Two new API endpoints for tags and tag-filtered courses. Complete rewrite of `Onboarding.tsx` into a 4-step wizard with mascot speech bubbles. Onboarding guard in `App.tsx` switches from `direction` check to `onboarding_complete` flag.

**Tech Stack:** FastAPI, SQLAlchemy, Alembic (backend); React, Framer Motion, Zustand (frontend)

**Spec:** `docs/superpowers/specs/2026-04-22-new-onboarding-design.md`

---

### Task 1: Add `tags` field to Course model + migration

**Files:**
- Modify: `backend/app/models/course.py:11-34`
- Modify: `backend/app/schemas/courses.py:10-31`

- [ ] **Step 1: Add `tags` field to Course model**

In `backend/app/models/course.py`, add after line 20 (`category` field):

```python
    tags: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
```

- [ ] **Step 2: Add `tags` to course schemas**

In `backend/app/schemas/courses.py`, add `tags` to `CreateCourseRequest`:

```python
class CreateCourseRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=5000)
    category: str = Field(default="other", max_length=50)
    tags: list[str] = Field(default_factory=list)
    difficulty: str = Field(default="beginner", max_length=20)
    price: int = Field(default=0, ge=0)
    currency: str = Field(default="USD", max_length=3)
    thumbnail_url: str | None = None
```

Add `tags` to `UpdateCourseRequest`:

```python
    tags: list[str] | None = None
```

- [ ] **Step 3: Generate and run Alembic migration**

Run:
```bash
cd backend
alembic revision --autogenerate -m "add tags to courses"
alembic upgrade head
```

- [ ] **Step 4: Commit**

```bash
git add backend/app/models/course.py backend/app/schemas/courses.py backend/alembic/versions/
git commit -m "feat: add tags JSON field to Course model"
```

---

### Task 2: Add `interests`, `onboarding_complete`, `assessment_context` to User model + migration

**Files:**
- Modify: `backend/app/models/user.py:11-29`
- Modify: `backend/app/schemas/user.py`
- Modify: `backend/app/schemas/auth.py`
- Modify: `backend/app/services/user_service.py`
- Modify: `backend/app/services/auth_service.py`
- Modify: `backend/app/routers/users.py`

- [ ] **Step 1: Add new fields to User model**

In `backend/app/models/user.py`, add after the `role` field (line 22):

```python
    interests: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    onboarding_complete: Mapped[bool] = mapped_column(default=False)
    assessment_context: Mapped[str | None] = mapped_column(Text, nullable=True)
```

Add `Text` and `JSON` to the SQLAlchemy imports (line 4):

```python
from sqlalchemy import String, DateTime, func, JSON, Text, Boolean
```

- [ ] **Step 2: Update auth schema — remove direction requirement from RegisterRequest**

In `backend/app/schemas/auth.py`, replace the entire `RegisterRequest` with:

```python
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    name: str = Field(min_length=1, max_length=100)
    direction: str = Field(default="", max_length=20)
    assessment_level: str = Field(default="beginner", pattern=r"^(beginner|intermediate|advanced)$")
    language: str = Field(default="ru", pattern=r"^(ru|en)$")
```

Key change: `direction` is now optional with default `""` (no regex pattern), since new onboarding doesn't set direction at registration time.

- [ ] **Step 3: Update user schemas — add new fields to responses and update request**

In `backend/app/schemas/user.py`, update `UserResponse` to include new fields:

```python
class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    direction: str
    assessment_level: str
    language: str
    avatar_url: str | None
    interests: list[str] = []
    onboarding_complete: bool = False
    created_at: datetime

    model_config = {"from_attributes": True}
```

Update `UserUpdateRequest` to accept new fields:

```python
class UserUpdateRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    language: str | None = Field(None, pattern=r"^(ru|en)$")
    avatar_url: str | None = None
    interests: list[str] | None = None
    onboarding_complete: bool | None = None
    assessment_context: str | None = None
    direction: str | None = None
    assessment_level: str | None = None
```

- [ ] **Step 4: Update user_service.py — handle new fields in update_me**

Replace `update_me` function in `backend/app/services/user_service.py`:

```python
async def update_me(db: AsyncSession, user_id: uuid.UUID, body: dict) -> dict:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    allowed_fields = ["name", "language", "avatar_url", "interests", "onboarding_complete", "assessment_context", "direction", "assessment_level"]
    for field in allowed_fields:
        value = body.get(field)
        if value is not None:
            setattr(user, field, value)

    await db.commit()
    return await get_me(db, user_id)
```

Also update `get_me` to return new fields — add after `"avatar_url"`:

```python
        "interests": user.interests or [],
        "onboarding_complete": user.onboarding_complete,
```

- [ ] **Step 5: Update users router to pass body dict**

In `backend/app/routers/users.py`, update the `update_me` endpoint:

```python
@router.patch("/me", response_model=UserWithProgressResponse)
async def update_me(body: UserUpdateRequest, user_id: uuid.UUID = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)):
    return await user_service.update_me(db, user_id, body.model_dump(exclude_none=True))
```

- [ ] **Step 6: Update auth_service.py — make direction optional at registration**

In `backend/app/services/auth_service.py`, the `register` function already accepts `direction` param. No change needed since we default it to `""` in the schema.

- [ ] **Step 7: Generate and run Alembic migration**

Run:
```bash
cd backend
alembic revision --autogenerate -m "add interests onboarding_complete assessment_context to users"
alembic upgrade head
```

- [ ] **Step 8: Commit**

```bash
git add backend/app/models/user.py backend/app/schemas/ backend/app/services/user_service.py backend/app/routers/users.py backend/alembic/versions/
git commit -m "feat: add interests, onboarding_complete, assessment_context to User model"
```

---

### Task 3: Add tags and recommend API endpoints

**Files:**
- Modify: `backend/app/routers/courses.py`
- Modify: `backend/app/services/course_service.py`

- [ ] **Step 1: Add `get_tags` and `recommend_by_tags` to course_service.py**

Add at the end of `backend/app/services/course_service.py`:

```python
async def get_course_tags(db: AsyncSession) -> list[str]:
    """Return unique tags from all published courses."""
    result = await db.execute(
        select(Course.tags).where(Course.status == "published", Course.tags.isnot(None))
    )
    all_tags: set[str] = set()
    for (tags,) in result:
        if tags:
            all_tags.update(tags)
    return sorted(all_tags)


async def recommend_by_tags(db: AsyncSession, tags: list[str], limit: int = 20) -> list[dict]:
    """Return published courses that have at least one matching tag."""
    result = await db.execute(
        select(Course)
        .join(User, Course.author_id == User.id)
        .where(Course.status == "published")
        .order_by(Course.total_enrolled.desc())
        .limit(100)
    )
    courses = result.scalars().all()

    # Filter in Python since JSON array overlap varies by DB
    matched = []
    tag_set = set(t.lower() for t in tags)
    for course in courses:
        course_tags = set(t.lower() for t in (course.tags or []))
        if course_tags & tag_set:
            matched.append(course)
        if len(matched) >= limit:
            break

    return [
        {
            "id": c.id,
            "title": c.title,
            "slug": c.slug,
            "description": c.description,
            "thumbnail_url": c.thumbnail_url,
            "category": c.category,
            "tags": c.tags or [],
            "difficulty": c.difficulty,
            "price": c.price,
            "currency": c.currency,
            "total_enrolled": c.total_enrolled,
            "rating_avg": c.rating_avg,
            "rating_count": c.rating_count,
        }
        for c in matched
    ]
```

Make sure `User` is imported in course_service.py (it likely is already for author joins).

- [ ] **Step 2: Add endpoints to courses router**

In `backend/app/routers/courses.py`, add BEFORE the `/{course_id}` route (to avoid path conflicts):

```python
@router.get("/tags", response_model=list[str])
async def get_tags(db: AsyncSession = Depends(get_db)):
    return await course_service.get_course_tags(db)


@router.get("/recommend")
async def recommend(
    tags: str = Query(..., description="Comma-separated tags"),
    db: AsyncSession = Depends(get_db),
):
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    return await course_service.recommend_by_tags(db, tag_list)
```

Add `List` import: these endpoints must be placed BEFORE `@router.get("/{course_id}")` otherwise FastAPI will try to match "tags" and "recommend" as a UUID.

- [ ] **Step 3: Commit**

```bash
git add backend/app/routers/courses.py backend/app/services/course_service.py
git commit -m "feat: add /api/courses/tags and /api/courses/recommend endpoints"
```

---

### Task 4: Update frontend types and API

**Files:**
- Modify: `src/store/authStore.ts`
- Modify: `src/services/courseApi.ts`

- [ ] **Step 1: Update UserData interface in authStore.ts**

In `src/store/authStore.ts`, add to the `UserData` interface after `role`:

```typescript
  interests: string[]
  onboarding_complete: boolean
```

- [ ] **Step 2: Update updateUser type to accept new fields**

In `src/store/authStore.ts`, update the `updateUser` type in `AuthState`:

```typescript
  updateUser: (data: Partial<Pick<UserData, 'name' | 'language' | 'avatar_url' | 'direction' | 'assessment_level' | 'interests' | 'onboarding_complete'>> & { assessment_context?: string }) => Promise<void>
```

- [ ] **Step 3: Add `tags` to CourseCard and add API methods in courseApi.ts**

In `src/services/courseApi.ts`, add `tags` to `CourseCard` interface after `category`:

```typescript
  tags: string[];
```

Add two new methods to the `courseApi` object:

```typescript
  getTags: async (): Promise<string[]> => {
    const resp = await fetch("/api/courses/tags");
    if (!resp.ok) return [];
    return resp.json();
  },

  recommend: async (tags: string[]): Promise<CourseCard[]> => {
    const query = tags.join(",");
    const resp = await fetch(`/api/courses/recommend?tags=${encodeURIComponent(query)}`);
    if (!resp.ok) return [];
    return resp.json();
  },
```

- [ ] **Step 4: Commit**

```bash
git add src/store/authStore.ts src/services/courseApi.ts
git commit -m "feat: update frontend types and API for new onboarding"
```

---

### Task 5: Update App.tsx onboarding guard

**Files:**
- Modify: `src/App.tsx:27-51`

- [ ] **Step 1: Replace direction-based guard with onboarding_complete**

In `src/App.tsx`, replace the `AuthGuard` function body (lines 27-51):

```typescript
function AuthGuard({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading, user } = useAuthStore()
  const location = useLocation()

  if (isLoading) {
    return <LoadingScreen />
  }

  if (!isAuthenticated) return <Navigate to="/login" replace />

  // If user hasn't completed onboarding, redirect to /
  const onboardingComplete = !!user?.onboarding_complete
  const isOnboardingRoute = location.pathname === '/'

  if (!onboardingComplete && !isOnboardingRoute) {
    return <Navigate to="/" replace />
  }

  // If user has already completed onboarding, don't let them back to /
  if (onboardingComplete && isOnboardingRoute) {
    return <Navigate to="/dashboard" replace />
  }

  return <>{children}</>
}
```

Key change: line `const onboardingComplete = !!user?.onboarding_complete` replaces `!!(user?.direction && user.direction !== '')`.

- [ ] **Step 2: Commit**

```bash
git add src/App.tsx
git commit -m "feat: switch onboarding guard to onboarding_complete flag"
```

---

### Task 6: Add i18n keys for new onboarding

**Files:**
- Modify: `src/lib/i18n.ts`

- [ ] **Step 1: Replace old onboarding keys with new ones**

In `src/lib/i18n.ts`, replace the `// ===== ONBOARDING =====` section (lines 52-76) with:

```typescript
  // ===== ONBOARDING =====
  "onboarding.welcome": { en: "Welcome to", ru: "Добро пожаловать в" },
  "onboarding.barsbek.hello": {
    en: "Hi! I'm Barsbek, your learning guide. Let's find the perfect courses for you!",
    ru: "Салам! Я Barsbek, твой гид в обучении. Давай подберём идеальные курсы для тебя!",
  },
  "onboarding.barsbek.interests": {
    en: "What are you interested in? Pick everything that catches your eye!",
    ru: "Что тебе интересно? Выбери всё, что нравится!",
  },
  "onboarding.barsbek.chat": {
    en: "Great choices! Let me ask a couple of quick questions.",
    ru: "Отличный выбор! Задам пару быстрых вопросов.",
  },
  "onboarding.barsbek.results": {
    en: "Here's what I picked for you!",
    ru: "Вот что я подобрал для тебя!",
  },
  "onboarding.barsbek.noCourses": {
    en: "No courses match your interests yet. Explore the marketplace!",
    ru: "Пока нет курсов по твоим интересам. Загляни в маркетплейс!",
  },
  "onboarding.letsGo": { en: "Let's go!", ru: "Поехали!" },
  "onboarding.pickInterests": { en: "Pick at least one", ru: "Выбери хотя бы один" },
  "onboarding.nextStep": { en: "Continue", ru: "Продолжить" },
  "onboarding.skip": { en: "Skip", ru: "Пропустить" },
  "onboarding.startLearning": { en: "Start Learning", ru: "Начать обучение" },
  "onboarding.exploreCourses": { en: "Explore Courses", ru: "Смотреть все курсы" },
  "onboarding.enrollAndContinue": { en: "Enroll & Continue", ru: "Записаться" },
  "onboarding.enrolled": { en: "Enrolled!", ru: "Записан!" },
  "onboarding.chatQ1": {
    en: "What's your experience with the topics you picked?",
    ru: "Какой у тебя опыт в выбранных темах?",
  },
  "onboarding.chatQ2": {
    en: "Are you learning for yourself or for work?",
    ru: "Учишься для себя или для работы?",
  },
  "onboarding.namePlaceholder": { en: "Enter your name", ru: "Введите имя" },
  "onboarding.nameLabel": { en: "What's your name?", ru: "Как вас зовут?" },
  "onboarding.choosePath": { en: "Choose your learning path", ru: "Выберите направление обучения" },
  "onboarding.assessment": { en: "Level Assessment", ru: "Оценка уровня" },
  "onboarding.question": { en: "Question", ru: "Вопрос" },
  "onboarding.answerPlaceholder": { en: "Type your answer...", ru: "Введите ваш ответ..." },
  "onboarding.ready": { en: "Your Learning Plan is Ready!", ru: "Ваш план обучения готов!" },
  "onboarding.result": { en: "Assessment Result", ru: "Результат оценки" },
  "onboarding.level.beginner": { en: "Beginner Level", ru: "Начальный уровень" },
  "onboarding.level.intermediate": { en: "Intermediate Level", ru: "Средний уровень" },
  "onboarding.level.advanced": { en: "Advanced Level", ru: "Продвинутый уровень" },
  "onboarding.direction": { en: "Direction", ru: "Направление" },
  "onboarding.planDescription": {
    en: "Your personalized roadmap has been generated with topics tailored to your level.",
    ru: "Персональная дорожная карта создана с учётом вашего уровня.",
  },
  "onboarding.chatHi": {
    en: "Hi {name}! I'm going to ask you a few questions to understand your current level. Let's start!",
    ru: "Привет, {name}! Я задам вам несколько вопросов, чтобы понять ваш текущий уровень. Начнём!",
  },
  "onboarding.analyzing": { en: "Great! Let me analyze your answers...", ru: "Отлично! Анализирую ваши ответы..." },
```

Note: old keys are kept for backward compatibility (assessment questions still used elsewhere). New keys are added at the top of the section.

- [ ] **Step 2: Commit**

```bash
git add src/lib/i18n.ts
git commit -m "feat: add i18n keys for new onboarding wizard"
```

---

### Task 7: Rewrite Onboarding.tsx — the 4-step wizard

**Files:**
- Rewrite: `src/pages/Onboarding.tsx`

- [ ] **Step 1: Write the new Onboarding component**

Replace the entire `src/pages/Onboarding.tsx` with:

```tsx
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { ArrowRight, Loader2, Check, BookOpen, Star } from 'lucide-react'
import { useAuthStore } from '@/store/authStore'
import { useTranslation } from '@/hooks/useTranslation'
import { courseApi, type CourseCard } from '@/services/courseApi'

const MASCOT_IMAGES: Record<number, string> = {
  0: '/images/mascot-happy.png',
  1: '/images/mascot-thinking.png',
  2: '/images/mascot-study.png',
  3: '/images/mascot-happy.png',
}

function SpeechBubble({ text }: { text: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="relative bg-white/8 border border-white/10 rounded-2xl rounded-bl-md px-5 py-3 text-sm text-white/80 max-w-sm"
    >
      {text}
    </motion.div>
  )
}

function MascotWithBubble({ step, text }: { step: number; text: string }) {
  return (
    <div className="flex items-end gap-3 mb-6">
      <motion.img
        key={step}
        src={MASCOT_IMAGES[step]}
        alt="Barsbek"
        className="w-20 h-20 object-contain"
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ type: 'spring', stiffness: 200 }}
      />
      <SpeechBubble text={text} />
    </div>
  )
}

export default function Onboarding() {
  const navigate = useNavigate()
  const { t } = useTranslation()
  const { user, updateUser, fetchUser } = useAuthStore()
  const [step, setStep] = useState(0)

  // Step 1
  const [nameInput, setNameInput] = useState(user?.name || '')

  // Step 2
  const [availableTags, setAvailableTags] = useState<string[]>([])
  const [selectedTags, setSelectedTags] = useState<string[]>([])
  const [tagsLoading, setTagsLoading] = useState(false)

  // Step 3
  const [chatStep, setChatStep] = useState(0)
  const [chatAnswers, setChatAnswers] = useState<string[]>([])
  const [currentAnswer, setCurrentAnswer] = useState('')

  // Step 4
  const [recommendedCourses, setRecommendedCourses] = useState<CourseCard[]>([])
  const [coursesLoading, setCoursesLoading] = useState(false)
  const [enrolledIds, setEnrolledIds] = useState<Set<string>>(new Set())
  const [saving, setSaving] = useState(false)

  // Load tags when entering step 2
  useEffect(() => {
    if (step === 1 && availableTags.length === 0) {
      setTagsLoading(true)
      courseApi.getTags().then((tags) => {
        setAvailableTags(tags)
        setTagsLoading(false)
      })
    }
  }, [step, availableTags.length])

  // Load recommendations when entering step 4
  useEffect(() => {
    if (step === 3) {
      setCoursesLoading(true)
      courseApi.recommend(selectedTags).then((courses) => {
        setRecommendedCourses(courses)
        setCoursesLoading(false)
      })
    }
  }, [step, selectedTags])

  const toggleTag = (tag: string) => {
    setSelectedTags((prev) =>
      prev.includes(tag) ? prev.filter((t) => t !== tag) : [...prev, tag]
    )
  }

  const handleNameNext = async () => {
    if (!nameInput.trim()) return
    if (nameInput !== user?.name) {
      await updateUser({ name: nameInput.trim() })
    }
    setStep(1)
  }

  const handleTagsNext = () => {
    if (selectedTags.length === 0) return
    setStep(2)
  }

  const handleChatAnswer = () => {
    if (!currentAnswer.trim()) return
    const newAnswers = [...chatAnswers, currentAnswer.trim()]
    setChatAnswers(newAnswers)
    setCurrentAnswer('')
    if (chatStep < 1) {
      setChatStep(chatStep + 1)
    } else {
      setStep(3)
    }
  }

  const handleSkipChat = () => {
    setStep(3)
  }

  const handleEnroll = async (courseId: string) => {
    try {
      await courseApi.enroll(courseId)
      setEnrolledIds((prev) => new Set([...prev, courseId]))
    } catch {
      // already enrolled or error
    }
  }

  const handleFinish = async () => {
    setSaving(true)
    try {
      await updateUser({
        interests: selectedTags,
        onboarding_complete: true,
        assessment_context: chatAnswers.length > 0 ? chatAnswers.join(' | ') : undefined,
      } as any)
      await fetchUser()
      navigate('/dashboard')
    } catch (err) {
      console.error('Failed to save onboarding', err)
    } finally {
      setSaving(false)
    }
  }

  const chatQuestions = [t('onboarding.chatQ1'), t('onboarding.chatQ2')]

  return (
    <div className="min-h-screen bg-black flex items-center justify-center p-4 relative overflow-hidden">
      {/* Ambient glow */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 700,
          height: 700,
          background: 'radial-gradient(circle, rgba(249,115,22,0.05), transparent 70%)',
          transform: 'translate(-50%, -50%)',
          left: '50%',
          top: '50%',
        }}
      />

      <div className="w-full max-w-2xl relative z-10">
        {/* Progress dots */}
        <div className="flex justify-center gap-2 mb-8">
          {[0, 1, 2, 3].map((i) => (
            <motion.div
              key={i}
              className="h-2 rounded-full"
              animate={{
                width: step === i ? 32 : 8,
                backgroundColor: step >= i ? '#F97316' : 'rgba(255,255,255,0.10)',
              }}
              transition={{ duration: 0.3 }}
            />
          ))}
        </div>

        <AnimatePresence mode="wait">
          {/* ── Step 0: Welcome ── */}
          {step === 0 && (
            <motion.div
              key="step0"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <div className="flex flex-col items-center">
                <MascotWithBubble step={0} text={t('onboarding.barsbek.hello')} />
              </div>

              <div className="text-center">
                <h1 className="text-3xl font-bold tracking-tight text-white">
                  {t('onboarding.welcome')} <span className="text-[#F97316]">Bars</span> AI
                </h1>
              </div>

              {!user?.name && (
                <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-6">
                  <label className="text-sm text-white/40 mb-2 block">{t('onboarding.nameLabel')}</label>
                  <input
                    className="w-full bg-transparent border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white outline-none focus:border-[#F97316]/50 placeholder:text-white/30"
                    placeholder={t('onboarding.namePlaceholder')}
                    value={nameInput}
                    onChange={(e) => setNameInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleNameNext()}
                  />
                </div>
              )}

              <div className="flex justify-center">
                <button
                  onClick={handleNameNext}
                  disabled={!nameInput.trim()}
                  className="inline-flex items-center gap-2 px-8 py-3 rounded-xl font-semibold text-white text-sm disabled:opacity-40 transition-opacity"
                  style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
                >
                  {t('onboarding.letsGo')} <ArrowRight size={18} />
                </button>
              </div>
            </motion.div>
          )}

          {/* ── Step 1: Interests ── */}
          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <MascotWithBubble step={1} text={t('onboarding.barsbek.interests')} />

              {tagsLoading ? (
                <div className="flex justify-center py-12">
                  <Loader2 className="animate-spin text-[#F97316]" size={24} />
                </div>
              ) : (
                <div className="flex flex-wrap gap-2 justify-center">
                  {availableTags.map((tag) => {
                    const selected = selectedTags.includes(tag)
                    return (
                      <motion.button
                        key={tag}
                        onClick={() => toggleTag(tag)}
                        whileTap={{ scale: 0.95 }}
                        className={`px-4 py-2 rounded-full text-sm font-medium border transition-all ${
                          selected
                            ? 'border-[#F97316] text-white'
                            : 'border-white/10 text-white/50 hover:border-white/20'
                        }`}
                        style={selected ? { background: 'linear-gradient(135deg, #F97316, #FB923C)' } : {}}
                      >
                        {tag}
                      </motion.button>
                    )
                  })}
                </div>
              )}

              {selectedTags.length === 0 && !tagsLoading && (
                <p className="text-center text-white/30 text-xs">{t('onboarding.pickInterests')}</p>
              )}

              <div className="flex justify-center">
                <button
                  onClick={handleTagsNext}
                  disabled={selectedTags.length === 0}
                  className="inline-flex items-center gap-2 px-8 py-3 rounded-xl font-semibold text-white text-sm disabled:opacity-40 transition-opacity"
                  style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
                >
                  {t('onboarding.nextStep')} <ArrowRight size={18} />
                </button>
              </div>
            </motion.div>
          )}

          {/* ── Step 2: Mini Chat ── */}
          {step === 2 && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <MascotWithBubble step={2} text={t('onboarding.barsbek.chat')} />

              <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-6 space-y-4">
                {/* Show previous Q&A */}
                {chatAnswers.map((ans, i) => (
                  <div key={i} className="space-y-2">
                    <p className="text-sm text-white/60">{chatQuestions[i]}</p>
                    <p className="text-sm text-white bg-white/5 rounded-xl px-4 py-2">{ans}</p>
                  </div>
                ))}

                {/* Current question */}
                {chatStep < 2 && (
                  <>
                    <p className="text-sm text-white/80 font-medium">{chatQuestions[chatStep]}</p>
                    <div className="flex gap-2">
                      <input
                        className="flex-1 bg-transparent border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white outline-none focus:border-[#F97316]/50 placeholder:text-white/30"
                        placeholder={t('onboarding.answerPlaceholder')}
                        value={currentAnswer}
                        onChange={(e) => setCurrentAnswer(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && handleChatAnswer()}
                      />
                      <button
                        onClick={handleChatAnswer}
                        disabled={!currentAnswer.trim()}
                        className="px-4 py-2.5 rounded-xl text-white font-semibold text-sm disabled:opacity-40 transition-opacity"
                        style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
                      >
                        <ArrowRight size={18} />
                      </button>
                    </div>
                  </>
                )}
              </div>

              <div className="flex justify-center">
                <button
                  onClick={handleSkipChat}
                  className="text-sm text-white/30 hover:text-white/50 transition-colors"
                >
                  {t('onboarding.skip')}
                </button>
              </div>
            </motion.div>
          )}

          {/* ── Step 3: Course Recommendations ── */}
          {step === 3 && (
            <motion.div
              key="step3"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <MascotWithBubble step={3} text={t('onboarding.barsbek.results')} />

              {coursesLoading ? (
                <div className="flex justify-center py-12">
                  <Loader2 className="animate-spin text-[#F97316]" size={24} />
                </div>
              ) : recommendedCourses.length === 0 ? (
                <div className="text-center py-8">
                  <p className="text-white/40 text-sm">{t('onboarding.barsbek.noCourses')}</p>
                </div>
              ) : (
                <div className="grid gap-3 max-h-[400px] overflow-y-auto pr-1">
                  {recommendedCourses.map((course) => {
                    const isEnrolled = enrolledIds.has(course.id)
                    return (
                      <motion.div
                        key={course.id}
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-4 flex gap-4 items-center"
                      >
                        {/* Thumbnail or icon */}
                        <div className="w-12 h-12 rounded-xl flex items-center justify-center shrink-0 bg-[#F97316]/10">
                          {course.thumbnail_url ? (
                            <img src={course.thumbnail_url} alt="" className="w-12 h-12 rounded-xl object-cover" />
                          ) : (
                            <BookOpen size={20} className="text-[#F97316]" />
                          )}
                        </div>

                        <div className="flex-1 min-w-0">
                          <h3 className="text-sm font-semibold text-white truncate">{course.title}</h3>
                          <div className="flex items-center gap-2 mt-1">
                            <span className="text-xs text-white/30">{course.difficulty}</span>
                            {course.rating_avg > 0 && (
                              <span className="text-xs text-white/30 flex items-center gap-0.5">
                                <Star size={10} className="text-[#FFB800]" fill="#FFB800" />
                                {course.rating_avg.toFixed(1)}
                              </span>
                            )}
                            <span className="text-xs text-white/30">
                              {course.total_enrolled} {t('courses.enrolled')}
                            </span>
                          </div>
                        </div>

                        <button
                          onClick={() => handleEnroll(course.id)}
                          disabled={isEnrolled}
                          className={`text-xs px-3 py-1.5 rounded-lg font-semibold transition-all shrink-0 ${
                            isEnrolled
                              ? 'bg-green-500/15 text-green-400'
                              : 'text-white'
                          }`}
                          style={!isEnrolled ? { background: 'linear-gradient(135deg, #F97316, #FB923C)' } : {}}
                        >
                          {isEnrolled ? (
                            <span className="flex items-center gap-1"><Check size={12} /> {t('onboarding.enrolled')}</span>
                          ) : (
                            t('onboarding.enrollAndContinue')
                          )}
                        </button>
                      </motion.div>
                    )
                  })}
                </div>
              )}

              <div className="flex flex-col items-center gap-3">
                <button
                  onClick={handleFinish}
                  disabled={saving}
                  className="inline-flex items-center gap-2 px-8 py-3 rounded-xl font-semibold text-white text-sm disabled:opacity-50 transition-opacity"
                  style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
                >
                  {saving ? <Loader2 className="animate-spin" size={18} /> : null}
                  {t('onboarding.startLearning')} <ArrowRight size={18} />
                </button>
                <button
                  onClick={() => { handleFinish().then(() => navigate('/courses')) }}
                  className="text-sm text-white/30 hover:text-white/50 transition-colors"
                >
                  {t('onboarding.exploreCourses')}
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  )
}
```

- [ ] **Step 2: Verify the component renders**

Run:
```bash
cd /Users/azamat/Desktop/платформа\ обучнеи && npm run dev
```

Open `http://localhost:5173` with a new user (or user with `onboarding_complete: false`) — should see step 0 with mascot.

- [ ] **Step 3: Commit**

```bash
git add src/pages/Onboarding.tsx
git commit -m "feat: rewrite Onboarding.tsx — 4-step wizard with Barsbek mascot"
```

---

### Task 8: Update course_service to handle tags in create/update

**Files:**
- Modify: `backend/app/services/course_service.py`

- [ ] **Step 1: Ensure tags are saved when creating/updating courses**

Find the `create_course` function in `backend/app/services/course_service.py` and ensure the `tags` field from the request body is passed to the Course constructor. Find where `Course(...)` is instantiated and add:

```python
tags=body.tags if hasattr(body, 'tags') else [],
```

Find the `update_course` function and ensure tags are updated. In the section where fields are conditionally updated, add:

```python
if body.tags is not None:
    course.tags = body.tags
```

- [ ] **Step 2: Commit**

```bash
git add backend/app/services/course_service.py
git commit -m "feat: handle tags in course create/update service"
```

---

### Task 9: Final integration commit and cleanup

**Files:**
- No new files — verify everything works end-to-end

- [ ] **Step 1: Run backend to verify migrations and endpoints**

```bash
cd backend
alembic upgrade head
uvicorn app.main:app --reload
```

Test endpoints:
```bash
curl http://localhost:8000/api/courses/tags
curl "http://localhost:8000/api/courses/recommend?tags=python,frontend"
```

- [ ] **Step 2: Run frontend to verify onboarding flow**

```bash
cd /Users/azamat/Desktop/платформа\ обучнеи && npm run dev
```

Test full flow: register new user → step 0 (name) → step 1 (tags) → step 2 (chat) → step 3 (courses) → dashboard.

- [ ] **Step 3: Commit final state**

```bash
git add -A
git commit -m "feat: complete new onboarding wizard with Barsbek mascot and course recommendations"
```
