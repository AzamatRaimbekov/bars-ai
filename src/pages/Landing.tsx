import { LandingNav } from '@/components/landing/LandingNav'
import { HeroSection } from '@/components/landing/HeroSection'
import { FeaturesSection } from '@/components/landing/FeaturesSection'
import { HowItWorksSection } from '@/components/landing/HowItWorksSection'
import { SprintsSection } from '@/components/landing/SprintsSection'
import { CreateCoursesSection } from '@/components/landing/CreateCoursesSection'
import { FAQSection } from '@/components/landing/FAQSection'
import { FinalCTASection } from '@/components/landing/FinalCTASection'

export default function Landing() {
  return (
    <div className="min-h-screen bg-black">
      <LandingNav />
      <main>
        <HeroSection />
        <FeaturesSection />
        <HowItWorksSection />
        <SprintsSection />
        <CreateCoursesSection />
        <FAQSection />
        <FinalCTASection />
      </main>
      <footer className="py-8 px-4 border-t border-white/[0.06]">
        <div className="max-w-6xl mx-auto text-center text-xs text-white/25">
          © 2026 Bars AI. Все права защищены.
        </div>
      </footer>
    </div>
  )
}
