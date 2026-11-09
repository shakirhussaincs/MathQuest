/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        quest: {
          dark: '#0a0e17',
          surface: '#131b2e',
          card: '#1a233a',
          border: '#2a3655',
          gold: '#f59e0b',
          amber: '#d97706',
          cyan: '#06b6d4',
          purple: '#8b5cf6',
          emerald: '#10b981',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

