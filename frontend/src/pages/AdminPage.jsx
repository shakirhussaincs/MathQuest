import React, { useState, useEffect } from 'react';
import { userApi } from '../api/client';
import { Shield, User, CheckCircle2, XCircle, Search, Filter } from 'lucide-react';

export default function AdminPage() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [search, setSearch] = useState('');
  const [roleFilter, setRoleFilter] = useState('all');

  const loadUsers = async () => {
    setLoading(true);
    try {
      const data = await userApi.listUsers();
      setUsers(data);
    } catch (err) {
      setError(err.message || 'Failed to load user list.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadUsers();
  }, []);

  const handleRoleChange = async (userId, newRole) => {
    try {
      await userApi.updateUserRole(userId, newRole);
      setUsers(users.map(u => u.id === userId ? { ...u, role: newRole } : u));
    } catch (err) {
      alert(`Failed to update role: ${err.message}`);
    }
  };

  const handleStatusToggle = async (userId, currentStatus) => {
    try {
      await userApi.updateUserStatus(userId, !currentStatus);
      setUsers(users.map(u => u.id === userId ? { ...u, is_active: !currentStatus } : u));
    } catch (err) {
      alert(`Failed to toggle account: ${err.message}`);
    }
  };

  const filtered = users.filter(u => {
    const matchesSearch = u.display_name.toLowerCase().includes(search.toLowerCase()) ||
                          u.email.toLowerCase().includes(search.toLowerCase());
    const matchesRole = roleFilter === 'all' || u.role === roleFilter;
    return matchesSearch && matchesRole;
  });

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 sm:px-6 space-y-6">
      
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="font-quest text-2xl sm:text-3xl font-extrabold text-white flex items-center space-x-2">
            <Shield className="w-6 h-6 text-purple-400" />
            <span>Administrator Control Console</span>
          </h1>
          <p className="text-slate-400 text-xs sm:text-sm mt-1">
            Manage user accounts, grade assignments, and role-based access control
          </p>
        </div>

        <button
          onClick={loadUsers}
          className="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-quest-border self-start sm:self-auto"
        >
          Refresh User Directory
        </button>
      </div>

      {/* Filter and Search */}
      <div className="glass-panel p-4 rounded-2xl border border-quest-border flex flex-col sm:flex-row gap-3">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by name or email..."
            className="w-full pl-10 pr-4 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs sm:text-sm text-slate-100 outline-none focus:border-purple-500"
          />
        </div>

        <select
          value={roleFilter}
          onChange={(e) => setRoleFilter(e.target.value)}
          className="px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs sm:text-sm text-slate-100 outline-none focus:border-purple-500"
        >
          <option value="all">All Roles</option>
          <option value="student">Students</option>
          <option value="teacher">Teachers</option>
          <option value="admin">Administrators</option>
        </select>
      </div>

      {/* Table */}
      <div className="glass-panel rounded-2xl border border-quest-border overflow-hidden">
        {loading ? (
          <div className="p-12 text-center text-slate-400">Loading directory...</div>
        ) : error ? (
          <div className="p-8 text-center text-red-400">{error}</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs sm:text-sm">
              <thead className="bg-slate-900/80 border-b border-quest-border text-slate-400 uppercase text-[11px] font-semibold">
                <tr>
                  <th className="py-3 px-4">User</th>
                  <th className="py-3 px-4">Role</th>
                  <th className="py-3 px-4">Grade</th>
                  <th className="py-3 px-4">Status</th>
                  <th className="py-3 px-4 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-quest-border/60">
                {filtered.map((u) => (
                  <tr key={u.id} className="hover:bg-slate-800/40 transition-colors">
                    <td className="py-3 px-4">
                      <div className="font-bold text-white">{u.display_name}</div>
                      <div className="text-[11px] text-slate-400">{u.email}</div>
                    </td>
                    <td className="py-3 px-4">
                      <select
                        value={u.role}
                        onChange={(e) => handleRoleChange(u.id, e.target.value)}
                        className="py-1 px-2 rounded-lg bg-slate-900 border border-quest-border text-xs text-slate-200 outline-none"
                      >
                        <option value="student">student</option>
                        <option value="teacher">teacher</option>
                        <option value="admin">admin</option>
                      </select>
                    </td>
                    <td className="py-3 px-4">
                      {u.grade ? (
                        <span className="px-2 py-0.5 rounded bg-emerald-500/15 text-emerald-400 text-xs font-semibold">
                          Grade {u.grade}
                        </span>
                      ) : (
                        <span className="text-slate-500 text-xs">N/A</span>
                      )}
                    </td>
                    <td className="py-3 px-4">
                      {u.is_active ? (
                        <span className="inline-flex items-center space-x-1 text-emerald-400 text-xs font-semibold">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Active</span>
                        </span>
                      ) : (
                        <span className="inline-flex items-center space-x-1 text-red-400 text-xs font-semibold">
                          <XCircle className="w-3.5 h-3.5" />
                          <span>Disabled</span>
                        </span>
                      )}
                    </td>
                    <td className="py-3 px-4 text-right">
                      <button
                        onClick={() => handleStatusToggle(u.id, u.is_active)}
                        className={`px-3 py-1 rounded-lg text-xs font-semibold transition-colors ${
                          u.is_active
                            ? 'bg-red-500/15 text-red-300 hover:bg-red-500/25 border border-red-500/30'
                            : 'bg-emerald-500/15 text-emerald-300 hover:bg-emerald-500/25 border border-emerald-500/30'
                        }`}
                      >
                        {u.is_active ? 'Deactivate' : 'Activate'}
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

    </div>
  );
}

