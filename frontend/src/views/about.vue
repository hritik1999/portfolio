<template>
    <div class="min-h-screen relative overflow-hidden">
      <section class="container mx-auto px-4 py-20 md:py-32">
        <div class="grid lg:grid-cols-[400px_1fr] gap-16 items-start">
          <!-- Sticky Profile Column -->
          <div class="lg:sticky lg:top-32 flex flex-col gap-12">
            <div class="relative before:absolute before:inset-0 before:animate-spin-slow before:rounded-full before:bg-gradient-to-b before:from-primary before:via-secondary before:to-primary before:content-[''] before:-z-10 before:[mask:linear-gradient(white,transparent_70%)]">
              <Avatar class="size-80 border-4 border-background bg-gradient-to-b from-primary/20 to-primary/5 backdrop-blur-lg">
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
  
            <!-- Quick Info Card -->
            <div class="p-8 rounded-2xl border border-border bg-background/50 backdrop-blur-lg space-y-4 shadow-lg">
              <h3 class="text-xl font-bold text-primary">Quick Stats</h3>
              <div class="grid grid-cols-2 gap-4">
                <div v-for="stat in quickStats" :key="stat.label" class="space-y-1">
                  <div class="text-2xl font-bold text-foreground">{{ stat.value }}</div>
                  <div class="text-sm text-muted-foreground">{{ stat.label }}</div>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Content Column -->
          <div class="space-y-20">
            <!-- Introduction Section -->
            <section class="space-y-6">
              <h2 class="text-4xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                Who Am I?
              </h2>
              <div class="space-y-4 text-lg text-muted-foreground">
                <p>
                  A full-stack developer with an AI obsession, building intelligent solutions that bridge 
                  <span class="text-primary font-medium">technical complexity</span> with 
                  <span class="font-medium">user-friendly experiences</span>. 
                  Currently pushing boundaries in generative AI applications while exploring solopreneurship.
                </p>
              </div>
            </section>
  
            <!-- Skills & Expertise -->
            <section class="space-y-6">
              <h3 class="text-3xl font-bold text-foreground">Technical Arsenal</h3>
              <div class="grid md:grid-cols-2 gap-4">
                <div 
                  v-for="(skill, index) in skills"
                  :key="index"
                  class="p-6 rounded-xl border border-border bg-background/50 hover:bg-gradient-to-br from-primary/5 to-secondary/5 transition-all group"
                >
                  <div class="flex items-center gap-4">
                    <div class="p-3 rounded-lg bg-primary/10">
                      <component :is="skill.icon" class="h-8 w-8" />
                    </div>
                    <div>
                      <h4 class="text-lg font-semibold">{{ skill.name }}</h4>
                      <p class="text-sm text-muted-foreground">{{ skill.description }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </section>
  
            <!-- Mission & Vision -->
            <section class="grid md:grid-cols-2 gap-8">
              <div class="p-8 rounded-2xl bg-primary/5 border border-primary/20">
                <h3 class="text-2xl font-bold text-primary mb-4">Mission</h3>
                <p class="text-muted-foreground">
                  Democratize AI capabilities through intuitive interfaces, enabling businesses to harness 
                  cutting-edge technology without technical overhead.
                </p>
              </div>
              <div class="p-8 rounded-2xl bg-secondary/5 border border-primary/20">
                <h3 class="text-2xl font-bold mb-4">Vision</h3>
                <p class="text-muted-foreground">
                  Create self-sustaining AI systems that empower individuals and small businesses to compete 
                  with enterprise-level resources.
                </p>
              </div>
            </section>
  
            <!-- Experience & Achievements -->
            <section class="space-y-6">
              <h3 class="text-3xl font-bold text-foreground">Journey</h3>
              <div class="space-y-8">
                <div 
                  v-for="(item, index) in timeline"
                  :key="index"
                  class="relative pl-10 border-l-2 border-border group"
                >
                  <div class="absolute w-4 h-4 bg-primary rounded-full -left-[9px] top-1 border-2 border-background transition-transform group-hover:scale-125" />
                  <h4 class="text-xl font-semibold">{{ item.title }}</h4>
                  <div class="text-sm text-primary mb-2">{{ item.date }}</div>
                  <p class="text-muted-foreground">{{ item.description }}</p>
                  <div v-if="item.achievement" class="mt-3 p-3 rounded-lg bg-secondary/5 border border-secondary/20">
                    🏆 {{ item.achievement }}
                  </div>
                </div>
              </div>
            </section>
          </div>
        </div>
      </section>

                  <!-- Call to Action -->
                  <section class="text-center py-16 space-y-6 border-t">
              <h3 class="text-3xl font-bold text-foreground">Ready to Create Magic?</h3>
              <p class="text-lg text-muted-foreground max-w-2xl mx-auto">
                Whether you want to discuss AI innovations, potential collaborations, or just geek out about 
                the future of technology - let's connect!
              </p>
              <div class="flex justify-center gap-4">
         <!-- Social Links -->
          <div class="flex gap-6 text-muted-foreground justify-center md:justify-start">
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
  
      <!-- Background Effects -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute right-0 top-1/4 -z-10 h-[600px] w-[600px] rounded-full bg-primary/10 blur-[100px]"></div>
        <div class="absolute left-0 bottom-1/3 -z-10 h-[500px] w-[500px] rounded-full bg-secondary/10 blur-[100px]"></div>
      </div>
    </div>
  </template>
  
  
  <script>
import { MessageSquareText } from 'lucide-vue-next';
import { Button } from '@/components/ui/button';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { Download, ArrowRight,Github, Linkedin, Mail,X,Brain } from 'lucide-vue-next';
import ProfilePic from '../assets/IMG_8346.jpg'

    export default {
        name: 'About',
        data() {
            return {
                quickStats :[
                    { label: 'Projects Completed', value: '50+' },
                    { label: 'AI Models Deployed', value: '200+' },
                    { label: 'Years Experience', value: '5' },
                    { label: 'Open Source Contributions', value: '1.2k' }
                    ],
                skills : [
                    { 
                        name: 'Generative AI', 
                        icon: 'Brain',
                        description: 'LLM fine-tuning, RAG systems, AI agent development' 
                    },
                    // Add other skills...
                    ],
                    timeline : [
                        {
                            title: 'Lead AI Developer @TechCo',
                            date: '2022 - Present',
                            description: 'Led development of AI-powered SaaS platform with 95% accuracy rate'
                        },
                        {
                            title: 'Full Stack Engineer @Startup',
                            date: '2020 - 2022',
                            description: 'Built scalable web applications with real-time analytics'
                        },
                        {
                            title: 'Computer Science Degree',
                            date: '2016 - 2020',
                            description: 'Specialized in AI and Distributed Systems'
                        }
                        ],
                        Pic: ProfilePic,
                        socialLinks: [
                            { id: 1, icon: 'Github', url: 'https://github.com/hritik1999', label: 'GitHub' },
                            { id: 2, icon: 'Linkedin', url: 'https://www.linkedin.com/in/hritik-gupta-985b371a1/', label: 'LinkedIn' },
                            { id: 3, icon: 'Mail', url: 'mailto:guptahritik1999@gmail.com', label: 'Email' },
                            { id: 4, icon: 'X', url: 'https://x.com/AI_Bhaiiii', label: 'X' },
                        ],
            }
        },
        components: {
        Avatar,
        AvatarImage,
        AvatarFallback,
        Button,
        Download,
        ArrowRight,
        Github,
        Linkedin,
        Mail,
        X,
        Brain
        },
    }
  </script>
  