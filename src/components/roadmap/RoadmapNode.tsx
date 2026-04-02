import { memo } from "react";
import { Handle, Position, type NodeProps } from "@xyflow/react";
import { motion } from "framer-motion";
import { Check, Lock } from "lucide-react";
import type { NodeStatus } from "@/types";

export interface RoadmapNodeProps {
  title: string;
  status: NodeStatus;
  color: string;
  section: string;
}

export const RoadmapNodeComponent = memo(({ data }: NodeProps) => {
  const { title, status, color, section } = data as unknown as RoadmapNodeProps;

  return (
    <motion.div
      whileHover={status !== "locked" ? { scale: 1.05 } : undefined}
      className="relative"
    >
      <Handle type="target" position={Position.Top} className="!bg-transparent !border-0 !w-0 !h-0" />

      <div
        className={`w-44 px-4 py-3 rounded-2xl border-2 text-center transition-all ${
          status === "completed"
            ? "bg-surface border-success/50"
            : status === "available"
            ? "bg-surface border-primary/50 shadow-lg cursor-pointer"
            : "bg-bg/50 border-border/30 opacity-40 blur-[0.5px]"
        }`}
        style={
          status === "available"
            ? { boxShadow: `0 0 20px ${color}25` }
            : undefined
        }
      >
        <div className="flex items-center justify-center gap-2 mb-1">
          {status === "completed" && (
            <div className="w-5 h-5 rounded-full bg-success/20 flex items-center justify-center">
              <Check size={12} className="text-success" />
            </div>
          )}
          {status === "locked" && <Lock size={12} className="text-text-secondary/50" />}
        </div>
        <p className={`text-xs font-semibold ${status === "locked" ? "text-text-secondary/50" : "text-text"}`}>
          {title}
        </p>
        <p className="text-[10px] text-text-secondary/60 mt-0.5">{section}</p>
      </div>

      <Handle type="source" position={Position.Bottom} className="!bg-transparent !border-0 !w-0 !h-0" />
    </motion.div>
  );
});

RoadmapNodeComponent.displayName = "RoadmapNodeComponent";
