import { apiFetch, setAccessToken } from "./api";

interface AuthResponse {
  access_token: string;
  token_type: string;
}

interface RegisterParams {
  email: string;
  password: string;
  name: string;
  direction: string;
  assessment_level?: string;
  language?: string;
}

export async function register(params: RegisterParams): Promise<void> {
  const data = await apiFetch<AuthResponse>("/auth/register", {
    method: "POST",
    body: JSON.stringify(params),
  });
  setAccessToken(data.access_token);
}

export async function login(email: string, password: string): Promise<void> {
  const data = await apiFetch<AuthResponse>("/auth/login", {
    method: "POST",
    body: JSON.stringify({ email, password }),
  });
  setAccessToken(data.access_token);
}

export async function logout(): Promise<void> {
  try {
    await apiFetch("/auth/logout", { method: "POST" });
  } finally {
    setAccessToken(null);
  }
}
