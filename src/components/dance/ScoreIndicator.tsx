interface ScoreIndicatorProps {
  score: number // 0-100
  size?: number
  label?: string
}

export function ScoreIndicator({ score, size = 80, label }: ScoreIndicatorProps) {
  const radius = (size - 8) / 2
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (score / 100) * circumference
  const color = score >= 70 ? "#10B981" : score >= 40 ? "#F59E0B" : "#EF4444"

  return (
    <div className="flex flex-col items-center gap-1">
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size/2} cy={size/2} r={radius} fill="none" stroke="rgba(255,255,255,0.1)" strokeWidth={4} />
        <circle cx={size/2} cy={size/2} r={radius} fill="none" stroke={color} strokeWidth={4}
          strokeDasharray={circumference} strokeDashoffset={offset} strokeLinecap="round"
          className="transition-all duration-500" />
      </svg>
      <div className="absolute flex items-center justify-center" style={{width: size, height: size}}>
        <span className="text-lg font-bold" style={{color}}>{score}%</span>
      </div>
      {label && <span className="text-xs text-white/50">{label}</span>}
    </div>
  )
}
