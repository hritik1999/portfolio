<script>
import { Button } from '@/components/ui/button'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ArrowRight, Terminal, Github, Linkedin, Mail,X} from 'lucide-vue-next';
import ProfilePic from '../assets/IMG_0397_2.jpg'
export default {
  name: 'Home',
  data() {
    return {
      socialLinks: [
        { id: 1, icon: 'Github', url: 'https://github.com/hritik1999', label: 'GitHub' },
        { id: 2, icon: 'Linkedin', url: 'https://www.linkedin.com/in/hritik-gupta-985b371a1/', label: 'LinkedIn' },
        { id: 3, icon: 'Mail', url: 'mailto:guptahritik1999@gmail.com', label: 'Email' },
        { id: 4, icon: 'X', url: 'https://x.com/AI_Bhaiiii', label: 'X' },
      ],
      Pic: ProfilePic
    };
  },
  components: {
    Button,
    Avatar,
    AvatarImage,
    AvatarFallback,
    Card,
    CardHeader,
    CardTitle,
    CardContent,
    Badge,
    ArrowRight,
    Terminal,
    Github,
    Linkedin,
    X,
    Mail,
  }
};
</script>

<template>
  <div class="min-h-screen relative overflow-hidden">
    <section class="container mx-auto px-4 py-20 md:py-32">
      <div class="grid md:grid-cols-2 gap-12 items-center">
        <!-- Avatar Section -->
        <div class="flex justify-center md:justify-end relative">
          <div
            class="relative before:absolute before:inset-0 before:animate-spin-slow before:rounded-full before:bg-gradient-to-b before:from-primary before:via-secondary before:to-primary before:content-[''] before:-z-10 before:[mask:linear-gradient(white,transparent_70%)]"
          >
            <Avatar class="size-45 border-4 border-background bg-gradient-to-b from-primary/20 to-primary/5 backdrop-blur-lg">
              <AvatarImage
                :src="Pic"
                alt="@Hritik Gupta"
                class="hover:scale-105 transition-transform"
              />
              <AvatarFallback class="bg-transparent text-3xl font-bold">
                HG
              </AvatarFallback>
            </Avatar>
          </div>
        </div>

        <!-- Content Section -->
        <div class="space-y-6 text-center md:text-left">
          <h1
            class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent"
          >
            Hritik Gupta
          </h1>
          <h3
            class="text-1xl md:text-3xl font-bold "
          >
            Full Stack AI Developer | Aspiring Entrepreneur
          </h3>
          <p class="text-xl md:text-2xl text-muted-foreground leading-relaxed" id="text">
            Will be Bringing bold, unconventional ideas to life  
              and sharing them with the world. <br><br>

          </p>

          <!-- Buttons -->
          <div class="flex flex-wrap gap-4 justify-center md:justify-start">
            <Button as-child variant="outline" class="gap-2 group">
              <RouterLink to="/about">
                <span class="group-hover:translate-x-1 transition-transform">
                  Learn more
                </span>
                <ArrowRight
                  class="h-4 w-4 group-hover:translate-x-1 transition-transform"
                />
              </RouterLink>
            </Button>
            <Button as-child variant="outline" class="gap-2 group">
              <RouterLink to="/projects">
                <span class="group-hover:text-primary transition-colors">
                  View Projects
                </span>
                <ArrowRight
                  class="h-4 w-4 group-hover:translate-x-1 transition-transform"
                />
              </RouterLink>
            </Button>
          </div>

          <!-- Social Links -->
          <div class="flex gap-6 mt-8 text-muted-foreground justify-center md:justify-start">
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
        </div>
      </div>
    </section>

    <!-- Background Blurs -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute right-20 top-1/3 -z-10 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
      <div class="absolute left-32 bottom-1/4 -z-10 h-64 w-64 rounded-full bg-secondary/10 blur-3xl"></div>
    </div>
  </div>
</template>

