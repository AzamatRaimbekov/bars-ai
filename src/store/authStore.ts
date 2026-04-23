import { create } from 'zustand'
import { apiFetch, setAccessToken, getAccessToken } from '@/services/api'
import * as authApi from '@/services/authApi'

export interface UserData {
  id: string
  email: string
  name: string
  direction: string
  assessment_level: string
  language: string
  avatar_url: string | null
  xp: number
  level: string
  streak: number
  longest_streak: number
  completed_nodes: string[]
  completed_lessons: string[]
  earned_badges: string[]
  role: string
  interests: string[]
  onboarding_complete: boolean
}

interface AuthState {
  user: UserData | null
  isAuthenticated: boolean
  isLoading: boolean
  register: (params: {
    email: string
    password: string
    name: string
    direction: string
    assessment_level?: string
    language?: string
  }) => Promise<void>
  login: (email: string, password: string) => Promise<void>
  logout: () => Promise<void>
  fetchUser: () => Promise<void>
  updateUser: (data: Partial<Pick<UserData, 'name' | 'language' | 'avatar_url' | 'direction' | 'assessment_level' | 'interests' | 'onboarding_complete'>> & { assessment_context?: string }) => Promise<void>
  tryRestore: () => Promise<void>
}

export const useAuthStore = create<AuthState>()((set) => {
  // Auto-logout when refresh token fails
  if (typeof window !== 'undefined') {
    window.addEventListener('auth:session-expired', () => {
      set({ user: null, isAuthenticated: false })
    })
  }

  return {
  user: null,
  isAuthenticated: false,
  isLoading: true,

  register: async (params) => {
    await authApi.register(params)
    const user = await apiFetch<UserData>('/users/me')
    set({ user, isAuthenticated: true })
  },

  login: async (email, password) => {
    await authApi.login(email, password)
    const user = await apiFetch<UserData>('/users/me')
    set({ user, isAuthenticated: true })
  },

  logout: async () => {
    await authApi.logout()
    set({ user: null, isAuthenticated: false })
  },

  fetchUser: async () => {
    const user = await apiFetch<UserData>('/users/me')
    set({ user, isAuthenticated: true })
  },

  updateUser: async (data) => {
    await apiFetch('/users/me', {
      method: 'PATCH',
      body: JSON.stringify(data),
    })
    const user = await apiFetch<UserData>('/users/me')
    set({ user })
  },

  tryRestore: async () => {
    try {
      // If we have a cached token in sessionStorage, try using it first
      if (getAccessToken()) {
        try {
          const user = await apiFetch<UserData>('/users/me')
          set({ user, isAuthenticated: true, isLoading: false })
          return
        } catch {
          // Token expired or invalid, fall through to refresh
        }
      }

      // Try refreshing via httpOnly cookie
      const resp = await fetch('/api/auth/refresh', {
        method: 'POST',
        credentials: 'include',
      })
      if (resp.ok) {
        const data = await resp.json()
        setAccessToken(data.access_token)
        const user = await apiFetch<UserData>('/users/me')
        set({ user, isAuthenticated: true, isLoading: false })
      } else {
        setAccessToken(null)
        set({ isLoading: false })
      }
    } catch {
      setAccessToken(null)
      set({ isLoading: false })
    }
  },
}})
