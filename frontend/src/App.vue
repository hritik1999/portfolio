<script setup>
import { ref,watch,onMounted,  nextTick } from 'vue'
import { RouterLink, RouterView,useRouter } from 'vue-router'
import { Skeleton } from '@/components/ui/skeleton'
import { Input } from '@/components/ui/input'
import { useColorMode } from '@vueuse/core'
import { Button } from '@/components/ui/button'
import { Icon } from '@iconify/vue'

const mode = useColorMode('dark')
const isMenuOpen = ref(false)
const router = useRouter()

const tone = ref('')
const theme = ref('')
const isGenerating = ref(false)
const customThemes = ref({
  light: null,
  dark: null
})

// Toggle between dark/light modes
const toggleTheme = () => {
  mode.value = mode.value === 'dark' ? 'light' : 'dark'
  // Apply stored theme for current mode
  if (customThemes.value[mode.value]) {
    applyTheme(customThemes.value[mode.value])
  }
}

// Function to update text dynamically across all pages
const updateToneContent = async () => {
  if (!tone.value) return // Only update if tone is set
  console.log('Updating tone:', tone.value)
  await nextTick() // Ensure DOM is updated before selecting elements

  document.querySelectorAll('main #text').forEach((element) => {
    const originalText = element.innerText
    element.innerHTML = `<span class="animate-pulse">⏳ Changing tone...</span>` // Show loading state

    fetch("https://hritikgupta.com/api/change/tone", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tone: tone.value, context: originalText }),
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        element.innerText = data.result
      })
      .catch((error) => {
        console.error('Error:', error)
        element.innerText = originalText // Restore original text on error
      })
  })
}


const generateTheme = async () => {
  if (!theme.value) return;
  isGenerating.value = true;
  try {
    const mainContent = document.querySelector('main');
    const response = await fetch('https://hritikgupta.com/api/change/style', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        style: theme.value,
        html: mainContent.innerHTML,
      }),
    });
    const data = await response.json();
    if (data.error) {
      console.error('Server error:', data.error);
      return;
    }
    if (data.result) {
      const styles = data.result;
      // Remove any previously added dynamic style tags
      const oldStyles = document.querySelectorAll('style[data-dynamic-style]');
      oldStyles.forEach((style) => style.remove());

      // Create a new style element for dynamic styles
      const styleSheet = document.createElement('style');
      styleSheet.setAttribute('data-dynamic-style', 'true');

      // Build CSS Variables (make sure your Tailwind config uses these variables)
      const cssVars = `
        :root {
          --background: ${styles.theme.background};
          --foreground: ${styles.theme.text};
          --primary: ${styles.theme.primary};
          --secondary: ${styles.theme.secondary};
          --accent: ${styles.theme.accent};
          --card-bg: ${styles.theme.background};
          --button-bg: ${styles.theme.primary};
          --button-text: ${styles.theme.background};
          --nav-bg: ${styles.theme.background};
          --section-bg: ${styles.theme.secondary};
        }
      `;

      // Build component CSS using the provided styling tokens
      // Note: Changed "background-color" to "background" and added extra properties
      const componentStyles = `
        /* Base Styles */
        body {
          background: var(--background);
          background-size: cover;
          background-position: center;
          background-repeat: no-repeat;
          color: var(--foreground);
          font-family: ${styles.typography.body[0]};
          font-weight: ${styles.typography.body[1]};
          line-height: ${styles.typography.body[2] || '1.5'};
          /* Fallback text shadow to boost contrast */
          text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.6);
        }
        /* Dramatically enhanced background overlay (if needed) */
        .background-overlay {
          background: rgba(0,0,0,0.3);
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
        }
        /* Headings with neon glow */
        h1, h2, h3, h4, h5, h6 {
          font-family: ${styles.typography.headings[0]};
          font-weight: ${styles.typography.headings[1]};
          letter-spacing: ${styles.typography.headings[2] || 'normal'};
          text-transform: ${styles.typography.headings[3] || 'none'};
          color: var(--foreground);
          text-shadow: 0 0 2px var(--accent), 0 0 5px var(--accent);
        }
        h1 { ${styles.typography.sizes.h1} }
        h2 { ${styles.typography.sizes.h2} }
        p  { ${styles.typography.sizes.body} }

        input {
          color: var(--foreground);
          background-color: var(--card-bg);
          border: 1px solid var(--secondary);
        }
        input::placeholder {
          color: var(--secondary);
        }
        
        /* Component Styles */
        .card {
          ${styles.components.card.join(';')};
          background: var(--card-bg);
          ${styles.theme.patterns && styles.theme.patterns.length ? `background-image: ${styles.theme.patterns[0]};` : ''}
          transition: all 0.3s ease;
        }
        .button, button {
          ${styles.components.button.join(';')};
          background-color: var(--button-bg);
          color: var(--button-text);
          transition: all 0.3s ease;
          position: relative;
          overflow: hidden;
        }
        nav {
          ${styles.components.nav.join(';')};
          background: var(--nav-bg);
        }
        section {
          ${styles.components.section.join(';')};
          padding: ${styles.spacing.section};
        }
        .container {
          padding: ${styles.spacing.container};
          margin: ${styles.spacing.elements || '0 auto'};
        }
        /* Hover & transition effects */
        .card:hover {
          ${styles.effects.hover.join(';')};
          transform: translateY(-2px);
          box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .button:hover, button:hover {
          transform: translateY(-1px);
          filter: brightness(110%);
          ${styles.effects.hover.join(';')};
        }
        .card, .button, button, nav, section {
          ${styles.effects.transition.join(';')};
        }
        /* Optional animations */
        ${styles.effects.animation ? `
          @keyframes theme-animation {
            ${styles.effects.animation.join(';')}
          }
          .animated-element {
            animation: theme-animation 1s ease-in-out infinite;
          }
        ` : ''}
        /* Links and badges */
        a {
          color: var(--primary);
          transition: color 0.3s ease;
        }
        a:hover {
          color: var(--accent);
        }
        .badge {
          background-color: var(--accent);
          color: var(--background);
        }
        .text-muted-foreground {
          color: var(--secondary);
        }
        .element-spacing {
          margin: ${styles.spacing.elements || 'inherit'};
        }
      `;

      // Inject the built styles
      styleSheet.textContent = cssVars + componentStyles;
      document.head.appendChild(styleSheet);

      // Optionally update a preview area with the updated main content
      this.styledContent = document.querySelector('main').innerHTML;

      // Add a theme-specific class to body (for any further style targeting)
      document.body.className = `theme-${theme.value.toLowerCase()}`;

      // Apply background patterns if provided
      if (styles.theme.patterns && styles.theme.patterns.length > 0) {
        document.body.style.backgroundImage = styles.theme.patterns[0];
        document.body.style.backgroundSize = 'cover';
        document.body.style.backgroundRepeat = 'no-repeat';
        document.body.style.backgroundPosition = 'center center';
      } else {
        document.body.style.background = styles.theme.background;
      }

      // Add animation classes if animations are defined
      if (styles.effects.animation) {
        const animatedElements = document.querySelectorAll('.animate-theme');
        animatedElements.forEach(el => el.classList.add('animated-element'));
      }
    }
  } catch (error) {
    console.error('Error changing style:', error);
  } finally {
    isGenerating.value = false;
  }
};




// Ensure content updates when the page loads & when route changes
onMounted(updateToneContent)
router.afterEach(() => {
  if (tone.value) updateToneContent()
})


</script>

<template>
   <div class="w-full min-h-screen flex flex-col">
    <!-- Navigation Header -->
    <nav class="w-full bg-slate-200 dark:bg-gray-900 fixed top-0 left-0 right-0 z-50">
      <div class="w-full p-4 flex justify-between items-center">
        <!-- Logo -->
        <div class="flex items-center">
          <RouterLink to="/" class="text-xl font-bold tracking-wide ">HG</RouterLink>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-4 lg:gap-6">
          <RouterLink 
            v-for="link in ['About', 'Products', 'Projects', 'Blog']" 
            :key="link"
            :to="`/${link.toLowerCase()}`" 
            class="hover:text-gray-300"
          >
            {{ link }}
          </RouterLink>

          <!-- Tone and Style Controls -->
          <div class="flex items-center gap-2 lg:gap-4">
            <Input
              class="w-32 lg:w-48"
              placeholder="Enter tone..."
              v-model="tone"
            />
            <Button variant="default" class="rounded-full whitespace-nowrap text-sm" @click="updateToneContent(tone)">Change Tone</Button>
            <Input
              class="w-32 lg:w-48"
              placeholder="Enter theme..."
              v-model="theme"
            />
            <Button @click="generateTheme":disabled="isGenerating" class="rounded-full whitespace-nowrap text-sm">{{ isGenerating ? 'Generating...' : 'Apply Theme' }}</Button>
          </div>

          <!-- Dark mode toggle button for Desktop -->
          <Button variant="outline" @click="toggleTheme">
            <Icon 
              :icon="mode.value === 'dark' ? 'radix-icons:sun' : 'radix-icons:moon'" 
              class="h-[1.2rem] w-[1.2rem]" 
            />
            <span class="sr-only">Toggle theme</span>
          </Button>
        </div>

        <!-- Mobile Navigation: Dark mode toggle and Menu button -->
        <div class="flex items-center space-x-2 md:hidden">
          <!-- Mobile Dark Mode Toggle -->
          <Button variant="outline" @click="toggleTheme">
            <Icon 
              :icon="mode.value === 'dark' ? 'radix-icons:sun' : 'radix-icons:moon'" 
              class="h-[1.2rem] w-[1.2rem]" 
            />
            <span class="sr-only">Toggle theme</span>
          </Button>

          <!-- Mobile Menu Button -->
          <button 
            class="text-white p-2"
            @click="isMenuOpen = !isMenuOpen"
            aria-label="Toggle menu"
          >
            <div class="w-6 h-5 relative flex flex-col justify-between">
              <span 
                class="w-full h-0.5 bg-white transition-transform duration-200"
                :class="{ 'rotate-45 translate-y-2': isMenuOpen }"
              ></span>
              <span 
                class="w-full h-0.5 bg-white transition-opacity duration-200"
                :class="{ 'opacity-0': isMenuOpen }"
              ></span>
              <span 
                class="w-full h-0.5 bg-white transition-transform duration-200"
                :class="{ '-rotate-45 -translate-y-2': isMenuOpen }"
              ></span>
            </div>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div 
        v-if="isMenuOpen" 
        class="md:hidden border-t "
      >
        <div class="flex flex-col p-4 space-y-4">
          <RouterLink 
            v-for="link in ['About', 'Products', 'Projects', 'Blog']" 
            :key="link"
            :to="`/${link.toLowerCase()}`" 
            class="hover:text-gray-300 py-2"
            @click="isMenuOpen = false"
          >
            {{ link }}
          </RouterLink>
          
          <!-- Mobile Tone and Style Controls -->
          <div class="space-y-4 pt-4 border-t">
            <div class="space-y-2">
              <Input
                class="w-full"
                placeholder="Enter tone..."
                v-model="tone"
              />
              <Button variant="default" class="rounded-full w-full" @click="updateToneContent(tone)">Change Tone</Button>
            </div>
            <div class="space-y-2">
              <Input
                class=" w-full"
                placeholder="Enter theme..."
                v-model="theme"
              />
              <Button @click="generateTheme":disabled="isGenerating" class="rounded-full w-full whitespace-nowrap text-sm">{{ isGenerating ? 'Generating...' : 'Apply Theme' }}</Button>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="w-full pt-[40px] overflow-x-hidden">
      <RouterView class="w-full h-full" />
    </main>

    <!-- Footer -->
    <footer class="border-t mt-auto bottom-0">
      <div class="container mx-auto flex flex-col sm:flex-row h-auto sm:h-16 items-center justify-between p-4 gap-4 sm:gap-0">
        <p class="text-sm text-muted-foreground text-center sm:text-left">
          © 2025 Hritik Gupta. All rights reserved.
        </p>
        <div class="flex space-x-4">
          <a 
            href="https://github.com/hritik1999" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-sm text-muted-foreground hover:text-foreground"
          >
            GitHub
          </a>
          <a 
            href="https://www.linkedin.com/in/hritik-gupta-985b371a1/" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-sm text-muted-foreground hover:text-foreground"
          >
            LinkedIn
          </a>
          <a 
            href="https://x.com/AI_Bhaiiii" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-sm text-muted-foreground hover:text-foreground"
          >
            X
          </a>
        </div>
      </div>
    </footer>
  </div>
</template>