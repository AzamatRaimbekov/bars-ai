const API_URL = import.meta.env.VITE_API_URL || "";

export async function apiFetch<T>(
  path: string,
  options?: RequestInit
): Promise<T> {
  const token = sessionStorage.getItem("bars_admin_token");
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options?.headers,
    },
  });
  if (res.status === 401) {
    sessionStorage.removeItem("bars_admin_token");
    window.location.href = "/login";
    throw new Error("Unauthorized");
  }
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
