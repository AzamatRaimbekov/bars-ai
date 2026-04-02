import { create } from "zustand";
import type { RoadmapNodeData, NodeStatus } from "@/types";

interface RoadmapState {
  nodes: RoadmapNodeData[];
  selectedNodeId: string | null;
  setNodes: (nodes: RoadmapNodeData[]) => void;
  selectNode: (id: string | null) => void;
  getNodeStatus: (nodeId: string, completedNodes: string[]) => NodeStatus;
}

export const useRoadmapStore = create<RoadmapState>()((set, get) => ({
  nodes: [],
  selectedNodeId: null,

  setNodes: (nodes) => set({ nodes }),
  selectNode: (id) => set({ selectedNodeId: id }),

  getNodeStatus: (nodeId, completedNodes) => {
    if (completedNodes.includes(nodeId)) return "completed";
    const { nodes } = get();
    const nodeIndex = nodes.findIndex((n) => n.id === nodeId);
    if (nodeIndex <= 0) return "available";
    const prevNode = nodes[nodeIndex - 1];
    return completedNodes.includes(prevNode.id) ? "available" : "locked";
  },
}));
