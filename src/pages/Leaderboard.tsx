import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { PageWrapper } from "@/components/layout/PageWrapper";
import { Card } from "@/components/ui/Card";
import { useTranslation } from "@/hooks/useTranslation";
import { useAuthStore } from "@/store/authStore";
import { apiFetch } from "@/services/api";
import { Crown, Medal, Trophy, Loader2 } from "lucide-react";

type Period = "weekly" | "monthly" | "alltime";

interface LeaderboardEntry {
  rank: number;
  user_id: string;
  name: string;
  avatar_url: string | null;
  xp: number;
  level: string;
  direction: string;
}

interface LeaderboardResponse {
  period: string;
  entries: LeaderboardEntry[];
}

interface MyRankEntry {
  period: string;
  rank: number | null;
  total_users: number;
}

interface MyRankResponse {
  weekly: MyRankEntry;
  monthly: MyRankEntry;
  all_time: MyRankEntry;
}

const TABS: { key: Period; labelKey: "leaderboard.weekly" | "leaderboard.monthly" | "leaderboard.allTime" }[] = [
  { key: "weekly", labelKey: "leaderboard.weekly" },
  { key: "monthly", labelKey: "leaderboard.monthly" },
  { key: "alltime", labelKey: "leaderboard.allTime" },
];

const PERIOD_ENDPOINTS: Record<Period, string> = {
  weekly: "/leaderboard/weekly",
  monthly: "/leaderboard/monthly",
  alltime: "/leaderboard/all-time",
};

// Podium: gold, silver, bronze — kept as semantic medal colors, not overriding with orange
const PODIUM_COLORS = [
  { bg: "from-yellow-500/20 to-yellow-600/5", border: "border-yellow-500/20", text: "text-yellow-400", shadow: "0 0 24px rgba(234,179,8,0.10)" },
  { bg: "from-white/10 to-white/5", border: "border-white/10", text: "text-white/60", shadow: "0 0 24px rgba(255,255,255,0.05)" },
  { bg: "from-amber-700/15 to-amber-800/5", border: "border-amber-700/20", text: "text-amber-600", shadow: "0 0 24px rgba(180,83,9,0.08)" },
];

const PODIUM_ICONS = [Crown, Trophy, Medal];

const containerVariants = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.04 } },
};

const itemVariants = {
  hidden: { opacity: 0, y: 12 },
  show: { opacity: 1, y: 0 },
};

function getInitials(name: string): string {
  return name
    .split(" ")
    .map((w) => w[0])
    .join("")
    .toUpperCase()
    .slice(0, 2);
}

function getLevelColor(level: string): string {
  switch (level) {
    case "Legend": return "bg-yellow-500/10 text-yellow-400 border-yellow-500/20";
    case "Master": return "bg-red-500/10 text-red-400 border-red-500/20";
    case "Expert": return "bg-[#FFB800]/10 text-[#FFB800] border-[#FFB800]/20";
    case "Practitioner": return "bg-[#FB923C]/10 text-[#FB923C] border-[#FB923C]/20";
    case "Apprentice": return "bg-[#F97316]/10 text-[#F97316] border-[#F97316]/20";
    default: return "bg-white/5 text-white/40 border-white/10";
  }
}

export default function Leaderboard() {
  const { t } = useTranslation();
  const currentUserId = useAuthStore((s) => s.user?.id);
  const [activePeriod, setActivePeriod] = useState<Period>("weekly");
  const [entries, setEntries] = useState<LeaderboardEntry[]>([]);
  const [myRank, setMyRank] = useState<MyRankResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    async function fetchData() {
      try {
        const [lb, rank] = await Promise.all([
          apiFetch<LeaderboardResponse>(PERIOD_ENDPOINTS[activePeriod]),
          apiFetch<MyRankResponse>("/leaderboard/my-rank"),
        ]);
        if (!cancelled) {
          setEntries(lb.entries);
          setMyRank(rank);
        }
      } catch {
        // silently fail
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    fetchData();
    return () => { cancelled = true; };
  }, [activePeriod]);

  const top3 = entries.slice(0, 3);
  const rest = entries.slice(3);

  const currentRank = myRank
    ? activePeriod === "weekly"
      ? myRank.weekly.rank
      : activePeriod === "monthly"
        ? myRank.monthly.rank
        : myRank.all_time.rank
    : null;

  return (
    <PageWrapper>
      <div className="max-w-3xl mx-auto space-y-6">

        {/* ── Header ── */}
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-1 text-white">{t("leaderboard.title")}</h1>
          {currentRank && (
            <p className="text-white/40 text-sm">
              {t("leaderboard.rank")}:{' '}
              <span className="text-[#F97316] font-semibold">#{currentRank}</span>
            </p>
          )}
        </div>

        {/* ── Tab Switcher ── */}
        <div className="flex justify-center">
          <div className="inline-flex rounded-xl bg-[#0A0A0A] border border-white/6 p-1 gap-1">
            {TABS.map((tab) => (
              <button
                key={tab.key}
                onClick={() => setActivePeriod(tab.key)}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                  activePeriod === tab.key
                    ? "bg-[#F97316]/15 text-[#F97316]"
                    : "text-white/40 hover:text-white/70"
                }`}
              >
                {t(tab.labelKey)}
              </button>
            ))}
          </div>
        </div>

        {loading ? (
          <div className="flex justify-center py-20">
            <Loader2 className="animate-spin text-[#F97316]" size={32} />
          </div>
        ) : entries.length === 0 ? (
          <div className="bg-[#0A0A0A] border border-white/6 rounded-2xl p-16 text-center">
            <p className="text-white/40">{t("leaderboard.empty")}</p>
          </div>
        ) : (
          <>
            {/* ── Podium — Top 3 ── */}
            {top3.length > 0 && (
              <div className="flex items-end justify-center gap-3 pt-4 pb-2">
                {/* Reorder: 2nd, 1st, 3rd */}
                {[1, 0, 2].map((podiumIndex) => {
                  const entry = top3[podiumIndex];
                  if (!entry) return <div key={podiumIndex} className="w-28" />;
                  const colors = PODIUM_COLORS[podiumIndex];
                  const PodiumIcon = PODIUM_ICONS[podiumIndex];
                  const isFirst = podiumIndex === 0;
                  const isMe = entry.user_id === currentUserId;

                  return (
                    <motion.div
                      key={entry.user_id}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: podiumIndex * 0.1 }}
                      className="flex flex-col items-center"
                    >
                      <div
                        className={[
                          "w-28 rounded-2xl border bg-[#0A0A0A] flex flex-col items-center gap-2 p-3",
                          isFirst ? "pb-8 pt-5" : "pb-6 pt-4",
                          colors.border,
                          isMe ? "ring-2 ring-[#F97316]/30" : "",
                        ].join(" ")}
                        style={{ boxShadow: colors.shadow }}
                      >
                        <PodiumIcon size={isFirst ? 22 : 18} className={colors.text} />

                        {entry.avatar_url ? (
                          <img
                            src={entry.avatar_url}
                            alt={entry.name}
                            className={`rounded-full object-cover border-2 ${colors.border} ${isFirst ? "w-16 h-16" : "w-12 h-12"}`}
                          />
                        ) : (
                          <div
                            className={`rounded-full flex items-center justify-center font-bold bg-gradient-to-br ${colors.bg} border ${colors.border} ${isFirst ? "w-16 h-16 text-lg" : "w-12 h-12 text-sm"}`}
                          >
                            {getInitials(entry.name)}
                          </div>
                        )}

                        <div className="text-center w-full">
                          <p className={`font-semibold truncate px-1 text-white ${isFirst ? "text-sm" : "text-xs"}`}>
                            {entry.name}
                          </p>
                          {isMe && (
                            <p className="text-[10px] text-[#F97316] font-medium">{t("leaderboard.you")}</p>
                          )}
                        </div>

                        {/* Rank number with orange accent for #1 */}
                        <p className={`font-bold ${isFirst ? "text-[#F97316] text-lg" : `${colors.text} text-base`}`}>
                          {entry.xp.toLocaleString()} XP
                        </p>

                        <span className={`text-[10px] px-2 py-0.5 rounded-full border ${getLevelColor(entry.level)}`}>
                          {t(`level.${entry.level}` as any)}
                        </span>
                      </div>
                    </motion.div>
                  );
                })}
              </div>
            )}

            {/* ── Rows (4–50) ── */}
            {rest.length > 0 && (
              <motion.div
                variants={containerVariants}
                initial="hidden"
                animate="show"
                className="space-y-1.5"
              >
                {rest.map((entry, idx) => {
                  const isMe = entry.user_id === currentUserId;
                  const isEven = idx % 2 === 0;

                  return (
                    <motion.div key={entry.user_id} variants={itemVariants}>
                      <div
                        className={[
                          "flex items-center gap-3 rounded-xl px-3 py-2.5 transition-colors",
                          isMe
                            ? "border-l-2 border-[#F97316] bg-[#F97316]/5 pl-2.5"
                            : isEven
                              ? "bg-[#0A0A0A]"
                              : "bg-transparent hover:bg-white/[0.02]",
                        ].join(" ")}
                      >
                        {/* Rank number */}
                        <div className="w-8 text-center shrink-0">
                          <span className={`text-sm font-bold ${isMe ? "text-[#F97316]" : "text-white/30"}`}>
                            {entry.rank}
                          </span>
                        </div>

                        {/* Avatar */}
                        {entry.avatar_url ? (
                          <img
                            src={entry.avatar_url}
                            alt={entry.name}
                            className="w-9 h-9 rounded-full object-cover border border-white/8 shrink-0"
                          />
                        ) : (
                          <div className="w-9 h-9 rounded-full flex items-center justify-center font-bold text-sm bg-white/5 border border-white/8 text-white/60 shrink-0">
                            {getInitials(entry.name)}
                          </div>
                        )}

                        {/* Name & Level */}
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-2">
                            <p className="text-sm font-medium truncate text-white">{entry.name}</p>
                            {isMe && (
                              <span className="text-[10px] bg-[#F97316]/15 text-[#F97316] px-1.5 py-0.5 rounded-full font-medium shrink-0">
                                {t("leaderboard.you")}
                              </span>
                            )}
                          </div>
                          <span className={`text-[10px] px-1.5 py-0.5 rounded-full border ${getLevelColor(entry.level)}`}>
                            {t(`level.${entry.level}` as any)}
                          </span>
                        </div>

                        {/* XP */}
                        <div className="text-right shrink-0">
                          <p className="text-sm font-bold text-[#F97316]">
                            {entry.xp.toLocaleString()}
                          </p>
                          <p className="text-[10px] text-white/30">XP</p>
                        </div>
                      </div>
                    </motion.div>
                  );
                })}
              </motion.div>
            )}
          </>
        )}
      </div>
    </PageWrapper>
  );
}
