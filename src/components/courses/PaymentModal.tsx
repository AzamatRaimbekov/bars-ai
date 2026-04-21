import { useState, useRef } from 'react'
import { X, Upload, CheckCircle2, Loader2, Image as ImageIcon, CreditCard } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'
import { paymentApi } from '@/services/paymentApi'

interface PaymentModalProps {
  course: { id: string; title: string; price: number; currency: string }
  onClose: () => void
  onSuccess: () => void
}

export function PaymentModal({ course, onClose, onSuccess }: PaymentModalProps) {
  const [screenshot, setScreenshot] = useState<string | null>(null)
  const [submitting, setSubmitting] = useState(false)
  const [success, setSuccess] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const fileRef = useRef<HTMLInputElement>(null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    setError(null)
    const reader = new FileReader()
    reader.onload = () => {
      setScreenshot(reader.result as string)
    }
    reader.onerror = () => {
      setError('Не удалось загрузить файл')
    }
    reader.readAsDataURL(file)
  }

  const handleSubmit = async () => {
    if (!screenshot) return
    setSubmitting(true)
    setError(null)
    try {
      await paymentApi.create(course.id, screenshot)
      setSuccess(true)
      setTimeout(() => {
        onSuccess()
      }, 2000)
    } catch (err: any) {
      setError(err.message || 'Ошибка при отправке заявки')
    } finally {
      setSubmitting(false)
    }
  }

  const displayPrice = course.price > 0 ? (course.price / 100).toFixed(0) : '0'

  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm"
        onClick={(e) => {
          if (e.target === e.currentTarget) onClose()
        }}
      >
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 20 }}
          className="bg-[#0A0A0A] border border-white/10 rounded-2xl w-full max-w-md overflow-hidden"
        >
          {/* Header */}
          <div className="flex items-center justify-between px-5 py-4 border-b border-white/6">
            <div className="flex items-center gap-2">
              <CreditCard size={16} className="text-[#F97316]" />
              <h2 className="text-base font-semibold text-white">Оплата курса</h2>
            </div>
            <button
              onClick={onClose}
              className="text-white/30 hover:text-white/60 transition-colors cursor-pointer"
            >
              <X size={18} />
            </button>
          </div>

          <div className="p-5 space-y-5">
            {success ? (
              /* Success State */
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center py-6 space-y-3"
              >
                <div className="w-14 h-14 rounded-full bg-green-500/10 flex items-center justify-center mx-auto">
                  <CheckCircle2 size={28} className="text-green-400" />
                </div>
                <h3 className="text-base font-semibold text-white">Заявка отправлена!</h3>
                <p className="text-sm text-white/40">Ожидайте подтверждения.</p>
              </motion.div>
            ) : (
              <>
                {/* Course Info */}
                <div className="bg-white/[0.03] border border-white/6 rounded-xl p-4 space-y-2">
                  <p className="text-sm text-white font-medium">{course.title}</p>
                  <p className="text-lg font-bold text-[#F97316]">
                    {displayPrice} {course.currency}
                  </p>
                </div>

                {/* Payment Instructions */}
                <div className="space-y-2">
                  <h3 className="text-sm font-semibold text-white">Инструкция по оплате</h3>
                  <div className="bg-white/[0.03] border border-white/6 rounded-xl p-4 space-y-2 text-sm">
                    <p className="text-white/60">
                      Переведите <span className="text-white font-medium">{displayPrice} {course.currency}</span> на MBank
                    </p>
                    <p className="text-white/60">
                      Номер: <span className="text-white font-mono font-medium">0XXX XXX XXX</span>
                    </p>
                    <p className="text-white/60">
                      Назначение: <span className="text-white/80">Оплата курса &laquo;{course.title}&raquo;</span>
                    </p>
                  </div>
                </div>

                {/* Screenshot Upload */}
                <div className="space-y-2">
                  <h3 className="text-sm font-semibold text-white">Скриншот оплаты</h3>
                  <input
                    ref={fileRef}
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                    className="hidden"
                  />

                  {screenshot ? (
                    <div className="relative">
                      <img
                        src={screenshot}
                        alt="Скриншот оплаты"
                        className="w-full max-h-48 object-contain rounded-xl border border-white/6"
                      />
                      <button
                        onClick={() => {
                          setScreenshot(null)
                          if (fileRef.current) fileRef.current.value = ''
                        }}
                        className="absolute top-2 right-2 w-7 h-7 rounded-full bg-black/70 border border-white/10 flex items-center justify-center text-white/60 hover:text-white transition-colors cursor-pointer"
                      >
                        <X size={14} />
                      </button>
                    </div>
                  ) : (
                    <button
                      onClick={() => fileRef.current?.click()}
                      className="w-full border border-dashed border-white/10 rounded-xl p-6 flex flex-col items-center gap-2 text-white/30 hover:text-white/50 hover:border-white/20 transition-colors cursor-pointer"
                    >
                      <ImageIcon size={24} />
                      <span className="text-sm">Нажмите, чтобы загрузить скриншот</span>
                    </button>
                  )}
                </div>

                {/* Error */}
                {error && (
                  <p className="text-sm text-red-400 bg-red-400/10 rounded-xl px-4 py-2">{error}</p>
                )}

                {/* Submit */}
                <button
                  onClick={handleSubmit}
                  disabled={!screenshot || submitting}
                  className="w-full bg-[#F97316] hover:bg-[#EA6C0E] disabled:opacity-40 disabled:cursor-not-allowed text-white font-medium text-sm rounded-xl px-4 py-3 flex items-center justify-center gap-2 transition-colors cursor-pointer"
                >
                  {submitting ? (
                    <>
                      <Loader2 size={16} className="animate-spin" />
                      Отправка...
                    </>
                  ) : (
                    <>
                      <Upload size={16} />
                      Отправить на проверку
                    </>
                  )}
                </button>
              </>
            )}
          </div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  )
}
