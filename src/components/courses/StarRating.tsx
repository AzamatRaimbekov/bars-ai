import { Star } from "lucide-react";

interface StarRatingProps {
  rating: number;
  max?: number;
  size?: number;
  clickable?: boolean;
  onChange?: (rating: number) => void;
}

export function StarRating({
  rating,
  max = 5,
  size = 14,
  clickable = false,
  onChange,
}: StarRatingProps) {
  return (
    <div className="flex items-center gap-0.5">
      {Array.from({ length: max }, (_, i) => {
        const filled = i < Math.round(rating);
        return (
          <button
            key={i}
            type="button"
            disabled={!clickable}
            onClick={() => clickable && onChange?.(i + 1)}
            className={`transition-transform ${
              clickable ? "cursor-pointer hover:scale-110" : "cursor-default"
            }`}
          >
            <Star
              size={size}
              className={
                filled
                  ? "fill-[#FFB800] text-[#FFB800]"
                  : "fill-transparent text-white/20"
              }
            />
          </button>
        );
      })}
    </div>
  );
}
