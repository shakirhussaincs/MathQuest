import React, { useState, useEffect } from 'react';
import { userApi, dashboardApi, adminApi } from '../api/client';
import { 
  Shield, 
  Users, 
  Layers, 
  Server, 
  Search, 
  Filter, 
  CheckCircle2, 
  XCircle, 
  PlusCircle, 
  RefreshCw, 
  AlertCircle,
  GraduationCap,
  Sparkles,
  BookOpen,
  Compass
} from 'lucide-react';

export default function AdminPage() {
  const [activeTab, setActiveTab] = useState('overview'); // 'overview', 'users', 'curriculum'
  
  // Overview state
  const [adminOverview, setAdminOverview] = useState(null);
  const [overviewLoading, setOverviewLoading] = useState(true);

  // Users state
  const [users, setUsers] = useState([]);
  const [usersLoading, setUsersLoading] = useState(false);
  const [search, setSearch] = useState('');
  const [roleFilter, setRoleFilter] = useState('all');

  // Worlds for curriculum builder dropdowns
  const [allWorlds, setAllWorlds] = useState([]);
  
  // Forms state for curriculum builder
  const [worldForm, setWorldForm] = useState({
    title: '',
    description: '',
    grade: 11,
    icon: 'compass',
    theme_color: 'purple',
    display_order: 1
  });
  const [topicForm, setTopicForm] = useState({
    world_id: '',
    title: '',
    description: '',
    learning_objectives: '',
    display_order: 1
  });
  const [missionForm, setMissionForm] = useState({
    topic_id: '',
    title: '',
    instructions: '',
    category: 'practice',
    difficulty: 'easy',
    question_count: 5,
    xp_reward: 20,
    is_boss: false,
    display_order: 1
  });

  const [formMsg, setFormMsg] = useState({ type: '', text: '' });
  const [formLoading, setFormLoading] = useState(false);

  const loadOverview = async () => {
    setOverviewLoading(true);
    try {
      const data = await dashboardApi.getAdminDashboard();
      setAdminOverview(data);
    } catch (err) {
      console.error('Failed to load admin overview', err);
    } finally {
      setOverviewLoading(false);
    }
  };

  const loadUsers = async () => {
    setUsersLoading(true);
    try {
      const data = await userApi.listUsers();
      setUsers(data);
    } catch (err) {
      alert(`Failed to load users: ${err.message}`);
    } finally {
      setUsersLoading(false);
    }
  };

  const loadWorldsForBuilder = async () => {
    try {
      const data = await dashboardApi.getWorlds();
      setAllWorlds(data);
      if (data.length > 0 && !topicForm.world_id) {
        setTopicForm(prev => ({ ...prev, world_id: data[0].id }));
      }
    } catch (err) {
      console.error('Failed to load worlds', err);
    }
  };

  useEffect(() => {
    loadOverview();
    loadUsers();
    loadWorldsForBuilder();
  }, []);

  const handleRoleChange = async (userId, newRole) => {
    try {
      await userApi.updateUserRole(userId, newRole);
      setUsers(users.map(u => u.id === userId ? { ...u, role: newRole } : u));
      loadOverview();
    } catch (err) {
      alert(`Failed to update role: ${err.message}`);
    }
  };

  const handleStatusToggle = async (userId, currentStatus) => {
    try {
      await userApi.updateUserStatus(userId, !currentStatus);
      setUsers(users.map(u => u.id === userId ? { ...u, is_active: !currentStatus } : u));
      loadOverview();
    } catch (err) {
      alert(`Failed to toggle account: ${err.message}`);
    }
  };

  // Content Creation Handlers
  const handleCreateWorld = async (e) => {
    e.preventDefault();
    setFormLoading(true);
    setFormMsg({ type: '', text: '' });
    try {
      await adminApi.createWorld({
        ...worldForm,
        grade: Number(worldForm.grade),
        display_order: Number(worldForm.display_order)
      });
      setFormMsg({ type: 'success', text: `World "${worldForm.title}" created successfully!` });
      setWorldForm({
        title: '',
        description: '',
        grade: 11,
        icon: 'compass',
        theme_color: 'purple',
        display_order: 1
      });
      loadWorldsForBuilder();
      loadOverview();
    } catch (err) {
      setFormMsg({ type: 'error', text: err.message || 'Failed to create world.' });
    } finally {
      setFormLoading(false);
    }
  };

  const handleCreateTopic = async (e) => {
    e.preventDefault();
    if (!topicForm.world_id) {
      alert('Please select a target world.');
      return;
    }
    setFormLoading(true);
    setFormMsg({ type: '', text: '' });
    try {
      const objectivesList = topicForm.learning_objectives
        ? topicForm.learning_objectives.split('\n').map(s => s.trim()).filter(Boolean)
        : [];

      await adminApi.createTopic(topicForm.world_id, {
        title: topicForm.title,
        description: topicForm.description,
        learning_objectives: objectivesList,
        display_order: Number(topicForm.display_order)
      });
      setFormMsg({ type: 'success', text: `Topic "${topicForm.title}" added successfully!` });
      setTopicForm(prev => ({
        ...prev,
        title: '',
        description: '',
        learning_objectives: '',
        display_order: 1
      }));
      loadWorldsForBuilder();
      loadOverview();
    } catch (err) {
      setFormMsg({ type: 'error', text: err.message || 'Failed to create topic.' });
    } finally {
      setFormLoading(false);
    }
  };

  const handleCreateMission = async (e) => {
    e.preventDefault();
    if (!missionForm.topic_id) {
      alert('Please select a target topic.');
      return;
    }
    setFormLoading(true);
    setFormMsg({ type: '', text: '' });
    try {
      await adminApi.createMission(missionForm.topic_id, {
        ...missionForm,
        question_count: Number(missionForm.question_count),
        xp_reward: Number(missionForm.xp_reward),
        display_order: Number(missionForm.display_order)
      });
      setFormMsg({ type: 'success', text: `Mission "${missionForm.title}" added successfully!` });
      setMissionForm(prev => ({
        ...prev,
        title: '',
        instructions: '',
        display_order: 1
      }));
      loadWorldsForBuilder();
      loadOverview();
    } catch (err) {
      setFormMsg({ type: 'error', text: err.message || 'Failed to create mission.' });
    } finally {
      setFormLoading(false);
    }
  };

  const filteredUsers = users.filter(u => {
    const matchesSearch = u.display_name.toLowerCase().includes(search.toLowerCase()) ||
                          u.email.toLowerCase().includes(search.toLowerCase());
    const matchesRole = roleFilter === 'all' || u.role === roleFilter;
    return matchesSearch && matchesRole;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 space-y-8">
      
      {/* Header Banner */}
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-purple-500/30 bg-gradient-to-r from-purple-950/40 via-slate-900 to-slate-950 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="flex items-start space-x-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-600 flex items-center justify-center text-white shadow-xl shadow-purple-500/20 border border-purple-400/40">
              <Shield className="w-9 h-9" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="px-2.5 py-0.5 text-[11px] font-bold rounded-md bg-purple-500/20 text-purple-300 border border-purple-500/30 uppercase tracking-wider">
                  System Administration
                </span>
                <span className="text-xs text-slate-400">Sindh STREAM Platform Operations</span>
              </div>
              <h1 className="font-quest text-2xl sm:text-3xl font-extrabold text-white mt-1">
                Command Console
              </h1>
              <p className="text-slate-300 text-xs sm:text-sm mt-1 max-w-2xl">
                Platform statistics, role management, user account status, and mathematics curriculum creation.
              </p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <div className="bg-slate-900/90 p-1.5 rounded-2xl border border-purple-500/30 flex items-center space-x-1 self-start md:self-auto">
            <button
              onClick={() => setActiveTab('overview')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                activeTab === 'overview'
                  ? 'bg-purple-600 text-white shadow-md shadow-purple-500/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Overview
            </button>
            <button
              onClick={() => setActiveTab('users')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                activeTab === 'users'
                  ? 'bg-purple-600 text-white shadow-md shadow-purple-500/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Users Directory
            </button>
            <button
              onClick={() => setActiveTab('curriculum')}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                activeTab === 'curriculum'
                  ? 'bg-purple-600 text-white shadow-md shadow-purple-500/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Curriculum Builder
            </button>
          </div>
        </div>
      </div>

      {/* TAB 1: OVERVIEW & PLATFORM STATS */}
      {activeTab === 'overview' && (
        <div className="space-y-6">
          {/* User Metrics */}
          <div>
            <h2 className="text-sm font-bold text-slate-300 uppercase tracking-wider mb-3 flex items-center space-x-2">
              <Users className="w-4 h-4 text-purple-400" />
              <span>User Base Metrics</span>
            </h2>
            <div className="grid grid-cols-2 lg:grid-cols-5 gap-3.5">
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-white">{adminOverview?.users?.total ?? 0}</div>
                <div className="text-xs text-slate-400">Total Accounts</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-amber-400">{adminOverview?.users?.students ?? 0}</div>
                <div className="text-xs text-slate-400">Students</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-cyan-400">{adminOverview?.users?.teachers ?? 0}</div>
                <div className="text-xs text-slate-400">Educators</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-purple-400">{adminOverview?.users?.admins ?? 0}</div>
                <div className="text-xs text-slate-400">Administrators</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-emerald-400">{adminOverview?.users?.active ?? 0}</div>
                <div className="text-xs text-slate-400">Active Status</div>
              </div>
            </div>
          </div>

          {/* Curriculum Stats */}
          <div>
            <h2 className="text-sm font-bold text-slate-300 uppercase tracking-wider mb-3 flex items-center space-x-2">
              <Layers className="w-4 h-4 text-purple-400" />
              <span>Curriculum Content Summary</span>
            </h2>
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-3.5">
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-white">{adminOverview?.curriculum?.total_worlds ?? 0}</div>
                <div className="text-xs text-slate-400">Realms (Worlds)</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-white">{adminOverview?.curriculum?.total_topics ?? 0}</div>
                <div className="text-xs text-slate-400">Topics</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-white">{adminOverview?.curriculum?.total_missions ?? 0}</div>
                <div className="text-xs text-slate-400">Missions</div>
              </div>
              <div className="glass-panel p-4 rounded-2xl border border-quest-border">
                <div className="text-2xl font-extrabold text-white">{adminOverview?.curriculum?.total_questions ?? 0}</div>
                <div className="text-xs text-slate-400">Active Questions</div>
              </div>
            </div>
          </div>

          {/* Grade 1-12 Coverage Matrix */}
          <div className="glass-panel rounded-2xl border border-quest-border p-6 space-y-3">
            <h3 className="text-sm font-bold text-white flex items-center space-x-2">
              <BookOpen className="w-4 h-4 text-purple-400" />
              <span>Grade 1–12 Curriculum Inventory</span>
            </h3>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs">
                <thead className="bg-slate-900/80 border-b border-quest-border text-slate-400 uppercase text-[10px]">
                  <tr>
                    <th className="py-2.5 px-3">Grade</th>
                    <th className="py-2.5 px-3">Worlds</th>
                    <th className="py-2.5 px-3">Topics</th>
                    <th className="py-2.5 px-3">Missions</th>
                    <th className="py-2.5 px-3">Questions</th>
                    <th className="py-2.5 px-3">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-quest-border/60">
                  {adminOverview?.curriculum?.grade_matrix?.map((row) => (
                    <tr key={row.grade} className="hover:bg-slate-800/40">
                      <td className="py-2 px-3 font-semibold text-white">Grade {row.grade}</td>
                      <td className="py-2 px-3 text-slate-300">{row.worlds}</td>
                      <td className="py-2 px-3 text-slate-300">{row.topics}</td>
                      <td className="py-2 px-3 text-slate-300">{row.missions}</td>
                      <td className="py-2 px-3 text-slate-300">{row.questions}</td>
                      <td className="py-2 px-3">
                        {row.questions > 0 ? (
                          <span className="text-[10px] text-emerald-400 font-semibold">Active ({row.questions} Qs)</span>
                        ) : (
                          <span className="text-[10px] text-slate-500">Unseeded</span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Platform Health Status */}
          <div className="glass-panel p-5 rounded-2xl border border-quest-border flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-purple-500/15 text-purple-400 flex items-center justify-center">
                <Server className="w-5 h-5" />
              </div>
              <div>
                <div className="text-sm font-bold text-white">Infrastructure Status</div>
                <div className="text-xs text-slate-400">
                  Environment: <strong className="text-purple-300">{adminOverview?.system?.environment || 'production'}</strong> • Database: <strong className="text-emerald-400">{adminOverview?.system?.database_status || 'connected'}</strong>
                </div>
              </div>
            </div>
            <div className="text-xs text-slate-400">
              Active Attempt Sessions: <strong className="text-white">{adminOverview?.system?.active_attempt_sessions ?? 0}</strong>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: USER DIRECTORY & ROLE MANAGEMENT */}
      {activeTab === 'users' && (
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <h2 className="text-base font-bold text-white">User Accounts & Access Control</h2>
              <p className="text-xs text-slate-400">Update user roles, academic grade alignment, and account activation</p>
            </div>
            <button
              onClick={loadUsers}
              className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-quest-border flex items-center space-x-1.5 self-start sm:self-auto"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              <span>Refresh List</span>
            </button>
          </div>

          {/* Search & Filter */}
          <div className="glass-panel p-3.5 rounded-2xl border border-quest-border flex flex-col sm:flex-row gap-3">
            <div className="relative flex-1">
              <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-2.5" />
              <input
                type="text"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder="Search by name or email..."
                className="w-full pl-10 pr-4 py-1.5 rounded-xl bg-slate-900 border border-quest-border text-xs sm:text-sm text-slate-100 outline-none focus:border-purple-500"
              />
            </div>

            <select
              value={roleFilter}
              onChange={(e) => setRoleFilter(e.target.value)}
              className="px-3 py-1.5 rounded-xl bg-slate-900 border border-quest-border text-xs sm:text-sm text-slate-100 outline-none focus:border-purple-500"
            >
              <option value="all">All Roles</option>
              <option value="student">Students</option>
              <option value="teacher">Teachers</option>
              <option value="admin">Administrators</option>
            </select>
          </div>

          {/* Users Table */}
          <div className="glass-panel rounded-2xl border border-quest-border overflow-hidden">
            {usersLoading ? (
              <div className="p-12 text-center text-slate-400 text-sm">Loading users directory...</div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs">
                  <thead className="bg-slate-900/80 border-b border-quest-border text-slate-400 uppercase text-[10px] font-semibold">
                    <tr>
                      <th className="py-3 px-4">User</th>
                      <th className="py-3 px-4">Role</th>
                      <th className="py-3 px-4">Grade</th>
                      <th className="py-3 px-4">Status</th>
                      <th className="py-3 px-4 text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-quest-border/60">
                    {filteredUsers.map((u) => (
                      <tr key={u.id} className="hover:bg-slate-800/40 transition-colors">
                        <td className="py-3 px-4">
                          <div className="font-bold text-white">{u.display_name}</div>
                          <div className="text-[11px] text-slate-400">{u.email}</div>
                        </td>
                        <td className="py-3 px-4">
                          <select
                            value={u.role}
                            onChange={(e) => handleRoleChange(u.id, e.target.value)}
                            className="py-1 px-2 rounded-lg bg-slate-900 border border-quest-border text-xs text-slate-200 outline-none focus:border-purple-500"
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
      )}

      {/* TAB 3: CURRICULUM BUILDER */}
      {activeTab === 'curriculum' && (
        <div className="space-y-6">
          <div>
            <h2 className="text-base font-bold text-white">Mathematics Curriculum Creator</h2>
            <p className="text-xs text-slate-400">Directly create new learning worlds, topics, and missions into the database</p>
          </div>

          {formMsg.text && (
            <div className={`p-4 rounded-xl border text-xs font-semibold flex items-center space-x-2 ${
              formMsg.type === 'success'
                ? 'bg-emerald-500/15 border-emerald-500/30 text-emerald-300'
                : 'bg-red-500/15 border-red-500/30 text-red-300'
            }`}>
              {formMsg.type === 'success' ? <CheckCircle2 className="w-4 h-4" /> : <AlertCircle className="w-4 h-4" />}
              <span>{formMsg.text}</span>
            </div>
          )}

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            {/* 1. Create World Form */}
            <form onSubmit={handleCreateWorld} className="glass-panel p-5 rounded-2xl border border-quest-border space-y-4">
              <div className="flex items-center space-x-2 pb-3 border-b border-quest-border">
                <Compass className="w-4 h-4 text-purple-400" />
                <h3 className="text-sm font-bold text-white">1. Create World</h3>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">World Title</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Geometry Citadel"
                  value={worldForm.title}
                  onChange={(e) => setWorldForm({ ...worldForm, title: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Description</label>
                <textarea
                  required
                  rows="2"
                  placeholder="Summary of mathematical domain..."
                  value={worldForm.description}
                  onChange={(e) => setWorldForm({ ...worldForm, description: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Grade (1–12)</label>
                  <select
                    value={worldForm.grade}
                    onChange={(e) => setWorldForm({ ...worldForm, grade: Number(e.target.value) })}
                    className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                  >
                    {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].map(g => (
                      <option key={g} value={g}>Grade {g}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Order</label>
                  <input
                    type="number"
                    min="1"
                    value={worldForm.display_order}
                    onChange={(e) => setWorldForm({ ...worldForm, display_order: Number(e.target.value) })}
                    className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={formLoading}
                className="w-full py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white transition-colors"
              >
                Create World
              </button>
            </form>

            {/* 2. Create Topic Form */}
            <form onSubmit={handleCreateTopic} className="glass-panel p-5 rounded-2xl border border-quest-border space-y-4">
              <div className="flex items-center space-x-2 pb-3 border-b border-quest-border">
                <BookOpen className="w-4 h-4 text-purple-400" />
                <h3 className="text-sm font-bold text-white">2. Create Topic</h3>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Target World</label>
                <select
                  value={topicForm.world_id}
                  onChange={(e) => setTopicForm({ ...topicForm, world_id: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                >
                  <option value="">Select a World...</option>
                  {allWorlds.map((w) => (
                    <option key={w.id} value={w.id}>
                      {w.title} (Grade {w.grade})
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Topic Title</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Conic Sections"
                  value={topicForm.title}
                  onChange={(e) => setTopicForm({ ...topicForm, title: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Description</label>
                <input
                  type="text"
                  placeholder="Topic summary..."
                  value={topicForm.description}
                  onChange={(e) => setTopicForm({ ...topicForm, description: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Learning Objectives (One per line)</label>
                <textarea
                  rows="2"
                  placeholder="Calculate eccentricity..."
                  value={topicForm.learning_objectives}
                  onChange={(e) => setTopicForm({ ...topicForm, learning_objectives: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <button
                type="submit"
                disabled={formLoading}
                className="w-full py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white transition-colors"
              >
                Add Topic
              </button>
            </form>

            {/* 3. Create Mission Form */}
            <form onSubmit={handleCreateMission} className="glass-panel p-5 rounded-2xl border border-quest-border space-y-4">
              <div className="flex items-center space-x-2 pb-3 border-b border-quest-border">
                <Sparkles className="w-4 h-4 text-purple-400" />
                <h3 className="text-sm font-bold text-white">3. Create Mission</h3>
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Target Topic ID</label>
                <input
                  type="number"
                  required
                  placeholder="Enter numeric Topic ID"
                  value={missionForm.topic_id}
                  onChange={(e) => setMissionForm({ ...missionForm, topic_id: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Mission Title</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Parabola Challenge"
                  value={missionForm.title}
                  onChange={(e) => setMissionForm({ ...missionForm, title: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Instructions</label>
                <textarea
                  required
                  rows="2"
                  placeholder="Instructions for students..."
                  value={missionForm.instructions}
                  onChange={(e) => setMissionForm({ ...missionForm, instructions: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">Difficulty</label>
                  <select
                    value={missionForm.difficulty}
                    onChange={(e) => setMissionForm({ ...missionForm, difficulty: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                  >
                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>
                    <option value="boss">Boss</option>
                  </select>
                </div>
                <div>
                  <label className="block text-[11px] font-semibold text-slate-300 uppercase mb-1">XP Reward</label>
                  <input
                    type="number"
                    min="5"
                    value={missionForm.xp_reward}
                    onChange={(e) => setMissionForm({ ...missionForm, xp_reward: Number(e.target.value) })}
                    className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-quest-border text-xs text-white outline-none focus:border-purple-500"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={formLoading}
                className="w-full py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white transition-colors"
              >
                Add Mission
              </button>
            </form>

          </div>
        </div>
      )}

    </div>
  );
}
