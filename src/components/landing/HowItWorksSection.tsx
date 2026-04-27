import { motion } from 'framer-motion'
import { t, useLandingLang } from '@/lib/landing-i18n'

export function HowItWorksSection() {
  useLandingLang()

  const steps = [
    {
      number: '1',
      title: t('how.step1.title'),
      description: t('how.step1.desc'),
    },
    {
      number: '2',
      title: t('how.step2.title'),
      description: t('how.step2.desc'),
    },
    {
      number: '3',
      title: t('how.step3.title'),
      description: t('how.step3.desc'),
    },
  ]

  return (
    <section className="py-24 px-4">
      <div className="max-w-2xl mx-auto">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-3xl font-bold text-white text-center mb-12"
        >
          {t('how.title')}
        </motion.h2>

        <div className="flex flex-col gap-6">
          {steps.map((step, i) => (
            <motion.div
              key={step.number}
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.15 }}
              className="flex items-start gap-4"
            >
              <div className="w-10 h-10 min-w-10 rounded-xl bg-[#F97316]/15 border border-[#F97316]/30 flex items-center justify-center text-[#F97316] font-extrabold text-base">
                {step.number}
              </div>
              <div>
                <h3 className="text-base font-semibold text-white">{step.title}</h3>
                <p className="text-sm text-white/40 mt-1">{step.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
