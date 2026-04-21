import { apiFetch } from "./api";

export interface PaymentRequest {
  id: string;
  course_id: string;
  course_title: string;
  user_name: string;
  user_email: string;
  amount: number;
  currency: string;
  screenshot_url: string;
  status: "pending" | "approved" | "rejected";
  admin_note: string | null;
  created_at: string;
  reviewed_at: string | null;
}

export const paymentApi = {
  create: (courseId: string, screenshotUrl: string) =>
    apiFetch<PaymentRequest>("/payments/request", {
      method: "POST",
      body: JSON.stringify({ course_id: courseId, screenshot_url: screenshotUrl }),
    }),

  myPayments: () => apiFetch<PaymentRequest[]>("/payments/my"),

  adminList: () => apiFetch<PaymentRequest[]>("/admin/payments"),

  review: (paymentId: string, action: "approve" | "reject", note?: string) =>
    apiFetch<PaymentRequest>(`/admin/payments/${paymentId}/review`, {
      method: "POST",
      body: JSON.stringify({ action, note }),
    }),
};
