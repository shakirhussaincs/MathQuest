import React, { useState, useEffect } from 'react';
import { dashboardApi } from '../api/client';
import { 
  Compass, 
  BookOpen, 
  ArrowLeft, 
  Trophy, 
  Play, 
  Target, 
  Sparkles, 
  Lock, 
  CheckCircle2, 
  ShieldAlert,
  Flame
} from 'lucide-react';

export default function WorldDetailPage({ worldId, onBack, onSelectMission }) {
  const [world, setWorld] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    async function loadWorld() {
      setLoading(true);
      try {
        const data = await dashboardApi.getWorldDetail(worldId);
        setWorld(data);
      } catch (err) {
        setError(err.message || 'Failed to load world details.');
      } finally {
        setLoading(false);
      }
    }
    loadWorld();
  }, [worldId]);

  if (loading) {
    return (
      <div className="min-h-[60vh] flex flex-col items-center justify-center space-y-3">
        <div className="w-10 h-10 border-4 border-amber-500/20 border-t-amber-500 rounded-full animate-spin" />
        <p className="text-slate-400 font-quest text-xs tracking-wider">Loading World Atlas...</p>
      </div>
    );
  }

  if (error || !world) {
    return (
      <div className="max-w-xl mx-auto my-12 p-6 glass-panel rounded-2xl text-center">
        <p className="text-red-400 mb-4">{error || 'World not found.'}</p>
        <button onClick={onBack} className="px-4 py-2 bg-slate-800 text-white rounded-xl">
          Return to Dashboard
        </button>
      </div>
    );
  }

  const getWorldEmoji = (title) => {
    if (title.includes('Algebra')) return '📐';
    if (title.includes('Trigonometry')) return '🌊';
    if (title.includes('Calculus')) return '🏰';
    if (title.includes('Statistics')) return '📊';
    return '🧭';
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 sm:px-6 space-y-8">
      
      {/* Top back button */}
      <button
        onClick={onBack}
        className="inline-flex items-center space-x-2 text-xs sm:text-sm text-slate-400 hover:text-white transition-colors"
      >
        <ArrowLeft className="w-4 h-4" />
        <span>Back to Student Dashboard</span>
      </button>

      {/* World Hero Banner */}
      <div className="glass-panel-glow rounded-3xl p-6 sm:p-8 relative overflow-hidden">
        <div className="flex items-start space-x-5">
          <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-slate-800 flex items-center justify-center text-3xl sm:text-4xl border border-quest-border flex-shrink-0 shadow-lg">
            {getWorldEmoji(world.title)}
          </div>
          <div>
            <div className="flex items-center space-x-2 mb-1.5">
              <span className="px-2.5 py-0.5 text-xs font-bold rounded-md bg-amber-500/20 text-amber-300 border border-amber-500/30">
                Grade {world.grade} Syllabus
              </span>
              <span className="text-xs text-slate-400 font-medium">Interactive Mathematics Realm</span>
            </div>
            <h1 className="font-quest text-2xl sm:text-3xl font-extrabold text-white">
              {world.title}
            </h1>
            <p className="text-slate-300 text-xs sm:text-sm mt-1 max-w-2xl leading-relaxed">
              {world.description}
            </p>
          </div>
        </div>
      </div>

      {/* Topics and Missions List */}
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="font-quest text-xl font-bold text-white flex items-center space-x-2">
            <BookOpen className="w-5 h-5 text-amber-400" />
            <span>Curriculum Topics & Quest Stages</span>
          </h2>
          <span className="text-xs text-slate-400">
            {world.topics.length} Syllabus Topics
          </span>
        </div>

        {world.topics.map((topic, tIdx) => (
          <div key={topic.id} className="glass-panel rounded-2xl p-5 sm:p-6 border border-quest-border space-y-4">
            
            {/* Topic Header & Description */}
            <div className="border-b border-quest-border/80 pb-4">
              <div className="text-xs text-amber-400 font-bold uppercase tracking-wider">
                Topic {tIdx + 1}
              </div>
              <h3 className="text-lg font-bold text-white mt-0.5">{topic.title}</h3>
              {topic.description && (
                <p className="text-xs text-slate-300 mt-1">{topic.description}</p>
              )}

              {/* Learning Objectives Pills */}
              {topic.learning_objectives && topic.learning_objectives.length > 0 && (
                <div className="mt-3">
                  <div className="text-[11px] font-semibold text-slate-400 mb-1.5 flex items-center space-x-1">
                    <Target className="w-3.5 h-3.5 text-emerald-400" />
                    <span>Learning Objectives:</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5">
                    {topic.learning_objectives.map((obj, oIdx) => (
                      <span 
                        key={oIdx}
                        className="px-2.5 py-1 rounded-lg text-[11px] font-medium bg-slate-900/80 text-slate-200 border border-quest-border flex items-center space-x-1"
                      >
                        <span className="text-emerald-400 font-bold">•</span>
                        <span>{obj}</span>
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Missions Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {topic.missions.map((mission) => {
                const isBoss = mission.is_boss;

                return (
                  <div
                    key={mission.id}
                    className={`p-4 sm:p-5 rounded-2xl border flex flex-col justify-between transition-all ${
                      isBoss 
                        ? 'bg-purple-950/20 border-purple-500/40 hover:border-purple-400 shadow-md shadow-purple-950/20'
                        : 'bg-slate-900/60 border-quest-border hover:border-amber-500/40'
                    }`}
                  >
                    <div>
                      {/* Mission Badges */}
                      <div className="flex items-center justify-between mb-2">
                        <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${
                          isBoss
                            ? 'bg-purple-500/20 text-purple-300 border border-purple-500/40 flex items-center space-x-1'
                            : mission.category === 'concept_exploration'
                            ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                            : 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30'
                        }`}>
                          {isBoss ? '👑 Boss Challenge' : mission.category ? mission.category.replace('_', ' ') : 'Practice'}
                        </span>

                        <span className="text-xs font-bold text-amber-400">
                          +{mission.xp_reward} XP
                        </span>
                      </div>

                      <h4 className="font-bold text-white text-base">
                        {mission.title}
                      </h4>
                      <p className="text-xs text-slate-300 mt-1 line-clamp-2">
                        {mission.instructions}
                      </p>
                    </div>

                    <div className="mt-4 pt-3 border-t border-quest-border/60 flex items-center justify-between">
                      <span className="text-[11px] text-slate-400">
                        {mission.question_count} Questions • {mission.difficulty}
                      </span>
                      <button
                        onClick={() => onSelectMission(mission.id)}
                        className={`px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center space-x-1.5 transition-all ${
                          isBoss
                            ? 'bg-purple-600 hover:bg-purple-500 text-white shadow-md shadow-purple-600/30'
                            : 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-md shadow-amber-500/20'
                        }`}
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                        <span>Embark</span>
                      </button>
                    </div>

                  </div>
                );
              })}
            </div>

          </div>
        ))}

      </div>

    </div>
  );
}
