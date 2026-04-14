import { motion } from "framer-motion";

interface WaveformVisualizerProps {
  active: boolean;
  color?: string;
  size?: "sm" | "md" | "lg";
}

const sizeConfig = {
  sm: { bars: 5, width: "w-1", gap: "gap-1", height: "h-8", min: 6, max: 20 },
  md: { bars: 7, width: "w-1.5", gap: "gap-1", height: "h-10", min: 8, max: 28 },
  lg: { bars: 12, width: "w-1.5", gap: "gap-[3px]", height: "h-14", min: 6, max: 40 },
};

export function WaveformVisualizer({ active, color = "#F97316", size = "sm" }: WaveformVisualizerProps) {
  if (!active) return null;

  const cfg = sizeConfig[size];

  return (
    <div className={`flex items-center ${cfg.gap} ${cfg.height}`}>
      {Array.from({ length: cfg.bars }).map((_, i) => (
        <motion.div
          key={i}
          className={`${cfg.width} rounded-full`}
          style={{ backgroundColor: color }}
          animate={{
            height: [
              cfg.min,
              cfg.min + Math.random() * (cfg.max - cfg.min),
              cfg.min + Math.random() * (cfg.max - cfg.min) * 0.5,
              cfg.max - Math.random() * 8,
              cfg.min,
            ],
          }}
          transition={{
            repeat: Infinity,
            duration: 0.8 + Math.random() * 0.6,
            delay: i * 0.08,
            ease: "easeInOut",
          }}
        />
      ))}
    </div>
  );
}
