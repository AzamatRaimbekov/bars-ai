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

        <div className="flex items-center gap-2 sm:gap-3">
          {/* Language switcher */}
          <select
            value={lang}
            onChange={(e) => setLang(e.target.value as LandingLang)}
            aria-label="Language"
            className="appearance-none bg-white/5 border border-white/10 text-white/80 text-xs font-semibold rounded-lg pl-2 pr-6 py-1.5 cursor-pointer hover:bg-white/10 hover:text-white transition-colors focus:outline-none focus:ring-2 focus:ring-[#F97316]/40 bg-[url('data:image/svg+xml;charset=UTF-8,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20viewBox=%270%200%2024%2024%27%20fill=%27none%27%20stroke=%27white%27%20stroke-width=%272.5%27%20stroke-linecap=%27round%27%20stroke-linejoin=%27round%27%3e%3cpolyline%20points=%276%209%2012%2015%2018%209%27/%3e%3c/svg%3e')] bg-no-repeat bg-[length:10px] bg-[right_6px_center]"
          >
            {(Object.keys(LANG_LABELS) as LandingLang[]).map((code) => (
              <option key={code} value={code} className="bg-[#0a0a0a] text-white">
                {LANG_LABELS[code]}
              </option>
            ))}
          </select>

          <Link
            to="/login"
            className="hidden sm:inline text-sm text-white/60 hover:text-white transition-colors"
          >
            {t('nav.login')}
          </Link>
          <Link
            to="/register"
            className="text-xs sm:text-sm font-semibold text-black bg-[#F97316] hover:bg-[#FB923C] px-3 sm:px-4 py-2 rounded-xl transition-colors whitespace-nowrap"
          >
            {t('nav.start')}
          </Link>
        </div>
      </div>
    </motion.nav>
  )
}
