import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

const navLinks = [
  { label: 'Фичи', href: '#features' },
  { label: 'Спринты', href: '#sprints' },
  { label: 'Авторам', href: '#create' },
  { label: 'FAQ', href: '#faq' },
]

export function LandingNav() {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const scrollTo = (href: string) => {
    const el = document.querySelector(href)
    el?.scrollIntoView({ behavior: 'smooth' })
  }

  return (
    <motion.nav
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled
          ? 'bg-black/80 backdrop-blur-xl border-b border-white/6'
          : 'bg-transparent'
      }`}
    >
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <Link to="/" className="text-xl font-bold text-white">
          Bars<span className="text-[#F97316]"> AI</span>
        </Link>

        <div className="hidden md:flex items-center gap-6">
          {navLinks.map((link) => (
            <button
              key={link.href}
              onClick={() => scrollTo(link.href)}
              className="text-sm text-white/50 hover:text-white transition-colors"
            >
              {link.label}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3">
          <Link
            to="/login"
            className="text-sm text-white/60 hover:text-white transition-colors"
          >
            Войти
          </Link>
          <Link
            to="/register"
            className="text-sm font-semibold text-black bg-[#F97316] hover:bg-[#FB923C] px-4 py-2 rounded-xl transition-colors"
          >
            Начать бесплатно
          </Link>
        </div>
      </div>
    </motion.nav>
  )
}
