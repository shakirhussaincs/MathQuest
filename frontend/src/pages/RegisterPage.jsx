import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { Compass, User, Mail, Lock, GraduationCap, AlertCircle, CheckCircle, ArrowRight } from 'lucide-react';

const AVATARS = [
  { id: 'avatar_explorer_1', label: 'Adventurer', emoji: '🧭' },
  { id: 'avatar_wizard_gold', label: 'Math Wizard', emoji: '🧙‍♂️' },
  { id: 'avatar_knight', label: 'Knight', emoji: '⚔️' },
  { id: 'avatar_scholar', label: 'Scholar', emoji: '📜' },
  { id: 'avatar_alchemist', label: 'Alchemist', emoji: '🧪' },
];

export default function RegisterPage({ onNavigate }) {
  const { register } = useAuth();
  const [displayName, setDisplayName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('student');
  const [grade, setGrade] = useState(11); // default grade 11
  const [avatar, setAvatar] = useState('avatar_explorer_1');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (role === 'student' && !grade) {
      setError('Please select your grade level.');
      return;
    }

    setLoading(true);
    try {
      await register({
        display_name: displayName,
        email,
        password,
        role,
        grade: role === 'student' ? Number(grade) : null,
        avatar
      });
      onNavigate('dashboard');
    } catch (err) {
      setError(err.message || 'Registration failed. Please check your details.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[85vh] flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-xl">
        
        {/* Header */}
        <div className="text-center mb-6">
          <div className="inline-flex p-3 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-amber-400 mb-3">
            <Compass className="w-7 h-7" />
          </div>
          <h1 className="font-quest text-3xl font-extrabold text-white tracking-wide">
            Join the Adventure
          </h1>
          <p className="text-slate-400 text-sm mt-1">
            Create your learner profile and unlock mathematics missions
          </p>
        </div>

        {/* Card */}
        <div className="glass-panel-glow rounded-2xl p-6 sm:p-8 shadow-2xl">
          
          {error && (
            <div className="mb-5 p-3.5 rounded-xl bg-red-500/15 border border-red-500/30 text-red-300 text-sm flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">
            
            {/* Display Name & Email */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">
                  Display Name
                </label>
                <div className="relative">
                  <User className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
                  <input
                    type="text"
                    required
                    value={displayName}
                    onChange={(e) => setDisplayName(e.target.value)}
                    placeholder="e.g. Tariq Khan"
                    className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-quest-border focus:border-amber-500 text-slate-100 text-sm outline-none"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">
                  Email Address
                </label>
                <div className="relative">
                  <Mail className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
                  <input
                    type="email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="student@school.edu"
                    className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-quest-border focus:border-amber-500 text-slate-100 text-sm outline-none"
                  />
                </div>
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">
                Password (min. 6 characters)
              </label>
              <div className="relative">
                <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
                <input
                  type="password"
                  required
                  minLength={6}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Create a secure password"
                  className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-quest-border focus:border-amber-500 text-slate-100 text-sm outline-none"
                />
              </div>
            </div>

            {/* Role Selection */}
            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
                Account Role
              </label>
              <div className="grid grid-cols-2 gap-3">
                <button
                  type="button"
                  onClick={() => setRole('student')}
                  className={`p-2.5 rounded-xl border text-sm font-medium flex items-center justify-center space-x-2 transition-all ${
                    role === 'student'
                      ? 'bg-amber-500/15 border-amber-500 text-amber-300 shadow-sm'
                      : 'border-quest-border text-slate-400 hover:bg-slate-800'
                  }`}
                >
                  <GraduationCap className="w-4 h-4" />
                  <span>Student Learner</span>
                </button>

                <button
                  type="button"
                  onClick={() => setRole('teacher')}
                  className={`p-2.5 rounded-xl border text-sm font-medium flex items-center justify-center space-x-2 transition-all ${
                    role === 'teacher'
                      ? 'bg-cyan-500/15 border-cyan-500 text-cyan-300 shadow-sm'
                      : 'border-quest-border text-slate-400 hover:bg-slate-800'
                  }`}
                >
                  <User className="w-4 h-4" />
                  <span>Educator / Teacher</span>
                </button>
              </div>
            </div>

            {/* Grade Selection (1-10, 11th or 12th) */}
            {role === 'student' && (
              <div>
                <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
                  Select Grade Level (1–10, 11th, or 12th)
                </label>
                <div className="grid grid-cols-4 sm:grid-cols-6 gap-2">
                  {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((g) => (
                    <button
                      key={g}
                      type="button"
                      onClick={() => setGrade(g)}
                      className={`py-2 px-3 rounded-xl border text-xs font-bold transition-all ${
                        grade === g
                          ? 'bg-amber-500 text-slate-950 border-amber-400 shadow-md shadow-amber-500/20 scale-105'
                          : 'bg-slate-900/60 border-quest-border text-slate-300 hover:border-slate-500'
                      }`}
                    >
                      {g >= 11 ? `${g}th` : `Gr ${g}`}
                    </button>
                  ))}
                </div>
                <p className="text-[11px] text-amber-400/80 mt-1.5">
                  ⭐ Core high-school worlds (Algebra Kingdom, Trigonometry, Calculus Tower) are currently featured for Grades 11 and 12.
                </p>
              </div>
            )}

            {/* Avatar Picker */}
            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
                Choose Explorer Avatar
              </label>
              <div className="grid grid-cols-5 gap-2">
                {AVATARS.map((av) => (
                  <button
                    key={av.id}
                    type="button"
                    onClick={() => setAvatar(av.id)}
                    className={`p-2.5 rounded-xl border text-center transition-all ${
                      avatar === av.id
                        ? 'bg-amber-500/20 border-amber-500 shadow-md'
                        : 'border-quest-border bg-slate-900/60 hover:bg-slate-800'
                    }`}
                  >
                    <div className="text-2xl mb-1">{av.emoji}</div>
                    <div className="text-[10px] text-slate-300 truncate">{av.label}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* Submit */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 px-4 rounded-xl font-semibold bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 shadow-lg shadow-amber-500/20 transition-all flex items-center justify-center space-x-2 mt-4 disabled:opacity-50"
            >
              <span>{loading ? 'Creating Account...' : 'Complete Registration'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </form>

          <div className="mt-6 text-center text-xs text-slate-400">
            Already registered?{' '}
            <button
              onClick={() => onNavigate('login')}
              className="text-amber-400 font-semibold hover:underline"
            >
              Log in to your account
            </button>
          </div>

        </div>

      </div>
    </div>
  );
}

