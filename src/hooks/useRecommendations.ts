import { useState, useEffect } from 'react'
import { mentorApi, type Recommendations } from '@/services/mentorApi'

export function useRecommendations() {
  const [data, setData] = useState<Recommendations | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    mentorApi.getRecommendations()
      .then(setData)
      .catch(err => console.error('Failed to load recommendations:', err))
      .finally(() => setIsLoading(false))
  }, [])

  return { recommendations: data, isLoading }
}
