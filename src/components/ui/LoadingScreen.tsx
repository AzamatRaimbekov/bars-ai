import { motion } from "framer-motion";

const TIPS = [
  "Barsbek готовит для вас что-то интересное...",
  "Знание — сила! Загружаем ваш прогресс...",
  "Каждый урок приближает вас к цели!",
  "Barsbek верит в вас! Подождите секунду...",
  "Лучшая инвестиция — в себя. Загружаемся...",
  "Маленькие шаги ведут к большим победам!",
  "Учиться никогда не поздно!",
];

function getRandomTip() {
  return TIPS[Math.floor(Math.random() * TIPS.length)];
}

interface Props {
  tip?: string;
}

export function LoadingScreen({ tip }: Props) {
  const displayTip = tip || getRandomTip();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-[#0A0A0F] relative overflow-hidden">
      {/* Background glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse at 50% 40%, rgba(249,115,22,0.08) 0%, transparent 60%)",
        }}
      />

      {/* Mascot with bounce animation */}
      <motion.div
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
        className="relative"
      >
        <motion.img
          src="/images/mascot-thinking.png"
          alt="Barsbek"
          className="w-32 h-32 object-contain drop-shadow-2xl"
          animate={{ y: [0, -12, 0] }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        />

        {/* Pulse ring behind mascot */}
        <motion.div
          className="absolute inset-0 rounded-full"
          style={{
            background:
              "radial-gradient(circle, rgba(249,115,22,0.15) 0%, transparent 70%)",
          }}
          animate={{ scale: [1, 1.4, 1], opacity: [0.5, 0, 0.5] }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        />
      </motion.div>

      {/* Brand */}
      <motion.h1
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 0.5 }}
        className="mt-6 text-xl font-bold text-white"
      >
        Bars AI
      </motion.h1>

      {/* Loading dots */}
      <div className="flex gap-1.5 mt-4">
        {[0, 1, 2].map((i) => (
          <motion.div
            key={i}
            className="w-2 h-2 rounded-full bg-[#F97316]"
            animate={{ scale: [1, 1.4, 1], opacity: [0.4, 1, 0.4] }}
            transition={{
              duration: 1,
              repeat: Infinity,
              delay: i * 0.2,
              ease: "easeInOut",
            }}
          />
        ))}
      </div>

      {/* Tip */}
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6, duration: 0.5 }}
        className="mt-6 text-sm text-white/40 text-center max-w-xs px-4"
      >
        {displayTip}
      </motion.p>
    </div>
  );
}
