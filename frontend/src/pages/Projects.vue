<template>
  <div class="container mx-auto px-4 py-16">
    <h1 class="text-4xl font-bold mb-8">Projects</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <Card v-for="(project, index) in projects" :key="index">
        <CardHeader>
          <CardTitle>{{ project.title }}</CardTitle>
          <CardDescription class="project-description">
            {{ project.description }}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div class="flex flex-wrap gap-2">
            <Badge v-for="tech in project.technologies" :key="tech" variant="secondary">
              {{ tech }}
            </Badge>
          </div>
        </CardContent>
        <CardFooter>
          <Button asChild>
            <a :href="project.link" target="_blank" rel="noopener noreferrer">View Project</a>
          </Button>
        </CardFooter>
      </Card>
    </div>
  </div>
</template>

<script setup>
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'

const projects = [
  {
    title: 'AI-Powered Portfolio',
    description: 'A dynamic portfolio website with AI-powered content customization using GPT-4 and Vue.js.',
    technologies: ['Vue.js', 'Python', 'OpenAI', 'Tailwind CSS'],
    link: 'https://github.com/yourusername/portfolio'
  },
  {
    title: 'Project Two',
    description: 'Description of your second project goes here. Make it engaging and informative.',
    technologies: ['React', 'Node.js', 'MongoDB'],
    link: 'https://github.com/yourusername/project-two'
  },
  {
    title: 'Project Three',
    description: 'Description of your third project goes here. Highlight the key features and technologies.',
    technologies: ['Django', 'PostgreSQL', 'Docker'],
    link: 'https://github.com/yourusername/project-three'
  }
]
</script>
