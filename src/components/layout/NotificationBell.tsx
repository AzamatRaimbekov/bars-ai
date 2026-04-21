import { useState, useEffect, useRef, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Bell, CheckCircle, XCircle, Info, X } from "lucide-react";
import { notificationApi, type NotificationItem } from "@/services/notificationApi";

function timeAgo(dateStr: string): string {
  const now = Date.now();
  const then = new Date(dateStr).getTime();
  const diff = Math.floor((now - then) / 1000);

  if (diff < 60) return "только что";
  if (diff < 3600) {
    const m = Math.floor(diff / 60);
    return `${m} мин назад`;
  }
  if (diff < 86400) {
    const h = Math.floor(diff / 3600);
    return `${h} ч назад`;
  }
  const d = Math.floor(diff / 86400);
  if (d === 1) return "вчера";
  return `${d} дн назад`;
}

function TypeIcon({ type }: { type: string }) {
  if (type === "course_approved")
    return <CheckCircle size={16} className="text-[#4ADE80] shrink-0" />;
  if (type === "course_rejected")
    return <XCircle size={16} className="text-[#F87171] shrink-0" />;
  return <Info size={16} className="text-[#60A5FA] shrink-0" />;
}

export function NotificationBell() {
  const navigate = useNavigate();
  const [unreadCount, setUnreadCount] = useState(0);
  const [open, setOpen] = useState(false);
  const [notifications, setNotifications] = useState<NotificationItem[]>([]);
  const [loading, setLoading] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  // Poll unread count every 30s
  const fetchUnreadCount = useCallback(() => {
    notificationApi.unreadCount().then((r) => setUnreadCount(r.count)).catch(() => {});
  }, []);

  useEffect(() => {
    fetchUnreadCount();
    const interval = setInterval(fetchUnreadCount, 30_000);
    return () => clearInterval(interval);
  }, [fetchUnreadCount]);

  // Close on outside click
  useEffect(() => {
    function handleClick(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    if (open) {
      document.addEventListener("mousedown", handleClick);
      return () => document.removeEventListener("mousedown", handleClick);
    }
  }, [open]);

  const handleOpen = async () => {
    if (open) {
      setOpen(false);
      return;
    }
    setOpen(true);
    setLoading(true);
    try {
      const list = await notificationApi.list();
      setNotifications(list.slice(0, 20));
    } catch {
      setNotifications([]);
    } finally {
      setLoading(false);
    }
  };

  const handleClickNotification = async (n: NotificationItem) => {
    if (!n.is_read) {
      try {
        await notificationApi.markRead(n.id);
        setNotifications((prev) =>
          prev.map((x) => (x.id === n.id ? { ...x, is_read: true } : x))
        );
        setUnreadCount((c) => Math.max(0, c - 1));
      } catch {}
    }
    if (n.link) {
      setOpen(false);
      navigate(n.link);
    }
  };

  const handleMarkAllRead = async () => {
    try {
      await notificationApi.markAllRead();
      setNotifications((prev) => prev.map((x) => ({ ...x, is_read: true })));
      setUnreadCount(0);
    } catch {}
  };

  return (
    <div ref={ref} className="relative">
      <button
        onClick={handleOpen}
        className="relative p-2 rounded-xl text-white/40 hover:text-white hover:bg-white/[0.06] transition-colors"
        aria-label="Уведомления"
      >
        <Bell size={18} />
        {unreadCount > 0 && (
          <span className="absolute -top-0.5 -right-0.5 min-w-[18px] h-[18px] flex items-center justify-center rounded-full bg-[#F97316] text-[10px] font-bold text-white px-1 leading-none">
            {unreadCount > 99 ? "99+" : unreadCount}
          </span>
        )}
      </button>

      {open && (
        <div className="absolute right-0 top-full mt-2 w-80 sm:w-96 bg-[#0A0A0A] border border-white/10 rounded-2xl shadow-2xl z-50 overflow-hidden">
          {/* Header */}
          <div className="flex items-center justify-between px-4 py-3 border-b border-white/[0.06]">
            <h3 className="text-sm font-semibold text-white">Уведомления</h3>
            <button
              onClick={() => setOpen(false)}
              className="text-white/30 hover:text-white transition-colors"
            >
              <X size={16} />
            </button>
          </div>

          {/* List */}
          <div className="max-h-[400px] overflow-y-auto">
            {loading ? (
              <div className="py-10 text-center text-white/30 text-sm">Загрузка...</div>
            ) : notifications.length === 0 ? (
              <div className="py-10 text-center text-white/30 text-sm">Нет уведомлений</div>
            ) : (
              notifications.map((n) => (
                <button
                  key={n.id}
                  onClick={() => handleClickNotification(n)}
                  className={`w-full text-left px-4 py-3 flex items-start gap-3 hover:bg-white/[0.04] transition-colors border-b border-white/[0.04] last:border-b-0 ${
                    !n.is_read ? "bg-white/[0.02]" : ""
                  }`}
                >
                  <div className="mt-0.5">
                    <TypeIcon type={n.type} />
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      {!n.is_read && (
                        <span className="w-1.5 h-1.5 rounded-full bg-[#F97316] shrink-0" />
                      )}
                      <span className="text-sm font-medium text-white truncate">{n.title}</span>
                    </div>
                    <p className="text-xs text-white/40 mt-0.5 line-clamp-2">{n.message}</p>
                    <span className="text-[10px] text-white/20 mt-1 block">
                      {timeAgo(n.created_at)}
                    </span>
                  </div>
                </button>
              ))
            )}
          </div>

          {/* Footer */}
          {notifications.length > 0 && (
            <div className="px-4 py-2.5 border-t border-white/[0.06]">
              <button
                onClick={handleMarkAllRead}
                className="w-full text-center text-xs font-medium text-[#F97316] hover:text-[#FB923C] transition-colors"
              >
                Прочитать все
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
