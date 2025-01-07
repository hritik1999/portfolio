<template>
  <div class="min-h-screen bg-background" :class="{ loading: isLoading }">
    <!-- Navigation -->
    <header class="border-b">
      <nav class="container mx-auto flex h-16 items-center px-4">
        <a href="#" class="text-lg font-bold">Portfolio</a>
        
        <!-- Tone and Style Selectors -->
        <div class="ml-auto flex items-center space-x-4">
          <div class="flex items-center space-x-2">
            <span class="text-sm font-medium">Tone:</span>
            <div class="flex items-center space-x-2">
              <Select v-model="selectedTone" :options="toneOptions" class="w-32">
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
              <Select v-model="selectedStyle" :options="styleOptions" class="w-32">
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

          <div class="ml-4 space-x-1">
            <Button variant="ghost" asChild>
              <a href="#about">About</a>
            </Button>
            <Button variant="ghost" asChild>
              <a href="#skills">Skills</a>
            </Button>
            <Button variant="ghost" asChild>
              <a href="#projects">Projects</a>
            </Button>
            <Button variant="ghost" asChild>
              <a href="#contact">Contact</a>
            </Button>
          </div>
        </div>
      </nav>
    </header>

    <main>
      <!-- Hero Section -->
      <section class="container mx-auto px-4 py-20 text-center">
        <div class="flex flex-col items-center space-y-4">
          <Avatar class="h-32 w-32">
            <AvatarImage src="https://github.com/yourusername.png" alt="@yourusername" />
            <AvatarFallback>YN</AvatarFallback>
          </Avatar>
          <h1 class="text-4xl font-bold">Your Name</h1>
          <p class="text-xl text-muted-foreground">Full Stack Developer</p>
          <div class="flex gap-4">
            <Button>Download CV</Button>
            <Button variant="outline">Contact Me</Button>
          </div>
        </div>
      </section>

      <!-- About Section -->
      <section id="about" class="border-t bg-muted/50">
        <div class="container mx-auto px-4 py-16">
          <h2 class="mb-8 text-3xl font-bold">About Me</h2>
          <Card class="p-6">
            <p class="text-muted-foreground">
              I'm a passionate full-stack developer with experience in building web applications.
              I love creating elegant solutions to complex problems and am constantly learning
              new technologies to stay at the forefront of web development.
            </p>
          </Card>
        </div>
      </section>

      <!-- Skills Section -->
      <section id="skills" class="border-t">
        <div class="container mx-auto px-4 py-16">
          <h2 class="mb-8 text-3xl font-bold">Skills</h2>
          <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
            <Card class="p-6">
              <h3 class="mb-4 text-xl font-semibold">Frontend</h3>
              <div class="flex flex-wrap gap-2">
                <Badge variant="secondary">Vue.js</Badge>
                <Badge variant="secondary">React</Badge>
                <Badge variant="secondary">TypeScript</Badge>
                <Badge variant="secondary">Tailwind CSS</Badge>
              </div>
            </Card>
            <Card class="p-6">
              <h3 class="mb-4 text-xl font-semibold">Backend</h3>
              <div class="flex flex-wrap gap-2">
                <Badge variant="secondary">Node.js</Badge>
                <Badge variant="secondary">Python</Badge>
                <Badge variant="secondary">Django</Badge>
                <Badge variant="secondary">PostgreSQL</Badge>
              </div>
            </Card>
            <Card class="p-6">
              <h3 class="mb-4 text-xl font-semibold">Tools</h3>
              <div class="flex flex-wrap gap-2">
                <Badge variant="secondary">Git</Badge>
                <Badge variant="secondary">Docker</Badge>
                <Badge variant="secondary">AWS</Badge>
                <Badge variant="secondary">Linux</Badge>
              </div>
            </Card>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section id="projects" class="border-t bg-muted/50">
        <div class="container mx-auto px-4 py-16">
          <h2 class="mb-8 text-3xl font-bold">Projects</h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            <Card>
              <div class="p-6">
                <h3 class="mb-2 text-xl font-semibold">Project One</h3>
                <p class="mb-4 text-sm text-muted-foreground">
                  A full-stack web application built with Vue.js and Node.js
                </p>
                <div class="mb-4 flex flex-wrap gap-2">
                  <Badge>Vue.js</Badge>
                  <Badge>Node.js</Badge>
                  <Badge>MongoDB</Badge>
                </div>
                <div class="flex gap-2">
                  <Button variant="outline" size="sm">Demo</Button>
                  <Button variant="outline" size="sm">GitHub</Button>
                </div>
              </div>
            </Card>

            <Card>
              <div class="p-6">
                <h3 class="mb-2 text-xl font-semibold">Project Two</h3>
                <p class="mb-4 text-sm text-muted-foreground">
                  An e-commerce platform with real-time updates
                </p>
                <div class="mb-4 flex flex-wrap gap-2">
                  <Badge>React</Badge>
                  <Badge>Firebase</Badge>
                  <Badge>Stripe</Badge>
                </div>
                <div class="flex gap-2">
                  <Button variant="outline" size="sm">Demo</Button>
                  <Button variant="outline" size="sm">GitHub</Button>
                </div>
              </div>
            </Card>

            <Card>
              <div class="p-6">
                <h3 class="mb-2 text-xl font-semibold">Project Three</h3>
                <p class="mb-4 text-sm text-muted-foreground">
                  A mobile-first progressive web application
                </p>
                <div class="mb-4 flex flex-wrap gap-2">
                  <Badge>Vue.js</Badge>
                  <Badge>PWA</Badge>
                  <Badge>Django</Badge>
                </div>
                <div class="flex gap-2">
                  <Button variant="outline" size="sm">Demo</Button>
                  <Button variant="outline" size="sm">GitHub</Button>
                </div>
              </div>
            </Card>
          </div>
        </div>
      </section>

      <!-- Contact Section -->
      <section id="contact" class="border-t">
        <div class="container mx-auto px-4 py-16">
          <h2 class="mb-8 text-3xl font-bold">Contact Me</h2>
          <Card class="mx-auto max-w-md">
            <div class="p-6">
              <div class="space-y-4">
                <div class="flex items-center gap-4">
                  <span class="font-semibold">Email:</span>
                  <a href="mailto:your.email@example.com" class="text-primary hover:underline">
                    your.email@example.com
                  </a>
                </div>
                <Separator />
                <div class="flex items-center gap-4">
                  <span class="font-semibold">GitHub:</span>
                  <a
                    href="https://github.com/yourusername"
                    target="_blank"
                    class="text-primary hover:underline"
                  >
                    @yourusername
                  </a>
                </div>
                <Separator />
                <div class="flex items-center gap-4">
                  <span class="font-semibold">LinkedIn:</span>
                  <a
                    href="https://linkedin.com/in/yourusername"
                    target="_blank"
                    class="text-primary hover:underline"
                  >
                    @yourusername
                  </a>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="border-t">
      <div class="container mx-auto flex h-16 items-center px-4">
        <p class="text-sm text-muted-foreground">
          {{ new Date().getFullYear() }} Your Name. All rights reserved.
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import { Badge } from '@/components/ui/badge'
import { Separator } from '@/components/ui/separator'
import { XIcon } from 'lucide-vue-next'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'

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

// Function to get text content from elements
const getTextContent = () => {
  const aboutSection = document.querySelector('#about p')?.textContent || ''
  const projectDescriptions = Array.from(document.querySelectorAll('.project-description'))
    .map(el => el.textContent)
    .join('\n')
  return { aboutSection, projectDescriptions }
}

// Function to update text content
const updateTextContent = (newText, section) => {
  if (section === 'about') {
    const aboutP = document.querySelector('#about p')
    if (aboutP) aboutP.textContent = newText
  } else if (section === 'projects') {
    const descriptions = document.querySelectorAll('.project-description')
    const newTexts = newText.split('\n')
    descriptions.forEach((desc, index) => {
      if (newTexts[index]) desc.textContent = newTexts[index]
    })
  }
}

// Function to change tone
const changeTone = async (tone) => {
  try {
    isLoading.value = true
    const { aboutSection, projectDescriptions } = getTextContent()
    
    // Change about section tone
    const aboutResponse = await fetch(`${API_BASE_URL}/change/tone`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tone,
        context: aboutSection
      })
    })
    const aboutResult = await aboutResponse.json()
    if (aboutResult.result) {
      updateTextContent(aboutResult.result, 'about')
    }

    // Change project descriptions tone
    const projectsResponse = await fetch(`${API_BASE_URL}/change/tone`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tone,
        context: projectDescriptions
      })
    })
    const projectsResult = await projectsResponse.json()
    if (projectsResult.result) {
      updateTextContent(projectsResult.result, 'projects')
    }
  } catch (error) {
    console.error('Error changing tone:', error)
  } finally {
    isLoading.value = false
  }
}

// Function to change style
const changeStyle = async (style) => {
  try {
    isLoading.value = true
    const mainContent = document.querySelector('main')?.innerHTML || ''
    
    const response = await fetch(`${API_BASE_URL}/change/style`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        style,
        html: mainContent
      })
    })
    
    const result = await response.json()
    if (result.result) {
      try {
        const newStyles = JSON.parse(result.result)
        Object.entries(newStyles).forEach(([selector, classes]) => {
          const elements = document.querySelectorAll(selector)
          elements.forEach(element => {
            // Remove existing style-related classes
            const existingClasses = element.className.split(' ')
            const newClassList = classes.split(' ')
            existingClasses.forEach(cls => {
              if (cls.includes('text-') || cls.includes('bg-') || cls.includes('border-')) {
                element.classList.remove(cls)
              }
            })
            // Add new classes
            element.classList.add(...newClassList)
          })
        })
      } catch (e) {
        console.error('Error parsing style response:', e)
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
