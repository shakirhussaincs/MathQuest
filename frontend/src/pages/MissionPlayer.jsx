import React, { useState, useEffect } from 'react';
import { missionApi } from '../api/client';
import { 
  ArrowLeft, 
  Sparkles, 
  CheckCircle2, 
  XCircle, 
  Zap, 
  ArrowRight, 
  Trophy, 
  BookOpen, 
  HelpCircle,
  Award,
  RotateCcw,
  Target,
  Calculator,
  Lock,
  Unlock
} from 'lucide-react';

export default function MissionPlayer({ missionId, onBack, onComplete, onNavigateMission }) {
  const [mission, setMission] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Player state
  const [stage, setStage] = useState('briefing'); // 'briefing', 'playing', 'victory'
  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedOption, setSelectedOption] = useState('');
  const [numericAnswer, setNumericAnswer] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [feedback, setFeedback] = useState(null);
  const [completionResult, setCompletionResult] = useState(null);

  useEffect(() => {
    async function loadMission() {
      setLoading(true);
      setError('');
      try {
        const data = await missionApi.getMission(missionId);
        setMission(data);
      } catch (err) {
        setError(err.message || 'Failed to open mission.');
      } finally {
        setLoading(false);
      }
    }
    loadMission();
  }, [missionId]);

  if (loading) {
    return (
      <div className="min-h-[70vh] flex flex-col items-center justify-center space-y-3">
        <div className="w-12 h-12 rounded-full border-4 border-amber-500/20 border-t-amber-500 animate-spin" />
        <p className="text-slate-400 font-quest text-sm tracking-wider">Unsealing Mission Parchment...</p>
      </div>
    );
  }

  if (error || !mission) {
    return (
      <div className="max-w-xl mx-auto my-12 p-6 glass-panel rounded-2xl text-center">
        <p className="text-red-400 mb-4">{error || 'Mission could not be found.'}</p>
        <button onClick={onBack} className="px-4 py-2 bg-slate-800 text-white rounded-xl">
          Return to Dashboard
        </button>
      </div>
    );
  }

  const currentQ = mission.questions[currentIdx];
  const isLastQuestion = currentIdx === mission.questions.length - 1;
  const isNumeric = currentQ?.question_type === 'numeric';

  const handleSubmitAnswer = async () => {
    const answerToSubmit = isNumeric ? numericAnswer.trim() : selectedOption;
    if (!answerToSubmit) return;

    setSubmitting(true);
    try {
      const res = await missionApi.submitAttempt(mission.id, currentQ.id, answerToSubmit);
      setFeedback(res);
    } catch (err) {
      alert(`Submission error: ${err.message}`);
    } finally {
      setSubmitting(false);
    }
  };

  const handleNextQuestion = () => {
    setFeedback(null);
    setSelectedOption('');
    setNumericAnswer('');
    if (!isLastQuestion) {
      setCurrentIdx(currentIdx + 1);
    } else {
      handleFinalizeMission();
    }
  };

  const handleFinalizeMission = async () => {
    setLoading(true);
    try {
      const summary = await missionApi.completeMission(mission.id);
      setCompletionResult(summary);
      setStage('victory');
    } catch (err) {
      alert(`Error completing mission: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleRetry = () => {
    setStage('playing');
    setCurrentIdx(0);
    setSelectedOption('');
    setNumericAnswer('');
    setFeedback(null);
    setCompletionResult(null);
  };

  // 1. Mission Briefing View
  if (stage === 'briefing') {
    return (
      <div className="max-w-3xl mx-auto px-4 py-12">
        <button
          onClick={onBack}
          className="inline-flex items-center space-x-2 text-sm text-slate-400 hover:text-white mb-6"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Exit to Realm</span>
        </button>

        <div className="glass-panel-glow rounded-3xl p-6 sm:p-10 border border-amber-500/30 text-center space-y-6">
          <div className="w-20 h-20 mx-auto rounded-3xl bg-amber-500/10 border border-amber-500/30 text-4xl flex items-center justify-center shadow-lg shadow-amber-500/10">
            {mission.is_boss ? '👑' : '📜'}
          </div>

          <div>
            <div className="flex items-center justify-center space-x-2 text-xs font-bold text-amber-400 uppercase tracking-widest mb-1.5">
              <span>{mission.world_title}</span>
              <span>•</span>
              <span>{mission.topic_title}</span>
            </div>
            <h1 className="font-quest text-3xl sm:text-4xl font-extrabold text-white">
              {mission.title}
            </h1>
            <p className="text-slate-300 text-sm sm:text-base max-w-xl mx-auto mt-3 leading-relaxed">
              {mission.instructions}
            </p>
          </div>

          {/* Mission Specifications (FR-13, FR-38) */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-lg mx-auto pt-2">
            <div className="p-3 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Stage Level</div>
              <div className="text-xs font-bold text-slate-200 capitalize mt-0.5">{mission.difficulty}</div>
            </div>
            <div className="p-3 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Questions</div>
              <div className="text-xs font-bold text-slate-200 mt-0.5">{mission.question_count} Challenges</div>
            </div>
            <div className="p-3 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Pass Criteria</div>
              <div className="text-xs font-bold text-emerald-400 mt-0.5">&ge; {mission.pass_percentage}% Score</div>
            </div>
            <div className="p-3 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Stage Bonus</div>
              <div className="text-xs font-bold text-amber-400 mt-0.5">+{mission.xp_reward} XP</div>
            </div>
          </div>

          {/* Unlock Explanation if applicable (FR-38) */}
          <div className="p-3 rounded-xl bg-slate-900/60 border border-quest-border/80 max-w-md mx-auto text-xs text-slate-400 flex items-center justify-center space-x-2">
            {mission.is_unlocked ? (
              <>
                <Unlock className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                <span className="text-emerald-300">{mission.unlock_explanation || 'Ready to embark!'}</span>
              </>
            ) : (
              <>
                <Lock className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <span className="text-amber-300">{mission.unlock_explanation}</span>
              </>
            )}
          </div>

          <button
            onClick={() => setStage('playing')}
            disabled={!mission.is_unlocked}
            className="w-full max-w-sm mx-auto py-3.5 px-6 rounded-2xl font-bold bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 shadow-xl shadow-amber-500/20 flex items-center justify-center space-x-2 transition-all transform hover:scale-[1.02] disabled:opacity-40"
          >
            <span>{mission.is_unlocked ? 'Begin Challenge' : 'Stage Locked'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    );
  }

  // 2. Victory / Completion Screen (FR-19, FR-39)
  if (stage === 'victory' && completionResult) {
    const isPassed = completionResult.is_passed;

    return (
      <div className="max-w-2xl mx-auto px-4 py-12 text-center">
        <div className="glass-panel-glow rounded-3xl p-8 sm:p-12 border border-amber-500/40 space-y-6">
          <div className={`w-24 h-24 mx-auto rounded-full flex items-center justify-center text-5xl shadow-2xl ${
            isPassed 
              ? 'bg-gradient-to-tr from-amber-500 to-amber-300 shadow-amber-500/30'
              : 'bg-gradient-to-tr from-slate-700 to-slate-500'
          }`}>
            {isPassed ? (mission.is_boss ? '👑' : '🏆') : '📚'}
          </div>

          <div>
            <div className={`text-xs font-bold uppercase tracking-widest ${isPassed ? 'text-amber-400' : 'text-slate-400'}`}>
              {isPassed ? 'Mission Conquered' : 'Practice Run Completed'}
            </div>
            <h1 className="font-quest text-3xl sm:text-4xl font-extrabold text-white mt-1">
              {completionResult.mission_title}
            </h1>
            <p className="text-slate-300 text-sm mt-2 max-w-md mx-auto">
              {completionResult.message}
            </p>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-3 gap-3">
            <div className="p-4 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Score</div>
              <div className="text-xl font-extrabold text-white">
                {completionResult.score} / {completionResult.total_questions}
              </div>
            </div>
            <div className="p-4 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Accuracy</div>
              <div className={`text-xl font-extrabold ${isPassed ? 'text-emerald-400' : 'text-amber-400'}`}>
                {completionResult.accuracy_percentage}%
              </div>
            </div>
            <div className="p-4 rounded-2xl bg-slate-900/80 border border-quest-border">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Total XP</div>
              <div className="text-xl font-extrabold text-amber-400">
                +{completionResult.total_mission_xp}
              </div>
            </div>
          </div>

          {/* Newly Unlocked Missions Announcement */}
          {completionResult.unlocked_missions && completionResult.unlocked_missions.length > 0 && (
            <div className="p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-left">
              <div className="flex items-center space-x-2 text-emerald-400 text-xs font-bold uppercase mb-1.5">
                <Unlock className="w-4 h-4" />
                <span>Subsequent Stage Unlocked!</span>
              </div>
              <p className="text-xs text-slate-300">
                You have unlocked: <strong className="text-white">{completionResult.unlocked_missions.join(', ')}</strong>
              </p>
            </div>
          )}

          {/* Badges Unlocked Celebration */}
          {completionResult.badges_unlocked && completionResult.badges_unlocked.length > 0 && (
            <div className="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-left">
              <div className="flex items-center space-x-2 text-amber-400 text-xs font-bold uppercase mb-2">
                <Award className="w-4 h-4" />
                <span>New Achievement Badge Unlocked!</span>
              </div>
              <div className="space-y-2">
                {completionResult.badges_unlocked.map((badge) => (
                  <div key={badge.id} className="flex items-center space-x-3 bg-slate-900/60 p-2.5 rounded-xl border border-quest-border">
                    <span className="text-2xl">⭐</span>
                    <div>
                      <div className="font-bold text-white text-xs">{badge.name}</div>
                      <div className="text-[11px] text-slate-300">{badge.description}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Action Buttons: Retry and Dashboard (FR-39) */}
          <div className="flex flex-col sm:flex-row gap-3 pt-2">
            <button
              onClick={handleRetry}
              className="w-full sm:w-1/2 py-3 px-4 rounded-2xl font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-quest-border transition-all flex items-center justify-center space-x-2"
            >
              <RotateCcw className="w-4 h-4 text-amber-400" />
              <span>Retry Challenge</span>
            </button>
            <button
              onClick={onBack}
              className="w-full sm:w-1/2 py-3 px-4 rounded-2xl font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-xl shadow-amber-500/20 transition-all"
            >
              Return to Dashboard
            </button>
          </div>
        </div>
      </div>
    );
  }

  // 3. Active Question Solving View
  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      
      {/* Top Progress & Exit */}
      <div className="flex items-center justify-between mb-4">
        <button
          onClick={onBack}
          className="text-xs text-slate-400 hover:text-white flex items-center space-x-1"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Exit Quest</span>
        </button>

        <div className="flex items-center space-x-3">
          <span className="text-xs font-bold text-amber-400">
            Question {currentIdx + 1} of {mission.questions.length}
          </span>
        </div>
      </div>

      {/* Progress bar */}
      <div className="w-full h-1.5 rounded-full bg-slate-800 overflow-hidden mb-6">
        <div 
          className="h-full bg-amber-500 transition-all duration-300 rounded-full"
          style={{ width: `${((currentIdx + 1) / mission.questions.length) * 100}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="glass-panel-glow rounded-3xl p-6 sm:p-8 space-y-6">
        
        {/* Header Tags */}
        <div className="flex items-center justify-between">
          <span className="inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-slate-800 text-slate-300 border border-quest-border">
            {isNumeric ? <Calculator className="w-3 h-3 text-cyan-400" /> : <BookOpen className="w-3 h-3 text-amber-400" />}
            <span>{isNumeric ? 'Numeric-Answer Challenge' : 'Multiple-Choice Question'}</span>
          </span>
          <span className="text-xs font-semibold text-slate-400 capitalize">
            {currentQ.difficulty}
          </span>
        </div>

        {/* Prompt */}
        <h2 className="text-xl sm:text-2xl font-bold text-white leading-relaxed font-sans">
          {currentQ.prompt}
        </h2>

        {/* Options / Input Form */}
        {!isNumeric ? (
          /* Multiple Choice Radio List */
          <div className="space-y-3">
            {currentQ.options && currentQ.options.map((option, idx) => {
              const isSelected = selectedOption === option;
              const isAnswered = !!feedback;

              return (
                <button
                  key={idx}
                  type="button"
                  disabled={isAnswered}
                  onClick={() => setSelectedOption(option)}
                  className={`w-full p-4 rounded-2xl text-left border text-sm sm:text-base font-medium transition-all flex items-center justify-between ${
                    isSelected 
                      ? 'bg-amber-500/20 border-amber-500 text-amber-200 shadow-md shadow-amber-500/10'
                      : 'bg-slate-900/60 border-quest-border text-slate-200 hover:border-slate-600'
                  } ${isAnswered ? 'cursor-default' : 'cursor-pointer'}`}
                >
                  <span>{option}</span>
                  <div className={`w-5 h-5 rounded-full border flex items-center justify-center ${
                    isSelected ? 'border-amber-500 bg-amber-500 text-slate-950 font-bold' : 'border-slate-600'
                  }`}>
                    {isSelected && '✓'}
                  </div>
                </button>
              );
            })}
          </div>
        ) : (
          /* Numeric Answer Input (FR-15) */
          <div className="space-y-2">
            <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
              Enter Your Numerical Result
            </label>
            <input
              type="text"
              disabled={!!feedback}
              value={numericAnswer}
              onChange={(e) => setNumericAnswer(e.target.value)}
              placeholder="e.g. 5, -3, 0.5, or fraction like 1/2"
              className="w-full p-4 rounded-2xl bg-slate-900 border border-quest-border text-slate-100 text-lg font-mono outline-none focus:border-amber-500 transition-colors disabled:opacity-70"
            />
            <p className="text-[11px] text-slate-400">
              * Numeric answers are evaluated with precision tolerance (&plusmn;0.01).
            </p>
          </div>
        )}

        {/* Submit Button */}
        {!feedback && (
          <button
            type="button"
            disabled={(!isNumeric && !selectedOption) || (isNumeric && !numericAnswer.trim()) || submitting}
            onClick={handleSubmitAnswer}
            className="w-full py-3.5 px-6 rounded-2xl font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-lg shadow-amber-500/20 transition-all disabled:opacity-40 flex items-center justify-center space-x-2"
          >
            <span>{submitting ? 'Checking Mathematical Solution...' : 'Submit Answer'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        )}

        {/* Step-by-Step Feedback & Solution (Module 5) */}
        {feedback && (
          <div className="space-y-4 pt-2">
            
            {/* Outcome Banner */}
            <div className={`p-4 rounded-2xl border flex items-start space-x-3 ${
              feedback.is_correct 
                ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-200'
                : 'bg-red-500/15 border-red-500/40 text-red-200'
            }`}>
              {feedback.is_correct ? (
                <CheckCircle2 className="w-5 h-5 text-emerald-400 flex-shrink-0 mt-0.5" />
              ) : (
                <XCircle className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
              )}
              <div className="space-y-1">
                <div className="font-bold text-sm">
                  {feedback.is_correct ? 'Correct Solution! (+10 XP)' : 'Incorrect Answer'}
                </div>
                <div className="text-xs text-slate-300">
                  {feedback.message}
                </div>
                {!feedback.is_correct && (
                  <div className="text-xs text-amber-300 font-semibold pt-1">
                    Correct Answer: <strong className="text-white bg-slate-900 px-2 py-0.5 rounded border border-quest-border">{feedback.correct_answer}</strong>
                  </div>
                )}
              </div>
            </div>

            {/* Diagnostic Mistake Explanation (FR-24, Module 5) */}
            {!feedback.is_correct && feedback.mistake_analysis && (
              <div className="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-left space-y-1.5">
                <div className="flex items-center space-x-1.5 text-xs font-bold text-amber-400 uppercase">
                  <HelpCircle className="w-4 h-4" />
                  <span>Understanding Your Mistake</span>
                </div>
                <p className="text-xs text-slate-200 leading-relaxed font-sans">
                  {feedback.mistake_analysis}
                </p>
              </div>
            )}

            {/* Step-by-Step Mathematical Solutions (FR-25, Module 5) */}
            <div className="p-4 rounded-2xl bg-slate-900/90 border border-quest-border space-y-2.5 text-left">
              <div className="flex items-center space-x-1.5 text-xs font-bold text-amber-400 uppercase">
                <BookOpen className="w-4 h-4" />
                <span>Step-by-Step Mathematical Solution</span>
              </div>
              
              {feedback.step_by_step_solution && feedback.step_by_step_solution.length > 0 ? (
                <div className="space-y-2">
                  {feedback.step_by_step_solution.map((step, sIdx) => (
                    <div key={sIdx} className="p-2.5 rounded-xl bg-slate-800/60 border border-quest-border/60 text-xs text-slate-200 flex items-start space-x-2">
                      <span className="w-5 h-5 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-[10px] flex-shrink-0 mt-0.5">
                        {sIdx + 1}
                      </span>
                      <span className="leading-relaxed">{step}</span>
                    </div>
                  ))}
                </div>
              ) : (
                <p className="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
                  {feedback.explanation}
                </p>
              )}
            </div>

            {/* Related Practice Recommendations (FR-26, Module 5) */}
            {!feedback.is_correct && feedback.related_practice && (
              <div className="p-4 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-between gap-4">
                <div className="text-left space-y-0.5">
                  <div className="text-xs font-bold text-cyan-400 flex items-center space-x-1">
                    <Target className="w-3.5 h-3.5" />
                    <span>Reinforcement Recommendation</span>
                  </div>
                  <div className="text-xs text-slate-300">
                    {feedback.related_practice.reason}
                  </div>
                </div>
                <button
                  type="button"
                  onClick={handleRetry}
                  className="px-3.5 py-1.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs whitespace-nowrap shadow-sm transition-all"
                >
                  Practise Similar
                </button>
              </div>
            )}

            {/* Next Question / Finalize Button */}
            <button
              onClick={handleNextQuestion}
              className="w-full py-3.5 px-6 rounded-2xl font-bold bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 shadow-xl shadow-amber-500/20 transition-all flex items-center justify-center space-x-2"
            >
              <span>{isLastQuestion ? 'Complete Mission' : 'Next Question'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>

          </div>
        )}

      </div>

    </div>
  );
}
