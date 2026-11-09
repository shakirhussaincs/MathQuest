import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { apiRequest } from '../api/client';
import { 
  Trophy, 
  Flame, 
  Award, 
  Sparkles, 
  Medal, 
  Crown, 
  Filter, 
  Calendar,
  CheckCircle2,
  TrendingUp,
  Zap,
  ArrowRight
} from 'lucide-react';

export default function LeaderboardPage({ onSelectStudent }) {
  const { user } = useAuth();
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  
  // Filters
  const [gradeFilter, setGradeFilter] = useState('all'); // 'all', '11', '12'
  const [timeframe, setTimeframe] = useState('all_time'); // 'all_time', 'weekly'

  // Streak state
  const [streakData, setStreakData] = useState(null);
  const [claiming, setClaiming] = useState(false);
  const [claimMsg, setClaimMsg] = useState('');

  const loadLeaderboard = async () => {
    setLoading(true);
    setError('');
    try {
      const gradeQuery = gradeFilter === 'all' ? '' : `&grade=${gradeFilter}`;
      const data = await apiRequest(`/gamification/leaderboard?timeframe=${timeframe}${gradeQuery}`);
      setLeaderboard(data);
    } catch (err) {
      setError(err.message || 'Failed to load leaderboard data.');
    } finally {
      setLoading(false);
    }
  };

  const loadStreak = async () => {
    try {
      const data = await apiRequest('/gamification/streak');
      setStreakData(data);
    } catch (err) {
      console.error('Streak error:', err);
    }
  };

  const handleClaimStreak = async () => {
    setClaiming(true);
    setClaimMsg('');
    try {
      const res = await apiRequest('/gamification/streak/claim', { method: 'POST' });
      setClaimMsg(res.message);
      await loadStreak();
      await loadLeaderboard();
    } catch (err) {
      alert(`Claim failed: ${err.message}`);
    } finally {
      setClaiming(false);
    }
  };

  useEffect(() => {
    loadLeaderboard();
    loadStreak();
  }, [gradeFilter, timeframe]);

  const topThree = leaderboard.slice(0, 3);
  const remaining = leaderboard.slice(3);

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 sm:px-6 space-y-8">
      
      {/* Header & Streak Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <div className="flex items-center space-x-2 text-xs font-bold text-amber-400 uppercase tracking-widest mb-1">
            <Trophy className="w-4 h-4" />
            <span>Sindh STREAM Friendly Competition</span>
          </div>
          <h1 className="font-quest text-3xl sm:text-4xl font-extrabold text-white">
            Realm Leaderboards
          </h1>
          <p className="text-slate-300 text-sm mt-1">
            Practice mathematics, conquer topic missions, and rise through the kingdom ranks
          </p>
        </div>

        {/* Daily Streak Widget */}
        {streakData && (
          <div className="glass-panel p-4 rounded-2xl border border-quest-border flex items-center space-x-4">
            <div className="w-12 h-12 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-2xl text-amber-400">
              🔥
            </div>
            <div>
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Daily Practice Streak</div>
              <div className="text-lg font-extrabold text-white">
                {streakData.current_streak} {streakData.current_streak === 1 ? 'Day' : 'Days'}
                <span className="text-xs font-normal text-slate-400 ml-1.5">(Record: {streakData.longest_streak}d)</span>
              </div>
              <button
                onClick={handleClaimStreak}
                disabled={claiming}
                className="mt-1 text-[11px] font-bold text-amber-400 hover:text-amber-300 flex items-center space-x-1"
              >
                <span>{claiming ? 'Logging...' : 'Log Today\'s Practice (+5 XP)'}</span>
                <ArrowRight className="w-3 h-3" />
              </button>
            </div>
          </div>
        )}
      </div>

      {claimMsg && (
        <div className="p-3.5 bg-emerald-500/15 border border-emerald-500/30 rounded-2xl text-emerald-300 text-xs flex items-center space-x-2">
          <CheckCircle2 className="w-4 h-4 flex-shrink-0" />
          <span>{claimMsg}</span>
        </div>
      )}

      {/* Filter Tabs */}
      <div className="glass-panel p-3 rounded-2xl border border-quest-border flex flex-col sm:flex-row items-center justify-between gap-3">
        {/* Grade filter */}
        <div className="flex items-center space-x-2 w-full sm:w-auto">
          <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider pl-2 hidden sm:inline">
            Grade:
          </span>
          <div className="grid grid-cols-3 gap-1 w-full sm:w-auto">
            <button
              onClick={() => setGradeFilter('all')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                gradeFilter === 'all'
                  ? 'bg-amber-500 text-slate-950 shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              All Grades
            </button>
            <button
              onClick={() => setGradeFilter('11')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                gradeFilter === '11'
                  ? 'bg-amber-500 text-slate-950 shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              Grade 11
            </button>
            <button
              onClick={() => setGradeFilter('12')}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                gradeFilter === '12'
                  ? 'bg-amber-500 text-slate-950 shadow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              Grade 12
            </button>
          </div>
        </div>

        {/* Timeframe filter */}
        <div className="flex items-center space-x-1 bg-slate-900/80 p-1 rounded-xl border border-quest-border w-full sm:w-auto">
          <button
            onClick={() => setTimeframe('all_time')}
            className={`flex-1 sm:flex-none px-3.5 py-1 rounded-lg text-xs font-bold transition-all ${
              timeframe === 'all_time'
                ? 'bg-slate-800 text-amber-300 shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            All-Time
          </button>
          <button
            onClick={() => setTimeframe('weekly')}
            className={`flex-1 sm:flex-none px-3.5 py-1 rounded-lg text-xs font-bold transition-all ${
              timeframe === 'weekly'
                ? 'bg-slate-800 text-amber-300 shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            Past 7 Days
          </button>
        </div>
      </div>

      {loading ? (
        <div className="p-16 text-center text-slate-400 font-quest">
          <div className="w-10 h-10 border-4 border-amber-500/20 border-t-amber-500 rounded-full animate-spin mx-auto mb-3" />
          <span>Summoning Champions...</span>
        </div>
      ) : error ? (
        <div className="p-8 text-center text-red-400 glass-panel rounded-2xl">{error}</div>
      ) : leaderboard.length === 0 ? (
        <div className="p-12 text-center text-slate-400 glass-panel rounded-2xl">
          No student activity found in this category yet.
        </div>
      ) : (
        <div className="space-y-8">
          
          {/* Top 3 Champions Podium */}
          {topThree.length > 0 && (
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4">
              
              {/* 2nd Place */}
              {topThree[1] && (
                <div className="order-2 sm:order-1 glass-panel p-6 rounded-3xl border border-slate-700 text-center flex flex-col justify-between relative sm:mt-6">
                  <div className="w-8 h-8 rounded-full bg-slate-700 text-slate-200 font-bold text-xs flex items-center justify-center absolute top-4 left-4 border border-slate-500">
                    2nd
                  </div>
                  <div className="w-16 h-16 rounded-full bg-gradient-to-tr from-slate-600 to-slate-400 text-white font-extrabold text-2xl flex items-center justify-center mx-auto shadow-lg">
                    🥈
                  </div>
                  <div className="mt-3">
                    <h3 className="font-bold text-white text-base truncate">{topThree[1].display_name}</h3>
                    <div className="text-xs text-slate-400">Level {topThree[1].level} • Grade {topThree[1].grade}</div>
                  </div>
                  <div className="mt-4 pt-3 border-t border-quest-border/80">
                    <span className="text-lg font-extrabold text-slate-200">{topThree[1].total_xp} XP</span>
                  </div>
                </div>
              )}

              {/* 1st Place (Crown) */}
              {topThree[0] && (
                <div className="order-1 sm:order-2 glass-panel-glow p-6 sm:p-8 rounded-3xl border border-amber-500/40 text-center flex flex-col justify-between relative shadow-xl shadow-amber-500/10 transform sm:-translate-y-2">
                  <div className="w-9 h-9 rounded-full bg-amber-500 text-slate-950 font-extrabold text-xs flex items-center justify-center absolute top-4 left-4 shadow-md">
                    1st
                  </div>
                  <div className="w-20 h-20 rounded-full bg-gradient-to-tr from-amber-500 to-amber-300 text-white font-extrabold text-3xl flex items-center justify-center mx-auto shadow-2xl shadow-amber-500/30">
                    👑
                  </div>
                  <div className="mt-3">
                    <h3 className="font-quest font-extrabold text-white text-lg truncate">{topThree[0].display_name}</h3>
                    <div className="text-xs text-amber-300 font-medium">Level {topThree[0].level} • Grade {topThree[0].grade}</div>
                    <div className="text-[11px] text-slate-400 mt-0.5">{topThree[0].rank_title}</div>
                  </div>
                  <div className="mt-4 pt-3 border-t border-quest-border/80">
                    <span className="text-2xl font-extrabold text-amber-400">{topThree[0].total_xp} XP</span>
                  </div>
                </div>
              )}

              {/* 3rd Place */}
              {topThree[2] && (
                <div className="order-3 glass-panel p-6 rounded-3xl border border-slate-700 text-center flex flex-col justify-between relative sm:mt-8">
                  <div className="w-8 h-8 rounded-full bg-amber-800 text-amber-200 font-bold text-xs flex items-center justify-center absolute top-4 left-4 border border-amber-600">
                    3rd
                  </div>
                  <div className="w-16 h-16 rounded-full bg-gradient-to-tr from-amber-800 to-amber-600 text-white font-extrabold text-2xl flex items-center justify-center mx-auto shadow-lg">
                    🥉
                  </div>
                  <div className="mt-3">
                    <h3 className="font-bold text-white text-base truncate">{topThree[2].display_name}</h3>
                    <div className="text-xs text-slate-400">Level {topThree[2].level} • Grade {topThree[2].grade}</div>
                  </div>
                  <div className="mt-4 pt-3 border-t border-quest-border/80">
                    <span className="text-lg font-extrabold text-slate-200">{topThree[2].total_xp} XP</span>
                  </div>
                </div>
              )}

            </div>
          )}

          {/* Full Ranked Table */}
          <div className="glass-panel rounded-2xl border border-quest-border overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs sm:text-sm">
                <thead className="bg-slate-900/80 border-b border-quest-border text-slate-400 uppercase text-[11px] font-semibold">
                  <tr>
                    <th className="py-3 px-4 w-16 text-center">Rank</th>
                    <th className="py-3 px-4">Student</th>
                    <th className="py-3 px-4">Level & Tier</th>
                    <th className="py-3 px-4">Grade</th>
                    <th className="py-3 px-4 text-center">Streak</th>
                    <th className="py-3 px-4 text-center">Badges</th>
                    <th className="py-3 px-4 text-right">Total XP</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-quest-border/60">
                  {leaderboard.map((entry) => {
                    const isCurrentUser = user && user.id === entry.user_id;

                    return (
                      <tr 
                        key={entry.user_id} 
                        className={`transition-colors ${
                          isCurrentUser 
                            ? 'bg-amber-500/15 font-semibold text-white' 
                            : 'hover:bg-slate-800/40 text-slate-200'
                        }`}
                      >
                        <td className="py-3.5 px-4 text-center">
                          <span className={`inline-flex items-center justify-center w-7 h-7 rounded-full text-xs font-extrabold ${
                            entry.rank === 1 ? 'bg-amber-500 text-slate-950' :
                            entry.rank === 2 ? 'bg-slate-400 text-slate-950' :
                            entry.rank === 3 ? 'bg-amber-700 text-white' :
                            'bg-slate-800 text-slate-400 border border-quest-border'
                          }`}>
                            {entry.rank}
                          </span>
                        </td>
                        <td className="py-3.5 px-4">
                          <div className="flex items-center space-x-2.5">
                            <div className="w-8 h-8 rounded-xl bg-slate-800 flex items-center justify-center text-sm border border-quest-border">
                              🧭
                            </div>
                            <div>
                              <div className="font-bold flex items-center space-x-1.5">
                                <span>{entry.display_name}</span>
                                {isCurrentUser && (
                                  <span className="text-[10px] bg-amber-500/20 text-amber-300 border border-amber-500/30 px-1.5 py-0.2 rounded font-bold">
                                    YOU
                                  </span>
                                )}
                              </div>
                              <div className="text-[11px] text-slate-400">{entry.rank_title}</div>
                            </div>
                          </div>
                        </td>
                        <td className="py-3.5 px-4">
                          <span className="px-2 py-0.5 rounded-lg bg-slate-800 border border-quest-border text-xs font-bold text-slate-300">
                            Level {entry.level}
                          </span>
                        </td>
                        <td className="py-3.5 px-4">
                          <span className="text-xs text-slate-300 font-semibold">
                            Grade {entry.grade}
                          </span>
                        </td>
                        <td className="py-3.5 px-4 text-center">
                          <span className="inline-flex items-center space-x-1 text-xs text-amber-400 font-bold">
                            <Flame className="w-3.5 h-3.5 fill-current" />
                            <span>{entry.current_streak}d</span>
                          </span>
                        </td>
                        <td className="py-3.5 px-4 text-center">
                          <span className="inline-flex items-center space-x-1 text-xs text-purple-300 font-bold">
                            <Award className="w-3.5 h-3.5" />
                            <span>{entry.badges_count}</span>
                          </span>
                        </td>
                        <td className="py-3.5 px-4 text-right">
                          <span className="font-extrabold text-amber-400 text-sm">
                            {entry.total_xp} XP
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>

        </div>
      )}

    </div>
  );
}

