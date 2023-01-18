/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './mainweb/templates/**/*.html',
    './node_modules/flowbite/**/*.js',
    './components/**/*.{html,py}',
    './pages/**/*.{html,py}',

  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
