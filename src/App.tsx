import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useUserStore } from "@/store/userStore";
import Onboarding from "@/pages/Onboarding";
import Dashboard from "@/pages/Dashboard";
import Roadmap from "@/pages/Roadmap";
import Mentor from "@/pages/Mentor";
import Simulator from "@/pages/Simulator";
import Lesson from "@/pages/Lesson";
import Achievements from "@/pages/Achievements";
import Profile from "@/pages/Profile";

function AuthGuard({ children }: { children: React.ReactNode }) {
  const profile = useUserStore((s) => s.profile);
  if (!profile?.onboardingComplete) return <Navigate to="/" replace />;
  return <>{children}</>;
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Onboarding />} />
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
          path="/profile"
          element={
            <AuthGuard>
              <Profile />
            </AuthGuard>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
