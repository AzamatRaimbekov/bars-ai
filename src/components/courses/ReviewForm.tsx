import { useState } from 'react'
import { Button } from '@/components/ui/Button'
import { Card } from '@/components/ui/Card'
import { StarRating } from './StarRating'
import { useTranslation } from '@/hooks/useTranslation'

interface ReviewFormProps {
  onSubmit: (rating: number, comment: string) => Promise<void>
}

export function ReviewForm({ onSubmit }: ReviewFormProps) {
  const { t } = useTranslation()
  const [rating, setRating] = useState(0)
  const [comment, setComment] = useState('')
  const [submitting, setSubmitting] = useState(false)

  const handleSubmit = async () => {
    if (rating === 0) return
    setSubmitting(true)
    try {
      await onSubmit(rating, comment)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <Card className="space-y-4">
      <h3 className="text-sm font-semibold">{t('courses.writeReview')}</h3>
      <div className="flex items-center gap-3">
        <StarRating rating={rating} clickable onChange={setRating} size={24} />
        {rating > 0 && (
          <span className="text-sm text-text-secondary">{rating}/5</span>
        )}
      </div>
      <textarea
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        placeholder={t('courses.writeReview')}
        rows={3}
        className="w-full rounded-xl border border-border bg-bg px-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-primary/50 resize-none text-sm"
      />
      <Button
        size="sm"
        disabled={rating === 0 || submitting}
        onClick={handleSubmit}
      >
        {submitting ? t('common.loading') : t('common.submit')}
      </Button>
    </Card>
  )
}
