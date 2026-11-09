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
  const [currentView, setCurrentView] = useState('dashboard');
  const [selectedWorldId, setSelectedWorldId] = useState(null);
  const [selectedMissionId, setSelectedMissionId] = useState(null);

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
        <Navbar currentView={currentView} setCurrentView={setCurrentView} />
        {currentView === 'register' ? (
          <RegisterPage onNavigate={setCurrentView} />
        ) : (
          <LoginPage onNavigate={setCurrentView} />
        )}
      </div>
    );
  }

  const handleSelectWorld = (worldId) => {
    setSelectedWorldId(worldId);
    setCurrentView('worldDetail');
  };

  const handleSelectMission = (missionId) => {
    setSelectedMissionId(missionId);
    setCurrentView('missionPlayer');
  };

  return (
    <div className="min-h-screen bg-[#0a0e17] flex flex-col">
      <Navbar currentView={currentView} setCurrentView={setCurrentView} />
      
      <main className="flex-1 pb-16">
        {currentView === 'dashboard' && (
          <StudentDashboard 
            onNavigate={setCurrentView}
            onSelectWorld={handleSelectWorld}
            onSelectMission={handleSelectMission}
          />
        )}

        {currentView === 'worldDetail' && (
          <WorldDetailPage 
            worldId={selectedWorldId}
            onBack={() => setCurrentView('dashboard')}
            onSelectMission={handleSelectMission}
          />
        )}

        {currentView === 'missionPlayer' && (
          <MissionPlayer
            missionId={selectedMissionId}
            onBack={() => setCurrentView('dashboard')}
            onComplete={() => setCurrentView('dashboard')}
          />
        )}

        {currentView === 'leaderboard' && (
          <LeaderboardPage />
        )}

        {currentView === 'profile' && (
          <ProfilePage />
        )}

        {currentView === 'admin' && (
          <AdminPage />
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
