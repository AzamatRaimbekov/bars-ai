import { motion } from 'framer-motion'
import { Bot, Code, Trophy, BookOpen } from 'lucide-react'
import { t, useLandingLang } from '@/lib/landing-i18n'

export function FeaturesSection() {
  useLandingLang()

  const features = [
    {
      icon: Bot,
      title: t('features.ai.title'),
      description: t('features.ai.desc'),
    },
    {
      icon: Code,
      title: t('features.python.title'),
      description: t('features.python.desc'),
    },
    {
      icon: Trophy,
      title: t('features.gamification.title'),
      description: t('features.gamification.desc'),
    },
    {
      icon: BookOpen,
      title: t('features.courses.title'),
      description: t('features.courses.desc'),
    },
  ]

  return (
    <section id="features" className="py-24 px-4">
      <div className="max-w-4xl mx-auto">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-3xl font-bold text-white text-center mb-12"
        >
          {t('features.title')}
        </motion.h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {features.map((feature, i) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className="bg-white/[0.03] border border-white/[0.08] rounded-2xl p-6 text-center backdrop-blur-sm hover:border-[#F97316]/20 transition-colors"
            >
              <div className="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#F97316]/10 mb-4">
                <feature.icon className="w-6 h-6 text-[#F97316]" />
              </div>
              <h3 className="text-base font-semibold text-white mb-1">{feature.title}</h3>
              <p className="text-sm text-white/40">{feature.description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
