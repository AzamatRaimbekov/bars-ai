import { useState } from "react";
import { motion } from "framer-motion";
import { Code2, Users, Mic } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { InterviewRoom } from "@/components/simulator/InterviewRoom";
import { useTranslation } from "@/hooks/useTranslation";

type SimMode = "technical" | "situation" | "voice";

export default function Simulator() {
  const [selectedMode, setSelectedMode] = useState<SimMode | null>(null);
  const { t } = useTranslation();

  const modes = [
    { id: "technical" as SimMode, name: t("sim.technical"), description: t("sim.technicalDesc"), icon: Code2, color: "#F97316" },
    { id: "situation" as SimMode, name: t("sim.situation"), description: t("sim.situationDesc"), icon: Users, color: "#FBBF24" },
    { id: "voice" as SimMode, name: t("sim.voice"), description: t("sim.voiceDesc"), icon: Mic, color: "#FB923C" },
  ];

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
          <motion.img
            src="/images/mascot-happy.png"
            alt="Simulator mascot"
            className="w-28 h-28 lg:w-40 lg:h-40 object-contain mx-auto mb-4 drop-shadow-2xl"
            animate={{ y: [0, -8, 0] }}
            transition={{ repeat: Infinity, duration: 2.5, ease: "easeInOut" }}
          />
          <h1 className="text-2xl font-bold mb-2">{t("sim.title")}</h1>
          <p className="text-text-secondary text-sm">{t("sim.chooseMode")}</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
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
