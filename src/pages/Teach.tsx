import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { Plus, Users, Pencil } from 'lucide-react'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { StarRating } from '@/components/courses/StarRating'
import { useTranslation } from '@/hooks/useTranslation'
import { courseApi, type CourseCard } from '@/services/courseApi'
import { useAuthStore } from '@/store/authStore'

const GRADIENT_THUMBNAILS = [
  'linear-gradient(135deg, #F97316 0%, #FB923C 100%)',
  'linear-gradient(135deg, #FF6B6B 0%, #F97316 100%)',
  'linear-gradient(135deg, #4ADE80 0%, #22C55E 100%)',
  'linear-gradient(135deg, #F97316 0%, #FF6B6B 100%)',
  'linear-gradient(135deg, #FB923C 0%, #4ADE80 100%)',
  'linear-gradient(135deg, #22C55E 0%, #F97316 100%)',
]

function getGradient(id: string) {
  let hash = 0
  for (let i = 0; i < id.length; i++) hash = id.charCodeAt(i) + ((hash << 5) - hash)
  return GRADIENT_THUMBNAILS[Math.abs(hash) % GRADIENT_THUMBNAILS.length]
}

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  show: { opacity: 1, y: 0 },
}

export default function Teach() {
  const navigate = useNavigate()
  const { t } = useTranslation()
  const [courses, setCourses] = useState<CourseCard[]>([])
  const [loading, setLoading] = useState(true)
  const [toast, setToast] = useState<string | null>(null)
  const [createError, setCreateError] = useState<string | null>(null)
  const user = useAuthStore((s) => s.user)

  useEffect(() => {
    courseApi
      .getMy()
      .then((res) => setCourses(res))
      .catch(() => setCourses([]))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    if (!toast) return
    const timer = setTimeout(() => setToast(null), 5000)
    return () => clearTimeout(timer)
  }, [toast])

  const handleCreate = async () => {
    setCreateError(null)
    try {
      const res = await courseApi.create({
        title: 'Untitled Course',
        description: '',
        category: 'Other',
        difficulty: 'Beginner',
        price: 0,
      })
      if (user?.role !== 'admin') {
        setToast('Ваш курс отправлен на модерацию. Вы получите уведомление когда он будет одобрён.')
      }
      navigate(`/teach/${res.id}`)
    } catch (err: unknown) {
      setCreateError(err instanceof Error ? err.message : 'Не удалось создать курс')
    }
  }

  return (
    <PageWrapper>
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="show"
        className="max-w-5xl mx-auto space-y-4 lg:space-y-6"
      >
        {/* Header */}
        <motion.div variants={itemVariants} className="flex items-center justify-between">
          <h1 className="text-xl lg:text-2xl font-bold">{t('teach.title')}</h1>
          <Button size="sm" onClick={handleCreate}>
            <Plus size={16} />
            {t('teach.create')}
          </Button>
        </motion.div>

        {/* Create error */}
        {createError && (
          <motion.div variants={itemVariants}>
            <p className="text-red-400 text-sm text-center">{createError}</p>
          </motion.div>
        )}

        {/* Course grid */}
        {loading ? (
          <motion.div variants={itemVariants} className="text-center py-12">
            <p className="text-text-secondary text-sm">{t('common.loading')}</p>
          </motion.div>
        ) : courses.length === 0 ? (
          <motion.div variants={itemVariants} className="text-center py-16">
            <motion.img
              src="/images/mascot-study.png"
              alt="No courses"
              className="w-28 h-28 object-contain mx-auto mb-4 drop-shadow-lg"
              animate={{ y: [0, -6, 0] }}
              transition={{ repeat: Infinity, duration: 2.5, ease: 'easeInOut' }}
            />
            <p className="text-text-secondary text-sm mb-4">{t('teach.noCourses')}</p>
            <Button size="sm" onClick={handleCreate}>
              <Plus size={16} />
              {t('teach.create')}
            </Button>
          </motion.div>
        ) : (
          <motion.div
            variants={containerVariants}
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"
          >
            {courses.map((course) => (
              <motion.div key={course.id} variants={itemVariants}>
                <Card className="p-0 overflow-hidden">
                  {/* Gradient thumbnail */}
                  <div
                    className="h-28 w-full flex items-center justify-center"
                    style={{
                      background: course.thumbnail_url
                        ? `url(${course.thumbnail_url}) center/cover`
                        : getGradient(course.id),
                    }}
                  >
                    {!course.thumbnail_url && (
                      <span className="text-white/80 text-3xl font-bold">
                        {course.title.charAt(0)}
                      </span>
                    )}
                  </div>

                  <div className="p-4 space-y-3">
                    {/* Badges row */}
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-[#F97316]/15 text-[#F97316] font-medium">
                        {course.category}
                      </span>
                      <span
                        className={`text-[10px] px-2 py-0.5 rounded-full font-medium ${
                          course.status === 'published'
                            ? 'bg-[#4ADE80]/10 text-[#4ADE80]'
                            : 'bg-white/6 text-white/40'
                        }`}
                      >
                        {course.status === 'published' ? t('teach.published') : t('teach.draft')}
                      </span>
                    </div>

                    {/* Title */}
                    <h3 className="text-sm font-semibold leading-tight line-clamp-2">{course.title}</h3>

                    {/* Stats */}
                    <div className="flex items-center gap-3">
                      <div className="flex items-center gap-1">
                        <StarRating rating={course.rating_avg} size={12} />
                        <span className="text-[11px] text-text-secondary">({course.rating_count})</span>
                      </div>
                      <div className="flex items-center gap-1 text-text-secondary">
                        <Users size={12} />
                        <span className="text-[11px]">{course.total_enrolled}</span>
                      </div>
                    </div>

                    <Button
                      variant="secondary"
                      size="sm"
                      className="w-full"
                      onClick={() => navigate(`/teach/${course.id}`)}
                    >
                      <Pencil size={14} />
                      {t('teach.edit')}
                    </Button>
                  </div>
                </Card>
              </motion.div>
            ))}
          </motion.div>
        )}
      </motion.div>

      {/* Moderation toast */}
      <AnimatePresence>
        {toast && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 20 }}
            className="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 max-w-md w-[90vw] bg-[#1A1A1A] border border-white/10 rounded-2xl px-5 py-3.5 text-sm text-white shadow-2xl"
          >
            {toast}
          </motion.div>
        )}
      </AnimatePresence>
    </PageWrapper>
  )
}
