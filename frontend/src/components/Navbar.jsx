import React from 'react';
import { useAuth } from '../context/AuthContext';
import { Compass, User, LogOut, Shield, Award, Sparkles } from 'lucide-react';

export default function Navbar({ currentView, setCurrentView }) {
  const { user, logout, isAdmin } = useAuth();

  return (
    <nav className="glass-panel sticky top-0 z-50 border-b border-quest-border px-4 py-3 sm:px-6">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        
        {/* Brand */}
        <div 
          onClick={() => setCurrentView('dashboard')}
          className="flex items-center space-x-3 cursor-pointer group"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center shadow-lg shadow-amber-500/20 group-hover:scale-105 transition-transform">
            <Compass className="w-6 h-6 text-slate-950 font-bold" />
          </div>
          <div>
            <span className="font-quest text-xl font-extrabold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-amber-200 to-amber-500">
              MATHQUEST
            </span>
            <span className="block text-[10px] tracking-widest text-slate-400 font-semibold uppercase">
              Sindh STREAM 2026–27
            </span>
          </div>
        </div>

        {/* User Stats & Navigation */}
        {user ? (
          <div className="flex items-center space-x-3 sm:space-x-4">
            
            {/* Grade & Role Badges */}
            <div className="hidden md:flex items-center space-x-2">
              {user.grade && (
                <span className="px-2.5 py-1 text-xs font-semibold rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  Grade {user.grade}
                </span>
              )}
              <span className={`px-2.5 py-1 text-xs font-semibold rounded-lg uppercase tracking-wider ${
                user.role === 'admin' 
                  ? 'bg-purple-500/15 text-purple-300 border border-purple-500/30'
                  : user.role === 'teacher'
                  ? 'bg-cyan-500/15 text-cyan-300 border border-cyan-500/30'
                  : 'bg-amber-500/15 text-amber-300 border border-amber-500/30'
              }`}>
                {user.role}
              </span>
            </div>

            {/* Navigation Buttons */}
            <button
              onClick={() => setCurrentView('dashboard')}
              className={`px-3 py-1.5 text-sm font-medium rounded-lg transition-colors ${
                currentView === 'dashboard' 
                  ? 'bg-amber-500 text-slate-950 font-semibold shadow-md shadow-amber-500/20' 
                  : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              Dashboard
            </button>

            <button
              onClick={() => setCurrentView('leaderboard')}
              className={`px-3 py-1.5 text-sm font-medium rounded-lg transition-colors flex items-center space-x-1.5 ${
                currentView === 'leaderboard' 
                  ? 'bg-amber-500 text-slate-950 font-semibold shadow-md shadow-amber-500/20' 
                  : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <Award className="w-4 h-4" />
              <span>Leaderboard</span>
            </button>

            <button
              onClick={() => setCurrentView('profile')}
              className={`px-3 py-1.5 text-sm font-medium rounded-lg transition-colors flex items-center space-x-1.5 ${
                currentView === 'profile' 
                  ? 'bg-amber-500 text-slate-950 font-semibold shadow-md shadow-amber-500/20' 
                  : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
              }`}
            >
              <User className="w-4 h-4" />
              <span className="hidden sm:inline">Profile</span>
            </button>

            {isAdmin && (
              <button
                onClick={() => setCurrentView('admin')}
                className={`px-3 py-1.5 text-sm font-medium rounded-lg transition-colors flex items-center space-x-1.5 ${
                  currentView === 'admin' 
                    ? 'bg-purple-600 text-white font-semibold shadow-md shadow-purple-500/20' 
                    : 'text-purple-300 hover:text-white hover:bg-purple-900/30'
                }`}
              >
                <Shield className="w-4 h-4" />
                <span className="hidden sm:inline">Admin</span>
              </button>
            )}

            {/* User display badge */}
            <div className="flex items-center space-x-2 pl-2 border-l border-quest-border">
              <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-600 flex items-center justify-center text-xs font-bold text-white shadow-inner">
                {user.display_name.charAt(0).toUpperCase()}
              </div>
              <span className="hidden lg:inline text-sm font-medium text-slate-200">
                {user.display_name}
              </span>
              <button
                onClick={logout}
                title="Logout"
                className="p-1.5 text-slate-400 hover:text-red-400 hover:bg-red-500/10 rounded-lg transition-colors"
              >
                <LogOut className="w-4 h-4" />
              </button>
            </div>

          </div>
        ) : (
          <div className="flex items-center space-x-3">
            <button
              onClick={() => setCurrentView('login')}
              className="px-4 py-1.5 text-sm font-medium text-slate-200 hover:text-white transition-colors"
            >
              Log In
            </button>
            <button
              onClick={() => setCurrentView('register')}
              className="px-4 py-1.5 text-sm font-semibold rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition-colors shadow-lg shadow-amber-500/20"
            >
              Register
            </button>
          </div>
        )}

      </div>
    </nav>
  );
}

