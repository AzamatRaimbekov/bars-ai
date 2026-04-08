import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { useTranslation } from "@/hooks/useTranslation";
import type { Slide } from "@/types/lesson";

interface LessonSlideProps {
  slide: Slide;
  onContinue: () => void;
}

export function LessonSlide({ slide, onContinue }: LessonSlideProps) {
  const { lang } = useTranslation();

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      className="flex flex-col h-full"
    >
      <div className="flex-1 overflow-y-auto px-1 pb-4">
        <h2 className="text-xl font-bold mb-4">{slide.title[lang]}</h2>
        <div className="text-sm text-text-secondary leading-relaxed whitespace-pre-line mb-6">{slide.content[lang]}</div>
        {slide.code && (
          <div className="rounded-xl bg-bg border border-border overflow-hidden mb-4">
            <div className="px-4 py-2 border-b border-border text-xs text-text-secondary uppercase">{slide.code.language}</div>
            <pre className="p-4 overflow-x-auto text-sm font-mono"><code className="text-accent">{slide.code.code}</code></pre>
          </div>
        )}
        {slide.image && <img src={slide.image} alt={slide.title[lang]} className="w-full rounded-xl border border-border mb-4" />}
      </div>
      <div className="pt-4 border-t border-border">
        <Button className="w-full" onClick={onContinue}>Continue <ArrowRight size={16} /></Button>
      </div>
    </motion.div>
  );
}
