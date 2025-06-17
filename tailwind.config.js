/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./content/**/*.mdx"
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--bg)",
        foreground: "var(--fg)"
      },
      typography: {
        DEFAULT: {
          css: {
            color: 'var(--fg)',
            a: {
              color: 'var(--fg)',
              '&:hover': {
                color: 'var(--fg)',
              },
            },
            h1: {
              color: 'var(--fg)',
            },
            h2: {
              color: 'var(--fg)',
            },
            h3: {
              color: 'var(--fg)',
            },
            h4: {
              color: 'var(--fg)',
            },
            strong: {
              color: 'var(--fg)',
            },
            code: {
              color: 'var(--fg)',
            },
            blockquote: {
              color: 'var(--fg)',
            },
          },
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
} 