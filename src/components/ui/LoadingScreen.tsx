import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

const TIPS = [
  "Barsbek готовит для вас что-то интересное...",
  "Знание — сила! Загружаем ваш прогресс...",
  "Каждый урок приближает вас к цели!",
  "Barsbek верит в вас! Подождите секунду...",
  "Лучшая инвестиция — в себя. Загружаемся...",
  "Маленькие шаги ведут к большим победам!",
  "Учиться никогда не поздно!",
  "Сегодня вы станете чуть лучше, чем вчера!",
  "Barsbek уже готовит ваш следующий урок...",
  "Великие дела начинаются с маленького шага!",
];

function getRandomTip() {
  return TIPS[Math.floor(Math.random() * TIPS.length)];
}

interface Props {
  tip?: string;
  minDelay?: number; // minimum display time in ms
}

export function LoadingScreen({ tip, minDelay = 1500 }: Props) {
  const [displayTip] = useState(() => tip || getRandomTip());
  const [visible, setVisible] = useState(true);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setReady(true), minDelay);
    return () => clearTimeout(timer);
  }, [minDelay]);

  // If parent unmounts us, that's fine. But if we control visibility:
  useEffect(() => {
    if (ready) {
      // Small fade-out delay
      const t = setTimeout(() => setVisible(false), 100);
      return () => clearTimeout(t);
    }
  }, [ready]);

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.4 }}
          className="min-h-screen flex flex-col items-center justify-center bg-[#0A0A0F] relative overflow-hidden"
        >
          {/* Background glow */}
          <div
            className="absolute inset-0 pointer-events-none"
            style={{
              background:
                "radial-gradient(ellipse at 50% 40%, rgba(249,115,22,0.08) 0%, transparent 60%)",
            }}
          />

          {/* Floating particles */}
          {[...Array(6)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 rounded-full bg-[#F97316]/30"
              style={{
                left: `${15 + i * 14}%`,
                top: `${20 + (i % 3) * 25}%`,
              }}
              animate={{
                y: [0, -30, 0],
                opacity: [0.2, 0.6, 0.2],
              }}
              transition={{
                duration: 3 + i * 0.5,
                repeat: Infinity,
                delay: i * 0.4,
                ease: "easeInOut",
              }}
            />
          ))}

          {/* Mascot with bounce animation */}
          <motion.div
            initial={{ scale: 0.5, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.6, ease: "backOut" }}
            className="relative"
          >
            <motion.img
              src="/images/mascot-thinking.png"
              alt="Barsbek"
              className="w-36 h-36 object-contain drop-shadow-2xl"
              animate={{ y: [0, -14, 0] }}
              transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
            />

            {/* Pulse ring behind mascot */}
            <motion.div
              className="absolute -inset-4 rounded-full"
              style={{
                background:
                  "radial-gradient(circle, rgba(249,115,22,0.12) 0%, transparent 70%)",
              }}
              animate={{ scale: [1, 1.5, 1], opacity: [0.4, 0, 0.4] }}
              transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
            />
          </motion.div>

          {/* Brand */}
          <motion.h1
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.5 }}
            className="mt-6 text-2xl font-bold text-white tracking-tight"
          >
            Bars <span className="text-[#F97316]">AI</span>
          </motion.h1>

          {/* Loading bar */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="mt-5 w-48 h-1 rounded-full bg-white/5 overflow-hidden"
          >
            <motion.div
              className="h-full rounded-full bg-gradient-to-r from-[#F97316] to-[#FB923C]"
              initial={{ width: "0%" }}
              animate={{ width: "100%" }}
              transition={{ duration: minDelay / 1000, ease: "easeInOut" }}
            />
          </motion.div>

          {/* Tip */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.6, duration: 0.5 }}
            className="mt-5 text-sm text-white/40 text-center max-w-xs px-4"
          >
            {displayTip}
          </motion.p>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
