import { apiFetch } from './api'

export interface Sprint {
  id: string
  title: string
  start_date: string
  end_date: string
  status: string
  prizes: { place: number; amount: number; currency: string; bonus?: string }[]
  winners: { user_id: string; name: string; place: number; trophies: number; prize: any }[] | null
}

export interface LeaderboardEntry {
  user_id: string
  name: string
  avatar_url: string | null
  trophies: number
  place: number
}

export interface MyTrophies {
  total: number
  sprint: number
}

export const sprintApi = {
  getActive: () => apiFetch<Sprint>('/sprints/active'),
  getLeaderboard: () => apiFetch<LeaderboardEntry[]>('/sprints/active/leaderboard'),
  getMyTrophies: () => apiFetch<MyTrophies>('/sprints/my-trophies'),
  getHistory: () => apiFetch<Sprint[]>('/sprints/history'),
  awardTrophy: (action: string, metadata?: Record<string, string>) =>
    apiFetch('/sprints/trophy', { method: 'POST', body: JSON.stringify({ action, metadata }) }),
}

export const adminApi = {
  getSprints: () => apiFetch<Sprint[]>('/admin/sprints'),
  createSprint: (data: { title: string; start_date: string; end_date: string; prizes?: any[] }) =>
    apiFetch<Sprint>('/admin/sprints', { method: 'POST', body: JSON.stringify(data) }),
  closeSprint: (id: string) => apiFetch('/admin/sprints/' + id + '/close', { method: 'POST' }),
  cancelSprint: (id: string) => apiFetch('/admin/sprints/' + id + '/cancel', { method: 'POST' }),
  getUsers: () => apiFetch<any[]>('/admin/users'),
  getStats: () => apiFetch<any>('/admin/stats'),
}
