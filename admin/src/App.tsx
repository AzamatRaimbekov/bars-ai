import { useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuthStore } from "./store/authStore";
import Layout from "./components/Layout";
import ProtectedRoute from "./components/ProtectedRoute";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import UsersPage from "./pages/UsersPage";
import CoursesPage from "./pages/CoursesPage";
import PaymentsPage from "./pages/PaymentsPage";
import SprintsPage from "./pages/SprintsPage";
import ModerationPage from "./pages/ModerationPage";
import AICoursePage from "./pages/AICoursePage";

export default function App() {
  const hydrate = useAuthStore((s) => s.hydrate);

  useEffect(() => {
    hydrate();
  }, [hydrate]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          element={
            <ProtectedRoute>
              <Layout />
            </ProtectedRoute>
          }
        >
          <Route path="/" element={<Dashboard />} />
          <Route path="/users" element={<UsersPage />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/moderation" element={<ModerationPage />} />
          <Route path="/payments" element={<PaymentsPage />} />
          <Route path="/sprints" element={<SprintsPage />} />
          <Route path="/ai-course" element={<AICoursePage />} />
        </Route>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
