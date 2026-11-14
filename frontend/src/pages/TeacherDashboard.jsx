import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { dashboardApi, missionApi } from '../api/client';
import { 
  GraduationCap, 
  BookOpen, 
  Users, 
  CheckCircle2, 
  TrendingUp, 
  Layers, 
  Compass, 
  ChevronRight, 
  Search, 
  Eye, 
  X, 
  FileText, 
  Sparkles, 
  AlertCircle,
  HelpCircle,
  Info
} from 'lucide-react';

export default function TeacherDashboard({ onNavigate }) {
  const { user } = useAuth();
  const [selectedGrade, setSelectedGrade] = useState(() => user?.grade || 11);
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  
  // Mission inspector state
  const [inspectingMissionId, setInspectingMissionId] = useState(null);
  const [missionPreview, setMissionPreview] = useState(null);
  const [previewLoading, setPreviewLoading] = useState(false);

  const loadData = async (grade) => {
    setLoading(true);
    setError('');
    try {
      const data = await dashboardApi.getTeacherDashboard(grade);
      setDashboardData(data);
    } catch (err) {
      setError(err.message || 'Failed to load educator dashboard.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData(selectedGrade);
  }, [selectedGrade]);

  const handleInspectMission = async (missionId) => {
    setInspectingMissionId(missionId);
    setPreviewLoading(true);
    try {
      const preview = await missionApi.getTeacherMissionPreview(missionId);
      setMissionPreview(preview);
    } catch (err) {
      alert(`Could not load mission details: ${err.message}`);
      setInspectingMissionId(null);
    } finally {
      setPreviewLoading(false);
    }
  };

  const closeInspector = () => {
    setInspectingMissionId(null);
    setMissionPreview(null);
  };

  if (loading && !dashboardData) {
    return (
      <div className="min-h-[70vh] flex flex-col items-center justify-center space-y-4">
        <div className="w-12 h-12 rounded-full border-4 border-cyan-500/20 border-t-cyan-500 animate-spin" />
        <p className="text-slate-400 font-quest text-sm tracking-wider">Loading Educator Workspace...</p>
      </div>
    );
  }

  const { teacher, insights, worlds = [], grades_coverage = [] } = dashboardData || {};

  return (
    <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 space-y-8">
      
      {/* 1. Educator Workspace Hero */}
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-cyan-500/30 bg-gradient-to-r from-cyan-950/30 via-slate-900 to-slate-950 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="flex items-start space-x-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-cyan-600 to-blue-600 flex items-center justify-center text-white shadow-xl shadow-cyan-500/20 border border-cyan-400/40">
              <GraduationCap className="w-9 h-9" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="px-2.5 py-0.5 text-[11px] font-bold rounded-md bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 uppercase tracking-wider">
                  Mathematics Educator
                </span>
                <span className="text-xs text-slate-400">Sindh STREAM Activities 2026–27</span>
              </div>
              <h1 className="font-quest text-2xl sm:text-3xl font-extrabold text-white mt-1">
                {teacher?.display_name || user?.display_name}
              </h1>
              <p className="text-slate-300 text-xs sm:text-sm mt-1 max-w-2xl">
                Curriculum planning, mission diagnosis, step-by-step mathematical solutions, and aggregate grade-level performance insights.
              </p>
            </div>
          </div>

          {/* Grade Selector */}
          <div className="bg-slate-900/90 p-3 rounded-2xl border border-cyan-500/30 flex flex-col sm:flex-row items-center gap-3">
            <span className="text-xs font-semibold text-cyan-300 uppercase tracking-wider">
              Grade Focus:
            </span>
            <select
              value={selectedGrade}
              onChange={(e) => setSelectedGrade(Number(e.target.value))}
              className="px-3 py-1.5 rounded-xl bg-slate-800 border border-cyan-500/40 text-sm font-bold text-white outline-none focus:ring-2 focus:ring-cyan-500 cursor-pointer"
            >
              {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((g) => (
                <option key={g} value={g}>
                  Grade {g}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {error && (
        <div className="p-4 rounded-xl bg-red-500/15 border border-red-500/30 text-red-300 text-sm flex items-center space-x-2">
          <AlertCircle className="w-5 h-5 flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* 2. Grade Learning Insights Cards */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h2 className="text-base font-bold text-white flex items-center space-x-2">
            <TrendingUp className="w-4 h-4 text-cyan-400" />
            <span>Grade {selectedGrade} Academic Insights</span>
          </h2>
          <span className="text-xs text-slate-400">Authorized aggregate statistics</span>
        </div>

        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="glass-panel p-4 rounded-2xl border border-quest-border flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-cyan-500/15 text-cyan-400 flex items-center justify-center font-bold">
              <Users className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xl font-extrabold text-white">{insights?.total_students ?? 0}</div>
              <div className="text-[11px] text-slate-400">Enrolled Students</div>
            </div>
          </div>

          <div className="glass-panel p-4 rounded-2xl border border-quest-border flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-blue-500/15 text-blue-400 flex items-center justify-center font-bold">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xl font-extrabold text-white">{insights?.total_attempts ?? 0}</div>
              <div className="text-[11px] text-slate-400">Practice Attempts</div>
            </div>
          </div>

          <div className="glass-panel p-4 rounded-2xl border border-quest-border flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-emerald-500/15 text-emerald-400 flex items-center justify-center font-bold">
              <CheckCircle2 className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xl font-extrabold text-white">{insights?.average_accuracy ?? 0}%</div>
              <div className="text-[11px] text-slate-400">Average Accuracy</div>
            </div>
          </div>

          <div className="glass-panel p-4 rounded-2xl border border-quest-border flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-purple-500/15 text-purple-400 flex items-center justify-center font-bold">
              <Layers className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xl font-extrabold text-white">
                {insights?.total_missions ?? 0}
              </div>
              <div className="text-[11px] text-slate-400">Available Missions ({insights?.total_questions ?? 0} Qs)</div>
            </div>
          </div>
        </div>
      </div>

      {/* 3. Mathematics Curriculum Explorer */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="font-quest text-xl font-bold text-white flex items-center space-x-2">
              <Compass className="w-5 h-5 text-cyan-400" />
              <span>Curriculum Explorer (Grade {selectedGrade})</span>
            </h2>
            <p className="text-xs text-slate-400">
              Browse learning realms, topic competencies, and inspect questions with step-by-step solutions
            </p>
          </div>
        </div>

        {worlds.length === 0 ? (
          <div className="glass-panel p-8 rounded-2xl border border-quest-border text-center space-y-3">
            <BookOpen className="w-10 h-10 text-cyan-400/50 mx-auto" />
            <h3 className="text-base font-bold text-white">No Curriculum Content for Grade {selectedGrade}</h3>
            <p className="text-xs text-slate-400 max-w-md mx-auto">
              Grade {selectedGrade} mathematics content has not yet been seeded in the platform. You can switch to Grade 11 or Grade 12 to explore existing topics and missions.
            </p>
          </div>
        ) : (
          <div className="space-y-6">
            {worlds.map((w) => (
              <div key={w.id} className="glass-panel rounded-2xl border border-quest-border p-6 space-y-5">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-quest-border">
                  <div>
                    <div className="flex items-center space-x-2">
                      <span className="text-lg">📐</span>
                      <h3 className="font-quest text-lg font-bold text-white">{w.title}</h3>
                      <span className="text-xs px-2 py-0.5 rounded bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">
                        Grade {w.grade}
                      </span>
                    </div>
                    <p className="text-xs text-slate-300 mt-1">{w.description}</p>
                  </div>
                  <div className="text-xs text-slate-400 flex items-center space-x-3">
                    <span><strong>{w.topics?.length || 0}</strong> Topics</span>
                  </div>
                </div>

                {/* Topics in this world */}
                <div className="grid grid-cols-1 gap-4">
                  {w.topics?.map((topic) => (
                    <div key={topic.id} className="bg-slate-900/60 rounded-xl p-4 border border-quest-border/80 space-y-3">
                      <div>
                        <h4 className="text-sm font-bold text-cyan-200">{topic.title}</h4>
                        {topic.description && (
                          <p className="text-xs text-slate-400 mt-0.5">{topic.description}</p>
                        )}
                        {topic.learning_objectives?.length > 0 && (
                          <div className="mt-2 flex flex-wrap gap-1.5">
                            {topic.learning_objectives.map((obj, i) => (
                              <span key={i} className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">
                                • {obj}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>

                      {/* Missions list */}
                      <div className="space-y-2 pt-2 border-t border-slate-800">
                        <div className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
                          Topic Practice Missions:
                        </div>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5">
                          {topic.missions?.map((m) => (
                            <div
                              key={m.id}
                              className="bg-slate-800/80 hover:bg-slate-800 p-3 rounded-xl border border-slate-700 flex flex-col justify-between transition-colors"
                            >
                              <div>
                                <div className="flex items-center justify-between text-xs mb-1">
                                  <span className={`px-1.5 py-0.5 rounded text-[10px] font-semibold uppercase ${
                                    m.is_boss 
                                      ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30' 
                                      : 'bg-cyan-500/15 text-cyan-300'
                                  }`}>
                                    {m.is_boss ? 'Boss Challenge' : m.difficulty}
                                  </span>
                                  <span className="text-slate-400 text-[11px]">{m.question_count} Qs</span>
                                </div>
                                <h5 className="text-xs font-bold text-white line-clamp-1">{m.title}</h5>
                                <p className="text-[11px] text-slate-400 mt-1 line-clamp-2">{m.instructions}</p>
                              </div>

                              <button
                                onClick={() => handleInspectMission(m.id)}
                                className="mt-3 w-full py-1.5 rounded-lg bg-cyan-600/20 hover:bg-cyan-600/40 text-cyan-300 border border-cyan-500/30 text-xs font-semibold flex items-center justify-center space-x-1.5 transition-colors"
                              >
                                <Eye className="w-3.5 h-3.5" />
                                <span>Inspect Questions</span>
                              </button>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* 4. Grade 1–12 Platform Curriculum Coverage Table */}
      <div className="glass-panel rounded-2xl border border-quest-border p-6 space-y-4">
        <div>
          <h2 className="text-base font-bold text-white flex items-center space-x-2">
            <Layers className="w-4 h-4 text-cyan-400" />
            <span>Grade 1–12 Mathematics Curriculum Coverage Matrix</span>
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Real-time platform audit of mathematics content availability and student enrollments across all 12 grades
          </p>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-900/80 border-b border-quest-border text-slate-400 uppercase text-[10px] font-semibold">
              <tr>
                <th className="py-2.5 px-3">Grade Level</th>
                <th className="py-2.5 px-3">Realms (Worlds)</th>
                <th className="py-2.5 px-3">Missions</th>
                <th className="py-2.5 px-3">Active Questions</th>
                <th className="py-2.5 px-3">Enrolled Students</th>
                <th className="py-2.5 px-3">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-quest-border/60">
              {grades_coverage.map((row) => (
                <tr 
                  key={row.grade} 
                  className={`hover:bg-slate-800/40 transition-colors ${
                    row.grade === selectedGrade ? 'bg-cyan-950/20 font-semibold' : ''
                  }`}
                >
                  <td className="py-2.5 px-3 text-white">
                    Grade {row.grade} {row.grade === selectedGrade && <span className="text-cyan-400 text-[10px] ml-1">(Selected)</span>}
                  </td>
                  <td className="py-2.5 px-3 text-slate-300">{row.worlds_count}</td>
                  <td className="py-2.5 px-3 text-slate-300">{row.missions_count}</td>
                  <td className="py-2.5 px-3 text-slate-300">{row.questions_count}</td>
                  <td className="py-2.5 px-3 text-slate-300">{row.students_count}</td>
                  <td className="py-2.5 px-3">
                    {row.questions_count > 0 ? (
                      <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded text-[10px] bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                        <CheckCircle2 className="w-3 h-3" />
                        <span>Ready</span>
                      </span>
                    ) : (
                      <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded text-[10px] bg-slate-800 text-slate-400 border border-slate-700">
                        <span>Pending Seeding</span>
                      </span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* 5. Sindh STREAM Teaching Resources */}
      <div className="glass-panel rounded-2xl border border-quest-border p-6 space-y-4">
        <h2 className="text-base font-bold text-white flex items-center space-x-2">
          <FileText className="w-4 h-4 text-cyan-400" />
          <span>Sindh STREAM 2026–27 Teaching Resources & Pedagogy</span>
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-slate-900/60 p-4 rounded-xl border border-quest-border space-y-2">
            <h3 className="text-xs font-bold text-cyan-300 flex items-center space-x-1.5">
              <span>📚</span>
              <span>Competency Guidelines</span>
            </h3>
            <p className="text-xs text-slate-300">
              Grade 11 emphasizes algebraic matrices, determinants, and circular functions. Grade 12 centers on differential calculus, limit continuity, and standard deviation.
            </p>
          </div>

          <div className="bg-slate-900/60 p-4 rounded-xl border border-quest-border space-y-2">
            <h3 className="text-xs font-bold text-cyan-300 flex items-center space-x-1.5">
              <span>🎯</span>
              <span>Diagnostic Interventions</span>
            </h3>
            <p className="text-xs text-slate-300">
              MathQuest provides diagnostic common mistakes on every problem. Review common wrong answers during classroom lectures to address algebraic misconceptions proactively.
            </p>
          </div>

          <div className="bg-slate-900/60 p-4 rounded-xl border border-quest-border space-y-2">
            <h3 className="text-xs font-bold text-cyan-300 flex items-center space-x-1.5">
              <span>🎲</span>
              <span>Anti-Cheat Randomization</span>
            </h3>
            <p className="text-xs text-slate-300">
              Questions are server-side randomized per student attempt. Concurrent students in the same lab receive different starting questions and independently shuffled order.
            </p>
          </div>
        </div>
      </div>

      {/* 6. Mission Question Inspector Modal */}
      {inspectingMissionId && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm overflow-y-auto">
          <div className="glass-panel w-full max-w-4xl max-h-[90vh] rounded-3xl border border-cyan-500/40 p-6 sm:p-8 flex flex-col overflow-hidden shadow-2xl relative animate-in fade-in zoom-in-95">
            <button
              onClick={closeInspector}
              className="absolute top-5 right-5 p-2 rounded-xl text-slate-400 hover:text-white bg-slate-800/80 hover:bg-slate-700 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>

            {previewLoading ? (
              <div className="py-24 text-center space-y-3">
                <div className="w-10 h-10 border-4 border-cyan-500/20 border-t-cyan-500 rounded-full animate-spin mx-auto" />
                <p className="text-xs text-slate-400">Loading mission questions and step-by-step solutions...</p>
              </div>
            ) : missionPreview ? (
              <div className="space-y-6 overflow-y-auto pr-2">
                <div>
                  <div className="flex items-center space-x-2 text-xs font-bold text-cyan-400 uppercase tracking-wider mb-1">
                    <span>{missionPreview.world?.title} (Grade {missionPreview.world?.grade})</span>
                    <span>•</span>
                    <span>{missionPreview.topic?.title}</span>
                  </div>
                  <h2 className="text-xl sm:text-2xl font-extrabold text-white">
                    {missionPreview.title}
                  </h2>
                  <p className="text-xs text-slate-300 mt-1">{missionPreview.instructions}</p>
                  
                  <div className="mt-3 flex flex-wrap gap-2 text-xs">
                    <span className="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                      Difficulty: {missionPreview.difficulty}
                    </span>
                    <span className="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                      Pass Threshold: {missionPreview.pass_percentage}%
                    </span>
                    <span className="px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">
                      XP Reward: {missionPreview.xp_reward} XP
                    </span>
                  </div>
                </div>

                {/* Questions List */}
                <div className="space-y-4 pt-4 border-t border-quest-border">
                  <h3 className="text-sm font-bold text-white flex items-center space-x-2">
                    <BookOpen className="w-4 h-4 text-cyan-400" />
                    <span>Curriculum Questions & Step-by-Step Solutions ({missionPreview.questions?.length || 0})</span>
                  </h3>

                  <div className="space-y-4">
                    {missionPreview.questions?.map((q, idx) => (
                      <div key={q.id} className="bg-slate-900/80 p-5 rounded-2xl border border-quest-border space-y-3">
                        <div className="flex items-center justify-between text-xs">
                          <span className="font-bold text-cyan-300">Question {idx + 1} ({q.question_type})</span>
                          <span className="text-slate-400 text-[11px]">ID #{q.id}</span>
                        </div>

                        <div className="text-sm font-semibold text-white whitespace-pre-wrap">
                          {q.prompt}
                        </div>

                        {q.options && q.options.length > 0 && (
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                            {q.options.map((opt, optIdx) => (
                              <div
                                key={optIdx}
                                className={`p-2 rounded-lg border ${
                                  opt.includes(q.correct_answer) || q.correct_answer.includes(opt)
                                    ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-300 font-semibold'
                                    : 'bg-slate-800/60 border-slate-700 text-slate-300'
                                }`}
                              >
                                {opt}
                              </div>
                            ))}
                          </div>
                        )}

                        <div className="p-3 rounded-xl bg-emerald-950/20 border border-emerald-500/30 text-xs text-emerald-300 space-y-1">
                          <div className="font-bold flex items-center space-x-1.5">
                            <CheckCircle2 className="w-3.5 h-3.5" />
                            <span>Correct Answer: {q.correct_answer}</span>
                          </div>
                          <p className="text-slate-300 text-[11px]">{q.explanation}</p>
                        </div>

                        {q.step_by_step_solution && q.step_by_step_solution.length > 0 && (
                          <div className="p-3 rounded-xl bg-slate-800/70 border border-slate-700 text-xs space-y-1.5">
                            <div className="font-bold text-cyan-300">Teacher Step-by-Step Solution:</div>
                            <ol className="list-decimal list-inside space-y-1 text-slate-300 text-[11px]">
                              {q.step_by_step_solution.map((step, sIdx) => (
                                <li key={sIdx}>{step}</li>
                              ))}
                            </ol>
                          </div>
                        )}

                        {q.common_mistakes && Object.keys(q.common_mistakes).length > 0 && (
                          <div className="p-3 rounded-xl bg-amber-950/20 border border-amber-500/30 text-xs space-y-1.5">
                            <div className="font-bold text-amber-300 flex items-center space-x-1">
                              <AlertCircle className="w-3.5 h-3.5" />
                              <span>Common Student Diagnostic Misconceptions:</span>
                            </div>
                            <div className="space-y-1 text-slate-300 text-[11px]">
                              {Object.entries(q.common_mistakes).map(([ansKey, expl]) => (
                                <div key={ansKey} className="border-l-2 border-amber-500/50 pl-2">
                                  <strong className="text-amber-200">If student enters '{ansKey}':</strong> {expl}
                                </div>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>

                <div className="pt-4 border-t border-quest-border flex justify-end">
                  <button
                    onClick={closeInspector}
                    className="px-5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-white transition-colors"
                  >
                    Close Inspector
                  </button>
                </div>
              </div>
            ) : null}
          </div>
        </div>
      )}

    </div>
  );
}
