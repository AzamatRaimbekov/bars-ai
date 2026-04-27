import { motion } from 'framer-motion'
import { Flame, Award, TrendingUp, Target } from 'lucide-react'
import { t, useLandingLang } from '@/lib/landing-i18n'

const levels = [
  { name: 'Novice', xp: '0', active: false },
  { name: 'Apprentice', xp: '500', active: false },
  { name: 'Practitioner', xp: '1.5K', active: true },
  { name: 'Expert', xp: '4K', active: false },
  { name: 'Master', xp: '8K', active: false },
  { name: 'Legend', xp: '15K', active: false },
]

const badges = [
  { emoji: '🚀', name: 'First Step', rarity: 'Common', color: '#6B7280' },
  { emoji: '🔥', name: 'Week Warrior', rarity: 'Uncommon', color: '#22C55E' },
  { emoji: '📚', name: 'Bookworm', rarity: 'Rare', color: '#3B82F6' },
  { emoji: '🏆', name: 'Streak Legend', rarity: 'Epic', color: '#A855F7' },
  { emoji: '💎', name: 'Unstoppable', rarity: 'Legendary', color: '#F97316' },
]

export function ProgressionSection() {
  useLandingLang()

  const quests = [
    { text: t('progression.quest1'), progress: 100, xp: 30, done: true },
    { text: t('progression.quest2'), progress: 70, xp: 50, done: false },
    { text: t('progression.quest3'), progress: 100, xp: 20, done: true },
  ]

  return (
    <section className="py-24 px-4">
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-12"
        >
          <h2 className="text-3xl font-bold text-white mb-3">
            {t('progression.title')}
          </h2>
          <p className="text-white/45">{t('progression.subtitle')}</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Left: Level progression */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="bg-white/[0.03] border border-white/[0.08] rounded-2xl p-5 backdrop-blur-sm"
          >
            <div className="flex items-center gap-2 mb-4">
              <TrendingUp className="w-4 h-4 text-[#F97316]" />
              <span className="text-sm font-semibold text-white">{t('progression.levels')}</span>
            </div>

            {/* Level ladder */}
            <div className="space-y-2">
              {levels.map((level, i) => (
                <div key={level.name} className="flex items-center gap-3">
                  <div
                    className={`w-8 h-8 rounded-lg flex items-center justify-center text-xs font-bold ${
                      level.active
                        ? 'bg-[#F97316]/20 border border-[#F97316]/40 text-[#F97316]'
                        : i < 2
                        ? 'bg-white/[0.06] text-white/30'
                        : 'bg-white/[0.03] text-white/15'
                    }`}
                  >
                    {i + 1}
                  </div>
                  <div className="flex-1">
                    <div className="flex items-center justify-between">
                      <span className={`text-xs font-medium ${level.active ? 'text-[#F97316]' : i < 2 ? 'text-white/50' : 'text-white/25'}`}>
                        {level.name}
                      </span>
                      <span className={`text-[10px] ${level.active ? 'text-[#F97316]/60' : 'text-white/20'}`}>
                        {level.xp} XP
                      </span>
                    </div>
                    {level.active && (
                      <div className="mt-1 h-1.5 bg-white/[0.06] rounded-full overflow-hidden">
                        <motion.div
                          initial={{ width: 0 }}
                          whileInView={{ width: '65%' }}
                          viewport={{ once: true }}
                          transition={{ delay: 0.5, duration: 0.8 }}
                          className="h-full bg-gradient-to-r from-[#F97316] to-[#FBBF24] rounded-full"
                        />
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </motion.div>

          {/* Right: Stats + Badges */}
          <div className="space-y-4">
            {/* Daily stats mockup */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.15 }}
              className="bg-white/[0.03] border border-white/[0.08] rounded-2xl p-5 backdrop-blur-sm"
            >
              <div className="flex items-center gap-2 mb-4">
                <Target className="w-4 h-4 text-[#3B82F6]" />
                <span className="text-sm font-semibold text-white">{t('progression.quests')}</span>
                <span className="text-[10px] text-white/30 ml-auto">2/3</span>
              </div>
              <div className="space-y-2.5">
                {quests.map((q) => (
                  <div key={q.text} className="flex items-center gap-3">
                    <div className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] ${
                      q.done ? 'border-[#22C55E] bg-[#22C55E]/20 text-[#22C55E]' : 'border-white/15 text-white/20'
                    }`}>
                      {q.done ? '✓' : ''}
                    </div>
                    <div className="flex-1">
                      <div className="flex items-center justify-between">
                        <span className={`text-xs ${q.done ? 'text-white/30 line-through' : 'text-white/60'}`}>{q.text}</span>
                        <span className="text-[10px] text-[#FBBF24]">+{q.xp} ⭐</span>
                      </div>
                      <div className="mt-1 h-1 bg-white/[0.06] rounded-full overflow-hidden">
                        <div className={`h-full rounded-full ${q.done ? 'bg-[#22C55E]' : 'bg-[#3B82F6]'}`} style={{ width: `${q.progress}%` }} />
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>

            {/* Streak + Badges row */}
            <div className="grid grid-cols-2 gap-4">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: 0.2 }}
                className="bg-white/[0.03] border border-white/[0.08] rounded-2xl p-4 backdrop-blur-sm text-center"
              >
                <Flame className="w-6 h-6 text-[#F97316] mx-auto mb-2" />
                <div className="text-2xl font-extrabold text-white">7</div>
                <div className="text-[10px] text-white/35">{t('progression.streak')}</div>
              </motion.div>

              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: 0.25 }}
                className="bg-white/[0.03] border border-white/[0.08] rounded-2xl p-4 backdrop-blur-sm text-center"
              >
                <Award className="w-6 h-6 text-[#A855F7] mx-auto mb-2" />
                <div className="text-2xl font-extrabold text-white">59</div>
                <div className="text-[10px] text-white/35">{t('progression.badges_count')}</div>
              </motion.div>
            </div>
          </div>
        </div>

        {/* Badges showcase */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: 0.3 }}
          className="mt-6 bg-white/[0.03] border border-white/[0.08] rounded-2xl p-5 backdrop-blur-sm"
        >
          <div className="text-xs text-white/40 mb-3">{t('progression.badges_label')}</div>
          <div className="flex flex-wrap justify-center gap-3">
            {badges.map((badge) => (
              <div
                key={badge.name}
                className="flex items-center gap-2 px-3 py-2 rounded-xl border"
                style={{
                  background: `${badge.color}10`,
                  borderColor: `${badge.color}25`,
                }}
              >
                <span className="text-lg">{badge.emoji}</span>
                <div>
                  <div className="text-xs font-medium text-white/80">{badge.name}</div>
                  <div className="text-[10px]" style={{ color: badge.color }}>{badge.rarity}</div>
                </div>
              </div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  )
}
