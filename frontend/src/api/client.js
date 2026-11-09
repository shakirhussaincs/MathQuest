const API_BASE = '/api/v1';

export async function apiRequest(endpoint, options = {}) {
  const token = localStorage.getItem('mathquest_token');
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers,
  });

  const contentType = response.headers.get('content-type');
  const data = (contentType && contentType.includes('application/json')) 
    ? await response.json() 
    : await response.text();

  if (!response.ok) {
    const errorMsg = data.detail || data.message || 'An error occurred during the request.';
    throw new Error(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg));
  }

  return data;
}

// Auth API
export const authApi = {
  login: (email, password) => apiRequest('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password })
  }),
  register: (payload) => apiRequest('/auth/register', {
    method: 'POST',
    body: JSON.stringify(payload)
  }),
  logout: () => apiRequest('/auth/logout', { method: 'POST' }),
  forgotPassword: (email) => apiRequest('/auth/forgot-password', {
    method: 'POST',
    body: JSON.stringify({ email })
  }),
  resetPassword: (reset_token, new_password) => apiRequest('/auth/reset-password', {
    method: 'POST',
    body: JSON.stringify({ reset_token, new_password })
  })
};

// User Profile API
export const userApi = {
  getProfile: () => apiRequest('/users/me'),
  updateProfile: (data) => apiRequest('/users/me', {
    method: 'PATCH',
    body: JSON.stringify(data)
  }),
  changePassword: (old_password, new_password) => apiRequest('/users/me/change-password', {
    method: 'POST',
    body: JSON.stringify({ old_password, new_password })
  }),
  listUsers: () => apiRequest('/users/'),
  updateUserRole: (userId, role) => apiRequest(`/users/${userId}/role`, {
    method: 'PATCH',
    body: JSON.stringify({ role })
  }),
  updateUserStatus: (userId, is_active) => apiRequest(`/users/${userId}/status`, {
    method: 'PATCH',
    body: JSON.stringify({ is_active })
  })
};

// Dashboard & Curriculum API
export const dashboardApi = {
  getStudentDashboard: () => apiRequest('/dashboard/student'),
  getWorlds: (grade) => apiRequest(`/worlds/${grade ? `?grade=${grade}` : ''}`),
  getWorldDetail: (worldId) => apiRequest(`/worlds/${worldId}`),
};

// Mission & Question Solving API
export const missionApi = {
  getMission: (missionId) => apiRequest(`/missions/${missionId}`),
  submitAttempt: (missionId, questionId, submittedAnswer) => apiRequest(`/missions/${missionId}/attempt`, {
    method: 'POST',
    body: JSON.stringify({
      question_id: questionId,
      submitted_answer: submittedAnswer
    })
  }),
  completeMission: (missionId) => apiRequest(`/missions/${missionId}/complete`, {
    method: 'POST'
  })
};
