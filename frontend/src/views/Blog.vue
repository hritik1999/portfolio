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
          title: '100 Days of Entrepreneurship Day 1',
          date: 'July 29, 2025',
          day: 1,
          snippet: 'I’m Hritik Gupta, 25 years old, and as of now—accomplishments? Nothing. Since I was a kid, my only passion has been creating new things and becoming an entrepreneur.',
          content: `
            <p>Hello readers,</p>
            <p>I’m Hritik Gupta, 25 years old, and as of now—accomplishments? Nothing. Since I was a kid, my only passion has been creating new things and becoming an entrepreneur. To chase that dream, I spent the last 20 years mostly daydreaming, thinking big, and ignoring almost every other aspect of life.</p>
            <p>As a result, I now find myself with a shallow understanding of many things but deep expertise in none. I’m not employable in the traditional sense—but entrepreneurship? That’s something I can still pursue. I have a ton of ideas and a little knowledge about domains ranging from product design and development to marketing and finance.</p>
            <p class="font-semibold text-primary">My plan is simple: keep launching products until one of them succeeds.</p>
            <p>The first product I started with is an ambitious one—driven by the dream of changing entertainment as we know it. , The initial idea was an interactive storytelling platform where users could participate in their favorite shows by joining a group chat with AI characters. Unlike platforms like Character.ai or CHAI, this wouldn’t be random—it would follow a proper story from beginning to end.I called it <a href="https://sitchat.ai" target="_blank" rel="noopener noreferrer" class="font-semibold text-primary hover:underline">Sitchat.ai</a> You know Sitcom but with Chat</p>
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
        },
        {
          id: 2,
          title:'100 Days of Entrepreneurship Day 2',
          slug: '100-days-of-entrepreneurship-day-2',
          day: 2,
          date: 'July 30, 2025',
          snippet: 'On the first day, we made some very big and ambitious plans—and on day two, when it was time to actually start working, those plans came crashing down.',
          content: `
            <p>Hello readers,</p>

    <p>On the first day, I made some very big and ambitious plans. But on Day 2, when it was time to actually work, those plans came crashing down.</p>

    <p>I started off my day with some sitcom and breakfast. The sitcom lasted a little longer than it should have, but then I remembered that I’ve committed to writing for 100 days and I need content for that. So I sat down with my laptop to run the code and start working again after a 2-month break.</p>

    <p>Well, the code threw a bunch of errors for some goddamn unknown reason—despite working perfectly the last time I ran it. It seemed like dependency issues, both in the frontend and backend. So I did what all programmers do in this era—I turned to ChatGPT. It gave me some commands, and the errors changed. This went on for an hour. Eventually, I deleted the code, recloned it from my GitHub repo, set up the environment again, and finally, the code worked.</p>

    <p>That was enough programming for me for the day.</p>

    <p>Next, I decided to do some research on what I’ll need and how I plan to implement things. I’d found a guy on Reddit who built an app to create short-form videos. I tried it out to figure out how it works. The most interesting concept I found there was “storyboarding,” which apparently is a standard procedure in the video industry. It’s like a roadmap for video creation.</p>

    <p>Then I dug into video models. Turns out, these models can only generate 5 to 20-second clips at a time—and even those are full of errors and need multiple attempts. Only a few models can generate both video and audio. They’re also extremely expensive. So, creating a 20-minute sitcom episode is pretty much algorithmically impossible right now.</p>

    <p>Next, I found some models that can generate lip-synced videos using a character image. So, for the initial version, I could just have videos of the characters speaking their dialogues one by one.</p>

    <p>Then I looked into audio models. This space is super competitive. Currently, Eleven Labs offers a model where you can control a lot of parameters like emotions and emphasis in the speech. This could help add realism to the episodes.</p>

    <p>But then came another hurdle: voice cloning. It's an ethically grey area. I could use models where cloning is easier, but the quality wouldn’t be great. Another option is RVC models that can change the voice of any audio. I could use them to change the Eleven Labs-generated audio so that it sounds like the actual characters. But that would require a lot of testing.</p>

    <p>On the bright side, comics are a well-established use case for image generation models, so that part should be easy.</p>

    <p>That was most of my day.</p>

    <p>Then came the part that felt like it lasted forever—reading the chats to understand what can be improved in the storytelling. I don’t know why, but I just couldn’t stay focused. Coincidentally, around the same time, my friend Naman, my mom, and my girlfriend all remembered I existed and needed to talk to me. As someone who has a hard time saying no, I entertained them all.</p>

    <p>So, with my interrupted analysis session, I discovered that my stories have repeated dialogues, many plotlines don’t make sense, the chats over-focus on the player—but somehow also ignore them just to push the story forward. Sometimes, it even sends a message <em>from</em> the player just to progress the story (amazing). Half the time, even I didn’t know what the story was trying to say.</p>

    <p>That was a bit depressing. The core part of my tech sucks ass.</p>

    <p>These are things that <strong>can</strong> be fixed, and this is where I should really be spending most of my time. But I know I’ll probably drift off chasing some shiny new feature.</p>

    <p>After all this, I somehow found myself watching sitcoms again—which I tell myself is part of developing “Sitchat” 😂.</p>

    <p>For tomorrow, I think I should focus on developing the mobile app since that will take time to get through the approval and bug-fixing cycle. But honestly, I don’t want to do that right now—it’s tedious and not fun. I <em>want</em> to work on audio, video, and comics. The cool, fun stuff. But unfortunately, the boring stuff like fixing the chat and building the mobile app is way more important.</p>

    <p>Well, I’ll see what mood I wake up in and go from there.</p>
            `
        },
        {
          id:3,
          title:'100 days of entrepreneurship day 3',
          slug:'100-days-of-entrepreneurship-day-3',
          day:3,
          date:'July 31, 2025',
          snippet:'It’s the third day, and I’ve already failed. I procrastinated the whole day—but that doesn’t mean I’ve lost.',
          content:`
          <p>Hello readers,</p>

  <p>It’s the third day, and I’ve already failed. I procrastinated the whole day—but that doesn’t mean I’ve lost.</p>

  <p>I didn’t get a good night’s sleep yesterday and woke up feeling very tired. This happens from time to time, and I usually manage. But the biggest mistake was starting <em>The Studio</em>. The first episode had me hooked, and I couldn’t stop. I ended up binge-watching the whole show. I felt deeply guilty about it, as I broke my commitment on just the third day.</p>

  <p>I also read a chapter about procrastination in the book <em>Tiny Experiments</em>. According to it, we often treat procrastination as an enemy—but it’s not. It’s a messenger. We should listen to it instead of feeling guilty or treating it as something to fight against.</p>

  <p>That’s hard to do, though.</p>

  <p>To make it a bit easier, the book suggests a “Triple Check” based on a study about motivation. There are three factors that affect our motivation to do something:</p>

  <ul>
    <li><strong>Head</strong> – Is it logical/appropriate to do the task?</li>
    <li><strong>Heart</strong> – Is it exciting for us?</li>
    <li><strong>Hand</strong> – Can we do it? (i.e., do we have the skills?)</li>
  </ul>

  <p>The suggested solutions are:</p>
  <ul>
    <li>Refine the strategy (Head)</li>
    <li>Redesign the experience (Heart)</li>
    <li>Upskill or take help (Hand)</li>
  </ul>

  <p>It also mentioned that other factors like sleep and overall health can influence motivation too.</p>

  <p>So based on that, I tried to understand why I was actually procrastinating—instead of drowning in negative self-talk about how useless I am.</p>

  <ul>
    <li><strong>Head</strong>: It’s logical and appropriate for me to work on this; this is my career.</li>
    <li><strong>Heart</strong>: Just the idea of publishing on the App Store excites me.</li>
    <li><strong>Hand</strong>: This is where I think I’m struggling. I don’t feel confident that I can actually do it.</li>
  </ul>

  <p>To overcome this, I realized I need to learn whatever I want to implement. I had tried using AI previously to develop an app, but I kept running into errors and wasted weeks without significant progress. Maybe that’s why I was hesitant to move forward this time.</p>

  <p>So, I’ve decided to start learning Capacitor.js using tutorial videos.</p>

  <p>Then I remembered—I’m also a student who hasn’t studied for the past two months, missed my first exam, and has another exam coming up on Sunday. The sheer volume of what I need to study overwhelmed me, and I continued to procrastinate instead of getting started.</p>

  <p>So until the exam is over, there probably won’t be much progress on the app front.</p>

  <p>At midnight, the guilt had really piled up. So I got up and decided to do <em>something</em> related to my product. I used Veo 3 to create a few clips and see how it works. I also created an account on ElevenLabs to explore voice cloning, its quality, and capabilities. That gave me some peace of mind.</p>

  <p>Well, let’s hope Day 4 turns out better than Day 3.</p>
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
          <h1 class="text-5xl font-bold text-center mb-12 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent" id="text">
            My Blog
          </h1>
          <div class="space-y-8">
            <Card v-for="post in posts" :key="post.id" class="hover:shadow-xl transition-shadow duration-300">
               <RouterLink :to="'/blog/' + post.slug" class="block">
                <CardHeader>
                  <CardTitle class="text-2xl font-bold group-hover:text-primary" id="text">{{ post.title }}</CardTitle>
                  <div class="flex items-center gap-4 text-sm text-muted-foreground pt-2">
                    <span>{{ post.date }}</span>
                    <Badge variant="outline">Day {{ post.day }}</Badge>
                  </div>
                </CardHeader>
                <CardContent>
                  <p class="text-muted-foreground" id="text">{{ post.snippet }}</p>
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