import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ChevronDown } from 'lucide-react'

const faqs = [
  {
    question: 'Это бесплатно?',
    answer: 'Да, регистрация и большинство курсов бесплатны.',
  },
  {
    question: 'Нужно устанавливать что-то?',
    answer: 'Нет, всё работает в браузере — включая Python.',
  },
  {
    question: 'Как заработать на спринтах?',
    answer: 'Проходи уроки, набирай звёзды, попади в топ рейтинга — забирай приз.',
  },
]

function FAQItem({ question, answer }: { question: string; answer: string }) {
  const [open, setOpen] = useState(false)

  return (
    <button
      onClick={() => setOpen(!open)}
      className="w-full text-left bg-white/[0.03] border border-white/[0.06] rounded-2xl p-5 transition-colors hover:border-white/10"
    >
      <div className="flex items-center justify-between">
        <span className="text-sm font-semibold text-white">{question}</span>
        <ChevronDown
          className={`w-4 h-4 text-white/30 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
        />
      </div>
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <p className="text-sm text-white/40 mt-3">{answer}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </button>
  )
}

export function FAQSection() {
  return (
    <section id="faq" className="py-24 px-4">
      <div className="max-w-2xl mx-auto">
        <motion.h2
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-3xl font-bold text-white text-center mb-12"
        >
          Частые вопросы
        </motion.h2>

        <div className="flex flex-col gap-3">
          {faqs.map((faq, i) => (
            <motion.div
              key={faq.question}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
            >
              <FAQItem {...faq} />
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
