import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { userApi } from '../api/client';
import { User, Lock, CheckCircle2, AlertCircle, Save, KeyRound } from 'lucide-react';

const AVATARS = [
  { id: 'avatar_explorer_1', label: 'Adventurer', emoji: '🧭' },
  { id: 'avatar_wizard_gold', label: 'Math Wizard', emoji: '🧙‍♂️' },
  { id: 'avatar_knight', label: 'Knight', emoji: '⚔️' },
  { id: 'avatar_scholar', label: 'Scholar', emoji: '📜' },
  { id: 'avatar_alchemist', label: 'Alchemist', emoji: '🧪' },
];

export default function ProfilePage() {
  const { user, refreshProfile } = useAuth();
  const [displayName, setDisplayName] = useState(user?.display_name || '');
  const [grade, setGrade] = useState(user?.grade || 11);
  const [avatar, setAvatar] = useState(user?.avatar || 'avatar_explorer_1');
  const [bio, setBio] = useState(user?.bio || '');
  const [profileMsg, setProfileMsg] = useState('');
  const [profileError, setProfileError] = useState('');
  const [profileLoading, setProfileLoading] = useState(false);

  // Password change state
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [pwMsg, setPwMsg] = useState('');
  const [pwError, setPwError] = useState('');
  const [pwLoading, setPwLoading] = useState(false);

  const handleProfileSubmit = async (e) => {
    e.preventDefault();
    setProfileMsg('');
    setProfileError('');
    setProfileLoading(true);
    try {
      await userApi.updateProfile({
        display_name: displayName,
        grade: Number(grade),
        avatar,
        bio
      });
      await refreshProfile();
      setProfileMsg('Profile successfully updated!');
    } catch (err) {
      setProfileError(err.message || 'Failed to update profile.');
    } finally {
      setProfileLoading(false);
    }
  };

  const handlePasswordSubmit = async (e) => {
    e.preventDefault();
    setPwMsg('');
    setPwError('');

    if (newPassword !== confirmPassword) {
      setPwError('New passwords do not match.');
      return;
    }

    setPwLoading(true);
    try {
      const res = await userApi.changePassword(oldPassword, newPassword);
      setPwMsg(res.message || 'Password successfully updated.');
      setOldPassword('');
      setNewPassword('');
      setConfirmPassword('');
    } catch (err) {
      setPwError(err.message || 'Failed to change password.');
    } finally {
      setPwLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 sm:px-6 space-y-8">
      
      <div>
        <h1 className="font-quest text-2xl sm:text-3xl font-extrabold text-white">
          Adventurer Profile & Settings
        </h1>
        <p className="text-slate-400 text-sm mt-1">
          Manage your identity, grade level, and security credentials
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        {/* Profile Settings */}
        <div className="glass-panel p-6 rounded-2xl border border-quest-border space-y-5">
          <div className="flex items-center space-x-2 text-amber-400 font-bold">
            <User className="w-5 h-5" />
            <span>Profile Details</span>
          </div>

          {profileMsg && (
            <div className="p-3 bg-emerald-500/15 border border-emerald-500/30 rounded-xl text-emerald-300 text-xs flex items-center space-x-2">
              <CheckCircle2 className="w-4 h-4 flex-shrink-0" />
              <span>{profileMsg}</span>
            </div>
          )}

          {profileError && (
            <div className="p-3 bg-red-500/15 border border-red-500/30 rounded-xl text-red-300 text-xs flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{profileError}</span>
            </div>
          )}

          <form onSubmit={handleProfileSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1">
                Display Name
              </label>
              <input
                type="text"
                required
                value={displayName}
                onChange={(e) => setDisplayName(e.target.value)}
                className="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1">
                Grade Selection (1–10, 11th or 12th)
              </label>
              <select
                value={grade}
                onChange={(e) => setGrade(Number(e.target.value))}
                className="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
              >
                {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map((g) => (
                  <option key={g} value={g}>
                    Grade {g} {g >= 11 ? '(Higher-Secondary)' : ''}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1.5">
                Explorer Avatar
              </label>
              <div className="grid grid-cols-5 gap-2">
                {AVATARS.map((av) => (
                  <button
                    key={av.id}
                    type="button"
                    onClick={() => setAvatar(av.id)}
                    className={`p-2 rounded-xl border text-center transition-all ${
                      avatar === av.id
                        ? 'bg-amber-500/20 border-amber-500 shadow-md'
                        : 'border-quest-border bg-slate-900/60 hover:bg-slate-800'
                    }`}
                  >
                    <div className="text-xl">{av.emoji}</div>
                    <div className="text-[9px] text-slate-300 truncate mt-0.5">{av.label}</div>
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1">
                Bio / Motto
              </label>
              <textarea
                rows={3}
                value={bio}
                onChange={(e) => setBio(e.target.value)}
                placeholder="Share your mathematical aspirations..."
                className="w-full px-3.5 py-2 rounded-xl bg-slate-900 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
              />
            </div>

            <button
              type="submit"
              disabled={profileLoading}
              className="w-full py-2.5 px-4 rounded-xl font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 flex items-center justify-center space-x-2 transition-all shadow-md shadow-amber-500/20"
            >
              <Save className="w-4 h-4" />
              <span>{profileLoading ? 'Saving...' : 'Save Profile Changes'}</span>
            </button>
          </form>
        </div>

        {/* Password Management */}
        <div className="glass-panel p-6 rounded-2xl border border-quest-border space-y-5">
          <div className="flex items-center space-x-2 text-amber-400 font-bold">
            <KeyRound className="w-5 h-5" />
            <span>Password Management</span>
          </div>

          {pwMsg && (
            <div className="p-3 bg-emerald-500/15 border border-emerald-500/30 rounded-xl text-emerald-300 text-xs flex items-center space-x-2">
              <CheckCircle2 className="w-4 h-4 flex-shrink-0" />
              <span>{pwMsg}</span>
            </div>
          )}

          {pwError && (
            <div className="p-3 bg-red-500/15 border border-red-500/30 rounded-xl text-red-300 text-xs flex items-center space-x-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0" />
              <span>{pwError}</span>
            </div>
          )}

          <form onSubmit={handlePasswordSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1">
                Current Password
              </label>
              <input
                type="password"
                required
                value={oldPassword}
                onChange={(e) => setOldPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1">
                New Password (min. 6 characters)
              </label>
              <input
                type="password"
                required
                minLength={6}
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 uppercase mb-1">
                Confirm New Password
              </label>
              <input
                type="password"
                required
                minLength={6}
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-quest-border text-slate-100 text-sm outline-none focus:border-amber-500"
              />
            </div>

            <button
              type="submit"
              disabled={pwLoading}
              className="w-full py-2.5 px-4 rounded-xl font-bold bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center space-x-2 transition-all border border-quest-border mt-4"
            >
              <Lock className="w-4 h-4" />
              <span>{pwLoading ? 'Updating Password...' : 'Update Password'}</span>
            </button>
          </form>
        </div>

      </div>

    </div>
  );
}

