import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { t, useLandingLang, LANG_LABELS, type LandingLang } from '@/lib/landing-i18n'

export function LandingNav() {
  const { lang, setLang } = useLandingLang()
  const [scrolled, setScrolled] = useState(false)

  const navLinks = [
    { label: t('nav.features'), href: '#features' },
    { label: t('nav.formats'), href: '#formats' },
    { label: t('nav.sprints'), href: '#sprints' },
    { label: t('nav.authors'), href: '#create' },
    { label: t('nav.faq'), href: '#faq' },
  ]

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
          {/* Language switcher */}
          <div className="flex items-center gap-1">
            {(Object.keys(LANG_LABELS) as LandingLang[]).map((code) => (
              <button
                key={code}
                onClick={() => setLang(code)}
                className={`text-xs font-semibold px-2 py-1 rounded-lg transition-colors ${
                  lang === code
                    ? 'bg-[#F97316] text-black'
                    : 'text-white/40 hover:text-white/70'
                }`}
              >
                {LANG_LABELS[code]}
              </button>
            ))}
          </div>

          <Link
            to="/login"
            className="text-sm text-white/60 hover:text-white transition-colors"
          >
            {t('nav.login')}
          </Link>
          <Link
            to="/register"
            className="text-sm font-semibold text-black bg-[#F97316] hover:bg-[#FB923C] px-4 py-2 rounded-xl transition-colors"
          >
            {t('nav.start')}
          </Link>
        </div>
      </div>
    </motion.nav>
  )
}
