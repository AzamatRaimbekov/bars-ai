/**
 * userStore — thin compatibility layer over authStore.
 *
 * All profile data comes from authStore.user (backend, snake_case).
 * This store maps it to the camelCase UserProfile shape that legacy
 * components expect, and provides progress API methods that each
 * refresh authStore.user after completion so the UI stays in sync.
 */
import { create } from 'zustand'
import { apiFetch } from '@/services/api'
import { useAuthStore, type UserData } from '@/store/authStore'
import type { UserProfile, Direction, Level } from '@/types'

// Map backend snake_case UserData → frontend camelCase UserProfile
function mapUserToProfile(user: UserData | null): UserProfile | null {
  if (!user) return null
  return {
    name: user.name,
    direction: user.direction as Direction,
    level: user.level as Level,
    xp: user.xp,
    streak: user.streak,
    lastActiveDate: new Date().toISOString().split('T')[0],
    completedNodes: user.completed_nodes,
    completedLessons: user.completed_lessons,
    earnedBadges: user.earned_badges,
    assessmentLevel: (() => {
      const validLevels = ['beginner', 'intermediate', 'advanced'];
      return validLevels.includes(user.assessment_level) ? user.assessment_level : 'beginner';
    })() as UserProfile['assessmentLevel'],
    onboardingComplete: !!(user.direction && user.direction !== ''),
  }
}

interface UserState {
  // Computed profile — kept in sync with authStore
  profile: UserProfile | null

  // Progress methods — each hits the API then refreshes user data
  addXP: (amount: number, source?: string) => Promise<void>
  completeNode: (nodeId: string) => Promise<void>
  completeLesson: (lessonId: string) => Promise<void>
  earnBadge: (badgeId: string) => Promise<void>
  updateStreak: () => Promise<void>

  // Kept for backwards compatibility in Profile.tsx
  reset: () => void

  // Internal: sync profile from authStore
  _syncProfile: () => void
}

export const useUserStore = create<UserState>()((set) => {
  // Derive the initial profile from whatever authStore already has
  const initialProfile = mapUserToProfile(useAuthStore.getState().user)

  // Subscribe to authStore changes so profile stays in sync
  useAuthStore.subscribe((authState) => {
    set({ profile: mapUserToProfile(authState.user) })
  })

  return {
    profile: initialProfile,

    _syncProfile: () => {
      set({ profile: mapUserToProfile(useAuthStore.getState().user) })
    },

    addXP: async (amount, source = 'activity') => {
      await apiFetch('/progress/xp', {
        method: 'POST',
        body: JSON.stringify({ amount, source }),
      })
      await useAuthStore.getState().fetchUser()
    },

    completeNode: async (nodeId) => {
      await apiFetch('/progress/node', {
        method: 'POST',
        body: JSON.stringify({ node_id: nodeId }),
      })
      await useAuthStore.getState().fetchUser()
    },

    completeLesson: async (lessonId) => {
      await apiFetch('/progress/lesson', {
        method: 'POST',
        body: JSON.stringify({ lesson_id: lessonId }),
      })
      await useAuthStore.getState().fetchUser()
    },

    earnBadge: async (badgeId) => {
      await apiFetch('/progress/badge', {
        method: 'POST',
        body: JSON.stringify({ badge_id: badgeId }),
      })
      await useAuthStore.getState().fetchUser()
    },

    updateStreak: async () => {
      await apiFetch('/progress/streak', { method: 'POST' })
      await useAuthStore.getState().fetchUser()
    },

    reset: () => {
      // In the backend-backed world "reset" means logout
      useAuthStore.getState().logout()
    },
  }
})
