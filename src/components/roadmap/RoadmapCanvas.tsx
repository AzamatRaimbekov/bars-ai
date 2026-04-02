import { useMemo, useCallback } from "react";
import {
  ReactFlow,
  Background,
  MiniMap,
  Controls,
  type Node,
  type Edge,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { RoadmapNodeComponent } from "./RoadmapNode";
import type { RoadmapNodeData, NodeStatus } from "@/types";

const nodeTypes = { roadmapNode: RoadmapNodeComponent };

interface RoadmapCanvasProps {
  roadmapData: RoadmapNodeData[];
  completedNodes: string[];
  color: string;
  onNodeClick: (nodeId: string) => void;
}

export function RoadmapCanvas({ roadmapData, completedNodes, color, onNodeClick }: RoadmapCanvasProps) {
  const getStatus = useCallback(
    (nodeId: string, index: number): NodeStatus => {
      if (completedNodes.includes(nodeId)) return "completed";
      if (index === 0) return "available";
      const prevNode = roadmapData[index - 1];
      return completedNodes.includes(prevNode.id) ? "available" : "locked";
    },
    [completedNodes, roadmapData]
  );

  const { nodes, edges } = useMemo(() => {
    const ns: Node[] = roadmapData.map((node, i) => ({
      id: node.id,
      type: "roadmapNode",
      position: {
        x: 300 + Math.sin(i * 0.8) * 150,
        y: i * 120,
      },
      data: {
        title: node.title,
        status: getStatus(node.id, i),
        color,
        section: node.section,
      },
    }));

    const es: Edge[] = roadmapData.slice(1).map((node, i) => ({
      id: `e-${roadmapData[i].id}-${node.id}`,
      source: roadmapData[i].id,
      target: node.id,
      animated: getStatus(node.id, i + 1) === "available",
      style: {
        stroke: completedNodes.includes(node.id)
          ? "#00FF94"
          : getStatus(node.id, i + 1) === "available"
          ? color
          : "#1E1E2E",
        strokeWidth: 2,
      },
    }));

    return { nodes: ns, edges: es };
  }, [roadmapData, completedNodes, color, getStatus]);

  return (
    <div className="w-full h-[calc(100vh-8rem)] rounded-2xl overflow-hidden border border-border bg-bg">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        onNodeClick={(_, node) => {
          const status = getStatus(node.id, roadmapData.findIndex((n) => n.id === node.id));
          if (status !== "locked") onNodeClick(node.id);
        }}
        fitView
        fitViewOptions={{ padding: 0.3 }}
        minZoom={0.3}
        maxZoom={1.5}
        proOptions={{ hideAttribution: true }}
      >
        <Background color="#1E1E2E" gap={20} size={1} />
        <MiniMap
          nodeColor={(n) => {
            const d = n.data as any;
            return d.status === "completed" ? "#00FF94" : d.status === "available" ? color : "#1E1E2E";
          }}
          style={{ background: "#111118", borderRadius: 12 }}
        />
        <Controls
          style={{ borderRadius: 12, overflow: "hidden", border: "1px solid #1E1E2E" }}
        />
      </ReactFlow>
    </div>
  );
}
