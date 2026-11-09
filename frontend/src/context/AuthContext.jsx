import React, { createContext, useContext, useState, useEffect } from 'react';
import { authApi, userApi } from '../api/client';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('mathquest_token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadUser() {
      if (token) {
        try {
          const profile = await userApi.getProfile();
          setUser(profile);
        } catch (err) {
          console.error("Session expired or invalid token:", err);
          logout();
        }
      }
      setLoading(false);
    }
    loadUser();
  }, [token]);

  const login = async (email, password) => {
    const data = await authApi.login(email, password);
    localStorage.setItem('mathquest_token', data.access_token);
    setToken(data.access_token);
    setUser(data.user);
    return data.user;
  };

  const register = async (payload) => {
    const data = await authApi.register(payload);
    localStorage.setItem('mathquest_token', data.access_token);
    setToken(data.access_token);
    setUser(data.user);
    return data.user;
  };

  const logout = () => {
    try {
      authApi.logout().catch(() => {});
    } finally {
      localStorage.removeItem('mathquest_token');
      setToken(null);
      setUser(null);
    }
  };

  const refreshProfile = async () => {
    if (token) {
      const updated = await userApi.getProfile();
      setUser(updated);
      return updated;
    }
  };

  return (
    <AuthContext.Provider value={{
      user,
      token,
      loading,
      login,
      register,
      logout,
      refreshProfile,
      isAuthenticated: !!user,
      isStudent: user?.role === 'student',
      isTeacher: user?.role === 'teacher',
      isAdmin: user?.role === 'admin',
    }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);

