import { useCallback, useEffect } from "react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { ChatWindow } from "@/components/chat/ChatWindow";
import { useChat } from "@/hooks/useChat";
import { useVoice } from "@/hooks/useVoice";
import { useUserStore } from "@/store/userStore";
import { useChatStore } from "@/store/chatStore";
import { DIRECTIONS } from "@/data/directions";

const SUGGESTIONS: Record<string, string[]> = {
  frontend: ["Explain CSS Flexbox", "How do React hooks work?", "What's the DOM?", "Review my code approach"],
  english: ["Practice conversation", "Explain present perfect", "Help with pronunciation", "Business email writing"],
  callcenter: ["Handle angry customer", "Upsell techniques", "Phone greeting scripts", "Complaint resolution"],
  cib: ["What is DCF?", "Explain M&A process", "Banking interview prep", "Financial modeling basics"],
};

export default function Mentor() {
  const profile = useUserStore((s) => s.profile);
  const clearMessages = useChatStore((s) => s.clearMessages);

  const direction = profile?.direction ?? "frontend";
  const dirConfig = DIRECTIONS[direction];
  const mentor = dirConfig.mentor;

  const contextPrompt = `${mentor.systemPrompt}\n\nThe student's name is ${profile?.name}. Their current level is ${profile?.assessmentLevel}. They are studying ${dirConfig.name}.`;

  const { messages, isLoading, send } = useChat(contextPrompt);
  const voice = useVoice();

  useEffect(() => {
    return () => clearMessages();
  }, []);

  const handleSend = useCallback(
    async (text: string) => {
      const response = await send(text);
      if (response && !voice.isSpeaking) {
        voice.speak(response);
      }
    },
    [send, voice]
  );

  const handleVoiceToggle = useCallback(() => {
    if (voice.isListening) {
      voice.stopListening();
      if (voice.transcript) {
        handleSend(voice.transcript);
      }
    } else if (voice.isSpeaking) {
      voice.stopSpeaking();
    } else {
      voice.startListening((finalText) => {
        handleSend(finalText);
      });
    }
  }, [voice, handleSend]);

  return (
    <PageWrapper>
      <div className="h-[calc(100vh-8rem)] rounded-2xl border border-border bg-surface/50 overflow-hidden">
        <ChatWindow
          messages={messages}
          isLoading={isLoading}
          onSend={handleSend}
          mentorAvatar={mentor.avatar}
          mentorName={mentor.name}
          voiceEnabled={voice.isSupported}
          isListening={voice.isListening}
          isSpeaking={voice.isSpeaking}
          transcript={voice.transcript}
          onVoiceToggle={handleVoiceToggle}
          suggestions={SUGGESTIONS[direction]}
        />
      </div>
    </PageWrapper>
  );
}
