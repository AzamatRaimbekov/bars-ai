import { useState } from "react";
import { Volume2, Loader2 } from "lucide-react";
import { voiceService } from "@/services/voiceService";

interface AudioButtonProps {
  text: string;
  lang: string;
  size?: number;
  className?: string;
}

/** Detect language from text content */
function detectLang(text: string, hint: string): string {
  if (hint !== "auto") return hint;
  // Check for CJK characters (Chinese/Japanese/Korean)
  if (/[\u4e00-\u9fff]/.test(text)) return "zh";
  // Check for Cyrillic with Kyrgyz-specific letters
  if (/[ңөүҮҢӨ]/.test(text)) return "ky";
  // Check for Kazakh-specific letters
  if (/[әғқұүһіӘҒҚҰ]/.test(text)) return "kk";
  // Check for French accents
  if (/[àâéèêëïîôùûüÿçœæ]/i.test(text)) return "fr";
  // General Cyrillic → Russian
  if (/[а-яА-Я]/.test(text)) return "ru";
  // Latin → English
  return "en";
}

export function AudioButton({ text, lang, size = 16, className = "" }: AudioButtonProps) {
  const [playing, setPlaying] = useState(false);

  const handlePlay = async (e: React.MouseEvent) => {
    e.stopPropagation();
    if (playing) {
      voiceService.stopSpeaking();
      setPlaying(false);
      return;
    }
    setPlaying(true);
    try {
      const resolvedLang = detectLang(text, lang);
      await voiceService.speakInLanguage(text, resolvedLang);
    } finally {
      setPlaying(false);
    }
  };

  if (!text?.trim()) return null;

  return (
    <button
      onClick={handlePlay}
      className={`inline-flex items-center justify-center w-7 h-7 rounded-lg bg-white/5 hover:bg-primary/20 border border-white/10 hover:border-primary/30 transition-all cursor-pointer shrink-0 ${playing ? "text-primary bg-primary/15" : "text-white/50 hover:text-primary"} ${className}`}
      title="Озвучить"
    >
      {playing ? <Loader2 size={size} className="animate-spin" /> : <Volume2 size={size} />}
    </button>
  );
}
