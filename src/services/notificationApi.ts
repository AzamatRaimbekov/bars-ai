import { apiFetch } from "./api";

export interface NotificationItem {
  id: string;
  title: string;
  message: string;
  type: string;
  is_read: boolean;
  link: string | null;
  created_at: string;
}

export const notificationApi = {
  list: () => apiFetch<NotificationItem[]>("/notifications"),
  unreadCount: () => apiFetch<{ count: number }>("/notifications/unread-count"),
  markRead: (id: string) => apiFetch<{ ok: boolean }>(`/notifications/${id}/read`, { method: "POST" }),
  markAllRead: () => apiFetch<{ ok: boolean }>("/notifications/read-all", { method: "POST" }),
};
