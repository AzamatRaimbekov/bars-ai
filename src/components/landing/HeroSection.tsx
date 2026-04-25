import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

const floatingBadges = [
  { text: '+250 XP', delay: 0 },
  { text: 'Level 5', delay: 0.1 },
  { text: '7 streak', delay: 0.2 },
]

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center px-4 pt-16 overflow-hidden">
      <div
        className="absolute pointer-events-none"
        style={{
          width: 800,
          height: 800,
          background: 'radial-gradient(circle, rgba(249,115,22,0.08), transparent 70%)',
          top: '-10%',
          right: '-10%',
        }}
      />

      <div className="relative z-10 text-center max-w-2xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-xs uppercase tracking-[3px] text-[#F97316] font-semibold mb-6"
        >
          Bars AI Platform
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="text-5xl md:text-7xl font-extrabold text-white leading-[1.1] mb-5"
        >
          Учись. Играй.
          <br />
          <span className="text-[#F97316]">Побеждай.</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="text-lg text-white/45 mb-8 max-w-md mx-auto"
        >
          AI-ментор, интерактивные курсы и геймификация — всё в одном месте
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          <Link
            to="/register"
            className="inline-block text-lg font-bold text-black px-8 py-4 rounded-2xl transition-all hover:scale-105"
            style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
          >
            Начать бесплатно
          </Link>
        </motion.div>

        <div className="flex justify-center gap-3 mt-8">
          {floatingBadges.map((badge) => (
            <motion.div
              key={badge.text}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5 + badge.delay }}
              className="bg-white/[0.04] border border-white/[0.08] rounded-lg px-4 py-2 text-xs text-white/50"
            >
              {badge.text}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
