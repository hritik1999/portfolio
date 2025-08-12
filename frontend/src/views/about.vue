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
                      <!-- Mission & Vision -->
              <section class="grid md:grid-rows-2 gap-8">
              <div class="p-8 rounded-2xl bg-primary/5 border border-primary/20">
                <h3 class="text-2xl font-bold text-primary mb-4">Mission</h3>
                <p class="text-muted-foreground" id="text">
                  My mission is to experiment with cutting-edge AI technologies and build innovative solutions.
                  Find new ways to leverage AI to make a positive impact on society.
                </p>
              </div>
              <div class="p-8 rounded-2xl bg-secondary/5 border border-primary/20">
                <h3 class="text-2xl font-bold mb-4">Vision</h3>
                <p class="text-muted-foreground" id="text">
                  I envision a future where AI is used to unleash human creativity and potential.
                  Build a world where AI is accessible to everyone and used to create a better future for all.
                </p>
              </div>
            </section>
          </div>
  
          <!-- Content Column -->
          <div class="space-y-20">
            <!-- Introduction Section -->
            <section class="space-y-6">
              <h2 class="text-4xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                Who Am I?
              </h2>
              <div class="space-y-4 text-lg text-muted-foreground" id="text">
                <p>I’m Hritik Gupta, 25 years old, and as of now—accomplishments? Nothing. Since I was a kid, my only passion has been creating new things and becoming an entrepreneur. To chase that dream, I spent the last 20 years mostly daydreaming, thinking big, and ignoring almost every other aspect of life.</p>
                <p>As a result, I now find myself with a shallow understanding of many things but deep expertise in none. I’m not employable in the traditional sense—but entrepreneurship? That’s something I can still pursue. I have a ton of ideas and a little knowledge about domains ranging from product design and development to marketing and finance.</p>
                <p class="font-semibold text-primary">My plan is simple: keep launching products until one of them succeeds.</p>
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
                      <p class="text-sm text-muted-foreground" id="text">{{ skill.description }}</p>
                      <div class="flex flex-wrap gap-2 mt-1">
                        <div v-for="label in skill.labels" :key="label">
                          <Badge variant="secondary" class="text-xs text-primary">{{ label }}</Badge>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
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
                  <p class="text-muted-foreground" id="text">{{ item.description }}</p>
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
            <h3 class="text-3xl font-bold text-foreground" id="text">Ready to Create Magic?</h3>
            <p class="text-lg text-muted-foreground max-w-2xl mx-auto" id="text">
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
import { Download, ArrowRight,Github, Linkedin, Mail,X,Brain,Server,Monitor,Cloud } from 'lucide-vue-next';
import ProfilePic from '../assets/IMG_8346.jpg'
import {Badge} from '@/components/ui/badge';

    export default {
        name: 'About',
        data() {
            return {
                quickStats :[
                    { label: 'Anime\'s watched', value: '100+' },
                    { label: 'Books read', value: '50+' },
                    { label: 'Unfinished Projects', value: '20+' },
                    { label: 'Ambition', value: '100+'}
                    ],
                skills : [
                    { 
                        name: 'Generative AI', 
                        icon: 'Brain',
                        description: 'LLM fine-tuning, RAG systems, AI agent development',
                        labels: ['OPENAI', 'HuggingFace', 'Langchain','PyTorch'] 
                    },
                    {
                      name: 'Backend Development',
                      icon: 'Server',
                      description: "Building scalable APIs, microservices, and serverless functions",
                      labels: ['flask','Redis','SQL','RestAPI','DBA']
                    },
                    {
                      name: 'Frontend Development',
                      icon: 'Monitor',
                      description: "Crafting responsive web applications with modern frameworks",
                      labels: ['Vue','Shadcn','TailwindCSS','Bootstrap','JavaScript','HTML','CSS']
                    },
                    {
                      name: 'DevOps & Cloud',
                      icon: 'Cloud',
                      description: "Automating CI/CD pipelines, containerization, and cloud deployments",
                      labels: ['Docker','AWS','Git','CI/CD']
                    },
                    {
                      name: 'Machine Learning & Deeplearning',
                      icon: 'Brain',
                      description: "Training models, data preprocessing, and model evaluation",
                      labels: ['Scikit-learn','Pytorch','Pandas','Numpy','Matplotlib','Seaborn']
                    },
                    {
                      name: 'Communication Skills',
                      icon: 'MessageSquareText',
                      description: "Presenting technical concepts, leading teams, and writing documentation",
                      labels: ['Public Speaking','Technical Writing','Team Leadership','Marketing','Design Thinking']
                    }
                    ],
                    timeline : [
                        {
                            title: 'Born',
                            date: '09-november-1999',
                            description: 'In Allahabad,UP and raised in Assam.',
                        },
                        {
                            title: 'Schooling',
                            date: '2004-2018',
                            description: 'Was severely bullied in school, So its all a blank dont remember any thing from this time.',
                        },
                        {
                            title: 'Bachelor of Technology in Computer science Engineering, Sharda University',
                            date: '2018-2019',
                            description: 'Was asked to repeat first year due to low attendance dispite of having good grades.So had to drop out but enjoyed it a lot.',
                        },
                        {
                            title: 'Bachelors of Business Administration, Sharda University',
                            date: 'august,2019 - july,2021',
                            description: 'Joined to learn about business learned that business school don\'t teach you business they do business! But had complete it.',
                        },
                        {
                          title:'First try at entrepreneurship',
                          date:'2020-2021',
                          description:"Started a gaming startup with my friends, failed miserably but Got into Influencer marketing made money, met youtubers but it was not my thing.",
                        },
                        {
                          title:'BS in Data Science and AI, IIT,Madras',
                          date:'April,2021-current',
                          description:"Joined this degree to follow my passion of tech. Enjoyed learning maths,stats,web development,ML and AI.",
                        },
                        {
                          title:'Master in Business Administration, Calcutta Business School , West Bengal',
                          date:' august,2022 - july, 2024',
                          description:"After BBA apperently it is compulsory to do MBA. After few fights with my parents I joined this college. Sucked a lot of my time but thankfully i am done with it.",
                        },
                        {
                          title:'AI Developer, Arkca Corporate Solutions',
                          date:'august,2023- august,2024',
                          description:"Joined as a AI developer, worked on various projects and learned a lot.",
                        },
                        {
                          title:'AI engineer Contract, Quicksand design Studio',
                          date:'september,2024 - February,2025',
                          description:'Quicksand is a consulting firm with over 15 year experience and I was hired to develop a RAG Chatbot over all their projects.It Challenging but fun.',
                        },
                        {
                          title:'Solo Entrepreneur',
                          date:'March,2025 - Present',
                          description:'Instead of getting a job.I am just gonna build products and see where it takes me! My first product will be launched Soon!',
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
        Brain,
        MessageSquareText,
        Badge,
        Server,
        Monitor,
        Cloud,
        },
    }
  </script>
  