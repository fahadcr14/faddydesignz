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
  safelist: [
    'animate-[fade-in_1s_ease-in-out]',
    'animate-[fade-in-down_1s_ease-in-out]',
    'animate-[fade-in-up_1s_ease-in-out]',
    'animate-[slide-in-right_1s_ease-in-out]',
    'animate-[slide-in-left_1s_ease-in-out]',
    'animate-[fade-in-left_1s_ease-in-out]',
    'animate-[fade-in_1s_ease-in-out]',
    'animate-[fade-in-right_1s_ease-in-out]',
    'animate-[fade-in-left_1s_ease-in-out]',

    'animate-[fade-out_1s_ease-in-out]',
    'animate-[slide-left_1s_ease-in-out]',
    'animate-[slide-right_1s_ease-in-out]',
    'animate-[slide-left_1s_ease-in-out]',
    'animate-[slide-up_1s_ease-in-out]',
    'animate-[slide-down_1s_ease-in-out]',
    // Add other animation classes here as needed
  ],
};
