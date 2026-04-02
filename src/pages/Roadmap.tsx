import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { RoadmapCanvas } from "@/components/roadmap/RoadmapCanvas";
import { NodePanel } from "@/components/roadmap/NodePanel";
import { useUserStore } from "@/store/userStore";
import { DIRECTIONS } from "@/data/directions";
import { frontendRoadmap } from "@/data/roadmaps/frontend";
import { englishRoadmap } from "@/data/roadmaps/english";
import { callcenterRoadmap } from "@/data/roadmaps/callcenter";
import { cibRoadmap } from "@/data/roadmaps/cib";
import type { Direction, RoadmapNodeData, NodeStatus } from "@/types";

const roadmapsByDirection: Record<Direction, RoadmapNodeData[]> = {
  frontend: frontendRoadmap,
  english: englishRoadmap,
  callcenter: callcenterRoadmap,
  cib: cibRoadmap,
};

export default function Roadmap() {
  const navigate = useNavigate();
  const profile = useUserStore((s) => s.profile);
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null);

  if (!profile) return null;

  const roadmap = roadmapsByDirection[profile.direction];
  const dirConfig = DIRECTIONS[profile.direction];
  const selectedNode = roadmap.find((n) => n.id === selectedNodeId) ?? null;

  const getStatus = (nodeId: string): NodeStatus => {
    if (profile.completedNodes.includes(nodeId)) return "completed";
    const idx = roadmap.findIndex((n) => n.id === nodeId);
    if (idx === 0) return "available";
    return profile.completedNodes.includes(roadmap[idx - 1].id) ? "available" : "locked";
  };

  return (
    <PageWrapper>
      <div className="relative">
        <RoadmapCanvas
          roadmapData={roadmap}
          completedNodes={profile.completedNodes}
          color={dirConfig.color}
          onNodeClick={setSelectedNodeId}
        />
        <NodePanel
          node={selectedNode}
          status={selectedNode ? getStatus(selectedNode.id) : "locked"}
          completedLessons={profile.completedLessons}
          onClose={() => setSelectedNodeId(null)}
          onStartLesson={(id) => navigate(`/lesson/${id}`)}
          onStartAI={() => navigate("/mentor")}
        />
      </div>
    </PageWrapper>
  );
}
