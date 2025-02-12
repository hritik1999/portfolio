<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from '@/components/ui/navigation-menu'
import { Input } from '@/components/ui/input'
import { useColorMode } from '@vueuse/core'
import { Button } from '@/components/ui/button'
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from '@/components/ui/dropdown-menu'
import { Icon } from '@iconify/vue'

const mode = useColorMode('dark')
const isMenuOpen = ref(false)

// Manually toggle between 'dark' and 'light'
const toggleTheme = () => {
  mode.value = mode.value === 'dark' ? 'light' : 'dark'
}

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
            v-for="link in ['About', 'Products', 'Projects', 'Contact', 'Blog']" 
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
            />
            <Button variant="default" class="rounded-full whitespace-nowrap text-sm">Change Tone</Button>
            <Input
              class="w-32 lg:w-48"
              placeholder="Enter style..."
            />
            <Button variant="default" class="rounded-full whitespace-nowrap text-sm">Change Style</Button>
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
        class="md:hidden bg-gray-900 border-t border-gray-800"
      >
        <div class="flex flex-col p-4 space-y-4">
          <RouterLink 
            v-for="link in ['About', 'Products', 'Projects', 'Contact', 'Blog']" 
            :key="link"
            :to="`/${link.toLowerCase()}`" 
            class="text-white hover:text-gray-300 py-2"
            @click="isMenuOpen = false"
          >
            {{ link }}
          </RouterLink>
          
          <!-- Mobile Tone and Style Controls -->
          <div class="space-y-4 pt-4 border-t border-gray-800">
            <div class="space-y-2">
              <Input
                class="bg-gray-800 border-gray-700 text-white w-full"
                placeholder="Enter tone..."
              />
              <Button variant="default" class="rounded-full w-full">Change Tone</Button>
            </div>
            <div class="space-y-2">
              <Input
                class="bg-gray-800 border-gray-700 text-white w-full"
                placeholder="Enter style..."
              />
              <Button variant="default" class="rounded-full w-full">Change Style</Button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <main class="flex-grow w-full pt-[80px] px-4 overflow-x-hidden">
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