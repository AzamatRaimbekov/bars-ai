import { motion } from "framer-motion";
import { Trophy } from "lucide-react";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Badge as BadgeComponent } from "@/components/ui/Badge";
import { useUserStore } from "@/store/userStore";
import { BADGES } from "@/data/achievements";
import { useTranslation } from "@/hooks/useTranslation";

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
  const { t, lang } = useTranslation();
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

        {/* ── Header ── */}
        <div className="text-center">
          <div className="w-16 h-16 rounded-2xl bg-[#F97316]/10 flex items-center justify-center mx-auto mb-4">
            <Trophy size={28} className="text-[#F97316]" />
          </div>
          <h1 className="text-2xl font-bold mb-2 text-white">{t("achievements.title")}</h1>
          <p className="text-white/40 text-sm">
            <span className="text-[#F97316] font-semibold">{earnedCount}</span>
            {' '}{t("common.of")}{' '}
            {totalCount} {t("achievements.unlocked")}
          </p>
        </div>

        {/* ── Streak Heatmap ── */}
        <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-5">
          <p className="text-xs text-white/40 uppercase tracking-wider mb-4">{t("achievements.streak")}</p>
          <div className="flex gap-1 flex-wrap">
            {days.map((day, i) => (
              <div
                key={i}
                className="w-6 h-6 rounded-sm transition-colors"
                style={{
                  backgroundColor: day.active ? '#F9731630' : '#ffffff05',
                  border: day.active ? '1px solid #F9731650' : '1px solid transparent',
                }}
                title={day.date.toLocaleDateString()}
              />
            ))}
          </div>
        </div>

        {/* ── Badge Grid ── */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          animate="show"
          className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 gap-3 lg:gap-4"
        >
          {BADGES.filter((b) => !b.direction || b.direction === profile.direction).map((badge) => {
            const isEarned = profile.earnedBadges.includes(badge.id);
            const isLegendary = badge.rarity === 'Legendary';

            return (
              <motion.div key={badge.id} variants={itemVariants}>
                <div
                  className={[
                    "flex flex-col items-center gap-2 p-4 rounded-2xl border transition-all",
                    !isEarned
                      ? "opacity-40 grayscale bg-[#0A0A0A] border-white/6"
                      : isLegendary
                        ? "bg-[#0A0A0A] border-[#F97316]/30 shadow-[0_0_20px_rgba(249,115,22,0.08)]"
                        : "bg-[#0A0A0A] border-white/6 hover:border-white/12",
                  ].join(" ")}
                >
                  <span className="text-3xl">{badge.icon}</span>
                  <span className="text-xs font-medium text-center text-white leading-tight">
                    {badge.name[lang]}
                  </span>
                  <span
                    className={[
                      "text-[10px] uppercase tracking-wider font-semibold",
                      !isEarned
                        ? "text-white/30"
                        : badge.rarity === 'Legendary'
                          ? "text-[#F97316]"
                          : badge.rarity === 'Epic'
                            ? "text-[#FB923C]"
                            : badge.rarity === 'Rare'
                              ? "text-[#F97316]/80"
                              : "text-white/40",
                    ].join(" ")}
                  >
                    {badge.rarity}
                  </span>
                </div>
              </motion.div>
            );
          })}
        </motion.div>

      </div>
    </PageWrapper>
  );
}
