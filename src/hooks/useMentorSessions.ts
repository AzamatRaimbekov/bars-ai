import { useState, useEffect, useCallback } from 'react'
import { mentorApi, type Session, type Message } from '@/services/mentorApi'

export function useMentorSessions() {
  const [sessions, setSessions] = useState<Session[]>([])
  const [activeSession, setActiveSession] = useState<Session | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const loadSessions = useCallback(async () => {
    try {
      const data = await mentorApi.getSessions()
      setSessions(data)
    } catch (err) {
      console.error('Failed to load sessions:', err)
    }
  }, [])

  const createSession = useCallback(async (direction: string) => {
    const session = await mentorApi.createSession(direction)
    setSessions(prev => [session, ...prev])
    setActiveSession(session)
    setMessages([])
    return session
  }, [])

  const selectSession = useCallback(async (session: Session) => {
    setActiveSession(session)
    setIsLoading(true)
    try {
      const msgs = await mentorApi.getMessages(session.id)
      setMessages(msgs)
    } catch (err) {
      console.error('Failed to load messages:', err)
    } finally {
      setIsLoading(false)
    }
  }, [])

  const deleteSession = useCallback(async (sessionId: string) => {
    await mentorApi.deleteSession(sessionId)
    setSessions(prev => prev.filter(s => s.id !== sessionId))
    if (activeSession?.id === sessionId) {
      setActiveSession(null)
      setMessages([])
    }
  }, [activeSession])

  const addMessage = useCallback((msg: Message) => {
    setMessages(prev => [...prev, msg])
  }, [])

  useEffect(() => { loadSessions() }, [loadSessions])

  return {
    sessions, activeSession, messages, isLoading,
    createSession, selectSession, deleteSession, addMessage,
    setActiveSession,
  }
}
