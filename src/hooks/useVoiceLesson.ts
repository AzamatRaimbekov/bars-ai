import { useState, useCallback } from 'react'
import { mentorApi, type VoiceLessonResponse } from '@/services/mentorApi'

type Phase = 'idle' | 'intro' | 'explain' | 'check' | 'practice' | 'summary' | 'complete'

export function useVoiceLesson(sessionId: string | null) {
  const [phase, setPhase] = useState<Phase>('idle')
  const [progress, setProgress] = useState(0)
  const [lastResponse, setLastResponse] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleResponse = useCallback((res: VoiceLessonResponse) => {
    setPhase(res.is_complete ? 'complete' : res.phase as Phase)
    setProgress(res.progress)
    setLastResponse(res.content)
  }, [])

  const start = useCallback(async (topic: string) => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'start', topic)
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const next = useCallback(async () => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'next')
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const answer = useCallback(async (content: string) => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'answer', undefined, content)
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const repeat = useCallback(async () => {
    if (!sessionId) return null
    setIsLoading(true)
    try {
      const res = await mentorApi.voiceLesson(sessionId, 'repeat')
      handleResponse(res)
      return res
    } finally {
      setIsLoading(false)
    }
  }, [sessionId, handleResponse])

  const reset = useCallback(() => {
    setPhase('idle')
    setProgress(0)
    setLastResponse('')
  }, [])

  return { phase, progress, lastResponse, isLoading, start, next, answer, repeat, reset }
}
