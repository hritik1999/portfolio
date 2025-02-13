<script>
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'

export default {
  name: 'Blog',
  components: {
    Button,
    Card,
    CardHeader,
    CardTitle,
    CardContent,
  }
}
</script>

<template>
  <div class="min-h-screen relative overflow-hidden flex items-center justify-center px-4 py-20">
    <!-- Main Card -->
    <Card class="max-w-2xl w-full p-8">
      <CardHeader class="mb-4">
        <CardTitle class="text-5xl font-bold text-center bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
          Blog
        </CardTitle>
      </CardHeader>
      <CardContent class="text-center">
        <p class="text-xl md:text-2xl text-muted-foreground leading-relaxed">
          I haven’t written any blog posts yet, but in the future I will share my thoughts and experiences here. Stay tuned!
        </p>
      </CardContent>
      <div class="mt-6 flex justify-center">
        <Button as-child variant="outline">
          <RouterLink to="/">
            Go Back Home
          </RouterLink>
        </Button>
      </div>
    </Card>

    <!-- Optional Background Blurs -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute right-20 top-1/3 -z-10 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
      <div class="absolute left-32 bottom-1/4 -z-10 h-64 w-64 rounded-full bg-secondary/10 blur-3xl"></div>
    </div>
  </div>
</template>
