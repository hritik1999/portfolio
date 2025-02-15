<script>
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent, CardFooter,CardDescription } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Github, ExternalLink, ArrowLeft, Car } from 'lucide-vue-next'
import hireai from '../assets/hire-ai.png'
import whatsapp from '../assets/whatsapp.jpg'
import iit from '../assets/iitbs.jpg'
import portfolio from '../assets/portfolio.png'
import billet from '../assets/billet.png'
import jupyter from '../assets/jupyter.png'
import kaggle from '../assets/kaggle.png'
import musicapp from '../assets/musicapp.png'  

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
            codeUrl:'https://github.com/hritik1999/IITMBS_RAG',
            date:'May 2024'
        },
        {
            id:4,
            title:'Fully Customizable Portfolio site',
            description:'This site has features to change the tone and style of the site making it fully customizable. I primarily made this site to learn who make visually appealing websties using shadcn and tailwind and how to deploy websties and buy domain names.So if you are seeing this then i was successful Yaay!',
            image:portfolio,
            codeUrl:'https://github.com/hritik1999/portfolio/tree/main',
            tech:['VueJs','Tailwind','Vite','Shadcn-vue','Flask','OPENAI-GPT-4o-mini'],
            date:'Febuary 2025'
        },
        {
            id:5,
            title:'Billet price prediction',
            date:'Febuary 2024',
            description:'Billet is the most important raw material in the steel industry. The price of billet is very volatile and is dependent on many factors like demand, supply, raw material prices, etc. I made a model that predicts the price of billet for the next 30 days. The model had only 200 RSME error in test set and was used by incredible industries to make decisions. They saved around 45 Lakh rupees in 1 months.',
            tech:['Scikitlearn','LSTM','ARIMA','Prophet','Matplotlib','Pandas','Numpy','SHAP'],
            codeUrl:'https://github.com/hritik1999/Billet-prediction/tree/main',
            image:billet
        },
        {
            id:6,
            title:'Video summarizer using VLLMs',
            date:'July 2024',
            description:'With new LLMs coming with image ability i wanted to try them out. So i made a video summarizer that would take a video of any length and give a summary of the video.',
            tech:['OPENAI','VLLMs','OPENCV'],
            codeUrl:'https://github.com/hritik1999/video-summarizer/tree/main',
            image:jupyter
        },
        {
            id:7,
            title:'Predict ratings of food using recipe- Kaggle',
            date:'January 2024',
            description:'This was my first kaggle competition. The task was to predict the ratings of food items using reviews.I learned about my competitive spirit then put my everything in it to be in the top 3 out of 1000 participants. Went through many notebooks and learned a lot about feature engineering and model selection.',
            tech:['Scikitlearn','XGBoost','LightGBM','Pandas','Numpy','Matplotlib','Seaborn'],
            codeUrl:'https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/21f1000564-notebook-t12024-81bc8104-62bb-41a2-a4ad-90735eab2275.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20250214/auto/storage/goog4_request%26X-Goog-Date%3D20250214T130328Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3Da4dffa37407af2877566e879390e919b650261f07f2d9784d0d448f638fd5922211babed20a661712b6285df74c117ce1e5263f0ce5eeef929221261f857f1a821eb75a8404160ed2f0186d32810ddf4908c6184ca477df93605b07954ea60afcc3121eedf45644aa97ffb0fa3d8b31bb9212942ee9cd67a1b63cbc1a22a21fb7f7ca0f1d2a522efa2523b39f418d27cf0d69b36791246090e8b4b7f61dc0670644d60cbc6ad0a181a035140bf881957c59341aee84f2939988d829ef82eb84af7d89d4b54e9f947c1bf4e31b4b6d6e67ae77e96b7ac7aafc865463969f2590037ed80e0ec0644752a7b51094b5379154a05a2754c930c78e6a6fbc43daa7a5d',
            image:kaggle
        },
        {
            id:8,
            title:'Fine tuning Resnet to predict animals species: Kaggle',
            date:'december 2024',
            description:'Learned how to use pytorch and fine tune models. The task was to predict the species of animals. I was in top 5 of the competition out of 200. I learned a lot about fine tuning and data augmentation.',
            tech:['Pytorch','Resnet','Pandas','Numpy','Matplotlib','Seaborn'],
            codeUrl:'https://www.kaggle.com/code/hritik1999/21f1000564',
            image:kaggle
        },
        {
            id:9,
            title:'Image upscaling and denoising: Kaggle',
            date:'Decemeber 2024',
            description:'The task was to upscale and denoise images. I learned about image processing and how to use GANs for image processing. I was in rankk 1 of the competition out of 200. I learned a lot about GANs and image processing.',
            tech:['Pytorch','GANs','Pandas','Numpy','Matplotlib','Seaborn'],
            codeUrl:'https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/denoising-upscaling-381b369d-ef55-4f0b-850b-bbfd1f8e2d48.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20250214/auto/storage/goog4_request%26X-Goog-Date%3D20250214T131018Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3Da8470020e480c3b1d65e6a28d98f31655323c0af8ef952e2c6f17662b1ea207f977cbfc4f7314bb033d0828f5a95b7cb91bcb1fa0c986f7964d695eaf1c11cb07e1ee588e1ee8fc1f16a8c202bc14948d35c71be6f5fd999e9ed4a6935a1a9b0f5aaf2456ada3964ae14a24e3ceb2b2a9619dd997e65c1f659eed1dc24b093fcdf4b07ec4aea8842283e0ee8b2ad6a6a9924de8955386d116840f1175c8266413725e7f6c161d7b79b53a0d87479b2297f1d41e51937847c40415419005d8ba2d3db006f9c08b7459f2895529ac4c3c53e5ee7af3d8328155c981a65c2cdfad171f5b9982c8ffc0b3aeaa0008c189f4127814b9482b87a73b59815d56d483c99',
            image:kaggle
        },
        {
            id:10,
            title:'Music app',
            date:'december 2023',
            description:'This first full stack i made for my web development course. It was a music app where you could upload music and listen to them.It had everything a full fledge app had like authentication, authorization,rolebased access, database, file upload, reactivity, Single Page application etc. I learned a lot about web development, struggled a lot but loved it. ',
            tech:['VueJs','Flask','SQLAlchemy','MYSQL','Vuetify','JWT','Flask-Login','Flask-Admin','Redis'],
            codeUrl:'https://github.com/hritik1999/music-app' ,
            image:musicapp
        },
        {
            id:11,
            title:'Implemented Naive Bayes from Scratch to predict spam emails',
            date:'december 2022',
            description:'I implemented Naive Bayes from scratch to predict spam emails. I learned a lot about probability and statistics. I was able to achieve 98% accuracy on the test set.',
            tech:['Python','Numpy','Pandas','Matplotlib'],
            codeUrl:'',
            image:jupyter
        }

        
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