import { motion } from 'framer-motion'
import { Star } from 'lucide-react'

const prizes = [
  { place: '1st', amount: '$500', highlight: true },
  { place: '2nd', amount: '$300', highlight: false },
  { place: '3rd', amount: '$150', highlight: false },
]

export function SprintsSection() {
  return (
    <section id="sprints" className="py-24 px-4 relative overflow-hidden">
      <div
        className="absolute pointer-events-none"
        style={{
          width: 500,
          height: 500,
          background: 'radial-gradient(circle, rgba(251,191,36,0.08), transparent 70%)',
          bottom: '-10%',
          right: '-5%',
        }}
      />

      <div className="max-w-2xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-10"
        >
          <h2 className="text-3xl font-bold text-white mb-3">
            Спринты — учись и зарабатывай
          </h2>
          <p className="text-white/45">Регулярные соревнования с реальными призами</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: 0.15 }}
          className="bg-white/[0.03] border border-white/[0.08] rounded-2xl p-6 backdrop-blur-sm"
        >
          <div className="flex items-center justify-between mb-5">
            <span className="text-base font-semibold text-white">Весенний спринт</span>
            <span className="text-sm text-[#FBBF24] font-semibold">3 дня осталось</span>
          </div>

          <div className="grid grid-cols-3 gap-3 mb-5">
            {prizes.map((prize) => (
              <div
                key={prize.place}
                className={`text-center rounded-xl p-4 border ${
                  prize.highlight
                    ? 'bg-[#FBBF24]/10 border-[#FBBF24]/20'
                    : 'bg-white/[0.03] border-white/[0.06]'
                }`}
              >
                <Star className={`w-5 h-5 mx-auto mb-2 ${prize.highlight ? 'text-[#FBBF24]' : 'text-white/30'}`} />
                <div className={`text-lg font-extrabold ${prize.highlight ? 'text-[#FBBF24]' : 'text-white/50'}`}>
                  {prize.place}
                </div>
                <div className="text-xs text-white/40 mt-1">{prize.amount}</div>
              </div>
            ))}
          </div>

          <p className="text-xs text-white/35 text-center">
            Набирай звёзды за выполнение уроков → поднимайся в рейтинге → забирай приз
          </p>
        </motion.div>
      </div>
    </section>
  )
}
