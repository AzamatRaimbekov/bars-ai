import { motion } from "framer-motion";

interface WaveformVisualizerProps {
  active: boolean;
  color?: string;
}

export function WaveformVisualizer({ active, color = "#00D9FF" }: WaveformVisualizerProps) {
  if (!active) return null;

  return (
    <div className="flex items-center gap-1 h-8">
      {Array.from({ length: 5 }).map((_, i) => (
        <motion.div
          key={i}
          className="w-1 rounded-full"
          style={{ backgroundColor: color }}
          animate={{
            height: active ? [8, 24, 8] : 8,
          }}
          transition={{
            repeat: Infinity,
            duration: 0.8,
            delay: i * 0.15,
            ease: "easeInOut",
          }}
        />
      ))}
    </div>
  );
}
