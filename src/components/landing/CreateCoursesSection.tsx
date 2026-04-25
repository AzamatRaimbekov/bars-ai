import { motion } from 'framer-motion'
import { PenLine, Bot, DollarSign } from 'lucide-react'

const benefits = [
  {
    icon: PenLine,
    title: 'Удобный редактор',
    description: 'Создавай уроки с видео, кодом и квизами',
    accent: false,
  },
  {
    icon: Bot,
    title: 'AI генерирует за тебя',
    description: 'Опиши тему — AI создаст структуру курса',
    accent: false,
  },
  {
    icon: DollarSign,
    title: 'Зарабатывай',
    description: 'Устанавливай цену и получай доход',
    accent: true,
  },
]

export function CreateCoursesSection() {
  return (
    <section id="create" className="py-24 px-4 relative overflow-hidden">
      <div
        className="absolute pointer-events-none"
        style={{
          width: 400,
          height: 400,
          background: 'radial-gradient(circle, rgba(74,222,128,0.06), transparent 70%)',
          top: '-5%',
          left: '-5%',
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
            Создавай курсы. Зарабатывай.
          </h2>
          <p className="text-white/45">Стань автором и получай доход с каждого ученика</p>
        </motion.div>

        <div className="flex flex-col gap-3">
          {benefits.map((item, i) => (
            <motion.div
              key={item.title}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
              className={`flex items-center gap-4 rounded-2xl p-4 border ${
                item.accent
                  ? 'bg-[#4ADE80]/[0.06] border-[#4ADE80]/15'
                  : 'bg-white/[0.03] border-white/[0.06]'
              }`}
            >
              <div
                className={`w-10 h-10 min-w-10 rounded-xl flex items-center justify-center ${
                  item.accent ? 'bg-[#4ADE80]/15' : 'bg-white/[0.06]'
                }`}
              >
                <item.icon className={`w-5 h-5 ${item.accent ? 'text-[#4ADE80]' : 'text-white/50'}`} />
              </div>
              <div>
                <h3 className={`text-sm font-semibold ${item.accent ? 'text-[#4ADE80]' : 'text-white'}`}>
                  {item.title}
                </h3>
                <p className="text-xs text-white/40 mt-0.5">{item.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
