import { apiFetch } from './api'

export interface Session {
  id: string
  direction: string
  title: string
  created_at: string
  updated_at: string
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  created_at: string
}

export interface KnowledgeProfile {
  direction: string
  strengths: string[]
  weaknesses: string[]
  notes: string[]
  updated_at: string
}

export interface RecommendationItem {
  lesson_id: string
  lesson_title: string
  course_title: string
  reason: string
  priority: string
}

export interface Recommendations {
  weekly_plan: RecommendationItem[]
  stats: {
    completed_percentage: number
    strong_topics: string[]
    weak_topics: string[]
  }
}

export interface ChatResponse {
  content: string
  session_id: string
  message_id: string
}

export interface VoiceLessonResponse {
  phase: string
  content: string
  exercise: Record<string, unknown> | null
  progress: number
  is_complete: boolean
}

export const mentorApi = {
  getSessions: () => apiFetch<Session[]>('/mentor/sessions'),

  createSession: (direction: string, title?: string) =>
    apiFetch<Session>('/mentor/sessions', {
      method: 'POST',
      body: JSON.stringify({ direction, title }),
    }),

  getMessages: (sessionId: string, limit = 50, offset = 0) =>
    apiFetch<Message[]>(`/mentor/sessions/${sessionId}/messages?limit=${limit}&offset=${offset}`),

  deleteSession: (sessionId: string) =>
    apiFetch<{ ok: boolean }>(`/mentor/sessions/${sessionId}`, { method: 'DELETE' }),

  getProfile: () => apiFetch<KnowledgeProfile>('/mentor/profile'),

  chat: (content: string, sessionId?: string) =>
    apiFetch<ChatResponse>('/mentor/chat', {
      method: 'POST',
      body: JSON.stringify({ content, session_id: sessionId }),
    }),

  getRecommendations: () => apiFetch<Recommendations>('/mentor/recommendations'),

  voiceLesson: (sessionId: string, action: string, topic?: string, content?: string) =>
    apiFetch<VoiceLessonResponse>('/mentor/voice-lesson', {
      method: 'POST',
      body: JSON.stringify({ session_id: sessionId, action, topic, content }),
    }),
}
