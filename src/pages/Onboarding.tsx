import { useState, useRef, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { Code2, Languages, Headphones, Building2, ArrowRight, Sparkles, Loader2 } from 'lucide-react'
import { Button } from '@/components/ui/Button'
import { Card } from '@/components/ui/Card'
import { DIRECTIONS } from '@/data/directions'
import { useAuthStore } from '@/store/authStore'
import { assessLevel } from '@/services/claudeApi'
import { useTranslation } from '@/hooks/useTranslation'
import type { Direction } from '@/types'
import type { TranslationKey } from '@/lib/i18n'

const iconMap = { Code2, Languages, Headphones, Building2 }
const directionList = Object.values(DIRECTIONS)

const ASSESSMENT_QUESTION_KEYS: Record<Direction, TranslationKey[]> = {
  frontend: [
    'assessment.frontend.q1', 'assessment.frontend.q2', 'assessment.frontend.q3',
    'assessment.frontend.q4', 'assessment.frontend.q5',
  ],
  english: [
    'assessment.english.q1', 'assessment.english.q2', 'assessment.english.q3',
    'assessment.english.q4', 'assessment.english.q5',
  ],
  callcenter: [
    'assessment.callcenter.q1', 'assessment.callcenter.q2', 'assessment.callcenter.q3',
    'assessment.callcenter.q4', 'assessment.callcenter.q5',
  ],
  cib: [
    'assessment.cib.q1', 'assessment.cib.q2', 'assessment.cib.q3',
    'assessment.cib.q4', 'assessment.cib.q5',
  ],
}

export default function Onboarding() {
  const navigate = useNavigate()
  const { t } = useTranslation()
  const { user, updateUser, fetchUser } = useAuthStore()
  const [step, setStep] = useState(0)
  const [selectedDirection, setSelectedDirection] = useState<Direction | null>(null)
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [answers, setAnswers] = useState<string[]>([])
  const [currentAnswer, setCurrentAnswer] = useState('')
  const [chatMessages, setChatMessages] = useState<Array<{ role: 'bot' | 'user'; text: string }>>([])
  const [isLoading, setIsLoading] = useState(false)
  const [isSaving, setIsSaving] = useState(false)
  const [assessmentResult, setAssessmentResult] = useState<'beginner' | 'intermediate' | 'advanced' | null>(null)
  const chatScrollRef = useRef<HTMLDivElement>(null)

  // Auto-scroll chat to bottom when new messages appear
  useEffect(() => {
    if (chatScrollRef.current) {
      chatScrollRef.current.scrollTo({ top: chatScrollRef.current.scrollHeight, behavior: 'smooth' })
    }
  }, [chatMessages, isLoading])

  const handleDirectionSelect = (dir: Direction) => {
    setSelectedDirection(dir)
    setStep(1)
    const questionKeys = ASSESSMENT_QUESTION_KEYS[dir]
    setChatMessages([
      { role: 'bot', text: t('onboarding.chatHi', { name: user?.name || 'there' }) },
      { role: 'bot', text: t(questionKeys[0]) },
    ])
  }

  const handleAnswer = async () => {
    if (!currentAnswer.trim() || !selectedDirection) return

    const newAnswers = [...answers, currentAnswer]
    setAnswers(newAnswers)
    setChatMessages((prev) => [...prev, { role: 'user', text: currentAnswer }])
    setCurrentAnswer('')

    const questionKeys = ASSESSMENT_QUESTION_KEYS[selectedDirection]
    if (currentQuestion < questionKeys.length - 1) {
      setCurrentQuestion((q) => q + 1)
      setChatMessages((prev) => [
        ...prev,
        { role: 'bot', text: t(questionKeys[currentQuestion + 1]) },
      ])
    } else {
      setIsLoading(true)
      setChatMessages((prev) => [
        ...prev,
        { role: 'bot', text: t('onboarding.analyzing') },
      ])

      let level: 'beginner' | 'intermediate' | 'advanced' = 'beginner'
      try {
        level = await assessLevel(DIRECTIONS[selectedDirection].name, newAnswers)
      } catch {
        // fallback to beginner
      }

      setAssessmentResult(level)
      setIsLoading(false)
      setStep(2)
    }
  }

  const handleFinish = async () => {
    if (!selectedDirection || !assessmentResult) return
    setIsSaving(true)
    try {
      await updateUser({
        direction: selectedDirection,
        assessment_level: assessmentResult,
      })
      await fetchUser()
      navigate('/dashboard')
    } catch (err) {
      console.error('Failed to save onboarding data', err)
    } finally {
      setIsSaving(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <div className="flex justify-center gap-2 mb-8">
          {[0, 1, 2].map((i) => (
            <motion.div
              key={i}
              className="h-2 rounded-full"
              animate={{
                width: step === i ? 32 : 8,
                backgroundColor: step >= i ? '#6C63FF' : '#1E1E2E',
              }}
              transition={{ duration: 0.3 }}
            />
          ))}
        </div>

        <AnimatePresence mode="wait">
          {step === 0 && (
            <motion.div
              key="step0"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-6"
            >
              <div className="text-center mb-8">
                <h1 className="text-3xl font-bold mb-2">
                  {t('onboarding.welcome')} <span className="text-primary">{t('app.name.path')}</span>
                  <span className="text-accent">{t('app.name.mind')}</span>
                </h1>
                <p className="text-text-secondary">{t('onboarding.choosePath')}</p>
                {user?.name && (
                  <p className="text-sm text-primary mt-2">{user.name}</p>
                )}
              </div>

              <div className="grid grid-cols-2 gap-4 mt-6">
                {directionList.map((dir) => {
                  const Icon = iconMap[dir.icon as keyof typeof iconMap]
                  return (
                    <Card
                      key={dir.id}
                      hover
                      glow={dir.color}
                      onClick={() => handleDirectionSelect(dir.id)}
                      className="flex flex-col items-center gap-3 text-center cursor-pointer"
                    >
                      <div
                        className="w-12 h-12 rounded-xl flex items-center justify-center"
                        style={{ backgroundColor: `${dir.color}15` }}
                      >
                        <Icon size={24} style={{ color: dir.color }} />
                      </div>
                      <h3 className="font-semibold text-sm">{t(`direction.${dir.id}.name` as any)}</h3>
                      <p className="text-xs text-text-secondary leading-relaxed">
                        {t(`direction.${dir.id}.desc` as any)}
                      </p>
                    </Card>
                  )
                })}
              </div>
            </motion.div>
          )}

          {step === 1 && (
            <motion.div
              key="step1"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="space-y-4"
            >
              <div className="text-center mb-4">
                <h2 className="text-xl font-bold">{t('onboarding.assessment')}</h2>
                <p className="text-text-secondary text-sm">
                  {t('onboarding.question')} {Math.min(currentQuestion + 1, 5)} / 5
                </p>
              </div>

              <Card className="h-80 overflow-hidden p-0">
                <div ref={chatScrollRef} className="h-full overflow-y-auto space-y-3 p-6">
                  {chatMessages.map((msg, i) => (
                    <motion.div
                      key={i}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                      <div
                        className={`max-w-[80%] px-4 py-2.5 rounded-2xl text-sm ${
                          msg.role === 'user'
                            ? 'bg-primary text-white rounded-br-md'
                            : 'bg-border/50 text-text rounded-bl-md'
                        }`}
                      >
                        {msg.text}
                      </div>
                    </motion.div>
                  ))}
                  {isLoading && (
                    <div className="flex justify-start">
                      <div className="bg-border/50 px-4 py-2.5 rounded-2xl rounded-bl-md">
                        <Loader2 className="animate-spin" size={16} />
                      </div>
                    </div>
                  )}
                </div>
              </Card>

              {!isLoading && currentQuestion < 5 && (
                <div className="flex gap-2">
                  <input
                    className="flex-1 bg-bg border border-border rounded-xl px-4 py-2.5 text-sm text-text outline-none focus:border-primary/50 placeholder:text-text-secondary/50"
                    placeholder={t('onboarding.answerPlaceholder')}
                    value={currentAnswer}
                    onChange={(e) => setCurrentAnswer(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleAnswer()}
                  />
                  <Button onClick={handleAnswer} disabled={!currentAnswer.trim()}>
                    <ArrowRight size={18} />
                  </Button>
                </div>
              )}
            </motion.div>
          )}

          {step === 2 && assessmentResult && (
            <motion.div
              key="step2"
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -50 }}
              className="text-center space-y-6"
            >
              <motion.div
                animate={{ scale: [0.8, 1.1, 1] }}
                transition={{ duration: 0.6 }}
              >
                <Sparkles size={48} className="mx-auto text-primary" />
              </motion.div>

              <h2 className="text-2xl font-bold">{t('onboarding.ready')}</h2>

              <Card glow="#6C63FF" className="text-left space-y-3">
                <p className="text-sm text-text-secondary">{t('onboarding.result')}</p>
                <p className="text-lg font-semibold capitalize text-primary">
                  {t(`onboarding.level.${assessmentResult}` as any)}
                </p>
                <p className="text-sm text-text-secondary">
                  {t('onboarding.direction')} {selectedDirection && t(`direction.${selectedDirection}.name` as any)}
                </p>
                <p className="text-sm text-text-secondary">
                  {t('onboarding.planDescription')}
                </p>
              </Card>

              <Button size="lg" onClick={handleFinish} disabled={isSaving}>
                {isSaving ? <Loader2 className="animate-spin" size={18} /> : null}
                {t('onboarding.startLearning')} <ArrowRight size={18} />
              </Button>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  )
}
