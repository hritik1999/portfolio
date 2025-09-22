<script>
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ArrowRight, Github, Linkedin, Mail, X } from 'lucide-vue-next'
import SitchatLogo from '@/assets/sitchat.jpg'
import TypeMyvibeLogo from '@/assets/typemyvibe.JPEG'

export default {
  name: 'Products',
  data() {
    return {
      // Add your future products here to automatically create new cards
      products: [
        {
          id: 1,
          name: 'Sitchat',
          logo: SitchatLogo,
          tagline: 'Experience your favourite show!',
          description: 'A storytelling platform where you can create new episodes and listen to them, watch them, read them, or even experience them in an interactive group chat.',
          url: 'https://sitchat.ai',
          features: ['Listen', 'Watch', 'Read', 'Interactive Chat', 'AI-Powered']
        },
        {
          id:2,
          name:'TypeMyvibe.ai',
          logo: TypeMyvibeLogo,
          tagline:'Your Personality Decoded!',
          description:'An AI psychoanlyst that analyzes your Social media post / personal chats and tells you your mbti,enneagram, big 5, apttitudinal psyche and Alignment. It uses those to give you insights about your personality and help you understand yourself.',
        }
      ],
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
    Badge,
    ArrowRight,
    Github,
    Linkedin,
    Mail,
    X,
  }
};
</script>

<template>
  <div class="min-h-screen relative overflow-hidden">
    <section class="container mx-auto px-4 py-20 md:py-32">
      <div class="max-w-4xl mx-auto text-center">
        <h1 class="text-5xl md:text-6xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent mb-4">
          Digital Creations
        </h1>
        <p class="text-xl md:text-2xl text-muted-foreground mb-16">
          A collection of projects and ideas brought to life.
        </p>

        <div class="grid gap-8 md:grid-cols-1">
          <Card
            v-for="product in products"
            :key="product.id"
            class="relative overflow-hidden backdrop-blur-lg bg-gradient-to-b from-primary/5 to-secondary/5 text-left transform hover:-translate-y-2 transition-transform duration-300"
          >
            <CardHeader>
              <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4">
                <img
                  :src="product.logo"
                  :alt="`${product.name} Logo`"
                  class="size-20 rounded-lg border-2 border-primary/20 shadow-lg"
                />
                <div>
                  <CardTitle class="text-3xl font-bold text-foreground">
                    {{ product.name }}
                  </CardTitle>
                  <p class="text-lg text-muted-foreground" id="text">{{ product.tagline }}</p>
                </div>
              </div>
            </CardHeader>
            <CardContent class="space-y-6">
              <p class="text-lg leading-relaxed" id="text">
                {{ product.description }}
              </p>

              <div class="flex flex-wrap gap-2">
                <Badge
                  v-for="feature in product.features"
                  :key="feature"
                  variant="secondary"
                >
                  {{ feature }}
                </Badge>
              </div>

              <div class="pt-4">
                <Button as="a" :href="product.url" target="_blank" class="gap-2 group">
                  <span>Visit {{ product.name }}</span>
                  <ArrowRight class="h-4 w-4 group-hover:translate-x-1 transition-transform" />
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>

        <div class="flex gap-6 mt-20 text-muted-foreground justify-center">
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
    </section>

    <div class="absolute inset-0 overflow-hidden pointer-events-none -z-10">
      <div class="absolute right-0 top-1/3 h-72 w-72 rounded-full bg-primary/10 blur-3xl animate-pulse"></div>
      <div class="absolute left-0 bottom-1/4 h-64 w-64 rounded-full bg-secondary/10 blur-3xl animate-pulse"></div>
    </div>
  </div>
</template>