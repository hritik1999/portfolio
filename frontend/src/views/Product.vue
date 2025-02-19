<script>
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Terminal, Github, Linkedin, Mail, X, Hammer, ArrowRight } from 'lucide-vue-next';

export default {
  name: 'Products',
  data() {
    return {
      socialLinks: [
        { id: 1, icon: 'Github', url: 'https://github.com/hritik1999', label: 'GitHub' },
        { id: 2, icon: 'Linkedin', url: 'https://www.linkedin.com/in/hritik-gupta-985b371a1/', label: 'LinkedIn' },
        { id: 3, icon: 'Mail', url: 'mailto:guptahritik1999@gmail.com', label: 'Email' },
        { id: 4, icon: 'X', url: 'https://x.com/AI_Bhaiiii', label: 'X' },
      ]
    };
  },
  components: {
    Button,
    Card,
    CardHeader,
    CardTitle,
    CardContent,
    Terminal,
    Github,
    Linkedin,
    X,
    Mail,
    Hammer,
    ArrowRight
  }
};
</script>

<template>
  <div class="min-h-screen relative overflow-hidden">
    <section class="container mx-auto px-4 py-20 md:py-32">
      <div class="max-w-3xl mx-auto text-center">
        <!-- Animated Construction Icon -->
        <div class="mb-8 animate-bounce">
          <Hammer class="h-16 w-16 mx-auto text-primary" />
        </div>

        <Card class="relative overflow-hidden backdrop-blur-lg bg-gradient-to-b from-primary/5 to-secondary/5">
          <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,#4f46e525_0%,transparent_70%)]"></div>
          <CardHeader>
            <CardTitle class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
              <h1>Digital Workshop</h1>
            </CardTitle>
          </CardHeader>
          <CardContent class="space-y-6">
            <div class="flex items-center justify-center gap-2 text-muted-foreground">
              <Terminal class="h-6 w-6 text-primary" />
              <span class="font-mono text-sm">hritik@build-process:~/products</span>
            </div>
            
            <p class="text-xl md:text-2xl leading-relaxed" id="text">
              Crafting something extraordinary behind the scenes.<br>
              <span class="text-primary">Innovation in progress</span> - stay tuned for the grand reveal!
            </p>

            <div class="flex flex-wrap gap-4 justify-center">
              <Button as-child variant="outline" class="gap-2 group">
                <RouterLink to="/">
                  <span class="group-hover:translate-x-1 transition-transform">
                    Return Home
                  </span>
                  <ArrowRight class="h-4 w-4 group-hover:translate-x-1 transition-transform" />
                </RouterLink>
              </Button>
            </div>
          </CardContent>
        </Card>

        <!-- Social Links -->
        <div class="flex gap-6 mt-12 text-muted-foreground justify-center">
          <a
            v-for="link in socialLinks"
            :key="link.id"
            :href="link.url"
            target="_blank"
            :aria-label="link.label"
            class="p-2 hover:text-primary transition-colors"
          >
            <component :is="link.icon" class="h-6 w-6" />
          </a>
        </div>
        <p class='mt-6 text-m md:text-xl leading-relaxed' id="text">PS: Would you like to see the change style and change tone features as a browser extension? Making the whole internet practically customizable🤯</p>
      </div>
    </section>
    <!-- Background Effects -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute right-0 top-1/3 -z-10 h-72 w-72 rounded-full bg-primary/10 blur-3xl animate-pulse"></div>
      <div class="absolute left-0 bottom-1/4 -z-10 h-64 w-64 rounded-full bg-secondary/10 blur-3xl animate-pulse"></div>
    </div>
  </div>
</template>