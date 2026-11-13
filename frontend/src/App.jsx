import React, { useState } from 'react';
import { AuthProvider, useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import StudentDashboard from './pages/StudentDashboard';
import WorldDetailPage from './pages/WorldDetailPage';
import MissionPlayer from './pages/MissionPlayer';
import LeaderboardPage from './pages/LeaderboardPage';
import ProfilePage from './pages/ProfilePage';
import AdminPage from './pages/AdminPage';

function AppContent() {
  const { user, loading } = useAuth();
  const [currentView, setCurrentView] = useState(() => {
    return localStorage.getItem('mathquest_view') || 'dashboard';
  });
  const [selectedWorldId, setSelectedWorldId] = useState(null);
  const [selectedMissionId, setSelectedMissionId] = useState(null);

  const navigateTo = (view) => {
    localStorage.setItem('mathquest_view', view);
    setCurrentView(view);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-[#0a0e17] flex flex-col items-center justify-center space-y-4">
        <div className="w-12 h-12 border-4 border-amber-500/20 border-t-amber-500 rounded-full animate-spin" />
        <p className="text-slate-400 font-quest text-sm tracking-wider">Awakening MathQuest Realm...</p>
      </div>
    );
  }

  // If not logged in, enforce Login or Register view
  if (!user) {
    return (
      <div className="min-h-screen bg-[#0a0e17]">
        <Navbar currentView={currentView} setCurrentView={navigateTo} />
        {currentView === 'register' ? (
          <RegisterPage onNavigate={navigateTo} />
        ) : (
          <LoginPage onNavigate={navigateTo} />
        )}
      </div>
    );
  }

  const handleSelectWorld = (worldId) => {
    setSelectedWorldId(worldId);
    navigateTo('worldDetail');
  };

  const handleSelectMission = (missionId) => {
    setSelectedMissionId(missionId);
    navigateTo('missionPlayer');
  };

  return (
    <div className="min-h-screen bg-[#0a0e17] flex flex-col">
      <Navbar currentView={currentView} setCurrentView={navigateTo} />
      
      <main className="flex-1 pb-16">
        {currentView === 'dashboard' && (
          <StudentDashboard 
            onNavigate={navigateTo}
            onSelectWorld={handleSelectWorld}
            onSelectMission={handleSelectMission}
          />
        )}

        {currentView === 'worldDetail' && (
          <WorldDetailPage 
            worldId={selectedWorldId}
            onBack={() => navigateTo('dashboard')}
            onSelectMission={handleSelectMission}
          />
        )}

        {currentView === 'missionPlayer' && (
          <MissionPlayer
            missionId={selectedMissionId}
            onBack={() => navigateTo('dashboard')}
            onComplete={() => navigateTo('dashboard')}
          />
        )}

        {currentView === 'leaderboard' && (
          <LeaderboardPage />
        )}

        {currentView === 'profile' && (
          <ProfilePage />
        )}

        {currentView === 'admin' && (
          user?.role === 'admin' ? (
            <AdminPage />
          ) : (
            <StudentDashboard 
              onNavigate={navigateTo}
              onSelectWorld={handleSelectWorld}
              onSelectMission={handleSelectMission}
            />
          )
        )}
      </main>

      <footer className="border-t border-quest-border/60 py-6 text-center text-xs text-slate-500">
        MathQuest &copy; 2026–27 Sindh STREAM Activities • Gamified Mathematics Practice for Grades 11–12
      </footer>
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}
