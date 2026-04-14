import { useCallback, useEffect, useRef, useState } from "react";
import { useLocation } from "react-router-dom";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { ChatWindow } from "@/components/chat/ChatWindow";
import { VoiceModeOverlay } from "@/components/chat/VoiceModeOverlay";
import { SessionList } from "@/components/mentor/SessionList";
import { ExerciseBlock } from "@/components/mentor/ExerciseBlock";
import { RecommendationCard } from "@/components/mentor/RecommendationCard";
import { VoiceLessonMode } from "@/components/mentor/VoiceLessonMode";
import { useMentorSessions } from "@/hooks/useMentorSessions";
import { useRecommendations } from "@/hooks/useRecommendations";
import { useVoiceLesson } from "@/hooks/useVoiceLesson";
import { useVoice } from "@/hooks/useVoice";
import { useUserStore } from "@/store/userStore";
import { useTranslation } from "@/hooks/useTranslation";
import { mentorApi } from "@/services/mentorApi";
import { DIRECTIONS } from "@/data/directions";
import { Menu, BookOpen } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import type { RoadmapNodeData } from "@/types";
import type { ChatMessage } from "@/types/chat";

const SUGGESTIONS_EN: Record<string, string[]> = {
  frontend: [
    "Explain CSS Flexbox",
    "How do React hooks work?",
    "What's the DOM?",
    "Review my code approach",
  ],
  english: [
    "Practice conversation",
    "Explain present perfect",
    "Help with pronunciation",
    "Business email writing",
  ],
  callcenter: [
    "Handle angry customer",
    "Upsell techniques",
    "Phone greeting scripts",
    "Complaint resolution",
  ],
  cib: [
    "What is DCF?",
    "Explain M&A process",
    "Banking interview prep",
    "Financial modeling basics",
  ],
};

const SUGGESTIONS_RU: Record<string, string[]> = {
  frontend: [
    "Объясни CSS Flexbox",
    "Как работают React хуки?",
    "Что такое DOM?",
    "Проверь мой подход к коду",
  ],
  english: [
    "Практика разговора",
    "Объясни Present Perfect",
    "Помоги с произношением",
    "Деловое письмо на английском",
  ],
  callcenter: [
    "Работа с недовольным клиентом",
    "Техники допродаж",
    "Скрипты приветствия",
    "Решение жалоб",
  ],
  cib: [
    "Что такое DCF?",
    "Объясни процесс M&A",
    "Подготовка к собеседованию в банк",
    "Основы финансового моделирования",
  ],
};

// Voice commands that the user can say (English)
const VOICE_COMMANDS_EN: Record<string, string> = {
  "repeat that": "__repeat__",
  "say that again": "__repeat__",
  "next topic": "What should I learn next?",
  "quiz me": "Give me a quick quiz question on what we just discussed.",
  "give me an example": "Can you give me a practical example of that?",
  "explain more": "Can you explain that in more detail?",
  "explain again": "Can you explain that differently? I didn't quite understand.",
};

// Voice commands (Russian)
const VOICE_COMMANDS_RU: Record<string, string> = {
  "повтори": "__repeat__",
  "скажи ещё раз": "__repeat__",
  "скажи еще раз": "__repeat__",
  "следующая тема": "Что мне изучить дальше?",
  "задай вопрос": "Задай мне быстрый вопрос по тому, что мы только что обсудили.",
  "дай пример": "Можешь дать практический пример?",
  "объясни подробнее": "Можешь объяснить подробнее?",
  "объясни ещё раз": "Можешь объяснить по-другому? Я не совсем понял.",
  "объясни еще раз": "Можешь объяснить по-другому? Я не совсем понял.",
};

function matchVoiceCommand(text: string, lang: string): string | null {
  const lower = text.toLowerCase().trim();
  const commands = lang === "ru"
    ? { ...VOICE_COMMANDS_RU, ...VOICE_COMMANDS_EN }
    : VOICE_COMMANDS_EN;
  for (const [trigger, command] of Object.entries(commands)) {
    if (lower.includes(trigger)) return command;
  }
  return null;
}

/** Check if a message content contains exercise markers */
function hasExerciseMarkers(content: string): boolean {
  return /\[EXERCISE:(code|qa|roleplay)\]/.test(content);
}

/** Convert mentor API messages to ChatMessage format for ChatWindow */
function toChatMessages(
  messages: { id: string; role: "user" | "assistant"; content: string; created_at: string }[]
): ChatMessage[] {
  return messages.map((m) => ({
    id: m.id,
    role: m.role,
    content: m.content,
    timestamp: new Date(m.created_at).getTime(),
  }));
}

export default function Mentor() {
  const profile = useUserStore((s) => s.profile);
  const [lastAIMessage, setLastAIMessage] = useState("");
  const [isSending, setIsSending] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [voiceLessonActive, setVoiceLessonActive] = useState(false);
  const { lang } = useTranslation();
  const location = useLocation();
  const topicNode = (location.state as { topicNode?: RoadmapNodeData })?.topicNode;
  const topicSentRef = useRef(false);

  const direction = profile?.direction ?? "frontend";
  const dirConfig = DIRECTIONS[direction];
  const mentor = dirConfig.mentor;

  // --- New hooks ---
  const {
    sessions,
    activeSession,
    messages: apiMessages,
    isLoading: sessionsLoading,
    createSession,
    selectSession,
    deleteSession,
    addMessage,
    setActiveSession,
  } = useMentorSessions();

  const { recommendations } = useRecommendations();
  const voiceLesson = useVoiceLesson(activeSession?.id ?? null);
  const voice = useVoice();

  // Convert API messages to ChatMessage format
  const chatMessages = toChatMessages(apiMessages);

  // Track the latest AI message for voice overlay display
  useEffect(() => {
    const lastMsg = [...apiMessages].reverse().find((m) => m.role === "assistant");
    if (lastMsg) setLastAIMessage(lastMsg.content);
  }, [apiMessages]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      voice.disableVoiceMode();
    };
  }, []);

  // Auto-start teaching when navigated from roadmap with a topic
  useEffect(() => {
    if (topicNode && !topicSentRef.current && !isSending && apiMessages.length === 0) {
      topicSentRef.current = true;
      const startMsg = lang === "ru"
        ? `Давай начнём урок по теме "${topicNode.title.ru}". Объясни мне основы.`
        : `Let's start learning about "${topicNode.title.en}". Explain the basics.`;
      handleSend(startMsg);
    }
  }, [topicNode, isSending, apiMessages.length, lang]);

  // Core send handler — sends text via mentorApi, speaks response, auto-listens
  const handleSend = useCallback(
    async (text: string) => {
      // Check for voice commands
      const command = matchVoiceCommand(text, lang);
      let actualText = text;

      if (command === "__repeat__") {
        if (lastAIMessage) {
          if (voice.voiceMode) {
            voice.speakAndListen(lastAIMessage, (finalText) => {
              handleSend(finalText);
            });
          } else {
            voice.speak(lastAIMessage);
          }
        }
        return;
      } else if (command) {
        actualText = command;
      }

      // Add user message to local state
      addMessage({
        id: crypto.randomUUID(),
        role: "user",
        content: actualText,
        created_at: new Date().toISOString(),
      });

      setIsSending(true);
      try {
        // Call API
        const response = await mentorApi.chat(actualText, activeSession?.id);

        // Update session if a new one was created
        if (!activeSession || activeSession.id !== response.session_id) {
          // Reload sessions to pick up the new one
          const freshSessions = await mentorApi.getSessions();
          const newSession = freshSessions.find((s) => s.id === response.session_id);
          if (newSession) {
            setActiveSession(newSession);
          }
        }

        // Add assistant message
        addMessage({
          id: response.message_id,
          role: "assistant",
          content: response.content,
          created_at: new Date().toISOString(),
        });

        // Voice handling
        if (response.content) {
          if (voice.voiceMode) {
            voice.speakAndListen(response.content, (finalText) => {
              handleSend(finalText);
            });
          } else {
            voice.speak(response.content);
          }
        }

        return response.content;
      } catch (err) {
        console.error("Failed to send message:", err);
      } finally {
        setIsSending(false);
      }
    },
    [addMessage, activeSession, voice, lastAIMessage, lang, setActiveSession]
  );

  // Handle exercise answer submission — send as a new chat message
  const handleExerciseAnswer = useCallback(
    (answer: string) => {
      handleSend(answer);
    },
    [handleSend]
  );

  // Single mic toggle for text-mode inline voice
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

  // Voice mode mic toggle
  const handleVoiceModeMicToggle = useCallback(() => {
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

  // When voice mode is enabled, auto-start listening
  const handleVoiceModeToggle = useCallback(() => {
    if (voice.voiceMode) {
      voice.disableVoiceMode();
    } else {
      voice.enableVoiceMode();
      setTimeout(() => {
        voice.startListening((finalText) => {
          handleSend(finalText);
        });
      }, 300);
    }
  }, [voice, handleSend]);

  const handleVoiceModeClose = useCallback(() => {
    voice.disableVoiceMode();
  }, [voice]);

  // --- Session management ---
  const handleCreateSession = useCallback(() => {
    createSession(direction);
    setSidebarOpen(false);
  }, [createSession, direction]);

  const handleSelectSession = useCallback(
    (session: Parameters<typeof selectSession>[0]) => {
      selectSession(session);
      setSidebarOpen(false);
    },
    [selectSession]
  );

  const handleDeleteSession = useCallback(
    (sessionId: string) => {
      deleteSession(sessionId);
    },
    [deleteSession]
  );

  // --- Voice lesson ---
  const handleStartVoiceLesson = useCallback(() => {
    const topic = lang === "ru" ? "Текущая тема разговора" : "Current conversation topic";
    const promptTopic = window.prompt(
      lang === "ru" ? "Тема голосового урока:" : "Voice lesson topic:",
      topic
    );
    if (promptTopic?.trim()) {
      voiceLesson.start(promptTopic.trim());
      setVoiceLessonActive(true);
    }
  }, [voiceLesson, lang]);

  const handleVoiceLessonClose = useCallback(() => {
    voiceLesson.reset();
    setVoiceLessonActive(false);
  }, [voiceLesson]);

  // Show recommendations only if there are some and fewer than 3 messages
  const showRecommendations =
    recommendations?.weekly_plan &&
    recommendations.weekly_plan.length > 0 &&
    apiMessages.length < 3;

  const isLoading = isSending || sessionsLoading;

  return (
    <PageWrapper>
      <div className="h-[calc(100dvh-11rem)] lg:h-[calc(100vh-8rem)] rounded-2xl border border-white/6 bg-[#0A0A0A] overflow-hidden relative flex">
        {/* Mobile sidebar toggle */}
        <button
          onClick={() => setSidebarOpen(!sidebarOpen)}
          className="lg:hidden absolute top-4 left-4 z-20 w-9 h-9 rounded-xl bg-surface border border-border flex items-center justify-center text-text-secondary hover:text-text transition-colors cursor-pointer"
        >
          <Menu size={16} />
        </button>

        {/* Sidebar — desktop always visible, mobile as overlay */}
        <AnimatePresence>
          {(sidebarOpen || typeof window !== "undefined") && (
            <>
              {/* Mobile overlay backdrop */}
              {sidebarOpen && (
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  onClick={() => setSidebarOpen(false)}
                  className="lg:hidden fixed inset-0 z-30 bg-black/50"
                />
              )}

              {/* Sidebar panel */}
              <div
                className={`
                  ${sidebarOpen ? "fixed inset-y-0 left-0 z-40" : "hidden"}
                  lg:relative lg:block lg:z-auto
                  w-64 shrink-0
                `}
              >
                <SessionList
                  sessions={sessions}
                  activeSession={activeSession}
                  onSelect={handleSelectSession}
                  onCreate={handleCreateSession}
                  onDelete={handleDeleteSession}
                />
              </div>
            </>
          )}
        </AnimatePresence>

        {/* Main chat area */}
        <div className="flex-1 flex flex-col min-w-0 relative">
          {/* Recommendations banner */}
          {showRecommendations && (
            <div className="px-4 pt-3">
              <RecommendationCard recommendations={recommendations!.weekly_plan} />
            </div>
          )}

          {/* Exercise-aware ChatWindow */}
          <div className="flex-1 overflow-hidden">
            <ChatWindow
              messages={chatMessages}
              isLoading={isLoading}
              onSend={handleSend}
              mentorAvatar={mentor.avatar}
              mentorName={mentor.name}
              voiceEnabled={voice.isSupported}
              isListening={voice.isListening}
              isSpeaking={voice.isSpeaking}
              transcript={voice.transcript}
              onVoiceToggle={handleVoiceToggle}
              suggestions={(lang === "ru" ? SUGGESTIONS_RU : SUGGESTIONS_EN)[direction]}
              voiceMode={voice.voiceMode}
              voiceState={voice.voiceState}
              onVoiceModeToggle={handleVoiceModeToggle}
              renderMessage={
                (msg) => {
                  if (msg.role === "assistant" && hasExerciseMarkers(msg.content)) {
                    return (
                      <ExerciseBlock
                        content={msg.content}
                        onSubmit={handleExerciseAnswer}
                      />
                    );
                  }
                  return undefined;
                }
              }
            />
          </div>

          {/* Voice lesson button — floating bottom-right */}
          {voice.isSupported && (
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={handleStartVoiceLesson}
              className="absolute bottom-20 right-4 z-10 flex items-center gap-2 px-4 py-2.5 rounded-xl bg-surface border border-border text-text-secondary hover:text-text hover:border-primary/30 transition-all cursor-pointer text-xs font-medium shadow-lg"
            >
              <BookOpen size={14} />
              {lang === "ru" ? "Голосовой урок" : "Voice lesson"}
            </motion.button>
          )}
        </div>

        {/* Voice mode overlay (free conversation) */}
        <VoiceModeOverlay
          active={voice.voiceMode}
          voiceState={voice.voiceState}
          mentorAvatar={mentor.avatar}
          mentorName={mentor.name}
          transcript={voice.transcript}
          lastAIMessage={lastAIMessage}
          isLoading={isLoading}
          onMicToggle={handleVoiceModeMicToggle}
          onClose={handleVoiceModeClose}
          onSwitchToText={handleVoiceModeClose}
        />

        {/* Voice lesson overlay */}
        {voiceLessonActive && voiceLesson.phase !== "idle" && (
          <VoiceLessonMode
            phase={voiceLesson.phase}
            progress={voiceLesson.progress}
            content={voiceLesson.lastResponse}
            isLoading={voiceLesson.isLoading}
            onNext={() => voiceLesson.next()}
            onRepeat={() => voiceLesson.repeat()}
            onAnswer={(text) => voiceLesson.answer(text)}
            onClose={handleVoiceLessonClose}
          />
        )}
      </div>
    </PageWrapper>
  );
}
