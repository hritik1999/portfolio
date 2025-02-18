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

    fetch("http://192.168.0.131:5001/api/change/tone", {
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

const applyTheme = (theme) => {
  if (!theme || typeof theme !== 'object') {
    console.warn('Invalid theme data received');
    return;
  }

  console.log('Applying theme:', theme); // Debugging

  const root = document.documentElement;
  Object.entries(theme).forEach(([key, value]) => {
    root.style.setProperty(`--${key}`, value);
  });

  console.log('Theme applied successfully');
};


const generateTheme = async () => {
  if (!theme.value) return;
  
  isGenerating.value = true;
  try {
    const response = await fetch('http://192.168.1.3:5001/api/change/theme', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ theme: theme.value })
    });

    const data = await response.json();

    if (response.status !== 200) {
      throw new Error(data.error || 'Server error occurred');
    }

    let themeData = data;

    if (!themeData.lightTheme || !themeData.darkTheme) {
      throw new Error('Missing theme data in response');
    }

    customThemes.value = {
      light: themeData.lightTheme,
      dark: themeData.darkTheme
    };

    // Apply current mode's theme
    applyTheme(mode.value === 'dark' ? themeData.darkTheme : themeData.lightTheme);

  } catch (error) {
    console.error('Theme generation failed:', error);
  } finally {
    isGenerating.value = false;
  }
};

// Ensure content updates when the page loads & when route changes
onMounted(updateToneContent)
onMounted(generateTheme)
router.afterEach(() => {
  if (tone.value) updateToneContent()
  
  if (theme.modelValue) {
    try {
      const parsed = JSON.parse(customThemes)
      if (parsed && parsed[mode.value]) {
        customThemes.value = parsed
        applyTheme(mode.value === 'dark' ? parsed.dark : parsed.light)
      }
    } catch (error) {
      console.error('Error loading saved themes:', error)
    }
  }
})


</script>

<template>
   <div class="w-full min-h-screen flex flex-col">
    <!-- Navigation Header -->
    <div class="w-full bg-slate-200 dark:bg-gray-900 fixed top-0 left-0 right-0 z-50">
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
              <Button @click="generateTheme":disabled="isGenerating" class="rounded-full whitespace-nowrap text-sm">{{ isGenerating ? 'Generating...' : 'Apply Theme' }}</Button>
            </div>
          </div>
        </div>
      </div>
    </div>

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