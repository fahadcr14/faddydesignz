/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./web/templates/**/*.html",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins'],
      },}
  },
  darkMode: "class",
  plugins: [require("tw-elements/dist/plugin.cjs")],
};
