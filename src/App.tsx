import { useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuthStore } from "@/store/authStore";
import Login from "@/pages/Login";
import Register from "@/pages/Register";
import Onboarding from "@/pages/Onboarding";
import Dashboard from "@/pages/Dashboard";
import Roadmap from "@/pages/Roadmap";
import Mentor from "@/pages/Mentor";
import Simulator from "@/pages/Simulator";
import Lesson from "@/pages/Lesson";
import Achievements from "@/pages/Achievements";
import Profile from "@/pages/Profile";
import { Loader2 } from "lucide-react";

function AuthGuard({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading } = useAuthStore();

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Loader2 className="animate-spin text-primary" size={32} />
      </div>
    );
  }

  if (!isAuthenticated) return <Navigate to="/login" replace />;
  return <>{children}</>;
}

export default function App() {
  const tryRestore = useAuthStore((s) => s.tryRestore);

  useEffect(() => {
    tryRestore();
  }, [tryRestore]);

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
