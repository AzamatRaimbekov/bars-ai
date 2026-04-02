import { useState } from "react";
import { motion } from "framer-motion";
import { Code2, Users, Mic } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { InterviewRoom } from "@/components/simulator/InterviewRoom";

type SimMode = "technical" | "situation" | "voice";

const modes = [
  { id: "technical" as SimMode, name: "Technical Interview", description: "Answer technical questions with AI evaluation", icon: Code2, color: "#6C63FF" },
  { id: "situation" as SimMode, name: "Situation Simulator", description: "Practice real-world customer scenarios", icon: Users, color: "#FFB800" },
  { id: "voice" as SimMode, name: "Voice Interview", description: "Fully voice-based interview simulation", icon: Mic, color: "#00D9FF" },
];

export default function Simulator() {
  const [selectedMode, setSelectedMode] = useState<SimMode | null>(null);

  if (selectedMode) {
    return (
      <PageWrapper>
        <InterviewRoom mode={selectedMode} onEnd={() => setSelectedMode(null)} />
      </PageWrapper>
    );
  }

  return (
    <PageWrapper>
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold mb-2">Interview Simulator</h1>
          <p className="text-text-secondary text-sm">Choose a mode to practice</p>
        </div>

        <div className="grid grid-cols-3 gap-4">
          {modes.map((mode) => (
            <motion.div key={mode.id} whileHover={{ y: -4 }}>
              <Card
                hover
                glow={mode.color}
                onClick={() => setSelectedMode(mode.id)}
                className="text-center cursor-pointer py-8"
              >
                <div
                  className="w-14 h-14 rounded-2xl flex items-center justify-center mx-auto mb-4"
                  style={{ backgroundColor: `${mode.color}15` }}
                >
                  <mode.icon size={24} style={{ color: mode.color }} />
                </div>
                <h3 className="font-semibold text-sm mb-2">{mode.name}</h3>
                <p className="text-xs text-text-secondary">{mode.description}</p>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </PageWrapper>
  );
}
