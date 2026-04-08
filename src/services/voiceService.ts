import { getLanguage } from "@/lib/i18n";

type ListenCallback = (transcript: string, isFinal: boolean) => void;

class VoiceService {
  private recognition: InstanceType<typeof window.SpeechRecognition> | null = null;
  private synthesis = window.speechSynthesis;
  private isListening = false;
  private voicesLoaded = false;

  init() {
    const SR =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SR) {
      this.recognition = new SR();
      this.recognition.continuous = true;
      this.recognition.interimResults = true;
      this.recognition.lang = this.getRecognitionLang();
    }

    // Pre-load voices
    if (this.synthesis.getVoices().length > 0) {
      this.voicesLoaded = true;
    }
    this.synthesis.onvoiceschanged = () => {
      this.voicesLoaded = true;
    };

    // React to language changes
    window.addEventListener("lang-change", () => {
      if (this.recognition) {
        this.recognition.lang = this.getRecognitionLang();
      }
    });
  }

  private getRecognitionLang(): string {
    const lang = getLanguage();
    return lang === "ru" ? "ru-RU" : "en-US";
  }

  private pickBestVoice(preferredName?: string): SpeechSynthesisVoice | null {
    const voices = this.synthesis.getVoices();
    if (voices.length === 0) return null;

    const lang = getLanguage();
    const langPrefix = lang === "ru" ? "ru" : "en";

    // If a preferred name is given, try to find it
    if (preferredName) {
      const match = voices.find((v) => v.name.includes(preferredName));
      if (match) return match;
    }

    // Preferred voices by language
    const preferredVoices: Record<string, string[]> = {
      en: [
        "Samantha", "Karen", "Daniel", "Google US English",
        "Microsoft Zira", "Microsoft David", "Alex",
      ],
      ru: [
        "Milena", "Yuri", "Google русский", "Microsoft Irina",
        "Microsoft Pavel", "Katya", "Anna",
      ],
    };

    const preferred = preferredVoices[langPrefix] || preferredVoices.en;
    for (const name of preferred) {
      const match = voices.find((v) => v.name.includes(name) && v.lang.startsWith(langPrefix));
      if (match) return match;
    }

    // Fallback to any voice matching current language
    const langMatch = voices.find((v) => v.lang.startsWith(langPrefix));
    if (langMatch) return langMatch;

    // Last resort: any voice
    return voices[0];
  }

  startListening(onResult: ListenCallback, onEnd?: () => void) {
    if (!this.recognition || this.isListening) return;

    // Update lang before each listen session
    this.recognition.lang = this.getRecognitionLang();
    this.isListening = true;

    this.recognition.onresult = (event: SpeechRecognitionEvent) => {
      const last = event.results[event.results.length - 1];
      onResult(last[0].transcript, last.isFinal);
    };

    this.recognition.onend = () => {
      this.isListening = false;
      onEnd?.();
    };

    this.recognition.onerror = (e: SpeechRecognitionErrorEvent) => {
      // Don't treat "no-speech" as fatal — just restart
      if (e.error === "no-speech" || e.error === "aborted") {
        this.isListening = false;
        onEnd?.();
        return;
      }
      this.isListening = false;
      onEnd?.();
    };

    this.recognition.start();
  }

  stopListening() {
    if (this.recognition && this.isListening) {
      this.recognition.stop();
      this.isListening = false;
    }
  }

  speak(text: string, voiceName?: string): Promise<void> {
    return new Promise((resolve) => {
      this.synthesis.cancel();

      // Clean text for speech — remove markdown, code blocks, URLs
      const cleanText = text
        .replace(/```[\s\S]*?```/g, " code example ")
        .replace(/`([^`]+)`/g, "$1")
        .replace(/\*\*([^*]+)\*\*/g, "$1")
        .replace(/\*([^*]+)\*/g, "$1")
        .replace(/#{1,6}\s/g, "")
        .replace(/https?:\/\/\S+/g, "link")
        .replace(/\n{2,}/g, ". ")
        .replace(/\n/g, " ")
        .trim();

      if (!cleanText) {
        resolve();
        return;
      }

      // Split long text into chunks to avoid synthesis cut-off
      const chunks = this.splitIntoChunks(cleanText, 200);
      let index = 0;

      const speakNext = () => {
        if (index >= chunks.length) {
          resolve();
          return;
        }

        const utterance = new SpeechSynthesisUtterance(chunks[index]);
        utterance.rate = 0.95;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;

        const voice = this.pickBestVoice(voiceName);
        if (voice) {
          utterance.voice = voice;
          utterance.lang = voice.lang;
        } else {
          utterance.lang = this.getRecognitionLang();
        }

        utterance.onend = () => {
          index++;
          speakNext();
        };
        utterance.onerror = () => {
          index++;
          speakNext();
        };

        this.synthesis.speak(utterance);
      };

      speakNext();
    });
  }

  private splitIntoChunks(text: string, maxLen: number): string[] {
    const sentences = text.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [text];
    const chunks: string[] = [];
    let current = "";

    for (const sentence of sentences) {
      if ((current + sentence).length > maxLen && current) {
        chunks.push(current.trim());
        current = sentence;
      } else {
        current += sentence;
      }
    }
    if (current.trim()) chunks.push(current.trim());
    return chunks;
  }

  stopSpeaking() {
    this.synthesis.cancel();
  }

  getIsListening() {
    return this.isListening;
  }

  isSupported() {
    return !!(window.SpeechRecognition || window.webkitSpeechRecognition);
  }

  getAvailableVoices(): SpeechSynthesisVoice[] {
    const lang = getLanguage();
    const langPrefix = lang === "ru" ? "ru" : "en";
    return this.synthesis.getVoices().filter((v) => v.lang.startsWith(langPrefix));
  }
}

export const voiceService = new VoiceService();
