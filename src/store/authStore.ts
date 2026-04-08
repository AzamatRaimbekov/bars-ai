import { create } from 'zustand'
import { apiFetch, setAccessToken } from '@/services/api'
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
  updateUser: (data: Partial<Pick<UserData, 'name' | 'language' | 'avatar_url' | 'direction' | 'assessment_level'>>) => Promise<void>
  tryRestore: () => Promise<void>
}

export const useAuthStore = create<AuthState>()((set) => ({
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
        set({ isLoading: false })
      }
    } catch {
      set({ isLoading: false })
    }
  },
}))
