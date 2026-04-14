import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { ArrowLeft } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { LessonPlayer } from '@/components/lesson/LessonPlayer'
import { CourseStepPlayer } from '@/components/courses/CourseStepPlayer'
import { useTranslation } from '@/hooks/useTranslation'
import { LESSONS_V2 } from '@/data/lessons'
import { courseApi, type LessonStep } from '@/services/courseApi'

// Shape we care about after fetching
interface ResolvedLesson {
  id: string
  title: string
  content_markdown: string
  xp_reward: number
  steps: LessonStep[] | null
}

type PlayerMode =
  | { kind: 'v2'; v2Key: string; allSiblingIds: string[] }
  | { kind: 'steps'; steps: LessonStep[]; title: string }
  | { kind: 'empty' }

export default function CourseLearn() {
  const { id: courseId, lessonId } = useParams<{ id: string; lessonId: string }>()
  const navigate = useNavigate()
  const { t } = useTranslation()

  const [mode, setMode] = useState<PlayerMode | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!lessonId) return

    setLoading(true)

    courseApi
      .getLesson(lessonId)
      .then((lesson: ResolvedLesson) => {
        // Priority 1: DB-stored steps array (non-empty)
        if (Array.isArray(lesson.steps) && lesson.steps.length > 0) {
          setMode({ kind: 'steps', steps: lesson.steps, title: lesson.title })
          return
        }

        // Priority 2: content_markdown holds a V2 static lesson ID
        const key = lesson.content_markdown?.trim()
        if (key && LESSONS_V2[key]) {
          const nodePrefix = key.split('-').slice(0, 2).join('-')
          const siblings = Object.keys(LESSONS_V2).filter((k) =>
            k.startsWith(nodePrefix + '-')
          )
          setMode({ kind: 'v2', v2Key: key, allSiblingIds: siblings })
          return
        }

        // Priority 3: no content available yet
        setMode({ kind: 'empty' })
      })
      .catch(() => {
        navigate(`/courses/${courseId}/roadmap`)
      })
      .finally(() => setLoading(false))
  }, [lessonId, courseId, navigate])

  // ── Handlers ────────────────────────────────────────────────────────────

  const handleStepsComplete = async () => {
    if (!lessonId) return
    try {
      await courseApi.completeLesson(lessonId)
    } catch {
      // Award attempt failed — still allow the user to see the congrats screen
    }
  }

  const handleClose = () => {
    navigate(`/courses/${courseId}/roadmap`)
  }

  // ── Loading ──────────────────────────────────────────────────────────────

  if (loading) {
    return (
      <div className="min-h-screen min-h-[100dvh] flex items-center justify-center bg-black">
        <p className="text-white/40 text-sm">{t('common.loading')}</p>
      </div>
    )
  }

  // ── V2 static lesson ─────────────────────────────────────────────────────

  if (mode?.kind === 'v2') {
    const v2Lesson = mode.v2Key in LESSONS_V2 ? LESSONS_V2[mode.v2Key] : undefined
    if (!v2Lesson) return null
    const nodeId = mode.v2Key.split('-').slice(0, 2).join('-')
    return (
      <LessonPlayer
        lesson={v2Lesson}
        nodeId={nodeId}
        allLessonIdsForNode={mode.allSiblingIds}
        onClose={handleClose}
      />
    )
  }

  // ── DB steps ─────────────────────────────────────────────────────────────

  if (mode?.kind === 'steps') {
    return (
      <CourseStepPlayer
        steps={mode.steps}
        lessonTitle={mode.title}
        onComplete={handleStepsComplete}
        onClose={handleClose}
      />
    )
  }

  // ── Placeholder ──────────────────────────────────────────────────────────

  return (
    <div className="min-h-screen min-h-[100dvh] flex flex-col items-center justify-center bg-black px-6">
      <img
        src="/images/mascot-confused.png"
        alt="Coming soon"
        className="w-28 h-28 object-contain mb-4 opacity-60"
      />
      <p className="text-text-secondary text-sm text-center mb-4">
        Контент для этого урока скоро появится
      </p>
      <Button variant="secondary" size="sm" onClick={handleClose}>
        <ArrowLeft size={14} /> Назад к роадмапу
      </Button>
    </div>
  )
}
