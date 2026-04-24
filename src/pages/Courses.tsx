import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Search, Users, ChevronDown, Plus, BookOpen, Sparkles, Zap, ArrowRight } from 'lucide-react'
import { PageWrapper } from '@/components/layout/PageWrapper'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import { StarRating } from '@/components/courses/StarRating'
import { useTranslation } from '@/hooks/useTranslation'
import { useAuthStore } from '@/store/authStore'
import { courseApi, type CourseCard } from '@/services/courseApi'

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.06 } },
}
const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

const CATEGORIES = ['All', 'Frontend', 'English', 'Call Center', 'CIB', 'Other']
const DIFFICULTIES = ['All', 'Beginner', 'Intermediate', 'Advanced']
const PRICE_FILTERS = ['All', 'Free', 'Paid'] as const

const GRADIENT_THUMBNAILS = [
  'linear-gradient(135deg, #F97316 0%, #FB923C 100%)',
  'linear-gradient(135deg, #FF6B6B 0%, #F97316 100%)',
  'linear-gradient(135deg, #4ADE80 0%, #22C55E 100%)',
  'linear-gradient(135deg, #F97316 0%, #FF6B6B 100%)',
  'linear-gradient(135deg, #FB923C 0%, #4ADE80 100%)',
  'linear-gradient(135deg, #22C55E 0%, #F97316 100%)',
]

function getGradient(id: string) {
  let hash = 0
  for (let i = 0; i < id.length; i++) hash = id.charCodeAt(i) + ((hash << 5) - hash)
  return GRADIENT_THUMBNAILS[Math.abs(hash) % GRADIENT_THUMBNAILS.length]
}

export default function Courses() {
  const navigate = useNavigate()
  const { t } = useTranslation()
  const { isAuthenticated } = useAuthStore()
  const [courses, setCourses] = useState<CourseCard[]>([])
  const [total, setTotal] = useState(0)
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')
  const [category, setCategory] = useState('All')
  const [difficulty, setDifficulty] = useState('All')
  const [priceFilter, setPriceFilter] = useState<typeof PRICE_FILTERS[number]>('All')
  const [sort, setSort] = useState('popular')
  const [showSort, setShowSort] = useState(false)
  const [availableTags, setAvailableTags] = useState<string[]>([])
  const [selectedTags, setSelectedTags] = useState<string[]>([])

  useEffect(() => {
    courseApi.getTags().then(setAvailableTags).catch(() => setAvailableTags([]))
  }, [])

  const sortOptions = [
    { value: 'popular', label: t('courses.popular') },
    { value: 'newest', label: t('courses.newest') },
    { value: 'rating', label: t('courses.highestRated') },
    { value: 'price_asc', label: t('courses.priceLow') },
  ]

  useEffect(() => {
    setLoading(true)
    const params: Record<string, string> = { sort }
    if (search) params.search = search
    if (category !== 'All') params.category = category
    if (difficulty !== 'All') params.difficulty = difficulty
    if (priceFilter === 'Free') params.max_price = '0'
    if (priceFilter === 'Paid') params.min_price = '1'
    if (selectedTags.length > 0) params.tags = selectedTags.join(',')

    courseApi
      .list(params)
      .then((res: any) => {
        setCourses(res.items || res.courses || [])
        setTotal(res.total || 0)
      })
      .catch(() => {
        setCourses([])
        setTotal(0)
      })
      .finally(() => setLoading(false))
  }, [search, category, difficulty, priceFilter, sort, selectedTags])

  return (
    <PageWrapper>
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="show"
        className="max-w-5xl mx-auto space-y-4 lg:space-y-6"
      >
        {/* Header */}
        <motion.div variants={itemVariants} className="flex items-center justify-between gap-3">
          <h1 className="text-xl lg:text-2xl font-bold">{t('courses.title')}</h1>
          {isAuthenticated && (
            <div className="flex items-center gap-2">
              <Button variant="secondary" size="sm" onClick={() => navigate('/teach')}>
                <BookOpen size={14} />
                <span className="hidden sm:inline">Мои курсы</span>
              </Button>
              <Button size="sm" onClick={async () => {
                try {
                  const res = await courseApi.create({
                    title: 'Новый курс',
                    description: '',
                    category: 'Other',
                    difficulty: 'Beginner',
                    price: 0,
                  })
                  navigate(`/teach/${res.id}`)
                } catch {}
              }}>
                <Plus size={14} />
                <span className="hidden sm:inline">Создать курс</span>
              </Button>
            </div>
          )}
        </motion.div>

        {/* Create Course Banner */}
        {isAuthenticated && (
          <motion.div variants={itemVariants}>
            <div
              className="relative overflow-hidden rounded-2xl border border-purple-500/20 bg-gradient-to-r from-purple-900/40 via-indigo-900/30 to-purple-900/40 p-4 cursor-pointer hover:border-purple-500/40 transition-all group"
              onClick={() => navigate('/teach')}
            >
              <div className="absolute inset-0 opacity-20 pointer-events-none"
                style={{ background: 'radial-gradient(ellipse at 80% 50%, #7C3AED 0%, transparent 60%)' }} />
              <div className="relative flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-purple-500/20 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
                  <Sparkles size={20} className="text-purple-400" />
                </div>
                <div className="flex-1 min-w-0">
                  <h3 className="text-sm font-bold text-white">Создай курс — получи 500 XP!</h3>
                  <p className="text-xs text-white/50">Поделись знаниями с сообществом</p>
                </div>
                <div className="flex items-center gap-1 text-purple-400 text-sm font-medium shrink-0">
                  <Zap size={14} />
                  <span className="hidden sm:inline">+500 XP</span>
                  <ArrowRight size={14} className="group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </div>
          </motion.div>
        )}

        {/* Search */}
        <motion.div variants={itemVariants}>
          <div className="relative">
            <Search size={18} className="absolute left-4 top-1/2 -translate-y-1/2 text-text-secondary" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder={t('courses.search')}
              className="w-full rounded-xl border border-white/6 bg-[#0A0A0A] backdrop-blur-xl pl-11 pr-4 py-2.5 text-text placeholder:text-text-secondary/50 outline-none transition-colors focus:border-[#F97316]/50 text-sm"
            />
          </div>
        </motion.div>

        {/* Category Pills */}
        <motion.div variants={itemVariants} className="flex gap-2 overflow-x-auto pb-1 scrollbar-hide">
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => setCategory(cat)}
              className={`shrink-0 px-4 py-1.5 rounded-full text-xs font-medium transition-all cursor-pointer ${
                category === cat
                  ? 'bg-[#F97316] text-white shadow-lg shadow-[#F97316]/25'
                  : 'bg-[#0A0A0A] border border-white/6 text-text-secondary hover:text-text hover:border-[#F97316]/50'
              }`}
            >
              {cat === 'All' ? t('courses.all') : cat}
            </button>
          ))}
        </motion.div>

        {/* Difficulty + Price + Sort Row */}
        <motion.div variants={itemVariants} className="flex flex-wrap items-center gap-2">
          {/* Difficulty pills */}
          <div className="flex gap-1.5">
            {DIFFICULTIES.map((diff) => (
              <button
                key={diff}
                onClick={() => setDifficulty(diff)}
                className={`px-3 py-1 rounded-full text-[11px] font-medium transition-all cursor-pointer ${
                  difficulty === diff
                    ? 'bg-[#F97316]/15 text-[#F97316] border border-[#F97316]/30'
                    : 'bg-[#0A0A0A] border border-white/6 text-text-secondary hover:text-text'
                }`}
              >
                {diff === 'All' ? t('courses.all') : diff}
              </button>
            ))}
          </div>

          {/* Price toggle */}
          <div className="flex gap-1.5 ml-auto">
            {PRICE_FILTERS.map((pf) => (
              <button
                key={pf}
                onClick={() => setPriceFilter(pf)}
                className={`px-3 py-1 rounded-full text-[11px] font-medium transition-all cursor-pointer ${
                  priceFilter === pf
                    ? 'bg-[#F97316]/15 text-[#F97316] border border-[#F97316]/30'
                    : 'bg-[#0A0A0A] border border-white/6 text-text-secondary hover:text-text'
                }`}
              >
                {pf === 'All' ? t('courses.all') : pf === 'Free' ? t('courses.free') : t('courses.paid')}
              </button>
            ))}
          </div>

          {/* Sort dropdown */}
          <div className="relative">
            <button
              onClick={() => setShowSort(!showSort)}
              className="flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-medium bg-[#0A0A0A] border border-white/6 text-text-secondary hover:text-text transition-all cursor-pointer"
            >
              {sortOptions.find((s) => s.value === sort)?.label}
              <ChevronDown size={12} />
            </button>
            {showSort && (
              <div className="absolute right-0 top-full mt-1 bg-[#111111] border border-white/6 rounded-xl shadow-xl z-50 overflow-hidden min-w-[160px]">
                {sortOptions.map((opt) => (
                  <button
                    key={opt.value}
                    onClick={() => {
                      setSort(opt.value)
                      setShowSort(false)
                    }}
                    className={`w-full text-left px-4 py-2 text-xs transition-colors cursor-pointer ${
                      sort === opt.value ? 'text-[#F97316] bg-[#F97316]/10' : 'text-text-secondary hover:text-text hover:bg-white/5'
                    }`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            )}
          </div>
        </motion.div>

        {/* Tag Filter Chips */}
        {availableTags.length > 0 && (
          <motion.div variants={itemVariants} className="flex flex-wrap gap-2">
            {availableTags.map((tag) => {
              const active = selectedTags.includes(tag)
              return (
                <button
                  key={tag}
                  onClick={() =>
                    setSelectedTags((prev) =>
                      active ? prev.filter((t) => t !== tag) : [...prev, tag]
                    )
                  }
                  className={`px-3 py-1 rounded-full text-[11px] font-medium transition-all cursor-pointer ${
                    active
                      ? 'bg-[#F97316]/15 text-[#F97316] border border-[#F97316]/30'
                      : 'bg-[#0A0A0A] border border-white/6 text-text-secondary hover:text-text hover:border-[#F97316]/30'
                  }`}
                >
                  #{tag}
                </button>
              )
            })}
            {selectedTags.length > 0 && (
              <button
                onClick={() => setSelectedTags([])}
                className="px-3 py-1 rounded-full text-[11px] font-medium transition-all cursor-pointer bg-[#0A0A0A] border border-white/6 text-text-secondary hover:text-text"
              >
                Сбросить
              </button>
            )}
          </motion.div>
        )}

        {/* Course Grid */}
        {loading ? (
          <motion.div variants={itemVariants} className="text-center py-12">
            <p className="text-text-secondary text-sm">{t('common.loading')}</p>
          </motion.div>
        ) : courses.length === 0 ? (
          <motion.div variants={itemVariants} className="text-center py-16">
            <motion.img
              src="/images/mascot-thinking.png"
              alt="No courses"
              className="w-28 h-28 object-contain mx-auto mb-4 drop-shadow-lg"
              animate={{ y: [0, -6, 0] }}
              transition={{ repeat: Infinity, duration: 2.5, ease: 'easeInOut' }}
            />
            <p className="text-text-secondary text-sm">{t('courses.noCourses')}</p>
          </motion.div>
        ) : (
          <motion.div
            variants={containerVariants}
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"
          >
            {courses.map((course) => (
              <motion.div key={course.id} variants={itemVariants}>
                <Card
                  hover
                  onClick={() => navigate(`/courses/${course.id}`)}
                  className="p-0 overflow-hidden cursor-pointer"
                >
                  {/* Thumbnail */}
                  <div
                    className="h-36 w-full flex items-center justify-center"
                    style={{
                      background: course.thumbnail_url
                        ? `url(${course.thumbnail_url}) center/cover`
                        : getGradient(course.id),
                    }}
                  >
                    {!course.thumbnail_url && (
                      <span className="text-white/80 text-3xl font-bold">
                        {course.title.charAt(0)}
                      </span>
                    )}
                  </div>

                  <div className="p-4 space-y-2">
                    {/* Category + Difficulty badges */}
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-[#F97316]/15 text-[#F97316] font-medium">
                        {course.category}
                      </span>
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-white/6 text-text-secondary font-medium">
                        {course.difficulty}
                      </span>
                    </div>

                    {/* Title */}
                    <h3 className="text-sm font-semibold leading-tight line-clamp-2">
                      {course.title}
                    </h3>

                    {/* Author */}
                    <p className="text-xs text-text-secondary">{course.author_name}</p>

                    {/* Rating + Enrolled */}
                    <div className="flex items-center gap-3">
                      <div className="flex items-center gap-1">
                        <StarRating rating={course.rating_avg} size={12} />
                        <span className="text-[11px] text-text-secondary">
                          ({course.rating_count})
                        </span>
                      </div>
                      <div className="flex items-center gap-1 text-text-secondary">
                        <Users size={12} />
                        <span className="text-[11px]">
                          {course.total_enrolled} {t('courses.enrolled')}
                        </span>
                      </div>
                    </div>

                    {/* Price */}
                    <div>
                      {course.price === 0 ? (
                        <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-[#4ADE80]/15 text-[#4ADE80]">
                          {t('courses.free')}
                        </span>
                      ) : (
                        <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-[#F97316]/15 text-[#F97316]">
                          {(course.price / 100).toFixed(2)} {course.currency}
                        </span>
                      )}
                    </div>

                    {/* Tags */}
                    {course.tags?.length > 0 && (
                      <div className="flex flex-wrap gap-1 mt-2">
                        {course.tags.slice(0, 3).map(tag => (
                          <span key={tag} className="text-[10px] px-2 py-0.5 rounded-full bg-[#F97316]/10 text-[#FB923C]">
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                </Card>
              </motion.div>
            ))}
          </motion.div>
        )}
      </motion.div>
    </PageWrapper>
  )
}
