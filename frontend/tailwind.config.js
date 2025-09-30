/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // 🔹 important pour utiliser la classe 'dark'
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
