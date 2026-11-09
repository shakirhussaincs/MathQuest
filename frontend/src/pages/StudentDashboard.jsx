import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { dashboardApi } from '../api/client';
import { 
  Sparkles, 
  Compass, 
  Trophy, 
  CheckCircle2, 
  Target, 
  Flame, 
  ArrowRight, 
  Lock, 
  Unlock, 
  BookOpen, 
  Award,
  ChevronRight,
  TrendingUp,
  RotateCcw,
  Zap,
  Star
} from 'lucide-react';

export default function StudentDashboard({ onNavigate, onSelectWorld, onSelectMission }) {
  const { user } = useAuth();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const loadDashboard = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await dashboardApi.getStudentDashboard();
      setData(res);
    } catch (err) {
      setError(err.message || 'Failed to load dashboard data.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDashboard();
  }, []);

  if (loading) {
    return (
      <div className="min-h-[70vh] flex flex-col items-center justify-center space-y-4">
        <div className="w-12 h-12 rounded-full border-4 border-amber-500/20 border-t-amber-500 animate-spin" />
        <p className="text-slate-400 font-quest text-sm tracking-wider">Gathering Realm Intelligence...</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="max-w-2xl mx-auto my-12 p-6 glass-panel rounded-2xl text-center">
        <p className="text-red-400 mb-4">{error || 'Unable to display dashboard'}</p>
        <button
          onClick={loadDashboard}
          className="px-4 py-2 bg-amber-500 text-slate-950 font-semibold rounded-xl"
        >
          Retry
        </button>
      </div>
    );
  }

  const { student_profile, gamification, learning_progress, worlds, recently_completed_missions, recommended_next_mission, achievements } = data;

  return (
    <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 space-y-8">
      
      {/* 1. Welcome Screen & Hero Banner */}
      <div className="glass-panel-glow rounded-3xl p-6 sm:p-8 relative overflow-hidden">
        {/* Background decorative glow */}
        <div className="absolute -top-24 -right-24 w-80 h-80 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute -bottom-24 -left-24 w-80 h-80 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col md:flex-row md:items-center md:justify-between gap-6">
          
          {/* Student Welcome info */}
          <div className="flex items-start space-x-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-amber-500 to-amber-700 flex items-center justify-center text-3xl shadow-xl shadow-amber-500/20 border border-amber-400/40">
              🧭
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="px-2.5 py-0.5 text-[11px] font-bold rounded-md bg-amber-500/20 text-amber-300 border border-amber-500/30 uppercase tracking-wider">
                  Grade {student_profile.grade || '11'}
                </span>
                <span className="text-xs text-slate-400 font-medium">
                  {gamification.rank_title}
                </span>
              </div>
              <h1 className="font-quest text-2xl sm:text-3xl font-extrabold text-white mt-1">
                Welcome back, {student_profile.display_name}!
              </h1>
              <p className="text-slate-300 text-sm mt-1 max-w-xl">
                Ready for today's mathematical mission? Practice curriculum concepts, level up, and earn achievement badges.
              </p>
            </div>
          </div>

          {/* Quick Level & XP Summary Card */}
          <div className="p-4 rounded-2xl bg-slate-900/80 border border-quest-border min-w-[260px] flex flex-col justify-between">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center space-x-2">
                <div className="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-extrabold text-sm border border-amber-500/30">
                  L{gamification.level}
                </div>
                <div>
                  <div className="text-[10px] text-slate-400 uppercase font-semibold">Current Tier</div>
                  <div className="text-xs font-bold text-slate-200">Level {gamification.level}</div>
                </div>
              </div>
              <div className="text-right">
                <div className="text-[10px] text-slate-400 uppercase font-semibold">Total XP</div>
                <div className="text-sm font-extrabold text-amber-400 flex items-center justify-end space-x-1">
                  <Zap className="w-3.5 h-3.5 fill-amber-400" />
                  <span>{gamification.current_xp}</span>
                </div>
              </div>
            </div>

            {/* Progress bar to next level */}
            <div className="mt-2 space-y-1">
              <div className="flex justify-between text-[11px] font-medium text-slate-400">
                <span>{gamification.progress_percentage}% to Level {gamification.level + 1}</span>
                <span>{gamification.xp_to_next_level} XP needed</span>
              </div>
              <div className="w-full h-2.5 rounded-full bg-slate-800 overflow-hidden border border-slate-700/50">
                <div 
                  className="h-full bg-gradient-to-r from-amber-500 to-amber-300 transition-all duration-500 rounded-full"
                  style={{ width: `${gamification.progress_percentage}%` }}
                />
              </div>
            </div>

          </div>

        </div>
      </div>

      {/* 2. Learning Progress Stat Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        
        <div className="glass-panel p-5 rounded-2xl border border-quest-border flex items-center space-x-4">
          <div className="p-3 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
            <CheckCircle2 className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Missions Done</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">
              {learning_progress.completed_missions} <span className="text-xs font-normal text-slate-400">/ {learning_progress.total_missions}</span>
            </div>
            <div className="text-[11px] text-emerald-400 font-medium">
              {learning_progress.completion_percentage}% completed
            </div>
          </div>
        </div>

        <div className="glass-panel p-5 rounded-2xl border border-quest-border flex items-center space-x-4">
          <div className="p-3 rounded-xl bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
            <Target className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Overall Accuracy</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">
              {learning_progress.overall_accuracy_percentage}%
            </div>
            <div className="text-[11px] text-slate-400">
              {learning_progress.correct_answers} correct of {learning_progress.total_questions_attempted}
            </div>
          </div>
        </div>

        <div className="glass-panel p-5 rounded-2xl border border-quest-border flex items-center space-x-4">
          <div className="p-3 rounded-xl bg-purple-500/10 text-purple-400 border border-purple-500/20">
            <Award className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Badges Earned</div>
            <div className="text-xl sm:text-2xl font-extrabold text-white">
              {achievements.earned_badges_count} <span className="text-xs font-normal text-slate-400">/ {achievements.total_badges}</span>
            </div>
            <div className="text-[11px] text-purple-300">
              Achievements
            </div>
          </div>
        </div>

        <div className="glass-panel p-5 rounded-2xl border border-quest-border flex items-center space-x-4">
          <div className="p-3 rounded-xl bg-amber-500/10 text-amber-400 border border-amber-500/20">
            <Flame className="w-6 h-6" />
          </div>
          <div>
            <div className="text-xs text-slate-400 uppercase tracking-wider font-semibold">Current Rank</div>
            <div className="text-lg font-bold text-amber-300 truncate max-w-[150px]">
              {gamification.rank_title}
            </div>
            <div className="text-[11px] text-slate-400">
              Level {gamification.level} Adventurer
            </div>
          </div>
        </div>

      </div>

      {/* 3. Recommended Next Mission Card (Hero Action) */}
      {recommended_next_mission && (
        <div className="p-6 rounded-2xl bg-gradient-to-r from-amber-950/40 via-slate-900 to-indigo-950/40 border border-amber-500/30 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-400 text-xs font-semibold">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Recommended Mission: {recommended_next_mission.recommendation_reason}</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-white">
              {recommended_next_mission.title}
            </h2>
            <p className="text-slate-300 text-sm max-w-2xl">
              {recommended_next_mission.instructions}
            </p>
            <div className="flex items-center space-x-4 text-xs text-slate-400 pt-1">
              <span>Topic: <strong className="text-slate-200">{recommended_next_mission.topic_title}</strong></span>
              <span>•</span>
              <span>Realm: <strong className="text-slate-200">{recommended_next_mission.world_title}</strong></span>
              <span>•</span>
              <span className="text-amber-400 font-bold">+{recommended_next_mission.xp_reward} Completion XP</span>
            </div>
          </div>

          <button
            onClick={() => {
              if (onSelectMission) {
                onSelectMission(recommended_next_mission.mission_id);
              } else {
                alert(`Starting Mission: ${recommended_next_mission.title}\n(Topic: ${recommended_next_mission.topic_title})`);
              }
            }}
            className="px-6 py-3.5 rounded-xl font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-lg shadow-amber-500/25 flex items-center justify-center space-x-2 transition-all flex-shrink-0"
          >
            <span>Embark on Mission</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      )}

      {/* 4. Available Mathematics Worlds */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="font-quest text-xl font-bold text-white flex items-center space-x-2">
              <Compass className="w-5 h-5 text-amber-400" />
              <span>Available Mathematics Worlds (Grade {student_profile.grade})</span>
            </h2>
            <p className="text-slate-400 text-xs">Curriculum-aligned practice realms available for your grade</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {worlds.map((world) => (
            <div 
              key={world.id}
              onClick={() => onSelectWorld && onSelectWorld(world.id)}
              className={`p-6 rounded-2xl border transition-all cursor-pointer relative overflow-hidden flex flex-col justify-between ${
                world.is_unlocked 
                  ? 'glass-panel hover:border-amber-500/50 hover:shadow-lg hover:shadow-amber-500/10'
                  : 'bg-slate-900/40 border-quest-border opacity-70'
              }`}
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <div className="w-12 h-12 rounded-xl bg-slate-800 flex items-center justify-center text-2xl border border-quest-border">
                    {world.title.includes('Algebra') ? '📐' : world.title.includes('Trig') ? '🌊' : '🏰'}
                  </div>
                  {world.is_unlocked ? (
                    <span className="inline-flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                      <Unlock className="w-3 h-3" />
                      <span>Unlocked</span>
                    </span>
                  ) : (
                    <span className="inline-flex items-center space-x-1 px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-400 border border-slate-700">
                      <Lock className="w-3 h-3" />
                      <span>Locked</span>
                    </span>
                  )}
                </div>

                <h3 className="font-quest text-lg font-bold text-white">
                  {world.title}
                </h3>
                <p className="text-slate-300 text-xs mt-1.5 line-clamp-2">
                  {world.description}
                </p>
              </div>

              <div className="mt-5 pt-4 border-t border-quest-border/80">
                <div className="flex justify-between items-center text-xs text-slate-400 mb-1.5">
                  <span>Progress</span>
                  <span className="font-semibold text-slate-200">{world.completed_missions} / {world.total_missions} Missions</span>
                </div>
                <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
                  <div 
                    className="h-full bg-emerald-500 rounded-full transition-all"
                    style={{ width: `${world.completion_percentage}%` }}
                  />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 5. Recently Completed Missions & Achievements Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        {/* Recently Completed Missions */}
        <div className="glass-panel p-6 rounded-2xl border border-quest-border">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-quest text-lg font-bold text-white flex items-center space-x-2">
              <BookOpen className="w-5 h-5 text-emerald-400" />
              <span>Recently Completed Missions</span>
            </h3>
          </div>

          {recently_completed_missions && recently_completed_missions.length > 0 ? (
            <div className="space-y-3">
              {recently_completed_missions.map((m) => (
                <div 
                  key={m.progress_id}
                  className="p-3.5 rounded-xl bg-slate-900/60 border border-quest-border/80 flex items-center justify-between"
                >
                  <div className="space-y-0.5">
                    <div className="text-sm font-bold text-slate-100">{m.mission_title}</div>
                    <div className="text-xs text-slate-400">{m.topic_title} • {m.world_title}</div>
                  </div>
                  <div className="text-right">
                    <div className="inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-bold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                      {m.accuracy}% Acc
                    </div>
                    <div className="text-[11px] text-amber-400 font-semibold mt-0.5">
                      +{m.xp_earned} XP
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="p-8 text-center text-slate-400 text-sm">
              <RotateCcw className="w-8 h-8 mx-auto mb-2 opacity-40" />
              No completed missions yet. Start with your recommended mission above!
            </div>
          )}
        </div>

        {/* Achievement Badges Showcase */}
        <div className="glass-panel p-6 rounded-2xl border border-quest-border">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-quest text-lg font-bold text-white flex items-center space-x-2">
              <Award className="w-5 h-5 text-amber-400" />
              <span>Achievement Badges</span>
            </h3>
            <span className="text-xs text-slate-400">
              {achievements.earned_badges_count} of {achievements.total_badges} unlocked
            </span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {achievements.badges.map((b) => (
              <div 
                key={b.id}
                className={`p-3.5 rounded-xl border text-center transition-all ${
                  b.is_earned 
                    ? 'bg-amber-500/10 border-amber-500/40 shadow-sm' 
                    : 'bg-slate-900/40 border-quest-border opacity-50'
                }`}
              >
                <div className="text-2xl mb-1">
                  {b.icon === 'footprints' ? '👣' : b.icon === 'shield' ? '🛡️' : b.icon === 'star' ? '⭐' : b.icon === 'flame' ? '🔥' : '🏆'}
                </div>
                <div className={`text-xs font-bold truncate ${b.is_earned ? 'text-amber-300' : 'text-slate-400'}`}>
                  {b.name}
                </div>
                <div className="text-[10px] text-slate-400 mt-0.5 line-clamp-2">
                  {b.criteria_description}
                </div>
              </div>
            ))}
          </div>
        </div>

      </div>

    </div>
  );
}

