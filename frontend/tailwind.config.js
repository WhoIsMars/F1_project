/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                f1: {
                    red: '#e10600',
                    black: '#15151e',
                    dark: '#1f1f27',
                    gray: '#38383f',
                    light: '#f3f3f3',
                    green: '#4caf50', // For best sectors
                    orange: '#ff9800', // For personal best
                    purple: '#e040fb', // For fastest lap
                }
            },
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
