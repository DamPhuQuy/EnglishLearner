/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ielts: {
          listening: '#3b82f6', // blue
          reading: '#10b981',   // emerald
          writing: '#f59e0b',   // amber
          speaking: '#ec4899',  // pink
          dark: '#0f172a',
          surface: '#1e293b',
          border: '#334155',
        }
      }
    },
  },
  plugins: [],
}
