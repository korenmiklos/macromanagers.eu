module.exports = {
  content: ['./_layouts/**/*.html', './_includes/**/*.html', './**/*.html', './*.html'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: "Brockmann,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji",
        mono: "DM Mono,ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas",
      },
      maxWidth: {
        '7xl': '78rem',
      },
      fontSize: {
        '6xl': '3.5rem',
      },
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'white': '#ffffff',
        'black': '#000000',
        'red': '#E61E25',
        'blue': '#1D1D40',
        'dark': '#232324',
        'gray-1': '#5D5A88',
        'gray-2': '#747297', //'#9795B5',
        'gray-3': '#D4D2E3',
        'gray-4': '#9795B5',
      },
      boxShadow: {
        'dropdown': '4px 10px 35px 0px rgba(151, 149, 181, 0.3)',
      }
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require('@tailwindcss/aspect-ratio'),
  ],
};

