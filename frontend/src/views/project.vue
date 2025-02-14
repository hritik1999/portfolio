<script>
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent, CardFooter,CardDescription } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Github, ExternalLink, ArrowLeft, Car } from 'lucide-vue-next'
import hireai from '../assets/hire-ai.png'
import whatsapp from '../assets/whatsapp.jpg'
import iit from '../assets/iitbs.jpg'
export default {
  name: 'Projects',
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'Hire-AI : An AI Interviewer',
          description: 'When chatgpt had just launched there api. I had the idea to make an AI interviewer. In the MVP you could paste job desceription and it would generate interview questions. After the interview was done it would evaluate each answer and give marks on various heuristics and put them on a leaderboard. More than 100 people tried it. but i realised that the model was hallucinating. So i had to shut it down. But it was a great learning experience.',
          tech: ['Python', 'Langchain', 'gpt-3', 'streamlit','supabase'],
          codeUrl: 'https://github.com/hritik1999/hire-ai/tree/main',
          image: hireai,
          date: 'september 2023'
        },
        {
          id: 2,
          title: 'Whatsapp Chat Personality Analyser',
          description: 'I made a web app where you could upload your whatsapp chat and it would do personality test of each user in the chat using LLMs. Analysed more than 10 groups and everyone really enjoyed it. It would also give tradition NLP metrics like most active day, most active user , most used word etc.I think This can be product. Many people read horoscopes and personality tests. This can be a fun way to do that. I will most probably make this into a product with integration with all major social media and chat platforms.',
          tech: ['Flask', 'VueJs', 'Langchain', 'GPT-3.5','NLP'],
          codeUrl: 'https://github.com/hritik1999/whatsapp_analyser',
          image: whatsapp,
          date:'April 2024'
        },
        {
            id: 3,
            title: 'IIT,Madras BS degree chatbot',
            description:'I made a RAG based chatbot because it was a hassle to refer to student handbook and grading document for every query i had and was also tired of people asking in groups chats that can be found in those documents. The chatbot would give citations and references for every answer.',
            image: iit,
            tech: ['Flask', 'VueJs', 'RAG','NLP','Langchain','LLama2'],
            date:'May 2024'
        },
        
        // Add more projects as needed
      ]
    }
  },
  components: {
    Button,
    Card,
    CardHeader,
    CardTitle,
    CardContent,
    CardFooter,
    Badge,
    CardDescription,
    Github,
    ExternalLink,
    ArrowLeft
  }
}
</script>

<template>
  <div class="min-h-screen relative overflow-hidden">
    <section class="container mx-auto px-4 py-20 md:py-24">

      <!-- Page Title -->
      <h1 class="text-4xl md:text-5xl font-bold text-center mb-16 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
        My Projects
      </h1>

      <!-- Projects Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Project Card -->
        <Card 
          v-for="project in projects" 
          :key="project.id"
          class="hover:shadow-lg transition-all duration-300 hover:scale-[1.02] group"
        >
          <CardHeader>
            <CardTitle class="">{{ project.title }}</CardTitle>
            <CardDescription class="">{{ project.date }}</CardDescription>
          </CardHeader>
          <CardContent class="space-y-4">
            <!-- Project Image -->
            <div class="relative aspect-video rounded-lg overflow-hidden bg-muted">
              <img 
                :src="project.image" 
                :alt="project.title" 
                class="object-cover w-full h-full hover:scale-100 transition-transform"
              />
            </div>

            <!-- Description with Read More -->
            <div>
                <p 
                    class="text-muted-foreground leading-relaxed transition-all duration-300" 
                    :class="{ 'line-clamp-3': !project.expanded }"
                >
                    {{ project.description }}
                </p>
                <button 
                    @click="project.expanded = !project.expanded" 
                    class="text-blue-500 hover:underline mt-1"
                >
                    {{ project.expanded ? "Read less" : "Read more" }}
                </button>
            </div>

            <!-- Tech Stack -->
            <div class="flex flex-wrap gap-2">
              <Badge 
                v-for="(tech, index) in project.tech" 
                :key="index"
                variant="outline"
                class="text-sm font-mono px-3 py-1 bg-secondary/10"
              >
                {{ tech }}
              </Badge>
            </div>
          </CardContent>

          <!-- Links -->
          <CardFooter class="flex gap-4">
            <Button as-child variant="default" class="gap-2 w-full">
              <a :href="project.codeUrl" target="_blank" rel="noopener">
                <Github class="h-4 w-4" />
                View Code
              </a>
            </Button>
          </CardFooter>
        </Card>
      </div>
    </section>

    <!-- Background Effects -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none -z-10">
      <div class="absolute right-0 top-1/4 h-96 w-96 rounded-full bg-primary/10 blur-3xl"></div>
      <div class="absolute left-0 bottom-1/3 h-80 w-80 rounded-full bg-secondary/10 blur-3xl"></div>
    </div>
  </div>
</template>

<style scoped>
/* Add custom animations if needed */
.group:hover .group-hover\:underline {
  text-decoration: underline;
}
</style>