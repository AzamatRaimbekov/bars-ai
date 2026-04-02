import { useState, useCallback, useEffect } from "react";
import { voiceService } from "@/services/voiceService";

export function useVoice() {
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [transcript, setTranscript] = useState("");

  useEffect(() => {
    voiceService.init();
  }, []);

  const startListening = useCallback((onFinal?: (text: string) => void) => {
    setIsListening(true);
    setTranscript("");
    voiceService.startListening(
      (text, isFinal) => {
        setTranscript(text);
        if (isFinal && onFinal) onFinal(text);
      },
      () => setIsListening(false)
    );
  }, []);

  const stopListening = useCallback(() => {
    voiceService.stopListening();
    setIsListening(false);
  }, []);

  const speak = useCallback(async (text: string, voiceName?: string) => {
    setIsSpeaking(true);
    await voiceService.speak(text, voiceName);
    setIsSpeaking(false);
  }, []);

  const stopSpeaking = useCallback(() => {
    voiceService.stopSpeaking();
    setIsSpeaking(false);
  }, []);

  return {
    isListening,
    isSpeaking,
    transcript,
    startListening,
    stopListening,
    speak,
    stopSpeaking,
    isSupported: voiceService.isSupported(),
  };
}
