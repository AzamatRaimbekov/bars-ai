import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import {
  ArrowLeft, Users, ChevronDown, ChevronRight, CheckCircle2,
  BookOpen, Pencil, Play, Clock, CreditCard,
} from 'lucide-react'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { ProgressBar } from '@/components/ui/ProgressBar'
import { StarRating } from '@/components/courses/StarRating'
import { ReviewForm } from '@/components/courses/ReviewForm'
import { useTranslation } from '@/hooks/useTranslation'
import { courseApi, type CourseDetail as CourseDetailType, type CourseProgress } from '@/services/courseApi'
import { paymentApi, type PaymentRequest } from '@/services/paymentApi'
import { PaymentModal } from '@/components/courses/PaymentModal'

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  show: { opacity: 1, y: 0 },
}

export default function CourseDetail() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const { t } = useTranslation()
  const [course, setCourse] = useState<CourseDetailType | null>(null)
  const [progress, setProgress] = useState<CourseProgress | null>(null)
  const [loading, setLoading] = useState(true)
  const [enrolling, setEnrolling] = useState(false)
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set())
  const [showReviewForm, setShowReviewForm] = useState(false)
  const [hasReviewed, setHasReviewed] = useState(false)
  const [showPaymentModal, setShowPaymentModal] = useState(false)
  const [myPayments, setMyPayments] = useState<PaymentRequest[]>([])

  useEffect(() => {
    if (!id) return
    setLoading(true)
    Promise.all([
      courseApi.get(id),
      courseApi.getProgress(id).catch(() => null),
      paymentApi.myPayments().catch(() => [] as PaymentRequest[]),
    ])
      .then(([courseData, progressData, payments]) => {
        setCourse(courseData)
        setProgress(progressData)
        setMyPayments(payments)
        // Expand first section by default
        if (courseData.sections.length > 0) {
          setExpandedSections(new Set([courseData.sections[0].id]))
        }
      })
      .catch(() => navigate('/courses'))
      .finally(() => setLoading(false))
  }, [id])

  const handleStart = async () => {
    if (!id || !course) return
    const firstLesson = course.sections?.[0]?.lessons?.[0]
    if (!firstLesson) return

    if (course.is_enrolled) {
      navigate(`/courses/${course.id}/learn/${firstLesson.id}`)
      return
    }
    setEnrolling(true)
    try {
      await courseApi.enroll(id)
      navigate(`/courses/${course.id}/learn/${firstLesson.id}`)
    } catch {
      // handle error silently
    } finally {
      setEnrolling(false)
    }
  }

  const handleReview = async (rating: number, comment: string) => {
    if (!id) return
    await courseApi.review(id, rating, comment)
    const updated = await courseApi.get(id)
    setCourse(updated)
    setShowReviewForm(false)
    setHasReviewed(true)
  }

  const toggleSection = (sectionId: string) => {
    setExpandedSections((prev) => {
      const next = new Set(prev)
      if (next.has(sectionId)) next.delete(sectionId)
      else next.add(sectionId)
      return next
    })
  }

  const completedSet = new Set(progress?.completed_lesson_ids ?? [])
  const pendingPayment = course ? myPayments.find(
    (p) => p.course_id === course.id && p.status === 'pending'
  ) : null
  const isPaid = course ? course.price > 0 : false

  // Find first incomplete lesson for "Continue Learning"
  const allLessons = course?.sections
    .sort((a, b) => a.position - b.position)
    .flatMap((s) => [...s.lessons].sort((a, b) => a.position - b.position)) ?? []
  const firstIncompleteLesson = allLessons.find((l) => !completedSet.has(l.id)) ?? allLessons[0]

  if (loading) {
    return (
      <PageWrapper>
        <div className="flex items-center justify-center py-20">
          <p className="text-text-secondary text-sm">{t('common.loading')}</p>
        </div>
      </PageWrapper>
    )
  }

  if (!course) return null

  // Rating breakdown
  const ratingCounts = [0, 0, 0, 0, 0]
  course.reviews.forEach((r) => {
    if (r.rating >= 1 && r.rating <= 5) ratingCounts[r.rating - 1]++
  })
  const maxRatingCount = Math.max(...ratingCounts, 1)

  const progressPercent =
    progress && progress.total_lessons > 0
      ? Math.round((progress.completed_count / progress.total_lessons) * 100)
      : 0

  return (
    <PageWrapper>
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="show"
        className="max-w-3xl mx-auto space-y-4 lg:space-y-6"
      >
        {/* Back button */}
        <motion.div variants={itemVariants}>
          <button
            onClick={() => navigate('/courses')}
            className="flex items-center gap-1.5 text-sm text-text-secondary hover:text-text transition-colors cursor-pointer"
          >
            <ArrowLeft size={16} />
            {t('common.back')}
          </button>
        </motion.div>

        {/* Hero */}
        <motion.div variants={itemVariants}>
          <Card className="relative overflow-hidden">
            <div className="relative space-y-3">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="text-[11px] px-3 py-1 rounded-full bg-[#F97316]/15 text-[#F97316] font-medium">
                  {course.category}
                </span>
                <span className="text-[11px] px-3 py-1 rounded-full bg-white/6 text-text-secondary font-medium">
                  {course.difficulty}
                </span>
              </div>
              <h1 className="text-xl lg:text-2xl font-bold">{course.title}</h1>
              <p className="text-sm text-text-secondary">{course.author_name}</p>
              <div className="flex items-center gap-4 flex-wrap">
                <div className="flex items-center gap-1.5">
                  <StarRating rating={course.rating_avg} size={14} />
                  <span className="text-xs text-text-secondary">
                    {course.rating_avg.toFixed(1)} ({course.rating_count})
                  </span>
                </div>
                <div className="flex items-center gap-1 text-text-secondary">
                  <Users size={14} />
                  <span className="text-xs">
                    {course.total_enrolled} {t('courses.enrolled')}
                  </span>
                </div>
              </div>

              {/* Progress if enrolled */}
              {course.is_enrolled && progress && (
                <div className="pt-2">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs text-text-secondary">{t('courses.progress')}</span>
                    <span className="text-xs font-bold text-[#F97316]">{progressPercent}%</span>
                  </div>
                  <ProgressBar value={progress.completed_count} max={progress.total_lessons} />
                </div>
              )}
            </div>
          </Card>
        </motion.div>

        {/* Description */}
        <motion.div variants={itemVariants}>
          <Card>
            <h2 className="text-sm font-semibold mb-3">{t('courses.description')}</h2>
            <p className="text-sm text-text-secondary leading-relaxed">{course.description}</p>
          </Card>
        </motion.div>

        {/* Curriculum */}
        <motion.div variants={itemVariants}>
          <Card>
            <h2 className="text-sm font-semibold mb-4">{t('courses.curriculum')}</h2>
            <div className="space-y-2">
              {course.sections
                .sort((a, b) => a.position - b.position)
                .map((section) => {
                  const isExpanded = expandedSections.has(section.id)
                  const sectionLessons = section.lessons.sort((a, b) => a.position - b.position)
                  const completedInSection = sectionLessons.filter((l) =>
                    completedSet.has(l.id)
                  ).length

                  return (
                    <div
                      key={section.id}
                      className="border border-white/6 rounded-xl overflow-hidden"
                    >
                      <button
                        onClick={() => toggleSection(section.id)}
                        className="w-full flex items-center justify-between px-4 py-3 hover:bg-surface/50 transition-colors cursor-pointer"
                      >
                        <div className="flex items-center gap-3">
                          <motion.div
                            animate={{ rotate: isExpanded ? 90 : 0 }}
                            transition={{ duration: 0.2 }}
                          >
                            <ChevronRight size={14} className="text-text-secondary" />
                          </motion.div>
                          <span className="text-sm font-medium">{section.title}</span>
                        </div>
                        <span className="text-[11px] text-text-secondary">
                          {completedInSection}/{sectionLessons.length}
                        </span>
                      </button>
                      <AnimatePresence>
                        {isExpanded && (
                          <motion.div
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: 'auto', opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.2 }}
                            className="overflow-hidden"
                          >
                            <div className="px-4 pb-3 space-y-1">
                              {sectionLessons.map((lesson) => {
                                const isCompleted = completedSet.has(lesson.id)
                                return (
                                  <div
                                    key={lesson.id}
                                    className={`flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${
                                      course.is_enrolled
                                        ? 'hover:bg-surface/50 cursor-pointer'
                                        : ''
                                    }`}
                                    onClick={() => {
                                      if (course.is_enrolled) {
                                        navigate(`/courses/${course.id}/learn/${lesson.id}`)
                                      }
                                    }}
                                  >
                                    {isCompleted ? (
                                      <CheckCircle2 size={16} className="text-green-400 shrink-0" />
                                    ) : (
                                      <Play size={14} className="text-text-secondary shrink-0" />
                                    )}
                                    <span
                                      className={`text-sm flex-1 ${
                                        isCompleted ? 'text-text-secondary line-through' : ''
                                      }`}
                                    >
                                      {lesson.title}
                                    </span>
                                    <span className="text-[10px] text-[#F97316]">+{lesson.xp_reward} XP</span>
                                  </div>
                                )
                              })}
                            </div>
                          </motion.div>
                        )}
                      </AnimatePresence>
                    </div>
                  )
                })}
            </div>
          </Card>
        </motion.div>

        {/* Reviews */}
        <motion.div variants={itemVariants}>
          <Card>
            <h2 className="text-sm font-semibold mb-4">{t('courses.reviews')}</h2>

            {/* Rating breakdown */}
            {course.reviews.length > 0 && (
              <div className="space-y-1.5 mb-5">
                {[5, 4, 3, 2, 1].map((star) => (
                  <div key={star} className="flex items-center gap-2">
                    <span className="text-xs text-text-secondary w-4 text-right">{star}</span>
                    <StarRating rating={star} size={10} />
                    <div className="flex-1 h-2 bg-border rounded-full overflow-hidden">
                      <div
                        className="h-full bg-yellow-400 rounded-full transition-all"
                        style={{
                          width: `${(ratingCounts[star - 1] / maxRatingCount) * 100}%`,
                        }}
                      />
                    </div>
                    <span className="text-[11px] text-text-secondary w-6 text-right">
                      {ratingCounts[star - 1]}
                    </span>
                  </div>
                ))}
              </div>
            )}

            {/* Individual reviews */}
            {course.reviews.length === 0 ? (
              <p className="text-sm text-text-secondary">{t('courses.noReviews')}</p>
            ) : (
              <div className="space-y-4">
                {course.reviews.map((review) => (
                  <div key={review.id} className="border-t border-border pt-3 first:border-0 first:pt-0">
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-sm font-medium">{review.user_name}</span>
                      <StarRating rating={review.rating} size={12} />
                    </div>
                    <p className="text-sm text-text-secondary">{review.comment}</p>
                    <p className="text-[10px] text-text-secondary/60 mt-1">
                      {new Date(review.created_at).toLocaleDateString()}
                    </p>
                  </div>
                ))}
              </div>
            )}
          </Card>
        </motion.div>

        {/* Review Form */}
        {course.is_enrolled && !showReviewForm && !hasReviewed && (
          <motion.div variants={itemVariants}>
            <Button variant="secondary" size="sm" onClick={() => setShowReviewForm(true)}>
              {t('courses.writeReview')}
            </Button>
          </motion.div>
        )}
        {showReviewForm && (
          <motion.div variants={itemVariants}>
            <ReviewForm onSubmit={handleReview} />
          </motion.div>
        )}

        {/* Bottom spacer for mobile sticky bar */}
        <div className="h-20 lg:h-0" />

        {/* Sticky bottom bar (mobile) */}
        <div className="fixed bottom-[80px] left-0 right-0 lg:bottom-0 z-30 lg:relative lg:mt-0">
          <motion.div
            variants={itemVariants}
            className="mx-3 lg:mx-0 mb-2 lg:mb-0"
          >
            <div className="bg-[#0A0A0A]/90 backdrop-blur-xl border border-white/6 rounded-2xl p-4 flex items-center justify-between gap-3 shadow-xl lg:shadow-none">
              <div>
                {course.price === 0 ? (
                  <span className="text-sm font-bold text-[#4ADE80]">{t('courses.free')}</span>
                ) : (
                  <span className="text-sm font-bold text-[#F97316]">
                    {(course.price / 100).toFixed(2)} {course.currency}
                  </span>
                )}
              </div>
              <div className="flex items-center gap-2">
                {course.is_author && (
                  <Button
                    variant="secondary"
                    size="sm"
                    onClick={() => navigate(`/teach/${course.id}`)}
                  >
                    <Pencil size={14} />
                    {t('teach.edit')}
                  </Button>
                )}
                {course.is_enrolled ? (
                  <Button size="sm" onClick={handleStart} disabled={enrolling}>
                    <BookOpen size={14} />
                    {enrolling ? t('common.loading') : t('courses.continue')}
                  </Button>
                ) : pendingPayment ? (
                  <Button size="sm" disabled className="!bg-yellow-500/15 !text-yellow-400 !border-yellow-500/20">
                    <Clock size={14} />
                    Ожидает подтверждения
                  </Button>
                ) : isPaid ? (
                  <Button size="sm" onClick={() => setShowPaymentModal(true)}>
                    <CreditCard size={14} />
                    Купить за {(course.price / 100).toFixed(0)} сом
                  </Button>
                ) : (
                  <Button size="sm" onClick={handleStart} disabled={enrolling}>
                    <BookOpen size={14} />
                    {enrolling ? t('common.loading') : 'Записаться бесплатно'}
                  </Button>
                )}
              </div>
            </div>
          </motion.div>
        </div>
      </motion.div>

      {/* Payment Modal */}
      {showPaymentModal && course && (
        <PaymentModal
          course={{
            id: course.id,
            title: course.title,
            price: course.price,
            currency: course.currency,
          }}
          onClose={() => setShowPaymentModal(false)}
          onSuccess={() => {
            setShowPaymentModal(false)
            paymentApi.myPayments().then(setMyPayments).catch(() => {})
          }}
        />
      )}
    </PageWrapper>
  )
}
