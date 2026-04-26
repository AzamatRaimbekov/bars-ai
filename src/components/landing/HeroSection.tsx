import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

const floatingBadges = [
  { text: '+250 XP', delay: 0, x: -20, y: 10 },
  { text: 'Level 5', delay: 0.1, x: 0, y: -5 },
  { text: '7 streak', delay: 0.2, x: 20, y: 10 },
]

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex flex-col items-center justify-center px-4 pt-16 overflow-hidden">
      {/* Nebula glows */}
      <div
        className="absolute pointer-events-none"
        style={{
          width: 900,
          height: 900,
          background: 'radial-gradient(circle, rgba(249,115,22,0.1), transparent 60%)',
          top: '-20%',
          right: '-15%',
        }}
      />
      <div
        className="absolute pointer-events-none"
        style={{
          width: 600,
          height: 600,
          background: 'radial-gradient(circle, rgba(139,92,246,0.06), transparent 60%)',
          bottom: '5%',
          left: '-10%',
        }}
      />
      <div
        className="absolute pointer-events-none"
        style={{
          width: 400,
          height: 400,
          background: 'radial-gradient(circle, rgba(56,189,248,0.04), transparent 60%)',
          top: '30%',
          left: '60%',
        }}
      />

      {/* Background video */}
      <video
        src="/video/hf_20260426_201936_a657836b-0181-49ed-b1bc-d0cd6f146260.mp4"
        autoPlay
        loop
        muted
        playsInline
        className="absolute inset-0 w-full h-full object-cover"
      />
      {/* Dark overlay for text readability */}
      <div className="absolute inset-0 bg-black/65" />

      {/* Text content */}
      <div className="relative z-10 text-center max-w-2xl mx-auto">
        {/* Subtitle badge */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="text-xs uppercase tracking-[3px] text-[#F97316] font-semibold mb-5"
        >
          Bars AI Platform
        </motion.div>

        {/* Main headline */}
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="text-5xl md:text-7xl font-extrabold text-white leading-[1.1] mb-5 drop-shadow-[0_2px_10px_rgba(0,0,0,0.5)]"
        >
          Учись. Играй.
          <br />
          <span className="bg-gradient-to-r from-[#F97316] to-[#FBBF24] bg-clip-text text-transparent">
            Побеждай.
          </span>
        </motion.h1>

        {/* Subtitle */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="text-lg text-white/70 mb-8 max-w-md mx-auto drop-shadow-[0_1px_4px_rgba(0,0,0,0.5)]"
        >
          AI-ментор, интерактивные курсы и геймификация — всё в одном месте
        </motion.p>

        {/* CTA button */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          <Link
            to="/register"
            className="inline-block text-lg font-bold text-black px-8 py-4 rounded-2xl transition-all hover:scale-105 shadow-[0_0_30px_rgba(249,115,22,0.3)]"
            style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
          >
            Начать бесплатно
          </Link>
        </motion.div>

        {/* Floating badges */}
        <div className="flex justify-center gap-3 mt-8">
          {floatingBadges.map((badge) => (
            <motion.div
              key={badge.text}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5 + badge.delay }}
              className="bg-black/30 border border-white/[0.15] rounded-lg px-4 py-2 text-xs text-white/70 backdrop-blur-sm"
            >
              {badge.text}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
