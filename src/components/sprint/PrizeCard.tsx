import { motion } from 'framer-motion'

const PLACE_CONFIG: Record<number, { medal: string; gradient: string; border: string; text: string }> = {
  1: {
    medal: '\uD83E\uDD47',
    gradient: 'from-yellow-500/20 to-yellow-600/5',
    border: 'border-yellow-500/30',
    text: 'text-yellow-400',
  },
  2: {
    medal: '\uD83E\uDD48',
    gradient: 'from-white/10 to-white/5',
    border: 'border-white/15',
    text: 'text-white/70',
  },
  3: {
    medal: '\uD83E\uDD49',
    gradient: 'from-amber-700/15 to-amber-800/5',
    border: 'border-amber-700/25',
    text: 'text-amber-500',
  },
}

interface PrizeCardProps {
  place: number
  amount: number
  currency: string
  bonus?: string
}

export function PrizeCard({ place, amount, currency, bonus }: PrizeCardProps) {
  const config = PLACE_CONFIG[place] ?? PLACE_CONFIG[3]

  const symbol = currency === 'USD' ? '$' : currency === 'EUR' ? '\u20AC' : currency

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: (place - 1) * 0.1 }}
      className={`bg-gradient-to-br ${config.gradient} border ${config.border} rounded-2xl p-5 text-center flex-1 min-w-0`}
    >
      <p className="text-3xl mb-2">{config.medal}</p>
      <p className={`text-2xl font-bold ${config.text}`}>
        {symbol}{amount}
      </p>
      {bonus && (
        <p className="text-xs text-white/40 mt-1.5">{bonus}</p>
      )}
      <p className="text-[11px] text-white/30 mt-1">
        {place === 1 ? '1-е место' : place === 2 ? '2-е место' : '3-е место'}
      </p>
    </motion.div>
  )
}
