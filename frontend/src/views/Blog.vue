<script>
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ArrowLeft } from 'lucide-vue-next';

export default {
  name: 'Blog',
  components: {
    Button,
    Card,
    CardHeader,
    CardTitle,
    CardContent,
    CardFooter,
    Badge,
    ArrowLeft,
  },
  data() {
    return {
      posts: [
        {
          id: 1,
          slug: '100-days-of-entrepreneurship-day-1', // <-- Added slug
          title: '100 Days of Entrepreneurship',
          date: 'July 29, 2025',
          day: 1,
          snippet: 'I’m Hritik Gupta, 25 years old, and as of now—accomplishments? Nothing. Since I was a kid, my only passion has been creating new things and becoming an entrepreneur.',
          content: `
            <p>Hello readers,</p>
            <p>I’m Hritik Gupta, 25 years old, and as of now—accomplishments? Nothing. Since I was a kid, my only passion has been creating new things and becoming an entrepreneur. To chase that dream, I spent the last 20 years mostly daydreaming, thinking big, and ignoring almost every other aspect of life.</p>
            <p>As a result, I now find myself with a shallow understanding of many things but deep expertise in none. I’m not employable in the traditional sense—but entrepreneurship? That’s something I can still pursue. I have a ton of ideas and a little knowledge about domains ranging from product design and development to marketing and finance.</p>
            <p class="font-semibold text-primary">My plan is simple: keep launching products until one of them succeeds.</p>
            <p>The first product I started with is an ambitious one—driven by the dream of changing entertainment as we know it. The initial idea was an interactive storytelling platform where users could participate in their favorite shows by joining a group chat with AI characters. Unlike platforms like Character.ai or CHAI, this wouldn’t be random—it would follow a proper story from beginning to end.</p>
            <p>You could create any show by just giving it a name and clicking a button. You could then create episodes by typing out an idea like “Joey gets nominated for an Oscar” and actually play that episode as a character. I thought it was a wild idea—something that would go viral instantly, make me famous, and turn me into a millionaire.</p>
            <p>So, I spent March and April building the prototype, which was ready by May. I launched it and shared it wherever I thought it was relevant. But by the end of May, all I had managed was 135 users—most of them one-time visitors.</p>
            <p>I assumed it was because it was a web app, so I started building a mobile version. That too failed.</p>
            <p>Then I went through the chat data and noticed that while users weren’t interacting much, they were completing the chats. This led me to an important realization: people were interested in reading the stories, not interacting with them.</p>
            <p>So I decided to pivot—to turn the app into a fan fiction storytelling platform. Users could create episodes, and those episodes would be transformed into podcasts, basic videos, and comics. The interactive version would still exist, but the focus would shift.</p>
            <p>This sparked new hope.</p>
            <p>Then in June, I went to Chennai to collect my degree. But there, I started experiencing unbearable pain in my lower back. When I got back and visited the doctor, it turned out to be Pilonidal Sinus, and I needed immediate surgery.</p>
            <p>After the surgery came two months of bedrest. The first month, I couldn’t do anything. The second month—July—I could sit and work, but instead, I spent my days doomscrolling and watching Netflix. I didn’t understand why I wasn’t working. Why was I wasting so much time?</p>
            <p>It wasn’t until I read <em class="italic text-primary/90">Tiny Experiments</em> by Anne-Laure Le Cunff that it clicked. I had been focusing too much on outcomes, and my first failure had scared me. The book teaches that we should shift our focus from results to the work itself. When we do that, the fear and anxiety subside, and procrastination goes away. The easiest way to implement this? Create a commitment like this one: 100 Days of Entrepreneurship.</p>
            <p class="font-semibold text-primary">Now, I don’t care about the outcome—I'm just showing up and doing the work, driven by curiosity, not results. Every day, for the next 100 days, I’ll write a blog.</p>
            <p>Today is Day 1.</p>
            <p>I’m kicking things off by reviewing all the work I did before I fell sick, making a future roadmap, and going through the chat data from those 135 users (not all of them today, but gradually). My goal is to revamp the app into a fan-based storytelling platform. Here’s what I plan to add:</p>
            <ul class="list-disc list-inside space-y-2 pl-4">
              <li>Voice cloning and an audio version of the stories</li>
              <li>A comic version</li>
              <li>A video version using Veo 3 and Heygen AI</li>
              <li>Launch the app on the App Store and Play Store using Capacitor.js</li>
              <li>Improve the UI to make it more intuitive</li>
              <li>Add a basic tutorial for first-time users</li>
            </ul>
            <p class="font-bold text-center pt-4">Let the journey begin.</p>
          `
        }
        // Future blog posts will be added here with their own unique slug
      ]
    };
  },
  computed: {
    // This computed property finds the post that matches the slug in the URL
    currentPost() {
      const slug = this.$route.params.slug;
      if (!slug) return null;
      return this.posts.find(post => post.slug === slug);
    }
  },
  // We no longer need the 'methods' block for selectPost/goBack
}
</script>

<template>
  <div class="min-h-screen relative overflow-hidden bg-background py-20 md:py-24">
    <div class="container mx-auto px-4">
      <main class="max-w-4xl mx-auto">
        <div v-if="currentPost">
          <Button as-child variant="outline" class="mb-8 gap-2">
            <RouterLink to="/blog">
              <ArrowLeft class="h-4 w-4" />
              Back to Blog List
            </RouterLink>
          </Button>
          <Card class="w-full shadow-lg">
            <CardHeader class="p-8 md:p-12">
              <CardTitle class="text-4xl md:text-5xl font-bold text-center mb-4 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent" id="text">
                {{ currentPost.title }}
              </CardTitle>
              <div class="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-muted-foreground mt-4">
                <span>By Hritik Gupta</span>
                <span class="hidden md:inline">|</span>
                <span>Published on {{ currentPost.date }}</span>
                <Badge variant="secondary" class="ml-2">Day {{ currentPost.day }}</Badge>
              </div>
            </CardHeader>
            <CardContent class="p-8 md:p-12 text-lg text-foreground/90 leading-relaxed space-y-6" v-html="currentPost.content" id="text">
            </CardContent>
          </Card>
        </div>

        <div v-else>
          <h1 class="text-5xl font-bold text-center mb-12 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
            My Blog
          </h1>
          <div class="space-y-8">
            <Card v-for="post in posts" :key="post.id" class="hover:shadow-xl transition-shadow duration-300">
               <RouterLink :to="'/blog/' + post.slug" class="block">
                <CardHeader>
                  <CardTitle class="text-2xl font-bold group-hover:text-primary">{{ post.title }}</CardTitle>
                  <div class="flex items-center gap-4 text-sm text-muted-foreground pt-2">
                    <span>{{ post.date }}</span>
                    <Badge variant="outline">Day {{ post.day }}</Badge>
                  </div>
                </CardHeader>
                <CardContent>
                  <p class="text-muted-foreground">{{ post.snippet }}</p>
                </CardContent>
                <CardFooter>
                   <p class="text-primary font-semibold">Read More &rarr;</p>
                </CardFooter>
              </RouterLink>
            </Card>
          </div>
        </div>
      </main>
    </div>

    <div class="absolute inset-0 -z-10 overflow-hidden pointer-events-none">
      <div class="absolute right-20 top-1/3 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
      <div class="absolute left-32 bottom-1/4 h-64 w-64 rounded-full bg-secondary/10 blur-3xl"></div>
    </div>
  </div>
</template>