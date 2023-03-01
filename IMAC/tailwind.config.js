/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./mainweb/templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        mainBrown: "#AF4B21",
        mainCream: "#D8D5CA",
        mainDarkGreen: "#0A262A",
        mainGray: "#0A262A40",
      },
    },
  },
  plugins: [require("flowbite/plugin"), require("@tailwindcss/line-clamp")],
};
