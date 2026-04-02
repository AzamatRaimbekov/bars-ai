import { motion } from "framer-motion";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { Badge as BadgeComponent } from "@/components/ui/Badge";
import { useUserStore } from "@/store/userStore";
import { BADGES } from "@/data/achievements";

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.05 } },
};
const itemVariants = {
  hidden: { opacity: 0, scale: 0.8 },
  show: { opacity: 1, scale: 1 },
};

export default function Achievements() {
  const profile = useUserStore((s) => s.profile);
  if (!profile) return null;

  const earnedCount = profile.earnedBadges.length;
  const totalCount = BADGES.filter((b) => !b.direction || b.direction === profile.direction).length;

  const today = new Date();
  const days = Array.from({ length: 30 }, (_, i) => {
    const d = new Date(today);
    d.setDate(d.getDate() - (29 - i));
    const isActive = profile.streak >= (30 - i);
    return { date: d, active: isActive };
  });

  return (
    <PageWrapper>
      <div className="max-w-4xl mx-auto space-y-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-2">Achievements</h1>
          <p className="text-text-secondary text-sm">
            {earnedCount} of {totalCount} badges unlocked
          </p>
        </div>

        <Card>
          <p className="text-xs text-text-secondary uppercase tracking-wider mb-3">Learning Streak</p>
          <div className="flex gap-1 flex-wrap">
            {days.map((day, i) => (
              <div
                key={i}
                className="w-6 h-6 rounded-sm"
                style={{
                  backgroundColor: day.active ? "#00FF9440" : "#1E1E2E",
                  border: day.active ? "1px solid #00FF9460" : "1px solid transparent",
                }}
                title={day.date.toLocaleDateString()}
              />
            ))}
          </div>
        </Card>

        <motion.div
          variants={containerVariants}
          initial="hidden"
          animate="show"
          className="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-6 gap-4"
        >
          {BADGES.filter((b) => !b.direction || b.direction === profile.direction).map((badge) => {
            const isEarned = profile.earnedBadges.includes(badge.id);
            return (
              <motion.div key={badge.id} variants={itemVariants}>
                <BadgeComponent
                  icon={badge.icon}
                  name={badge.name}
                  rarity={badge.rarity}
                  locked={!isEarned}
                />
              </motion.div>
            );
          })}
        </motion.div>
      </div>
    </PageWrapper>
  );
}
