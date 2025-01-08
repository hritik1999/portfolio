<template>
  <div>
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
          <Button asChild>
            <RouterLink to="/about">About Me</RouterLink>
          </Button>
          <Button asChild variant="outline">
            <RouterLink to="/projects">View Projects</RouterLink>
          </Button>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section class="border-t bg-muted/50">
      <div class="container mx-auto px-4 py-16">
        <h2 class="text-3xl font-bold mb-8">Skills</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <Card>
            <CardHeader>
              <CardTitle>Frontend</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="flex flex-wrap gap-2">
                <Badge variant="secondary">Vue.js</Badge>
                <Badge variant="secondary">React</Badge>
                <Badge variant="secondary">Tailwind CSS</Badge>
                <Badge variant="secondary">TypeScript</Badge>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Backend</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="flex flex-wrap gap-2">
                <Badge variant="secondary">Node.js</Badge>
                <Badge variant="secondary">Python</Badge>
                <Badge variant="secondary">Django</Badge>
                <Badge variant="secondary">PostgreSQL</Badge>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Tools & Others</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="flex flex-wrap gap-2">
                <Badge variant="secondary">Git</Badge>
                <Badge variant="secondary">Docker</Badge>
                <Badge variant="secondary">AWS</Badge>
                <Badge variant="secondary">CI/CD</Badge>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { Button } from '@/components/ui/button'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
</script>
