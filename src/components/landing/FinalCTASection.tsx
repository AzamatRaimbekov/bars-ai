import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

export function FinalCTASection() {
  return (
    <section className="py-24 px-4 relative overflow-hidden">
      <div
        className="absolute pointer-events-none"
        style={{
          width: 600,
          height: 600,
          background: 'radial-gradient(circle, rgba(249,115,22,0.08), transparent 60%)',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        className="max-w-xl mx-auto text-center relative z-10 border border-[#F97316]/20 rounded-2xl py-16 px-6 backdrop-blur-sm bg-[#F97316]/[0.03]"
      >
        <h2 className="text-3xl font-extrabold text-white mb-4">Готов начать?</h2>
        <p className="text-base text-white/45 mb-8">Присоединяйся — это бесплатно</p>
        <Link
          to="/register"
          className="inline-block text-lg font-bold text-black px-10 py-4 rounded-2xl transition-all hover:scale-105 shadow-[0_0_30px_rgba(249,115,22,0.3)]"
          style={{ background: 'linear-gradient(135deg, #F97316, #FB923C)' }}
        >
          Создать аккаунт
        </Link>
      </motion.div>
    </section>
  )
}
