import { useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom'
import { useAuthStore } from '@/store/authStore'
import { LoadingScreen } from '@/components/ui/LoadingScreen'
import Login from '@/pages/Login'
import Register from '@/pages/Register'
import Onboarding from '@/pages/Onboarding'
import Dashboard from '@/pages/Dashboard'
import Roadmap from '@/pages/Roadmap'
import Mentor from '@/pages/Mentor'
import Simulator from '@/pages/Simulator'
import Lesson from '@/pages/Lesson'
import Achievements from '@/pages/Achievements'
import Leaderboard from '@/pages/Leaderboard'
import Leagues from '@/pages/Leagues'
import Profile from '@/pages/Profile'
import Courses from '@/pages/Courses'
import CourseDetail from '@/pages/CourseDetail'
import CourseLearn from '@/pages/CourseLearn'
import CourseRoadmap from '@/pages/CourseRoadmap'
import Teach from '@/pages/Teach'
import CourseEditor from '@/pages/CourseEditor'
import Sprint from '@/pages/Sprint'
import Admin from '@/pages/Admin'
import { Loader2 } from 'lucide-react'

function AuthGuard({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading, user } = useAuthStore()
  const location = useLocation()

  if (isLoading) {
    return <LoadingScreen />
  }

  if (!isAuthenticated) return <Navigate to="/login" replace />

  // If user hasn't completed onboarding, redirect to /
  const onboardingComplete = !!user?.onboarding_complete
  const isOnboardingRoute = location.pathname === '/'

  if (!onboardingComplete && !isOnboardingRoute) {
    return <Navigate to="/" replace />
  }

  // If user has already completed onboarding, don't let them back to /
  if (onboardingComplete && isOnboardingRoute) {
    return <Navigate to="/dashboard" replace />
  }

  return <>{children}</>
}

export default function App() {
  const tryRestore = useAuthStore((s) => s.tryRestore)

  useEffect(() => {
    tryRestore()
  }, [tryRestore])

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/"
          element={
            <AuthGuard>
              <Onboarding />
            </AuthGuard>
          }
        />
        <Route
          path="/dashboard"
          element={
            <AuthGuard>
              <Dashboard />
            </AuthGuard>
          }
        />
        <Route
          path="/roadmap"
          element={
            <AuthGuard>
              <Roadmap />
            </AuthGuard>
          }
        />
        <Route
          path="/mentor"
          element={
            <AuthGuard>
              <Mentor />
            </AuthGuard>
          }
        />
        <Route
          path="/simulator"
          element={
            <AuthGuard>
              <Simulator />
            </AuthGuard>
          }
        />
        <Route
          path="/lesson/:id"
          element={
            <AuthGuard>
              <Lesson />
            </AuthGuard>
          }
        />
        <Route
          path="/achievements"
          element={
            <AuthGuard>
              <Achievements />
            </AuthGuard>
          }
        />
        <Route
          path="/leaderboard"
          element={
            <AuthGuard>
              <Leaderboard />
            </AuthGuard>
          }
        />
        <Route
          path="/leagues"
          element={
            <AuthGuard>
              <Leagues />
            </AuthGuard>
          }
        />
        <Route
          path="/profile"
          element={
            <AuthGuard>
              <Profile />
            </AuthGuard>
          }
        />
        <Route path="/courses" element={<Courses />} />
        <Route path="/courses/:id" element={<CourseDetail />} />
        <Route
          path="/courses/:id/roadmap"
          element={
            <AuthGuard>
              <CourseRoadmap />
            </AuthGuard>
          }
        />
        <Route
          path="/courses/:id/learn/:lessonId"
          element={
            <AuthGuard>
              <CourseLearn />
            </AuthGuard>
          }
        />
        <Route
          path="/teach"
          element={
            <AuthGuard>
              <Teach />
            </AuthGuard>
          }
        />
        <Route
          path="/teach/:id"
          element={
            <AuthGuard>
              <CourseEditor />
            </AuthGuard>
          }
        />
        <Route
          path="/sprint"
          element={
            <AuthGuard>
              <Sprint />
            </AuthGuard>
          }
        />
        <Route
          path="/admin"
          element={
            <AuthGuard>
              <Admin />
            </AuthGuard>
          }
        />
      </Routes>
    </BrowserRouter>
  )
}
