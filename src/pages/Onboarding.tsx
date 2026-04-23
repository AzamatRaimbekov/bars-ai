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
