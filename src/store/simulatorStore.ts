import { create } from "zustand";
import type { SimulatorSession, SimulatorQuestion } from "@/types";

interface SimulatorState {
  session: SimulatorSession | null;
  isInterviewing: boolean;
  startSession: (session: SimulatorSession) => void;
  addQuestion: (question: SimulatorQuestion) => void;
  nextQuestion: () => void;
  endSession: (overallScore: number) => void;
  setInterviewing: (v: boolean) => void;
  reset: () => void;
}

export const useSimulatorStore = create<SimulatorState>()((set) => ({
  session: null,
  isInterviewing: false,

  startSession: (session) => set({ session, isInterviewing: true }),

  addQuestion: (question) =>
    set((s) => {
      if (!s.session) return s;
      return {
        session: {
          ...s.session,
          questions: [...s.session.questions, question],
        },
      };
    }),

  nextQuestion: () =>
    set((s) => {
      if (!s.session) return s;
      return {
        session: { ...s.session, currentIndex: s.session.currentIndex + 1 },
      };
    }),

  endSession: (overallScore) =>
    set((s) => {
      if (!s.session) return s;
      return {
        session: { ...s.session, completed: true, overallScore },
        isInterviewing: false,
      };
    }),

  setInterviewing: (v) => set({ isInterviewing: v }),
  reset: () => set({ session: null, isInterviewing: false }),
}));
