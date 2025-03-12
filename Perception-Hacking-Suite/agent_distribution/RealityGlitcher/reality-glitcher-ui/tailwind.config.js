/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'spin-slow': 'spin 8s linear infinite',
        'spin-reverse': 'spin-reverse 6s linear infinite',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glitch-text': 'glitch 2s infinite',
        'flicker': 'flicker 3s linear infinite',
      },
      keyframes: {
        'spin-reverse': {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(-360deg)' },
        },
        'glitch': {
          '0%, 100%': { transform: 'translateX(0)' },
          '5%, 15%, 25%, 35%, 45%, 55%, 65%, 75%, 85%, 95%': { transform: 'translateX(-1px)' },
          '10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%': { transform: 'translateX(1px)' },
        },
        'flicker': {
          '0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100%': { opacity: '0.99' },
          '20%, 21.999%, 63%, 63.999%, 65%, 69.999%': { opacity: '0.4' },
        },
      },
      perspective: {
        '500': '500px',
      },
      transformOrigin: {
        'center': 'center',
      },
      transitionProperty: {
        'backdrop-filter': 'backdrop-filter',
      },
      backgroundImage: {
        'cyber-grid': `
          linear-gradient(rgba(57, 255, 20, 0.1) 1px, transparent 1px),
          linear-gradient(90deg, rgba(57, 255, 20, 0.1) 1px, transparent 1px)
        `,
      },
    },
  },
  plugins: [],
}