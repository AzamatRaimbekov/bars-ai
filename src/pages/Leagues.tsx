import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { useTranslation } from "@/hooks/useTranslation";
import { apiFetch } from "@/services/api";
import { Loader2, TrendingUp, TrendingDown } from "lucide-react";

interface LeagueInfo {
  league: string;
  xp_this_week: number;
  next_league: string | null;
  xp_to_next: number;
  rank_in_league: number;
}

interface LeagueMember {
  user_id: string;
  name: string;
  avatar_url: string | null;
  xp_this_week: number;
  rank: number;
}

const LEAGUE_CONFIG: Record<string, { emoji: string; color: string; label: string }> = {
  bronze: { emoji: "\uD83E\uDD49", color: "#CD7F32", label: "leagues.bronze" },
  silver: { emoji: "\uD83E\uDD48", color: "#C0C0C0", label: "leagues.silver" },
  gold: { emoji: "\uD83E\uDD47", color: "#FFD700", label: "leagues.gold" },
  platinum: { emoji: "\uD83D\uDCA0", color: "#E5E4E2", label: "leagues.platinum" },
  diamond: { emoji: "\uD83D\uDCA0", color: "#B9F2FF", label: "leagues.diamond" },
};

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.04 } },
};
const itemVariants = {
  hidden: { opacity: 0, y: 12 },
  show: { opacity: 1, y: 0 },
};

export default function Leagues() {
  const { t } = useTranslation();
  const [info, setInfo] = useState<LeagueInfo | null>(null);
  const [members, setMembers] = useState<LeagueMember[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const [leagueInfo, leagueMembers] = await Promise.all([
          apiFetch<LeagueInfo>("/leagues/me"),
          apiFetch<LeagueMember[]>("/leagues/members"),
        ]);
        setInfo(leagueInfo);
        setMembers(leagueMembers);
      } catch {
        // Fallback mock data for development
        setInfo({
          league: "bronze",
          xp_this_week: 120,
          next_league: "silver",
          xp_to_next: 380,
          rank_in_league: 5,
        });
        setMembers(
          Array.from({ length: 15 }, (_, i) => ({
            user_id: `user-${i}`,
            name: `Player ${i + 1}`,
            avatar_url: null,
            xp_this_week: Math.max(500 - i * 35, 10),
            rank: i + 1,
          }))
        );
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  if (loading) {
    return (
      <PageWrapper>
        <div className="flex items-center justify-center min-h-[60vh]">
          <Loader2 className="animate-spin text-primary" size={32} />
        </div>
      </PageWrapper>
    );
  }

  if (!info) return null;

  const config = LEAGUE_CONFIG[info.league] || LEAGUE_CONFIG.bronze;
  const xpForNextLeague = info.xp_this_week + info.xp_to_next;
  const totalMembers = members.length;

  return (
    <PageWrapper>
      <div className="max-w-2xl mx-auto space-y-6">
        {/* League Shield */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ type: "spring", stiffness: 300, damping: 20 }}
          className="text-center"
        >
          <div
            className="inline-flex items-center justify-center w-28 h-28 rounded-full mb-4"
            style={{
              background: `radial-gradient(circle, ${config.color}30 0%, transparent 70%)`,
              boxShadow: `0 0 40px ${config.color}20`,
            }}
          >
            <span className="text-6xl">{config.emoji}</span>
          </div>

          <h1
            className="text-2xl font-bold mb-1"
            style={{ color: config.color }}
          >
            {t(config.label as any)}
          </h1>
          <p className="text-sm text-text-secondary">{t("leagues.title")}</p>
        </motion.div>

        {/* Stats Cards */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="grid grid-cols-2 gap-3"
        >
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t("leagues.xpThisWeek")}</p>
            <p className="text-2xl font-bold text-primary">{info.xp_this_week}</p>
          </Card>
          <Card>
            <p className="text-xs text-text-secondary mb-1">{t("leagues.rank")}</p>
            <p className="text-2xl font-bold" style={{ color: config.color }}>
              #{info.rank_in_league}
            </p>
          </Card>
        </motion.div>

        {/* Progress to Next League */}
        {info.next_league && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <Card>
              <div className="flex justify-between items-center mb-2">
                <p className="text-xs text-text-secondary">{t("leagues.nextLeague")}</p>
                <p className="text-xs font-medium" style={{ color: LEAGUE_CONFIG[info.next_league]?.color || "#fff" }}>
                  {t((LEAGUE_CONFIG[info.next_league]?.label || "leagues.silver") as any)}
                </p>
              </div>
              <ProgressBar
                value={info.xp_this_week}
                max={xpForNextLeague}
                color={config.color}
                showLabel
              />
              <p className="text-xs text-text-secondary mt-2 text-center">
                {t("leagues.xpToNext")}: {info.xp_to_next} XP
              </p>
            </Card>
          </motion.div>
        )}

        {/* Members List */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
        >
          <h2 className="text-lg font-semibold mb-3">{t("leagues.members")}</h2>
          <motion.div
            variants={containerVariants}
            initial="hidden"
            animate="show"
            className="space-y-2"
          >
            {members.map((member) => {
              const isPromoted = member.rank <= 10;
              const isRelegated = totalMembers > 5 && member.rank > totalMembers - 5;

              return (
                <motion.div key={member.user_id} variants={itemVariants}>
                  <Card>
                    <div className="flex items-center gap-3">
                      {/* Rank */}
                      <div
                        className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold shrink-0"
                        style={{
                          backgroundColor:
                            member.rank === 1
                              ? "#FFD70030"
                              : member.rank === 2
                              ? "#C0C0C030"
                              : member.rank === 3
                              ? "#CD7F3230"
                              : "rgba(255,255,255,0.05)",
                          color:
                            member.rank === 1
                              ? "#FFD700"
                              : member.rank === 2
                              ? "#C0C0C0"
                              : member.rank === 3
                              ? "#CD7F32"
                              : "inherit",
                        }}
                      >
                        {member.rank}
                      </div>

                      {/* Avatar */}
                      <div
                        className="w-9 h-9 rounded-full flex items-center justify-center text-sm font-semibold shrink-0"
                        style={{
                          backgroundColor: `${config.color}20`,
                          color: config.color,
                        }}
                      >
                        {member.avatar_url ? (
                          <img
                            src={member.avatar_url}
                            alt={member.name}
                            className="w-full h-full rounded-full object-cover"
                          />
                        ) : (
                          member.name.charAt(0).toUpperCase()
                        )}
                      </div>

                      {/* Name & XP */}
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-medium truncate">{member.name}</p>
                        <p className="text-xs text-text-secondary">{member.xp_this_week} XP</p>
                      </div>

                      {/* Promoted / Relegated badge */}
                      {isPromoted && (
                        <div className="flex items-center gap-1 text-xs font-medium text-green-400">
                          <TrendingUp size={14} />
                          <span className="hidden sm:inline">{t("leagues.promoted")}</span>
                        </div>
                      )}
                      {isRelegated && (
                        <div className="flex items-center gap-1 text-xs font-medium text-red-400">
                          <TrendingDown size={14} />
                          <span className="hidden sm:inline">{t("leagues.relegated")}</span>
                        </div>
                      )}
                    </div>
                  </Card>
                </motion.div>
              );
            })}
          </motion.div>
        </motion.div>
      </div>
    </PageWrapper>
  );
}
