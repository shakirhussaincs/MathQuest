import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { authApi } from '../api/client';
import { Compass, Lock, Mail, AlertCircle, ArrowRight, KeyRound } from 'lucide-react';

export default function LoginPage({ onNavigate }) {
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [showForgot, setShowForgot] = useState(false);
  const [forgotEmail, setForgotEmail] = useState('');
  const [forgotMsg, setForgotMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(email, password);
      onNavigate('dashboard');
    } catch (err) {
      setError(err.message || 'Login failed. Please check your credentials.');
    } finally {
      setLoading(false);
    }
  };



  const handleForgotSubmit = async (e) => {
    e.preventDefault();
    setForgotMsg('');
    setError('');
    try {
      const res = await authApi.forgotPassword(forgotEmail);
      setForgotMsg(res.detail || res.message);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="min-h-[85vh] flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md">
        
        {/* Card Header */}
        <div className="text-center mb-8">
          <div className="inline-flex p-3 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-amber-400 mb-4 shadow-lg shadow-amber-500/10">
            <Compass className="w-8 h-8" />
          </div>
          <h1 className="font-quest text-3xl font-extrabold text-white tracking-wide">
            Enter the Realm
          </h1>
          <p className="text-slate-400 text-sm mt-1">
            Log in to continue your Grade 11–12 Mathematics Quest
          </p>
        </div>

        {/* Form Container */}
        <div className="glass-panel-glow rounded-2xl p-6 sm:p-8 shadow-2xl relative">
          
          {error && (
            <div className="mb-5 p-3.5 rounded-xl bg-red-500/15 border border-red-500/30 text-red-300 text-sm flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{error}</span>
            </div>
          )}

          {!showForgot ? (
            <form onSubmit={handleSubmit} className="space-y-4">
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
                    placeholder="student@mathquest.edu"
                    className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-quest-border focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-slate-100 placeholder-slate-500 text-sm outline-none transition-all"
                  />
                </div>
              </div>

              <div>
                <div className="flex items-center justify-between mb-1.5">
                  <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider">
                    Password
                  </label>
                  <button
                    type="button"
                    onClick={() => { setShowForgot(true); setError(''); }}
                    className="text-xs text-amber-400 hover:text-amber-300 transition-colors"
                  >
                    Forgot password?
                  </button>
                </div>
                <div className="relative">
                  <Lock className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
                  <input
                    type="password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="••••••••"
                    className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-quest-border focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-slate-100 placeholder-slate-500 text-sm outline-none transition-all"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full py-3 px-4 rounded-xl font-semibold bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 shadow-lg shadow-amber-500/20 transition-all flex items-center justify-center space-x-2 mt-2 disabled:opacity-50"
              >
                <span>{loading ? 'Authenticating...' : 'Commence Quest'}</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </form>
          ) : (
            <form onSubmit={handleForgotSubmit} className="space-y-4">
              <div className="flex items-center space-x-2 text-amber-400 mb-2">
                <KeyRound className="w-5 h-5" />
                <span className="font-semibold text-sm">Reset Your Password</span>
              </div>
              <p className="text-xs text-slate-400">
                Enter your email address to generate a secure reset token.
              </p>
              <div>
                <input
                  type="email"
                  required
                  value={forgotEmail}
                  onChange={(e) => setForgotEmail(e.target.value)}
                  placeholder="Enter registered email"
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-900/80 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
                />
              </div>

              {forgotMsg && (
                <div className="p-3 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-emerald-300 text-xs">
                  {forgotMsg}
                </div>
              )}

              <div className="flex space-x-2">
                <button
                  type="button"
                  onClick={() => setShowForgot(false)}
                  className="w-1/2 py-2 text-xs rounded-xl border border-quest-border text-slate-300 hover:bg-slate-800"
                >
                  Back to Login
                </button>
                <button
                  type="submit"
                  className="w-1/2 py-2 text-xs rounded-xl bg-amber-500 text-slate-950 font-semibold hover:bg-amber-400"
                >
                  Send Reset Token
                </button>
              </div>
            </form>
          )}

          {/* Quick Evaluator Demo Logins */}


          <div className="mt-6 text-center text-xs text-slate-400">
            Don't have an account yet?{' '}
            <button
              onClick={() => onNavigate('register')}
              className="text-amber-400 font-semibold hover:underline"
            >
              Register here
            </button>
          </div>

        </div>

      </div>
    </div>
  );
}

