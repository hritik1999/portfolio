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
        },
        {
          id:4,
          title:'100 days of entrepreneurship day 4',
          slug:'100-days-of-entrepreneurship-day-4',
          day:4,
          date:'August 1, 2025',
          snippet:'I thought studying for my exam would be a distraction from my goals, but the subject Design Thinking turned out to be more relevant to my journey than anything else.',
          content:`
          <p>Hello readers,</p>

  <p>I thought studying for my exam would be a distraction from my goals, but the subject <em>Design Thinking</em> turned out to be more relevant to my journey than anything else. I dropped all my other courses except this one, and I’m glad I didn’t drop it.</p>

  <p>Although I did mess up by not submitting the assignments on time, and I might fail this term, the learning itself is what truly matters.</p>

  <p>This course is based on the book <em>Karmic Design Thinking</em>, and the professor teaching it is the author of the book. I had heard of it before—it’s held in high regard. The course focuses on human-centric product design and is structured around four key phases: <strong>Empathize</strong>, <strong>Analyze</strong>, <strong>Solve</strong>, and <strong>Test</strong>.</p>

  <p>In the <strong>Empathize</strong> phase, we create user personas and customer journeys to understand our users as deeply as possible. The goal is to empathize with them. .</p>

  <p>Next, in the <strong>Analyze</strong> phase, we question the problem by conducting a multi-why analysis, which involves asking <em>why</em> repeatedly until we reach the root cause. This is best done with an expert or the user themselves for the most accurate insights.Then, we ask the question: <em>“How might we help them?”</em>—across different points in their journey and using the analysis we did—without jumping to solutions, just focusing on questions</p>

  <p>In the <strong>Solve</strong> stage, we conduct silent brainstorming—each team member contributes ideas in writing. Then we analyze those ideas and develop a final product concept.</p>

  <p>Finally, in the <strong>Test</strong> phase, we create a prototype and test it with real users. We observe them, revise our assumptions, and update the customer journey map. The cycle is then repeated to further refine the product.</p>

  <p>I never did any of this for my startup idea. Maybe I should have. It would’ve given me a clearer direction rather than just following what I <em>thought</em> was right. The concepts are simple and intuitive, but I imagine they’ll be challenging to apply effectively.</p>

  <p>Let’s see—I’ll try to incorporate what I’ve learned into my journey after exams are over.</p>

  <p>Tomorrow, I’ll be studying again, so there won’t be much progress on the startup front. But I promise that once the exams are done, I’ll give my full focus to it.</p>
          `
        },
        {
          id:5,
          title:'100 days of entrepreneurship day 5-10',
          slug:'100-days-of-entrepreneurship-day-5-10',
          day:'5-10',
          date:'August 7, 2025',
          snippet:'Why is it that whenever we want to do something, some unexpected problem comes up to derail us? Or are we self-sabotaging?',
          content:`
          <p>Hello readers,</p>
    <p>Why is it that whenever we want to do something, some unexpected problem comes up to derail us? Or are we self-sabotaging?</p>

    <p><strong>2nd August:</strong> I spent the day studying for the exam and went through previous years’ papers while also binge-watching <em>Foundation</em>. Apple TV is on a whole other level.</p>

    <p><strong>3rd August:</strong> I gave the exam and it went excellently well. But I still might not clear the subject because I forgot to update the sheet at the right time. I’ve sent an email to support—hopefully, this gets fixed. Apparently, it was Friendship Day too. So, plans were made: dinner, a movie, drinks. I thought, “It’s Sunday and Friendship Day, why not enjoy?” And enjoy I did.</p>

    <p><strong>4th August:</strong> I woke up feeling normal. But in the afternoon, after eating, I started feeling gassy—uncomfortably so, even while just moving around. It was my first time experiencing gas, and now I understand why people complain about it so much. I didn’t take any meds because I believe they should be a last resort. But in the evening, I puked, and while the gas was gone, a much bigger problem started: food poisoning.</p>

    <p>If I drank water, I’d puke. There was constant diarrhea, and a very high fever. On the 5th, I didn’t eat or drink anything. Someone told me I’d suffer from severe dehydration if I kept that up, so I got some ORS and drank it. Before that, I genuinely felt like I was going to die.</p>

    <p><strong>6th August:</strong> The fever had almost gone. I felt weak, had no appetite, but I was slowly getting better. What fascinated me most was seeing this reflected in the data from my Whoop band. My recovery hit <strong>1%</strong> for two days straight. I hope I never see that again, but it was interesting to witness it in data form.</p>

    <p>By evening, I was feeling better. I couldn’t eat much, but I managed a cup of khichdi and a few litres of ORS. I decided to meet my friend <strong>Harshal Bhaiya</strong>, who was visiting my town after a long time. He used to live here but doesn’t anymore.</p>

    <p>While catching up, the conversation got serious. He told me things I needed to hear. He asked me what I’m doing with my life and how I plan to live like this. He reminded me I can’t keep living off my father’s income. I’m 25—I need to become self-resilient. It’s high time.</p>

    <p>He was right. His words hit me in a way I can’t explain. I often think about productivity and why I can’t stay consistent, but I never really thought about <em>why</em> it’s important. If I don’t become self-resilient, who’s going to take care of my family? Not my friends, not the TV shows I watch, not the games I play. I <strong>have</strong> to become capable. There is no other option.</p>

    <p>With this perspective shift, it’s becoming easier to prioritize.</p>

    <p><strong>7th August:</strong> I’m writing this today. I’m going to focus on completing and launching the mobile app as soon as possible. After that, I’ll begin redesigning it. No more delays. No more wasting time.</p>

    <p>My friend also made me realize something else: I can’t do this alone, no matter how much I believe I can. Companies like Netflix are spending billions every year to create content—and here I am, thinking I can do it solo without spending anything. That’s not realistic. I’ll make the MVP myself, but once that’s done, I’ll shift my focus to gaining traction and securing funding.</p>

    <p>For the 5 days I lost, I’m going to write 5 more blog posts. At this point, this isn’t even an entrepreneurship blog anymore—it’s about my life now 😭</p>

          `
        },
        {
          id:6,
          title:'100 days of entrepreneurship day 11',
          slug:'100-days-of-entrepreneurship-day-11',
          day:'11',
          date:'August 8, 2025',
          snippet:'So, the work has finally started moving at a proper pace now. I’m still lazing around, but I’m managing to cover a significant amount of work.',
          content:`
                <p>Hello readers,</p>

      <p>So, the work has finally started moving at a proper pace now. I’m still lazing around, but I’m managing to cover a significant amount of work. Before the surgery, I had wasted a week trying to get the login to work in the mobile app using my current web implementation. I tried a browser plugin for it, but it didn’t work. Most of that code is gone now, and I thought, <em>let’s explore some other methods.</em></p>

      <p>I found one that’s simple yet works perfectly. Google login is done; now I just need to implement Apple login. But for some reason, I can’t log in to my Apple account. Well, I’ll figure it out.</p>

      <p>Aside from login, I think the rest of the features should work as is, since I kept mobile compatibility in mind the whole time while coding the web app. Let’s see if that holds true.</p>

      <p>The rest of the day, I spent playing with GPT-5. I implemented it in Sitchat, but it was too slow. The story has improved a little, though. Let’s see what happens when we modify the prompt to fit GPT-5 better, but the promises made by OpenAI give me high hopes.</p>
          `
        },
        {
          id:7,
          title:'100 days of entrepreneurship day 12',
          slug:'100-days-of-entrepreneurship-day-12',
          day:'12',
          date:'August 9, 2025',
          snippet:'<p>I’ve decided—fuck it—I’m taking a break from SitChat. I still believe in the idea with my whole heart, but right now, something else is sparking my interest. Another idea.</p>',
          content:`
          <p>Hello readers,</p>

    <p>I’ve decided—fuck it—I’m taking a break from SitChat. I still believe in the idea with my whole heart, but right now, something else is sparking my interest. Another idea.</p>

    <p>This is something I thought of a long time ago, and it’s something I’m personally passionate about. I want to create an app where you can upload your chat history, and it will do a personality analysis—MBTI, alignment, Enneagram, etc. I know this works because I’ve had friends who use ChatGPT a lot ask it to guess their type, and it’s been surprisingly accurate. It works even better than standard tests because it doesn’t rely on the person’s self-awareness.</p>

    <p>For privacy concerns, I won’t save any chats, and I’ll use open-source models. The app will support chats from all platforms—Facebook, Slack, Discord, everything.</p>

    <p>I’ve been wanting to build this for a few weeks now, but I didn’t want to stop working on SitChat. I was afraid that if I started this, I’d forget about SitChat. It’s been weighing on me—forcing myself to work on SitChat when all I really wanted was to build this new thing.</p>

    <p>Yesterday, during my regular drive with Naman, I shared my thoughts. He asked how long it would take to build, and I said, “One week.” He told me, “Take a break and work on this idea—it has potential.” Hearing that reassured me that pausing SitChat wasn’t a bad decision. Talking to him is always a good idea. I don’t know why I delayed this for so long.</p>

    <p>Since that chat, I’ve been thinking about names. I came up with many, but the one I liked most was <span class="highlight">VibeType</span>—unfortunately, it’s taken. I thought of <span class="highlight">VibeTyper</span>, but the .com domain is taken and currently used for a voice-to-text AI tool. The .ai domain, however, is available. <span class="highlight">TypeMyVibe</span> is another option. For now, I’ll move ahead with <span class="highlight">VibeTyper.ai</span> until I think of something better.</p>

    <p>Tomorrow, I’m going to start building the app. I’m excited and fired up. I think it could be a viral success—but we’ll see. I’m planning to charge $5 per analysis report.</p>

    <p class="muted">— Ready to ship</p>
          `
        },
        {
          id:8,
          title:'100 days of entrepreneurship day 13',
          slug:'100-days-of-entrepreneurship-day-13',
          day:'13',
          date:'August 10, 2025',
          snippet:'Working on a new idea is always exciting. I made the landing page yesterday and used GPT-5 for it.',
          content:`
          <p>Hello readers,</p>
<p>Working on a new idea is always exciting. I made the landing page yesterday and used GPT-5 for it.</p>
<p>It’s true — GPT-5 feels like the end of frontend developers. The landing page is glorious.</p>
<p>It’s not perfect, but it’s better than anything I could have done myself.</p>
<p>I’ve decided I will be charging $5 for one person’s analysis and I will support all the major websites.</p>
<p>One of my concerns is that people might be too lazy to export their chats and upload them, but there’s only one way to find out.</p>
<p>Some platforms, like Discord and Slack, will be easier since we can use their APIs to access data.</p>
<p>“Vibetyper” is already being used by a company for a text-to-voice product, so I’ll be going with TypeMyVibe instead. It’s not my first choice, but I think it will work.</p>
<p>Now it’s time to create a plan of action. Here are the things I need to implement for the product to work properly:</p>
<p>Authentication.</p>
<p>Support for all major chat apps.</p>
<p>A function to extract and process chats.</p>
<p>A function to split chats into chunks and generate analysis.</p>
<p>A function to compile those chunks into a final result.</p>
<p>A function to generate a text-to-PDF report.</p>
<p>A function to send the report via email.</p>
<p>A function to manage queues and handle processing tasks.</p>
<p>Payment and billing integration.</p>
<p>My target is to complete everything within this week. The landing page is done, and tomorrow I will start implementing authentication and building support for chat extraction and processing across social media platforms.</p>

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