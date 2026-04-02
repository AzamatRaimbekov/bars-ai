import { useMemo } from "react";
import { useUserStore } from "@/store/userStore";
import { frontendRoadmap } from "@/data/roadmaps/frontend";
import { englishRoadmap } from "@/data/roadmaps/english";
import { callcenterRoadmap } from "@/data/roadmaps/callcenter";
import { cibRoadmap } from "@/data/roadmaps/cib";
import type { Direction, RoadmapNodeData, NodeStatus } from "@/types";

const roadmaps: Record<Direction, RoadmapNodeData[]> = {
  frontend: frontendRoadmap,
  english: englishRoadmap,
  callcenter: callcenterRoadmap,
  cib: cibRoadmap,
};

export function useRoadmap() {
  const profile = useUserStore((s) => s.profile);
  const direction = profile?.direction ?? "frontend";
  const completedNodes = profile?.completedNodes ?? [];

  const roadmap = roadmaps[direction];

  const getNodeStatus = (nodeId: string): NodeStatus => {
    if (completedNodes.includes(nodeId)) return "completed";
    const idx = roadmap.findIndex((n) => n.id === nodeId);
    if (idx === 0) return "available";
    return completedNodes.includes(roadmap[idx - 1].id) ? "available" : "locked";
  };

  const currentNode = useMemo(() => {
    return roadmap.find((n) => getNodeStatus(n.id) === "available") ?? null;
  }, [roadmap, completedNodes]);

  const progress = useMemo(() => {
    return Math.round((completedNodes.length / roadmap.length) * 100);
  }, [completedNodes.length, roadmap.length]);

  return { roadmap, getNodeStatus, currentNode, progress };
}
