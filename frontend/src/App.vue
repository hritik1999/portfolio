<template>
  <div class="min-h-screen bg-background">
    <!-- Navigation -->
    <header class="border-b">
      <nav class="container mx-auto flex h-16 items-center px-4">
        <a href="#" class="text-lg font-bold">Portfolio</a>
        <div class="ml-auto space-x-1">
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
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import { Badge } from '@/components/ui/badge'
import { Separator } from '@/components/ui/separator'
</script>
