import { LandingNav } from '@/components/landing/LandingNav'
import { StarField } from '@/components/landing/StarField'
import { HeroSection } from '@/components/landing/HeroSection'
import { FeaturesSection } from '@/components/landing/FeaturesSection'
import { GameFormatsSection } from '@/components/landing/GameFormatsSection'
import { ProgressionSection } from '@/components/landing/ProgressionSection'
import { HowItWorksSection } from '@/components/landing/HowItWorksSection'
import { SprintsSection } from '@/components/landing/SprintsSection'
import { CreateCoursesSection } from '@/components/landing/CreateCoursesSection'
import { FAQSection } from '@/components/landing/FAQSection'
import { FinalCTASection } from '@/components/landing/FinalCTASection'

export default function Landing() {
  return (
    <div className="min-h-screen bg-[#050510] relative">
      <StarField />
      <LandingNav />
      <main className="relative z-10">
        <HeroSection />
        <FeaturesSection />
        <GameFormatsSection />
        <ProgressionSection />
        <HowItWorksSection />
        <SprintsSection />
        <CreateCoursesSection />
        <FAQSection />
        <FinalCTASection />
      </main>
      <footer className="relative z-10 py-8 px-4 border-t border-white/[0.06]">
        <div className="max-w-6xl mx-auto text-center text-xs text-white/25">
          © 2026 Bars AI. Все права защищены.
        </div>
      </footer>
    </div>
  )
}
