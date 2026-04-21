import { useEffect, useState } from 'react'
import { Navigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Trophy, Users, BarChart3, Plus, X, Clock, Loader2, Search, Ban, CreditCard, CheckCircle2, XCircle, Eye, Image as ImageIcon } from 'lucide-react'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Button } from '@/components/ui/Button'
import { SprintLeaderboard } from '@/components/sprint/SprintLeaderboard'
import { useAuthStore } from '@/store/authStore'
import { adminApi, sprintApi, type Sprint, type LeaderboardEntry } from '@/services/sprintApi'
import { paymentApi, type PaymentRequest } from '@/services/paymentApi'

type Tab = 'sprints' | 'payments' | 'users' | 'stats'

const TABS: { key: Tab; label: string; icon: typeof Trophy }[] = [
  { key: 'sprints', label: 'Спринты', icon: Trophy },
  { key: 'payments', label: 'Платежи', icon: CreditCard },
  { key: 'users', label: 'Пользователи', icon: Users },
  { key: 'stats', label: 'Статистика', icon: BarChart3 },
]

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.06 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  show: { opacity: 1, y: 0 },
}

function formatDate(dateStr: string): string {
  return new Date(dateStr).toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', year: 'numeric' })
}

function daysLeft(endDate: string): number {
  return Math.max(0, Math.ceil((new Date(endDate).getTime() - Date.now()) / (1000 * 60 * 60 * 24)))
}

/* ─────────────── Sprints Tab ─────────────── */

function SprintsTab() {
  const [sprints, setSprints] = useState<Sprint[]>([])
  const [leaderboard, setLeaderboard] = useState<LeaderboardEntry[]>([])
  const [loading, setLoading] = useState(true)
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({ title: '', start_date: '', end_date: '' })
  const [creating, setCreating] = useState(false)

  const fetchData = () => {
    setLoading(true)
    Promise.all([
      adminApi.getSprints().catch(() => []),
      sprintApi.getLeaderboard().catch(() => []),
    ]).then(([s, lb]) => {
      setSprints(s)
      setLeaderboard(lb)
    }).finally(() => setLoading(false))
  }

  useEffect(() => { fetchData() }, [])

  const activeSprint = sprints.find((s) => s.status === 'active')
  const history = sprints.filter((s) => s.status !== 'active')

  const handleCreate = async () => {
    if (!formData.title || !formData.start_date || !formData.end_date) return
    setCreating(true)
    try {
      await adminApi.createSprint(formData)
      setShowForm(false)
      setFormData({ title: '', start_date: '', end_date: '' })
      fetchData()
    } catch (err) {
      console.error('Failed to create sprint:', err)
    } finally {
      setCreating(false)
    }
  }

  const handleClose = async (id: string) => {
    if (!confirm('Закрыть спринт и выбрать победителей?')) return
    try {
      await adminApi.closeSprint(id)
      fetchData()
    } catch (err) {
      console.error('Failed to close sprint:', err)
    }
  }

  const handleCancel = async (id: string) => {
    if (!confirm('Отменить спринт?')) return
    try {
      await adminApi.cancelSprint(id)
      fetchData()
    } catch (err) {
      console.error('Failed to cancel sprint:', err)
    }
  }

  if (loading) {
    return (
      <div className="flex justify-center py-16">
        <Loader2 className="animate-spin text-[#F97316]" size={28} />
      </div>
    )
  }

  return (
    <motion.div variants={containerVariants} initial="hidden" animate="show" className="space-y-6">
      {/* Active Sprint */}
      {activeSprint && (
        <motion.div variants={itemVariants}>
          <div className="bg-[#0A0A0A] border border-yellow-500/20 rounded-2xl p-5 space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-yellow-500/10 flex items-center justify-center">
                  <Trophy size={18} className="text-yellow-400" />
                </div>
                <div>
                  <h3 className="text-base font-semibold text-white">{activeSprint.title}</h3>
                  <p className="text-xs text-white/40">
                    {formatDate(activeSprint.start_date)} — {formatDate(activeSprint.end_date)}
                    {' '}({daysLeft(activeSprint.end_date)} дней)
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-[10px] bg-green-500/15 text-green-400 px-2 py-0.5 rounded-full font-medium">
                  Активен
                </span>
              </div>
            </div>

            {/* Leaderboard preview */}
            {leaderboard.length > 0 && (
              <div>
                <p className="text-xs text-white/40 mb-2">Топ участники:</p>
                <SprintLeaderboard entries={leaderboard.slice(0, 5)} />
              </div>
            )}

            <div className="flex gap-2 pt-2">
              <Button size="sm" onClick={() => handleClose(activeSprint.id)}>
                Закрыть спринт
              </Button>
              <Button size="sm" variant="ghost" onClick={() => handleCancel(activeSprint.id)}>
                <Ban size={14} /> Отменить
              </Button>
            </div>
          </div>
        </motion.div>
      )}

      {/* Create Sprint */}
      <motion.div variants={itemVariants}>
        {showForm ? (
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 space-y-4">
            <div className="flex items-center justify-between mb-2">
              <h3 className="text-sm font-semibold text-white">Создать спринт</h3>
              <button onClick={() => setShowForm(false)} className="text-white/30 hover:text-white/60">
                <X size={16} />
              </button>
            </div>

            <div className="space-y-3">
              <div>
                <label className="text-xs text-white/40 mb-1 block">Название</label>
                <input
                  type="text"
                  value={formData.title}
                  onChange={(e) => setFormData((f) => ({ ...f, title: e.target.value }))}
                  placeholder="Апрельский спринт"
                  className="w-full bg-white/5 border border-white/10 rounded-xl px-3 py-2 text-sm text-white placeholder:text-white/20 outline-none focus:border-[#F97316]/50"
                />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="text-xs text-white/40 mb-1 block">Начало</label>
                  <input
                    type="date"
                    value={formData.start_date}
                    onChange={(e) => setFormData((f) => ({ ...f, start_date: e.target.value }))}
                    className="w-full bg-white/5 border border-white/10 rounded-xl px-3 py-2 text-sm text-white outline-none focus:border-[#F97316]/50 [color-scheme:dark]"
                  />
                </div>
                <div>
                  <label className="text-xs text-white/40 mb-1 block">Конец</label>
                  <input
                    type="date"
                    value={formData.end_date}
                    onChange={(e) => setFormData((f) => ({ ...f, end_date: e.target.value }))}
                    className="w-full bg-white/5 border border-white/10 rounded-xl px-3 py-2 text-sm text-white outline-none focus:border-[#F97316]/50 [color-scheme:dark]"
                  />
                </div>
              </div>
            </div>

            <Button size="sm" onClick={handleCreate} disabled={creating}>
              {creating ? <Loader2 size={14} className="animate-spin" /> : <Plus size={14} />}
              Создать
            </Button>
          </div>
        ) : (
          <button
            onClick={() => setShowForm(true)}
            className="w-full bg-[#0A0A0A] border border-dashed border-white/10 rounded-2xl p-4 flex items-center justify-center gap-2 text-sm text-white/40 hover:text-white/60 hover:border-white/20 transition-colors cursor-pointer"
          >
            <Plus size={16} /> Создать спринт
          </button>
        )}
      </motion.div>

      {/* History */}
      {history.length > 0 && (
        <motion.div variants={itemVariants}>
          <h3 className="text-sm font-semibold text-white/70 uppercase tracking-wider mb-3">История спринтов</h3>
          <div className="space-y-2">
            {history.map((s) => (
              <div key={s.id} className="bg-[#0A0A0A] border border-white/6 rounded-xl p-4 flex items-center justify-between hover:border-white/12 transition-colors">
                <div>
                  <p className="text-sm font-medium text-white">{s.title}</p>
                  <p className="text-xs text-white/30">
                    {formatDate(s.start_date)} — {formatDate(s.end_date)}
                    <span className={`ml-2 ${s.status === 'closed' ? 'text-green-400/60' : 'text-red-400/60'}`}>
                      {s.status === 'closed' ? 'Завершен' : 'Отменен'}
                    </span>
                  </p>
                </div>
                {s.winners && s.winners.length > 0 && (
                  <div className="text-right">
                    <p className="text-xs text-yellow-400 font-medium">
                      &#127942; {s.winners[0]?.name}
                    </p>
                    <p className="text-[10px] text-white/30">{s.winners[0]?.trophies} трофеев</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </motion.div>
      )}
    </motion.div>
  )
}

/* ─────────────── Users Tab ─────────────── */

function UsersTab() {
  const [users, setUsers] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')

  useEffect(() => {
    adminApi.getUsers()
      .then(setUsers)
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  const filtered = search
    ? users.filter((u) =>
        u.name?.toLowerCase().includes(search.toLowerCase()) ||
        u.email?.toLowerCase().includes(search.toLowerCase())
      )
    : users

  if (loading) {
    return (
      <div className="flex justify-center py-16">
        <Loader2 className="animate-spin text-[#F97316]" size={28} />
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {/* Search */}
      <div className="relative">
        <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-white/20" />
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Поиск по имени или email..."
          className="w-full bg-[#0A0A0A] border border-white/6 rounded-xl pl-10 pr-4 py-2.5 text-sm text-white placeholder:text-white/20 outline-none focus:border-[#F97316]/50"
        />
      </div>

      {/* Table */}
      <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl overflow-hidden">
        {/* Header */}
        <div className="grid grid-cols-12 gap-2 px-4 py-2.5 border-b border-white/6 text-[11px] text-white/30 uppercase tracking-wider">
          <span className="col-span-3">Имя</span>
          <span className="col-span-3">Email</span>
          <span className="col-span-1 text-center">Роль</span>
          <span className="col-span-1 text-center">&#127942;</span>
          <span className="col-span-1 text-center">XP</span>
          <span className="col-span-3">Направление</span>
        </div>

        {/* Rows */}
        {filtered.length === 0 ? (
          <div className="p-8 text-center text-white/30 text-sm">Пользователи не найдены</div>
        ) : (
          <div className="divide-y divide-white/[0.04]">
            {filtered.map((user) => (
              <div key={user.id} className="grid grid-cols-12 gap-2 px-4 py-3 items-center hover:bg-white/[0.02] transition-colors">
                <div className="col-span-3 flex items-center gap-2 min-w-0">
                  <div className="w-7 h-7 rounded-full bg-white/5 border border-white/8 flex items-center justify-center text-[10px] font-bold text-white/60 shrink-0">
                    {user.name?.[0]?.toUpperCase() ?? '?'}
                  </div>
                  <span className="text-sm text-white truncate">{user.name}</span>
                </div>
                <span className="col-span-3 text-sm text-white/40 truncate">{user.email}</span>
                <span className="col-span-1 text-center">
                  <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-medium ${
                    user.role === 'admin'
                      ? 'bg-[#F97316]/15 text-[#F97316]'
                      : 'bg-white/5 text-white/40'
                  }`}>
                    {user.role ?? 'user'}
                  </span>
                </span>
                <span className="col-span-1 text-center text-sm text-yellow-400 font-medium">{user.trophies ?? 0}</span>
                <span className="col-span-1 text-center text-sm text-[#FB923C] font-medium">{user.xp ?? 0}</span>
                <span className="col-span-3 text-sm text-white/30 truncate">{user.direction ?? '—'}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      <p className="text-[11px] text-white/20 text-right">{filtered.length} из {users.length} пользователей</p>
    </div>
  )
}

/* ─────────────── Stats Tab ─────────────── */

function StatsTab() {
  const [stats, setStats] = useState<any>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    adminApi.getStats()
      .then(setStats)
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="flex justify-center py-16">
        <Loader2 className="animate-spin text-[#F97316]" size={28} />
      </div>
    )
  }

  const cards = [
    { label: 'Всего пользователей', value: stats?.total_users ?? 0, color: '#F97316', icon: Users },
    { label: 'Активных за неделю', value: stats?.active_this_week ?? 0, color: '#FB923C', icon: Clock },
    { label: 'Курсов пройдено', value: stats?.courses_completed ?? 0, color: '#EAB308', icon: BarChart3 },
    { label: 'Трофеев выдано', value: stats?.trophies_awarded ?? 0, color: '#F59E0B', icon: Trophy },
  ]

  return (
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
      {cards.map((card) => (
        <motion.div
          key={card.label}
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5 hover:border-white/12 transition-colors"
        >
          <div
            className="w-10 h-10 rounded-xl flex items-center justify-center mb-3"
            style={{ backgroundColor: `${card.color}18` }}
          >
            <card.icon size={18} style={{ color: card.color }} />
          </div>
          <p className="text-2xl font-bold text-white">{card.value.toLocaleString()}</p>
          <p className="text-xs text-white/40 mt-1">{card.label}</p>
        </motion.div>
      ))}
    </div>
  )
}

/* ─────────────── Payments Tab ─────────────── */

function PaymentsTab({ onCountUpdate }: { onCountUpdate: (count: number) => void }) {
  const [payments, setPayments] = useState<PaymentRequest[]>([])
  const [loading, setLoading] = useState(true)
  const [reviewing, setReviewing] = useState<string | null>(null)
  const [previewImg, setPreviewImg] = useState<string | null>(null)

  const fetchPayments = () => {
    setLoading(true)
    paymentApi.adminList()
      .then((data) => {
        setPayments(data)
        onCountUpdate(data.filter((p) => p.status === 'pending').length)
      })
      .catch(() => {})
      .finally(() => setLoading(false))
  }

  useEffect(() => { fetchPayments() }, [])

  const handleReview = async (paymentId: string, action: 'approve' | 'reject') => {
    setReviewing(paymentId)
    try {
      await paymentApi.review(paymentId, action)
      fetchPayments()
    } catch (err) {
      console.error('Failed to review payment:', err)
    } finally {
      setReviewing(null)
    }
  }

  const statusBadge = (status: PaymentRequest['status']) => {
    switch (status) {
      case 'pending':
        return <span className="text-[10px] px-2 py-0.5 rounded-full bg-yellow-500/15 text-yellow-400 font-medium">Ожидает</span>
      case 'approved':
        return <span className="text-[10px] px-2 py-0.5 rounded-full bg-green-500/15 text-green-400 font-medium">Одобрен</span>
      case 'rejected':
        return <span className="text-[10px] px-2 py-0.5 rounded-full bg-red-500/15 text-red-400 font-medium">Отклонен</span>
    }
  }

  if (loading) {
    return (
      <div className="flex justify-center py-16">
        <Loader2 className="animate-spin text-[#F97316]" size={28} />
      </div>
    )
  }

  if (payments.length === 0) {
    return (
      <div className="text-center py-16 text-white/30 text-sm">Заявок на оплату пока нет</div>
    )
  }

  return (
    <>
      <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl overflow-hidden">
        {/* Header */}
        <div className="grid grid-cols-12 gap-2 px-4 py-2.5 border-b border-white/6 text-[11px] text-white/30 uppercase tracking-wider">
          <span className="col-span-2">Пользователь</span>
          <span className="col-span-3">Курс</span>
          <span className="col-span-1 text-center">Сумма</span>
          <span className="col-span-1 text-center">Скрин</span>
          <span className="col-span-2 text-center">Дата</span>
          <span className="col-span-1 text-center">Статус</span>
          <span className="col-span-2 text-center">Действия</span>
        </div>

        {/* Rows */}
        <div className="divide-y divide-white/[0.04]">
          {payments.map((p) => (
            <div key={p.id} className="grid grid-cols-12 gap-2 px-4 py-3 items-center hover:bg-white/[0.02] transition-colors">
              <div className="col-span-2 min-w-0">
                <p className="text-sm text-white truncate">{p.user_name}</p>
                <p className="text-[10px] text-white/30 truncate">{p.user_email}</p>
              </div>
              <span className="col-span-3 text-sm text-white/60 truncate">{p.course_title}</span>
              <span className="col-span-1 text-center text-sm text-[#F97316] font-medium">
                {(p.amount / 100).toFixed(0)} {p.currency}
              </span>
              <div className="col-span-1 flex justify-center">
                {p.screenshot_url ? (
                  <button
                    onClick={() => setPreviewImg(p.screenshot_url)}
                    className="w-8 h-8 rounded-lg bg-white/5 border border-white/8 flex items-center justify-center hover:border-white/20 transition-colors cursor-pointer overflow-hidden"
                  >
                    <img src={p.screenshot_url} alt="" className="w-full h-full object-cover" />
                  </button>
                ) : (
                  <ImageIcon size={14} className="text-white/20" />
                )}
              </div>
              <span className="col-span-2 text-center text-xs text-white/30">
                {new Date(p.created_at).toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}
              </span>
              <div className="col-span-1 flex justify-center">
                {statusBadge(p.status)}
              </div>
              <div className="col-span-2 flex justify-center gap-1.5">
                {p.status === 'pending' ? (
                  <>
                    <button
                      onClick={() => handleReview(p.id, 'approve')}
                      disabled={reviewing === p.id}
                      className="w-8 h-8 rounded-lg bg-green-500/10 border border-green-500/20 flex items-center justify-center text-green-400 hover:bg-green-500/20 transition-colors cursor-pointer disabled:opacity-40"
                      title="Подтвердить"
                    >
                      {reviewing === p.id ? <Loader2 size={14} className="animate-spin" /> : <CheckCircle2 size={14} />}
                    </button>
                    <button
                      onClick={() => handleReview(p.id, 'reject')}
                      disabled={reviewing === p.id}
                      className="w-8 h-8 rounded-lg bg-red-500/10 border border-red-500/20 flex items-center justify-center text-red-400 hover:bg-red-500/20 transition-colors cursor-pointer disabled:opacity-40"
                      title="Отклонить"
                    >
                      {reviewing === p.id ? <Loader2 size={14} className="animate-spin" /> : <XCircle size={14} />}
                    </button>
                  </>
                ) : (
                  <span className="text-[10px] text-white/20">—</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      <p className="text-[11px] text-white/20 text-right mt-2">
        {payments.filter((p) => p.status === 'pending').length} ожидают из {payments.length} заявок
      </p>

      {/* Full-size image preview */}
      {previewImg && (
        <div
          className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 cursor-pointer"
          onClick={() => setPreviewImg(null)}
        >
          <div className="relative max-w-2xl max-h-[80vh]">
            <img src={previewImg} alt="Скриншот оплаты" className="max-w-full max-h-[80vh] object-contain rounded-2xl border border-white/10" />
            <button
              onClick={() => setPreviewImg(null)}
              className="absolute top-2 right-2 w-8 h-8 rounded-full bg-black/70 border border-white/10 flex items-center justify-center text-white/60 hover:text-white cursor-pointer"
            >
              <X size={16} />
            </button>
          </div>
        </div>
      )}
    </>
  )
}

/* ─────────────── Admin Page ─────────────── */

export default function Admin() {
  const user = useAuthStore((s) => s.user)
  const [activeTab, setActiveTab] = useState<Tab>('sprints')
  const [pendingPaymentsCount, setPendingPaymentsCount] = useState(0)

  useEffect(() => {
    paymentApi.adminList()
      .then((data) => setPendingPaymentsCount(data.filter((p) => p.status === 'pending').length))
      .catch(() => {})
  }, [])

  // Admin guard
  if (user && user.role !== 'admin') {
    return <Navigate to="/dashboard" replace />
  }

  return (
    <PageWrapper>
      <div className="max-w-5xl mx-auto space-y-6">

        {/* Header */}
        <div>
          <h1 className="text-2xl font-bold text-white mb-1">Админ-панель</h1>
          <p className="text-sm text-white/40">Управление платформой</p>
        </div>

        {/* Tab Switcher */}
        <div className="inline-flex rounded-xl bg-[#0A0A0A] border border-white/6 p-1 gap-1">
          {TABS.map((tab) => (
            <button
              key={tab.key}
              onClick={() => setActiveTab(tab.key)}
              className={`flex items-center gap-1.5 px-4 py-2 rounded-lg text-sm font-medium transition-all cursor-pointer ${
                activeTab === tab.key
                  ? 'bg-[#F97316]/15 text-[#F97316]'
                  : 'text-white/40 hover:text-white/70'
              }`}
            >
              <tab.icon size={14} />
              {tab.label}
              {tab.key === 'payments' && pendingPaymentsCount > 0 && (
                <span className="ml-1 min-w-[18px] h-[18px] px-1 rounded-full bg-[#F97316] text-white text-[10px] font-bold flex items-center justify-center">
                  {pendingPaymentsCount}
                </span>
              )}
            </button>
          ))}
        </div>

        {/* Tab Content */}
        {activeTab === 'sprints' && <SprintsTab />}
        {activeTab === 'payments' && <PaymentsTab onCountUpdate={setPendingPaymentsCount} />}
        {activeTab === 'users' && <UsersTab />}
        {activeTab === 'stats' && <StatsTab />}

      </div>
    </PageWrapper>
  )
}
