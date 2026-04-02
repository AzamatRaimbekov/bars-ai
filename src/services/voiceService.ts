type ListenCallback = (transcript: string, isFinal: boolean) => void;

class VoiceService {
  private recognition: SpeechRecognition | null = null;
  private synthesis = window.speechSynthesis;
  private isListening = false;

  init() {
    const SR =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SR) {
      this.recognition = new SR();
      this.recognition.continuous = true;
      this.recognition.interimResults = true;
      this.recognition.lang = "en-US";
    }
  }

  startListening(onResult: ListenCallback, onEnd?: () => void) {
    if (!this.recognition || this.isListening) return;
    this.isListening = true;

    this.recognition.onresult = (event) => {
      const last = event.results[event.results.length - 1];
      onResult(last[0].transcript, last.isFinal);
    };

    this.recognition.onend = () => {
      this.isListening = false;
      onEnd?.();
    };

    this.recognition.onerror = () => {
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
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.95;
      utterance.pitch = 1;

      if (voiceName) {
        const voices = this.synthesis.getVoices();
        const voice = voices.find((v) => v.name.includes(voiceName));
        if (voice) utterance.voice = voice;
      }

      utterance.onend = () => resolve();
      utterance.onerror = () => resolve();
      this.synthesis.speak(utterance);
    });
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
}

export const voiceService = new VoiceService();
