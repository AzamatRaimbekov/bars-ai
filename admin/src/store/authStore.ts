import { create } from "zustand";
import { apiFetch } from "../lib/api";

interface AuthState {
  token: string | null;
  adminName: string | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  hydrate: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: null,
  adminName: null,
  isAuthenticated: false,

  login: async (email: string, password: string) => {
    const data = await apiFetch<{ access_token: string }>("/api/auth/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
    });
    sessionStorage.setItem("bars_admin_token", data.access_token);
    sessionStorage.setItem("bars_admin_email", email);
    set({
      token: data.access_token,
      adminName: email,
      isAuthenticated: true,
    });
  },

  logout: () => {
    sessionStorage.removeItem("bars_admin_token");
    sessionStorage.removeItem("bars_admin_email");
    set({ token: null, adminName: null, isAuthenticated: false });
    window.location.href = "/login";
  },

  hydrate: () => {
    const token = sessionStorage.getItem("bars_admin_token");
    const email = sessionStorage.getItem("bars_admin_email");
    if (token) {
      set({ token, adminName: email, isAuthenticated: true });
    }
  },
}));
