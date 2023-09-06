/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Templates within theme app (e.g. base.html)
    '../templates/**/*.html',
    // Templates in other apps
    '../social_posts/templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

