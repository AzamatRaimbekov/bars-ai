import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Gamepad2, Brain, Code, Layers, Swords, Zap } from 'lucide-react'
import { t, useLandingLang } from '@/lib/landing-i18n'

function TowerDefenseMockup() {
  return (
    <div className="space-y-3">
      {/* Game field */}
      <div className="bg-black/40 rounded-xl p-4 border border-white/[0.06]">
        <div className="flex items-center justify-between mb-3 text-xs">
          <span className="text-white/60">{t('formats.mock.wave')}</span>
          <div className="flex gap-3">
            <span className="text-[#FBBF24]">⭐ 85</span>
            <span className="text-red-400">❤️ 3</span>
          </div>
        </div>
        {/* Mini grid */}
        <div className="grid grid-cols-8 gap-1 mb-3">
          {Array.from({ length: 24 }).map((_, i) => {
            const isTower = [2, 10, 18, 5, 13].includes(i)
            const isEnemy = [0, 8, 16].includes(i)
            const isPath = [0, 1, 2, 3, 4, 5, 6, 7, 8, 16].includes(i)
            return (
              <div
                key={i}
                className={`h-5 rounded-sm text-[8px] flex items-center justify-center ${
                  isTower
                    ? 'bg-[#A855F7]/30 border border-[#A855F7]/40'
                    : isEnemy
                    ? 'bg-red-500/20 border border-red-500/30'
                    : isPath
                    ? 'bg-white/[0.04]'
                    : 'bg-white/[0.02]'
                }`}
              >
                {isTower ? '🔮' : isEnemy ? '🐛' : ''}
              </div>
            )
          })}
        </div>
        {/* Towers palette */}
        <div className="flex gap-2">
          {[
            { emoji: '🔮', name: 'Blaster', cost: 30, color: '#3B82F6' },
            { emoji: '⚡', name: 'Zapper', cost: 50, color: '#A855F7' },
            { emoji: '🎯', name: 'Cannon', cost: 80, color: '#22C55E' },
          ].map((t) => (
            <div
              key={t.name}
              className="flex items-center gap-1.5 bg-white/[0.04] border border-white/[0.08] rounded-lg px-2 py-1"
            >
              <span className="text-sm">{t.emoji}</span>
              <span className="text-[10px] text-white/50">{t.cost}⭐</span>
            </div>
          ))}
        </div>
      </div>
      {/* Question phase */}
      <div className="bg-[#A855F7]/[0.08] border border-[#A855F7]/20 rounded-xl p-3">
        <div className="text-[11px] text-[#A855F7] font-semibold mb-2">{t('formats.mock.question_phase')}</div>
        <div className="text-xs text-white/70 mb-2">{t('formats.mock.question_text')}</div>
        <div className="grid grid-cols-2 gap-1.5">
          {['6', '8', '9', '5'].map((a, i) => (
            <div
              key={a}
              className={`text-center text-xs py-1.5 rounded-lg border ${
                i === 1
                  ? 'bg-[#22C55E]/15 border-[#22C55E]/30 text-[#22C55E]'
                  : 'bg-white/[0.03] border-white/[0.06] text-white/50'
              }`}
            >
              {a}
            </div>
          ))}
        </div>
        <div className="text-[10px] text-[#FBBF24] mt-2">{t('formats.mock.reward')}</div>
      </div>
    </div>
  )
}

function QuizMockup() {
  return (
    <div className="bg-black/40 rounded-xl p-4 border border-white/[0.06]">
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs text-white/40">{t('formats.mock.q_counter')}</span>
        <span className="text-xs text-[#FBBF24]">+50 XP</span>
      </div>
      <div className="text-sm text-white mb-4">
        {t('formats.mock.q_array')}
      </div>
      <div className="space-y-2">
        {[
          { text: 'forEach()', correct: false, selected: false },
          { text: 'map()', correct: true, selected: true },
          { text: 'push()', correct: false, selected: false },
          { text: 'splice()', correct: false, wrong: true },
        ].map((opt) => (
          <div
            key={opt.text}
            className={`flex items-center gap-3 px-3 py-2.5 rounded-xl border text-xs ${
              opt.correct && opt.selected
                ? 'bg-[#22C55E]/10 border-[#22C55E]/30 text-[#22C55E]'
                : opt.wrong
                ? 'bg-red-500/10 border-red-500/30 text-red-400'
                : 'bg-white/[0.03] border-white/[0.06] text-white/60'
            }`}
          >
            <div
              className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] ${
                opt.correct && opt.selected
                  ? 'border-[#22C55E] bg-[#22C55E]/20'
                  : opt.wrong
                  ? 'border-red-500 bg-red-500/20'
                  : 'border-white/20'
              }`}
            >
              {opt.correct && opt.selected ? '✓' : opt.wrong ? '✕' : ''}
            </div>
            {opt.text}
          </div>
        ))}
      </div>
    </div>
  )
}

function CodingMockup() {
  return (
    <div className="bg-black/40 rounded-xl border border-white/[0.06] overflow-hidden">
      {/* Editor header */}
      <div className="flex items-center gap-1.5 px-3 py-2 border-b border-white/[0.06]">
        <div className="w-2 h-2 rounded-full bg-red-500/60" />
        <div className="w-2 h-2 rounded-full bg-yellow-500/60" />
        <div className="w-2 h-2 rounded-full bg-green-500/60" />
        <span className="text-[10px] text-white/30 ml-2">main.py</span>
      </div>
      {/* Code */}
      <div className="p-3 font-mono text-xs leading-relaxed">
        <div>
          <span className="text-[#C084FC]">def</span>{' '}
          <span className="text-[#60A5FA]">fibonacci</span>
          <span className="text-white/60">(n):</span>
        </div>
        <div className="pl-4">
          <span className="text-[#C084FC]">if</span>{' '}
          <span className="text-white/60">n {'<='} 1:</span>
        </div>
        <div className="pl-8">
          <span className="text-[#C084FC]">return</span>{' '}
          <span className="text-[#FBBF24]">n</span>
        </div>
        <div className="pl-4">
          <span className="text-[#C084FC]">return</span>{' '}
          <span className="text-[#60A5FA]">fibonacci</span>
          <span className="text-white/60">(n-1) + </span>
          <span className="text-[#60A5FA]">fibonacci</span>
          <span className="text-white/60">(n-2)</span>
        </div>
        <div className="mt-2">
          <span className="text-[#60A5FA]">print</span>
          <span className="text-white/60">(</span>
          <span className="text-[#60A5FA]">fibonacci</span>
          <span className="text-white/60">(8))</span>
        </div>
      </div>
      {/* Output */}
      <div className="border-t border-white/[0.06] p-3 bg-white/[0.02]">
        <div className="text-[10px] text-white/30 mb-1">Output:</div>
        <div className="font-mono text-xs text-[#22C55E]">21</div>
        <div className="text-[10px] text-[#22C55E] mt-1">{t('formats.mock.correct')}</div>
      </div>
    </div>
  )
}

function MatchMockup() {
  return (
    <div className="bg-black/40 rounded-xl p-4 border border-white/[0.06]">
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs text-white/40">{t('formats.mock.match_title')}</span>
        <span className="text-xs text-white/40">⏱ 12с</span>
      </div>
      <div className="space-y-2">
        {[
          { term: 'Variable', def: t('formats.mock.var'), matched: true },
          { term: 'Function', def: t('formats.mock.func'), matched: true },
          { term: 'Loop', def: t('formats.mock.loop'), matched: false, active: true },
          { term: 'Array', def: t('formats.mock.array'), matched: false },
        ].map((pair) => (
          <div key={pair.term} className="flex gap-2">
            <div
              className={`flex-1 text-xs px-3 py-2 rounded-lg border text-center ${
                pair.matched
                  ? 'bg-[#22C55E]/10 border-[#22C55E]/20 text-[#22C55E]/60 line-through'
                  : pair.active
                  ? 'bg-[#FBBF24]/10 border-[#FBBF24]/30 text-[#FBBF24]'
                  : 'bg-white/[0.03] border-white/[0.06] text-white/60'
              }`}
            >
              {pair.term}
            </div>
            <div
              className={`flex-1 text-xs px-3 py-2 rounded-lg border text-center ${
                pair.matched
                  ? 'bg-[#22C55E]/10 border-[#22C55E]/20 text-[#22C55E]/60 line-through'
                  : 'bg-white/[0.03] border-white/[0.06] text-white/50'
              }`}
            >
              {pair.def}
            </div>
          </div>
        ))}
      </div>
      <div className="mt-3 text-[10px] text-white/30 text-center">{t('formats.mock.match_found')}</div>
    </div>
  )
}

function FlashCardMockup() {
  const [flipped, setFlipped] = useState(false)

  return (
    <div className="bg-black/40 rounded-xl p-4 border border-white/[0.06]">
      <div className="flex items-center justify-between mb-3">
        <span className="text-xs text-white/40">{t('formats.mock.card_counter')}</span>
        <span className="text-xs text-[#22C55E]">{t('formats.mock.learned')}</span>
      </div>
      {/* Card */}
      <button
        onClick={() => setFlipped(!flipped)}
        className="w-full cursor-pointer"
      >
        <AnimatePresence mode="wait">
          <motion.div
            key={flipped ? 'back' : 'front'}
            initial={{ rotateY: 90, opacity: 0 }}
            animate={{ rotateY: 0, opacity: 1 }}
            exit={{ rotateY: -90, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className={`rounded-xl border p-6 text-center min-h-[100px] flex items-center justify-center ${
              flipped
                ? 'bg-[#F97316]/[0.08] border-[#F97316]/20'
                : 'bg-white/[0.04] border-white/[0.08]'
            }`}
          >
            {flipped ? (
              <div>
                <div className="text-xs text-[#F97316] mb-1">{t('formats.mock.answer')}</div>
                <div className="text-sm text-white/80">
                  {t('formats.mock.hashmap_answer')}
                </div>
              </div>
            ) : (
              <div>
                <div className="text-xs text-white/30 mb-1">{t('formats.mock.flip')}</div>
                <div className="text-sm text-white font-medium">{t('formats.mock.hashmap_q')}</div>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </button>
      {/* Actions */}
      <div className="flex gap-2 mt-3">
        <div className="flex-1 text-center text-xs py-2 rounded-lg bg-[#22C55E]/10 border border-[#22C55E]/20 text-[#22C55E]">
          {t('formats.mock.know')}
        </div>
        <div className="flex-1 text-center text-xs py-2 rounded-lg bg-white/[0.04] border border-white/[0.06] text-white/40">
          {t('formats.mock.skip')}
        </div>
      </div>
    </div>
  )
}

export function GameFormatsSection() {
  useLandingLang()
  const [active, setActive] = useState('tower')

  const formats = [
    {
      id: 'tower',
      icon: Swords,
      label: 'Tower Defense',
      color: '#A855F7',
      description: t('formats.tower.desc'),
      mockup: TowerDefenseMockup,
    },
    {
      id: 'quiz',
      icon: Brain,
      label: t('formats.quiz.label'),
      color: '#3B82F6',
      description: t('formats.quiz.desc'),
      mockup: QuizMockup,
    },
    {
      id: 'coding',
      icon: Code,
      label: t('features.python.title'),
      color: '#22C55E',
      description: t('formats.coding.desc'),
      mockup: CodingMockup,
    },
    {
      id: 'match',
      icon: Layers,
      label: 'Match Game',
      color: '#FBBF24',
      description: t('formats.match.desc'),
      mockup: MatchMockup,
    },
    {
      id: 'flash',
      icon: Zap,
      label: 'Flash Cards',
      color: '#F97316',
      description: t('formats.flash.desc'),
      mockup: FlashCardMockup,
    },
  ]

  const activeFormat = formats.find((f) => f.id === active)!
  const ActiveMockup = activeFormat.mockup

  return (
    <section id="formats" className="py-24 px-4">
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-10"
        >
          <h2 className="text-3xl font-bold text-white mb-3">
            {t('formats.title')}
          </h2>
          <p className="text-white/45">{t('formats.subtitle')}</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: 0.1 }}
        >
          {/* Format tabs */}
          <div className="flex flex-wrap justify-center gap-2 mb-6">
            {formats.map((f) => (
              <button
                key={f.id}
                onClick={() => setActive(f.id)}
                className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-medium transition-all ${
                  active === f.id
                    ? 'text-white border'
                    : 'bg-white/[0.03] border border-white/[0.06] text-white/40 hover:text-white/60'
                }`}
                style={
                  active === f.id
                    ? { background: `${f.color}15`, borderColor: `${f.color}40` }
                    : undefined
                }
              >
                <f.icon
                  className="w-4 h-4"
                  style={{ color: active === f.id ? f.color : undefined }}
                />
                {f.label}
              </button>
            ))}
          </div>

          {/* Active mockup */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
            <AnimatePresence mode="wait">
              <motion.div
                key={active}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 10 }}
                transition={{ duration: 0.2 }}
              >
                <ActiveMockup />
              </motion.div>
            </AnimatePresence>

            {/* Description + stats */}
            <div className="flex flex-col justify-center gap-4">
              <AnimatePresence mode="wait">
                <motion.div
                  key={active}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  transition={{ duration: 0.2 }}
                >
                  <div className="flex items-center gap-2 mb-2">
                    <Gamepad2 className="w-5 h-5" style={{ color: activeFormat.color }} />
                    <h3 className="text-lg font-bold text-white">{activeFormat.label}</h3>
                  </div>
                  <p className="text-sm text-white/50 leading-relaxed mb-4">
                    {activeFormat.description}
                  </p>
                </motion.div>
              </AnimatePresence>

              {/* Quick stats */}
              <div className="grid grid-cols-3 gap-2">
                <div className="bg-white/[0.03] border border-white/[0.06] rounded-xl p-3 text-center backdrop-blur-sm">
                  <div className="text-lg font-extrabold text-[#F97316]">5</div>
                  <div className="text-[10px] text-white/35">{t('formats.stat.formats')}</div>
                </div>
                <div className="bg-white/[0.03] border border-white/[0.06] rounded-xl p-3 text-center backdrop-blur-sm">
                  <div className="text-lg font-extrabold text-[#FBBF24]">⭐ 3</div>
                  <div className="text-[10px] text-white/35">{t('formats.stat.stars')}</div>
                </div>
                <div className="bg-white/[0.03] border border-white/[0.06] rounded-xl p-3 text-center backdrop-blur-sm">
                  <div className="text-lg font-extrabold text-[#22C55E]">+100</div>
                  <div className="text-[10px] text-white/35">{t('formats.stat.xp')}</div>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}
