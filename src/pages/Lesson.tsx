import { useParams, useNavigate } from "react-router-dom";
import { ArrowLeft } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Button } from "@/components/ui/Button";
import { LessonPlayer } from "@/components/lesson/LessonPlayer";
import { LESSONS_V2 } from "@/data/lessons";
import { useTranslation } from "@/hooks/useTranslation";

export default function Lesson() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { t } = useTranslation();

  const lesson = id ? LESSONS_V2[id] : undefined;

  if (!lesson) {
    return (
      <PageWrapper>
        <div className="text-center py-20">
          <p className="text-text-secondary">{t("lesson.comingSoon")}</p>
          <Button variant="ghost" className="mt-4" onClick={() => navigate(-1)}>
            <ArrowLeft size={14} /> {t("lesson.goBack")}
          </Button>
        </div>
      </PageWrapper>
    );
  }

  const nodeId = id ? id.split("-").slice(0, 2).join("-") : "";
  const allLessonIds = Object.keys(LESSONS_V2).filter((k) => k.startsWith(nodeId + "-"));

  return (
    <LessonPlayer
      lesson={lesson}
      nodeId={nodeId}
      allLessonIdsForNode={allLessonIds}
      onClose={() => navigate("/roadmap")}
    />
  );
}
