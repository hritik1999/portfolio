<template>
    <div class="container mx-auto px-4 py-16">
      <h1 class="text-4xl font-bold mb-8">About Me</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="space-y-6">
          <p class="text-lg leading-relaxed">
            I'm a passionate Full Stack Developer with expertise in modern web technologies.
            My journey in software development has been driven by a desire to create
            meaningful and impactful solutions that help businesses and individuals achieve their goals.
          </p>
          <p class="text-lg leading-relaxed">
            With experience in both frontend and backend development, I bring a comprehensive
            understanding of the entire development process. I'm particularly interested in
            AI and machine learning applications in web development.
          </p>
        </div>
          <div class="text-center">
            <h2 class="text-2xl font-bold">Your Name</h2>
            <p class="text-muted-foreground">Full Stack Developer</p>
          </div>
        </div>
        </div>
  </template>
  
  <script>
  import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'

    export default {
        name: 'About',
        data() {
            return {
                Pic: require('@/assets/images/avatar.jpg'),
            }
        },
        components: {
        Avatar,
        AvatarImage,
        AvatarFallback,
        },
    }
  </script>
  