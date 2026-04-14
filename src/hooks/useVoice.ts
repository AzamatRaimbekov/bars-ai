import { useState, useCallback, useEffect, useRef } from "react";
import { voiceService } from "@/services/voiceService";

export type VoiceState = "idle" | "listening" | "thinking" | "speaking";

export function useVoice() {
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [voiceMode, setVoiceMode] = useState(false);
  const [voiceState, setVoiceState] = useState<VoiceState>("idle");
  const autoListenRef = useRef(false);

  useEffect(() => {
    voiceService.init();
  }, []);

  // Track composite voice state
  useEffect(() => {
    if (isListening) setVoiceState("listening");
    else if (isSpeaking) setVoiceState("speaking");
    else setVoiceState("idle");
  }, [isListening, isSpeaking]);

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

  // Speak then auto-listen if voice mode is on
  const speakAndListen = useCallback(
    async (text: string, onFinal?: (text: string) => void, voiceName?: string) => {
      setIsSpeaking(true);
      await voiceService.speak(text, voiceName);
      setIsSpeaking(false);

      // Auto-listen after AI finishes speaking
      if (autoListenRef.current) {
        // Small delay so user hears the end of speech
        await new Promise((r) => setTimeout(r, 400));
        if (autoListenRef.current) {
          setIsListening(true);
          setTranscript("");
          voiceService.startListening(
            (t, final) => {
              setTranscript(t);
              if (final && onFinal) onFinal(t);
            },
            () => setIsListening(false)
          );
        }
      }
    },
    []
  );

  const stopSpeaking = useCallback(() => {
    voiceService.stopSpeaking();
    setIsSpeaking(false);
  }, []);

  const enableVoiceMode = useCallback(() => {
    setVoiceMode(true);
    autoListenRef.current = true;
  }, []);

  const disableVoiceMode = useCallback(() => {
    setVoiceMode(false);
    autoListenRef.current = false;
    voiceService.stopListening();
    voiceService.stopSpeaking();
    setIsListening(false);
    setIsSpeaking(false);
  }, []);

  const toggleVoiceMode = useCallback(() => {
    if (voiceMode) {
      disableVoiceMode();
    } else {
      enableVoiceMode();
    }
  }, [voiceMode, enableVoiceMode, disableVoiceMode]);

  return {
    isListening,
    isSpeaking,
    transcript,
    voiceMode,
    voiceState,
    startListening,
    stopListening,
    speak,
    speakAndListen,
    stopSpeaking,
    enableVoiceMode,
    disableVoiceMode,
    toggleVoiceMode,
    isSupported: voiceService.isSupported(),
  };
}
