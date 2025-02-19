const animate = require("tailwindcss-animate")

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  safelist: ["dark"],
  prefix: "",
  
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}", 
  ],
  
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        // NEW: Neon tokens for extra bold, cyberpunk vibes.
        neon: {
          DEFAULT: "hsl(var(--neon))",
          light: "hsl(var(--neon-light))",
          dark: "hsl(var(--neon-dark))",
        },
      },
      borderRadius: {
        xl: "calc(var(--radius) + 4px)",
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: 0 },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: 0 },
        },
        "collapsible-down": {
          from: { height: 0 },
          to: { height: 'var(--radix-collapsible-content-height)' },
        },
        "collapsible-up": {
          from: { height: 'var(--radix-collapsible-content-height)' },
          to: { height: 0 },
        },
        // NEW: Neon flicker for a pulsating glow effect.
        "neon-flicker": {
          "0%, 100%": { filter: "brightness(1)", textShadow: "0 0 8px hsl(var(--neon))" },
          "50%": { filter: "brightness(1.5)", textShadow: "0 0 16px hsl(var(--neon))" },
        },
        // NEW: Glitch effect for a digital distortion look.
        "glitch": {
          "0%": { clipPath: "inset(0 0 0 0)" },
          "20%": { clipPath: "inset(10% 0 85% 0)" },
          "40%": { clipPath: "inset(20% 0 65% 0)" },
          "60%": { clipPath: "inset(30% 0 35% 0)" },
          "80%": { clipPath: "inset(40% 0 15% 0)" },
          "100%": { clipPath: "inset(0 0 0 0)" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
        "collapsible-down": "collapsible-down 0.2s ease-in-out",
        "collapsible-up": "collapsible-up 0.2s ease-in-out",
        // NEW: Neon flicker animation for elements that need that cyberpunk pulse.
        "neon-flicker": "neon-flicker 1.5s ease-in-out infinite",
        // NEW: Glitch animation for digital distortion effects.
        "glitch": "glitch 1s steps(2, end) infinite",
      },
      fontFamily: {
        // Using a dynamic font variable allows the AI to update the look on the fly.
        display: ['var(--font_family)', 'sans-serif'],
      },
      // Optionally add custom spacing and shadows.
      spacing: {
        neon: "var(--spacing-neon, 1rem)",
      },
      boxShadow: {
        neon: "0 0 10px hsl(var(--neon))",
      },
    },
  },
  plugins: [animate],
}
