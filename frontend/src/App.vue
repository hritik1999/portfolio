<template>
  <div class="min-h-screen bg-background" :class="{ loading: isLoading }">
    <!-- Navigation -->
    <header class="border-b">
      <nav class="container mx-auto flex h-16 items-center justify-between px-4">
        <RouterLink to="/" class="text-lg font-bold">Portfolio</RouterLink>
        <div class="flex items-center space-x-8">
          <RouterLink to="/" class="text-sm font-medium">Home</RouterLink>
          <RouterLink to="/about" class="text-sm font-medium">About</RouterLink>
          <RouterLink to="/projects" class="text-sm font-medium">Projects</RouterLink>
          <div class="flex items-center space-x-2">
            <span class="text-sm font-medium">Tone:</span>
            <div class="flex items-center space-x-2">
              <Select v-model="selectedTone" class="w-32">
                <SelectTrigger>
                  <SelectValue :placeholder="selectedTone || 'Select tone'" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem v-for="tone in toneOptions" :key="tone.value" :value="tone.value">
                    {{ tone.label }}
                  </SelectItem>
                  <div class="p-2 border-t">
                    <input 
                      type="text" 
                      v-model="newTone"
                      @keyup.enter="addCustomTone"
                      placeholder="Add custom tone..."
                      class="w-full px-2 py-1 text-sm border rounded"
                    />
                  </div>
                </SelectContent>
              </Select>
              <Button v-if="selectedTone && !isDefaultTone(selectedTone)" 
                      variant="ghost" 
                      size="icon"
                      @click="removeTone(selectedTone)"
                      class="h-8 w-8">
                <XIcon class="h-4 w-4" />
              </Button>
            </div>
          </div>

          <div class="flex items-center space-x-2">
            <span class="text-sm font-medium">Style:</span>
            <div class="flex items-center space-x-2">
              <Select v-model="selectedStyle" class="w-32">
                <SelectTrigger>
                  <SelectValue :placeholder="selectedStyle || 'Select style'" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem v-for="style in styleOptions" :key="style.value" :value="style.value">
                    {{ style.label }}
                  </SelectItem>
                  <div class="p-2 border-t">
                    <input 
                      type="text" 
                      v-model="newStyle"
                      @keyup.enter="addCustomStyle"
                      placeholder="Add custom style..."
                      class="w-full px-2 py-1 text-sm border rounded"
                    />
                  </div>
                </SelectContent>
              </Select>
              <Button v-if="selectedStyle && !isDefaultStyle(selectedStyle)" 
                      variant="ghost" 
                      size="icon"
                      @click="removeStyle(selectedStyle)"
                      class="h-8 w-8">
                <XIcon class="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>

    <!-- Footer -->
    <footer class="border-t">
      <div class="container mx-auto flex h-16 items-center justify-between px-4">
        <p class="text-sm text-muted-foreground"> 2024 Your Name. All rights reserved.</p>
        <div class="flex space-x-4">
          <a href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer" class="text-sm text-muted-foreground hover:text-foreground">
            GitHub
          </a>
          <a href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer" class="text-sm text-muted-foreground hover:text-foreground">
            LinkedIn
          </a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { Button } from '@/components/ui/button'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { XIcon } from 'lucide-vue-next'

// API base URL
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5001/api'

// Default options
const defaultToneOptions = [
  { value: 'professional', label: 'Professional' },
  { value: 'casual', label: 'Casual' },
  { value: 'friendly', label: 'Friendly' },
  { value: 'formal', label: 'Formal' },
  { value: 'creative', label: 'Creative' }
]

const defaultStyleOptions = [
  { value: 'minimal', label: 'Minimal' },
  { value: 'modern', label: 'Modern' },
  { value: 'classic', label: 'Classic' },
  { value: 'bold', label: 'Bold' },
  { value: 'playful', label: 'Playful' }
]

// Reactive references
const toneOptions = ref([...defaultToneOptions])
const styleOptions = ref([...defaultStyleOptions])
const newTone = ref('')
const newStyle = ref('')
const selectedTone = ref('professional')
const selectedStyle = ref('modern')
const isLoading = ref(false)

// Helper functions to check if tone/style is default
const isDefaultTone = (value) => defaultToneOptions.some(t => t.value === value)
const isDefaultStyle = (value) => defaultStyleOptions.some(s => s.value === value)

// Function to change tone
const changeTone = async (tone) => {
  try {
    isLoading.value = true
    
    // Select all text elements we want to update
    const elements = document.querySelectorAll('main p, main h1, main h2, main h3, .project-description');
    
    // Create a map of elements and their content
    const contentMap = new Map();
    elements.forEach((el, index) => {
      if (el.textContent.trim()) {
        contentMap.set(`text-${index}`, {
          element: el,
          content: el.textContent.trim()
        });
      }
    });

    // If no content to update, return early
    if (contentMap.size === 0) return;

    // Prepare content for API request
    const contentArray = Array.from(contentMap.entries()).map(([id, data]) => ({
      id,
      content: data.content
    }));

    const response = await fetch(`${API_BASE_URL}/change/tone`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tone,
        context: contentArray.map(item => item.content).join('\n---\n')
      })
    });

    const result = await response.json();
    if (result.result) {
      // Split the response text and update elements
      const updatedTexts = result.result.split('\n---\n');
      contentArray.forEach((item, index) => {
        if (updatedTexts[index] && contentMap.has(item.id)) {
          const { element } = contentMap.get(item.id);
          element.textContent = updatedTexts[index].trim();
        }
      });
    }
  } catch (error) {
    console.error('Error changing tone:', error);
  } finally {
    isLoading.value = false;
  }
}

const changeStyle = async (style) => {
  try {
    isLoading.value = true
    const mainContent = document.querySelector('main')
    
    const response = await fetch(`${API_BASE_URL}/change/style`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        style,
        html: mainContent.innerHTML
      })
    })
    
    const data = await response.json()
    if (data.error) {
      console.error('Server error:', data.error)
      return
    }
    
    if (data.result) {
      const styles = data.result

      // Remove any previously added style tags
      const oldStyles = document.querySelectorAll('style[data-dynamic-style]')
      oldStyles.forEach(style => style.remove())

      // Create a new style element for our dynamic styles
      const styleSheet = document.createElement('style')
      styleSheet.setAttribute('data-dynamic-style', 'true')
      
      // Build CSS Variables with enhanced color options
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
      `

      // Build enhanced component styles
      const componentStyles = `
        /* Base Styles */
        body {
          background-color: var(--background);
          color: var(--foreground);
          font-family: ${styles.typography.body[0]};
          font-weight: ${styles.typography.body[1]};
          line-height: ${styles.typography.body[2] || 'inherit'};
        }

        /* Typography with enhanced options */
        h1, h2, h3, h4, h5, h6 {
          font-family: ${styles.typography.headings[0]};
          font-weight: ${styles.typography.headings[1]};
          letter-spacing: ${styles.typography.headings[2] || 'normal'};
          text-transform: ${styles.typography.headings[3] || 'none'};
          color: var(--foreground);
        }

        h1 { ${styles.typography.sizes.h1} }
        h2 { ${styles.typography.sizes.h2} }
        p { ${styles.typography.sizes.body} }

        /* Components with patterns and enhanced styling */
        .card {
          ${styles.components.card.join(';')};
          background-color: var(--card-bg);
          ${styles.theme.patterns ? `background-image: ${styles.theme.patterns[0]};` : ''}
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
          background-color: var(--nav-bg);
        }

        section {
          ${styles.components.section.join(';')};
          padding: ${styles.spacing.section};
        }

        .container {
          padding: ${styles.spacing.container};
          margin: ${styles.spacing.elements || '0 auto'};
        }

        /* Enhanced hover effects and animations */
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

        /* Advanced transitions */
        .card, .button, button, nav, section {
          ${styles.effects.transition.join(';')};
        }

        /* Animations if provided */
        ${styles.effects.animation ? `
          @keyframes theme-animation {
            ${styles.effects.animation.join(';')}
          }

          .animated-element {
            animation: theme-animation 1s ease-in-out infinite;
          }
        ` : ''}

        /* Theme-specific elements */
        a {
          color: var(--primary);
          transition: color 0.3s ease;
          ${styles.typography.body[2] ? `letter-spacing: ${styles.typography.body[2]};` : ''}
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

        /* Additional spacing utilities */
        .element-spacing {
          margin: ${styles.spacing.elements || 'inherit'};
        }
      `

      styleSheet.textContent = cssVars + componentStyles
      document.head.appendChild(styleSheet)

      // Add theme-specific class to body
      document.body.className = `theme-${style.toLowerCase()}`
      
      // Apply any patterns or background effects
      if (styles.theme.patterns && styles.theme.patterns.length > 0) {
        document.body.style.backgroundImage = styles.theme.patterns[0]
      }
      
      // Add animation class to elements if animations are defined
      if (styles.effects.animation) {
        const animatedElements = document.querySelectorAll('.animate-theme')
        animatedElements.forEach(el => el.classList.add('animated-element'))
      }
    }
  } catch (error) {
    console.error('Error changing style:', error)
  } finally {
    isLoading.value = false
  }
}

// Add custom tone
const addCustomTone = () => {
  if (newTone.value.trim()) {
    const value = newTone.value.toLowerCase().replace(/\s+/g, '-')
    if (!toneOptions.value.some(t => t.value === value)) {
      toneOptions.value.push({
        value,
        label: newTone.value.trim()
      })
      selectedTone.value = value
    }
    newTone.value = ''
  }
}

// Add custom style
const addCustomStyle = () => {
  if (newStyle.value.trim()) {
    const value = newStyle.value.toLowerCase().replace(/\s+/g, '-')
    if (!styleOptions.value.some(s => s.value === value)) {
      styleOptions.value.push({
        value,
        label: newStyle.value.trim()
      })
      selectedStyle.value = value
    }
    newStyle.value = ''
  }
}

// Remove custom tone
const removeTone = (value) => {
  if (!isDefaultTone(value)) {
    toneOptions.value = toneOptions.value.filter(t => t.value !== value)
    selectedTone.value = 'professional'
  }
}

// Remove custom style
const removeStyle = (value) => {
  if (!isDefaultStyle(value)) {
    styleOptions.value = styleOptions.value.filter(s => s.value !== value)
    selectedStyle.value = 'modern'
  }
}

// Watch for changes in tone and style
watch([selectedTone], async ([newTone]) => {
  if (newTone && !isLoading.value) {
    await changeTone(newTone)
  }
})

watch([selectedStyle], async ([newStyle]) => {
  if (newStyle && !isLoading.value) {
    await changeStyle(newStyle)
  }
})
</script>

<style>
.loading {
  opacity: 0.7;
  pointer-events: none;
}
</style>
