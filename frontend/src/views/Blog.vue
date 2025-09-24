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
          snippet:'I’ve decided—fuck it—I’m taking a break from SitChat. I still believe in the idea with my whole heart, but right now, something else is sparking my interest. Another idea.',
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
        },
        {
          id:9,
          title:'100 days of entrepreneurship day 14',
          slug:'100-days-of-entrepreneurship-day-14',
          day:'14',
          date:'August 11, 2025',
          snippet:'I have decided on something else: I’m not going to spend any of my father’s money unless it’s absolutely necessary. I won’t buy any clothes, eat outside food, drink, or spend on anything unnecessary. I will earn first, and only then will I buy.',
          content:`
          <p>Hello readers,</p>
<p>I have decided on something else: I’m not going to spend any of my father’s money unless it’s absolutely necessary. I won’t buy any clothes, eat outside food, drink, or spend on anything unnecessary. I will earn first, and only then will I buy.</p>
<p>I’m 25 years old, and I feel ashamed that I left my job to pursue entrepreneurship but haven’t been able to push myself to work. I feel like I’m scared of hard work or something. I have no sense of urgency. I take things too slow.</p>
<p>Yesterday, while trying to work, I made some progress—but then I took a break. I don’t understand why. This year, I have to become capable no matter what. If I’m not successful this year, next year I will take whatever job I can get—be it as an Uber driver, Zomato delivery person, or anything else.</p>
<p>It’s time to be capable. Living with my parents has made me complacent. I have big ambitions, but no drive. This is depressing. I put on a brave face in public, but inside I feel lost. I wonder if my depression ever really got cured, or if I just learned to cope with it. I haven’t had suicidal thoughts in years, though.</p>
<p>This new product idea, TypeMyVibe, is extremely exciting to me. I can’t stop thinking about how to make it and how to market it. But when it comes to actually doing the work, I start lazing around. I don’t know why.</p>
<p>I need to work 12 hours a day to make up for all the losses I’ve incurred in life. I’m going to start my day with work and keep going, even if my head hurts or my heart aches. That’s the only way I can redeem myself in my own eyes. Forget everything else—it’s high time.</p>
<p>I need to take care of my family. I want to marry my girlfriend and start a family. I’m 25—it’s time for that. I can’t waste any more of my life on distractions. For me, it’s going to be 24 hours of work, until I launch a product that succeeds. I’m going to be a solopreneur, launching product after product until one of them takes off.</p>
          `
        },
        {
          id:10,
          title:'100 days of entrepreneurship day 15',
          slug:'100-days-of-entrepreneurship-day-15',
          day:'15',
          date:'August 12, 2025',
          snippet:'This is the third time I’m setting up authentication, and it’s always frustrating. I ended up spending the whole day just trying to get auth working properly.',
          content:`
          <p>Hello readers,</p>
<p>This is the third time I’m setting up authentication, and it’s always frustrating. I ended up spending the whole day just trying to get auth working properly.</p>
<p>It’s easier with Supabase, but creating the page, setting up Google’s client, configuring the SMTP server, and making backend auth work still takes time. I think this process could definitely be simplified.</p>
<p>With authentication and the landing page done, I can finally start focusing on the core application. Next up is setting up the chat extraction process and the data processing pipeline. Once that’s done, about 70% of the work will be complete. After that, I just need to set up the analysis part, and finally, the email and payment systems. I think I can finish everything this week.</p>
<p>I’m also thinking about starting to tweet. Building a public presence is important if I want to succeed as a solopreneur. I’m not sure what to tweet or how to tweet yet, but I’ll learn by trial and error—just sharing things I find valuable and seeing what resonates.</p>
<p>On another note, I’ve also joined Google’s Gen-AI Hackathon with a friend. Our idea is to build an insurance purchasing assistant using LLMs. It’s a fun project that could even become a product. I’ll be dedicating around two hours a day to it until the deadline on September 14th.</p>
          `
        },
        {
          id:11,
          title:'100 days of entrepreneurship day 16',
          slug:'100-days-of-entrepreneurship-day-16',
          day:'16',
          date:'August 13, 2025',
          snippet:'The tweet I posted didn’t get many views or much engagement, but a few people followed me and some even DM’d me. It was fun engaging with them.',
          content:`
          <p>Hello readers,</p>
<p>The tweet I posted didn’t get many views or much engagement, but a few people followed me and some even DM’d me. It was fun engaging with them.</p>
<p>It’s important to be public in my field. I have severe social media anxiety due to the childhood cyberbullying I went through. This is why I don’t have any social media accounts. Every time I tweet something or make a Reddit post, I feel anxious and scared—even though it’s anonymous and I know most people don’t care. Posting on social media will probably always be a challenge for me.</p>
<p>Part of the reason I’m writing this blog is to improve my writing skills and reduce my fear of presenting myself online.</p>
<p>I’ve built the first page of the application, where the user selects the platform they want to analyze, follows the instructions to get the data, and uploads it. Now I need to set up the backend to process the data into a common format across all platforms.</p>
<p>The next part is the hard part—once the processing is set up, 80% of the application will be done.</p>
<p>I also bought the domains typemyvibe.ai and typemyvibe.com. That always makes me happy. I want to deploy as soon as possible.</p>
          `
        },
        {
          id:12,
          title:'100 days of entrepreneurship day 17',
          slug:'100-days-of-entrepreneurship-day-17',
          day:'17',
          date:'August 14, 2025',
          snippet:'The hard part of my application needs to start, and I have been procrastinating since the morning.',
          content:`
          <p>Hello readers,</p>
<p>It’s mid-day, but I am writing the blog. The hard part of my application needs to start, and I have been procrastinating since the morning. I don’t understand my fear of working hard. All the challenges I have had until now I’ve overcome, but I still feel some kind of dread when thinking about doing something I’m not sure how to do.</p>
<p>I will take a break today and just do research work, add screenshots, and elaborate on the instructions. Currently, there are only instructions for extracting from desktop. I will add instructions for Android and iOS.</p>
<p>I will also look into options where I can use an API or something similar to get access to the chat, to make it easier for users. I will also add to the landing page that users can analyze group chats and gather information about their friends, and that corporations can get insights into their employees to help them improve. This increases the total addressable market.</p>

          `
        },
        {
          id:13,
          title:'100 days of entrepreneurship day 18',
          slug:'100-days-of-entrepreneurship-day-18',
          day:'18',
          date:'August 15, 2025',
          snippet:'Happy indipendence day!',
          content:`
          <p>Hello readers,</p>
          <p> So someone i have convinced myself that today is holiday and its okay not to be productive today. So happy independence day</p>
          `
        },
        {
          id:14,
          title:'100 days of entrepreneurship day 19',
          slug:'100-days-of-entrepreneurship-day-19',
          day:'19',
          date:'August 16, 2025',
          snippet:'Millionaire fastlane is an awesome book',
          content:`
          <p>Hello readers,</p>
          <p> I think my independence day is still not over. I started reading millionaire fastlane yesterday and something about the book is so interesting to me that i can't stop. Maybe i am just avoiding work because its hard or it will fail or i am just so interested in this book</p>
          `
        },
        {
          id:15,
          title:'100 days of entrepreneurship day 20',
          slug:'100-days-of-entrepreneurship-day-20',
          day:'20',
          date:'August 17, 2025',
          snippet:'Sunday i take it light even tho every day is a sunday for me.I think i should stop including sunday’s in the day count. ',
          content:`
          <p>Hello readers,</p>
<p>Sunday, I take it light—even though every day feels like a Sunday for me. I think I should stop including Sundays in my day count.</p>
<p>Even today, I wasted most of my time just thinking, planning, and researching what I could do, how I could do it, how things should work, how to market it, what marketing really is, the types of content, etc. But there was no actual work or progress.</p>
<p>Half the day went into reading The Millionaire Fastlane. I started it just three days ago, and I’ve already read 200 pages. I think only I can manage to procrastinate by reading a book. But this isn’t right—I’ve wasted four days without making any real progress.</p>
<p>I need to take action and make good decisions. If I keep going like this, failure is inevitable. Let’s hope for the best tomorrow.</p>
          `
        },
        {
          id:16,
          title:'100 days of entrepreneurship day 21',
          slug:'100-days-of-entrepreneurship-day-21',
          day:'21',
          date:'August 18, 2025',
          snippet:'Marketing is interesting,I spent the whole day learning about marketing, and it’s much more complicated than I thought. Looking back, all my previous plans were pretty stupid.',
          content:`
          <p>Hello readers,</p>

<p>Man, marketing is <em>fucking interesting</em>. I spent the whole day learning about marketing, and it’s much more complicated than I thought. Looking back, all my previous plans were pretty stupid.</p>

<p>Here’s what I’ve understood after today’s deep dive into marketing:</p>

<h2>1. Market Research</h2>
<p>The first step is to do proper market research: Who are my competitors? How do they work, market, and position themselves? What gaps exist? This helps me understand their strengths but, more importantly, their weaknesses. With this knowledge, I can position my products much better.</p>

<h2>2. Building Buyer Personas</h2>
<p>I need to create buyer personas by understanding my target customers’ demographics, psychographics, and problem-centric profiles. I also need to define who my customer <em>isn’t</em>. This step is crucial—it will be my guiding light for content and marketing strategies. Buyer personas aren’t final; they should be regularly updated based on the data I receive.</p>

<h2>3. Creating a Unique Value Proposition (UVP)</h2>
<p>The UVP will be the core of my marketing strategy. It must be built with the buyer persona in mind, using their language and focusing on customer benefits. Like the buyer persona, this won’t be final—it should evolve as new information comes in.</p>

<p>I haven’t executed these steps yet—I’ve only studied them. I’ll start working on them tomorrow.</p>

<hr>

<h2>The Next Step: Building a Conversion Engine</h2>

<p>Before today, I thought conversion was all about “going viral.” But in reality, it’s about consistency, data, and experimentation.</p>

<h3>1. Landing Page</h3>
<p>My landing page is basically my 24/7 salesperson. It needs thorough A/B testing and constant optimization. The message should be crystal clear—users must understand what the product does within 5 seconds. The visuals should be hierarchical and flow logically:</p>
<ul>
    <li>Hero section → outlines the key benefit with a call-to-action</li>
    <li>Benefits listed below</li>
    <li>Social proof</li>
    <li>Final call-to-action</li>
</ul>

<h3>2. Content on the Landing Page</h3>
<p>All content should be written for the buyer persona, in a unified language designed to convert. Social proof is essential to eliminate user fears.</p>

<h3>3. SEO</h3>
<p>SEO brings inbound leads. To leverage this, I need a content calendar and must regularly publish:</p>
<ul>
    <li><strong>Top of Funnel (Awareness)</strong> content</li>
    <li><strong>Middle of Funnel (Consideration)</strong> content</li>
    <li><strong>Bottom of Funnel (Decision)</strong> content</li>
</ul>
<p>This content can also be repurposed into short-form videos, Reddit posts, and X (Twitter) posts. Again, all of it should be tailored to the buyer persona.</p>
<p>Off-page SEO is about backlinks. That can be built via paid PR or by genuinely being helpful in relevant communities.</p>

<h3>4. Short-Form Content</h3>
<p>For the best conversions, short-form content should follow this structure:</p>
<ul>
    <li>A 3-second hook</li>
    <li>Authenticity</li>
    <li>Leveraging trends</li>
    <li>Designed to work with sound off</li>
</ul>

<h3>5. Paid Ads</h3>
<p>Budget allocation should follow the 70/20/10 rule:</p>
<ul>
    <li>70% → Boosting proven content</li>
    <li>20% → Promising strategies</li>
    <li>10% → High-risk, high-reward experiments</li>
</ul>

<h3>6. Influencers</h3>
<p>I need to find influencers my target customers actually follow. Instead of cold approaching them, I should first warm up by engaging with their content. When I do reach out, the most important factors will be the product’s relevance to their content and how well the creator resonates with their audience.</p>

<h3>7. Metrics</h3>
<p>Finally, I need to track key metrics:</p>
<ul>
    <li>Customer Acquisition Cost (CAC)</li>
    <li>Customer Lifetime Value (LTV)</li>
    <li>Customer Churn Rate</li>
    <li>North Star Metric: LTV-to-CAC Ratio</li>
</ul>

<hr>

<p>If I diligently execute all of the above, I believe I can turn any one of my products into a rockstar product—like how the “pet rock” became a hit. Marketing is going to be an exciting challenge. I just hope I can pull it off.</p>

          `
        },
        {
          id:17,
          title:'100 days of entrepreneurship day 22',
          slug:'100-days-of-entrepreneurship-day-22',
          day:'22',
          date:'August 19, 2025',
          snippet:'Yesterday I enjoyed learning about marketing. So today I thought, let’s dive into company registration and what needs to be done after registering. Man, I really hate bureaucracy.',
          content:`
            <p>Hello readers,</p>
  <p>Yesterday I enjoyed learning about marketing. So today I thought, let’s dive into company registration and what needs to be done after registering. Man, I really hate bureaucracy.</p>
  <p>There are 5–6 options to choose from, ranging from sole proprietorship to private limited. Since I want to register as a startup, my only real options are LLP or Pvt Ltd. The problem is that both require at least 2 partners. I’m a solopreneur, so I’ll probably have to involve my father or mother.</p>
  <p>The registration process itself is cumbersome and lengthy—it’ll take at least a month. I thought I could start today, but nope. I need an office address. Like, what the hell? Apparently, I can use my home as an office. But for that, I need a rent agreement with my mother and an NOC stating I can use the place as an office. To create the rent agreement, though, I first need the flat’s mutation or something—which I don’t even understand.</p>
  <p>Next, after the company is registered, I’ll need to get a trade license, which will almost definitely involve corruption. Then I’ll have to register as a startup, which is another cumbersome process. But fine, all this is just a one-time headache. Once that’s done, I can finally open a bank account.</p>
  <p>But after all this, I’ll need to maintain every transaction, file monthly GST forms (three of them!), quarterly TDS returns, quarterly board meeting reports, quarterly financial reports to the ROC and MCA, and finally, annual reports on top of all that.</p>
  <p>If I miss any of these, I’ll face penalties. If I make mistakes, I could even face jail time. No wonder there are so few solopreneurs in India and so few startups overall. Just dealing with all this bureaucracy is a full-time job. If I start a company, all my focus will be wasted on this stuff—when will I have time to code or market? I’d probably need to hire a full-time person just to manage compliance.</p>
  <p>If I skip all this and just build and sell my product, I lose the benefits of having a separate legal entity. I won’t be able to deduct expenses, and I’ll be taxed on revenue, which would be catastrophic.</p>
  <p>Well, I guess the only option is to try and learn all of this.</p>
          `
        },
        {
          id:18,
          title:'100 days of entrepreneurship day 23',
          slug:'100-days-of-entrepreneurship-day-23',
          day:'23',
          date:'August 20, 2025',
          snippet:"Finally, a productive day that I’m actually happy about. From the moment I woke up until now—past midnight—I’ve been working.",
          content:`
          <p>Hello readers,</p>

  <p>Finally, a productive day that I’m actually happy about. From the moment I woke up until now—past midnight—I’ve been working. The main reason for this sudden drive is that a lot of ideas from <em>The Millionaire Fastlane</em> really resonated with me. I’ve realized I have to do whatever it takes to achieve what I want.</p>

  <p>So, about the long-term marketing plans we discussed two blogs ago—we’re still going to pursue those. But in the meantime, I’ve had some fun and interesting marketing ideas that I want to try out during the launch month. For example:</p>

  <ul>
    <li>Doing MBTI analyses of big Twitter influencers and tagging/sharing it with them.</li>
    <li>Analyzing the MBTI of my favorite TV show characters and sharing those in Reddit, Facebook communities, etc. (and turning them into blog posts).</li>
    <li>Offering free MBTI analyses for Reddit users as a way to promote and share my work.</li>
  </ul>

  <p>This will be my main launch plan. After that, I’ll transition into the long-term consistent marketing strategy we discussed earlier.</p>

  <p>As for company registration and other formalities—I’m going to skip that for now. I found out about the concept of presumptive tax, where it’s assumed that 50% of your revenue is profit, and you’re taxed on that. As long as my costs stay under 50%, it’s actually a pretty good deal without much headache. There are still some concerns about GST and international trade, but I’ll figure those out along the way.</p>

  <p>Regarding the product: about 80% of the MVP is done, and I should be able to finish it this week. Then the really interesting part begins—enabling payments, integrating PostHog, setting up A/B testing, and optimizing for SEO. Once that’s in place, I’ll start marketing. My target is to launch in the first week of next month.</p>

  <p>I feel much better and more relaxed now. I think this product has potential, but the real test is whether people will be willing to share their data with me. Even though I’m not storing it, will they feel comfortable? Another concern is the friction of having to export and upload their chats. Will people actually do it? Only time will tell—but I’m hopeful.</p>

          `
        },
        {
          id:19,
          title:'100 days of entrepreneurship day 24',
          slug:'100-days-of-entrepreneurship-day-24',
          day:'24',
          date:'August 21, 2025',
          snippet:'I had a grand vision of what the product could become and how it might help millions of people. ',
          content:`
          <p>Last night, I had a grand vision of what the product could become and how it might help millions of people. 
  I truly believe it has the potential to be revolutionary. These thoughts kept me up all night—thinking about 
  how I’m going to achieve it and what it needs in order to truly make an impact. Unfortunately, this lack of 
  sleep ruined my day today. I felt extremely tired and lazy, stuck between wanting to work and needing rest. 
  As a result, I wasted a lot of time without even realizing it, and no meaningful work got done.</p>

  <p>That said, I did manage to tweet, make a Reddit post, and engage with the community. I also came up with 
  some useful ideas. One key realization was that pricing plays a very important role in marketing. Initially, 
  I was planning to price the product at $5 so that everyone could afford it and benefit from it. But I realized 
  that at such a low price, people might perceive it as a cheap, fun tool rather than a serious productivity tool. 
  So I’ve decided to set the price at $20, with a 50% launch discount. Hopefully, this helps position it better.</p>

  <p>Another idea I’m considering is offering a free one-page introductory report. I’ll need to think more about 
  whether this is the right choice.</p>

  <h2>Revenue Goal</h2>
  <p>I also spent time calculating what it would take to reach my goal of earning $1 million a year. 
  To achieve that, I would need 50,000 customers at $20 each. That works out to around 5,000 new customers 
  per month. Assuming a 10% conversion rate, I’d need about 50,000 monthly visitors to my website. With a 
  5% click-through rate, that means I’d need around 1 million views per month. Breaking that down further, 
  I’d need roughly 35,000 daily views across six platforms.</p>

  <h2>Content Plan</h2>
  <p>To make that happen, my plan is to create two pieces of content daily: one long-form post (for Reddit, 
  X, and LinkedIn) and one short-form video (for Reels, Shorts, and TikTok). This feels doable and far more 
  realistic now that I’ve broken it down. Before, I thought it might not be possible.</p>

  <p>Hopefully, I get a good night’s sleep today and can make real progress on the product tomorrow. 
  My goal is still to launch during the first week of next month.</p>

          `
        },
        {
          id:20,
          title:'100 days of entrepreneurship day 25',
          slug:'100-days-of-entrepreneurship-day-25',
          day:'25',
          date:'August 22, 2025',
          snippet:"I love learning above everything else. I have ordered about 5–6 books on marketing, product design, and building a company. Yesterday, when I should have been focusing on building the product.",
          content:`
          <p>Hello readers,</p>
          <p>I love learning above everything else. I have ordered about 5–6 books on marketing, product design, and building a company. Yesterday, when I should have been focusing on building the product, I just kept absorbing information about marketing and how I can implement those strategies in my product’s go-to-market strategy. So, no progress in product development, but a bunch of progress in how to distribute and grow the business.</p>

  <p>The first thing I did was conduct a competitor analysis. I found that there are <strong>four types of businesses in my domain</strong>, which can be mapped across two axes: Business Model (free vs. paid) and Target Audience (consumer vs. business).</p>

  <ul>
    <li><strong>Quadrant 1</strong>: Businesses like <em>16 Personalities</em> and <em>Truity</em> that give free tests and results to consumers, then upsell them on more insights.</li>
    <li><strong>Quadrant 2</strong>: Paid niche products for people who are deep into psychology and personality types. This is the quadrant where my product <em>TypeMyVibe</em> will be placed.</li>
    <li><strong>Quadrant 3</strong>: B2B paid products targeting HRs and professionals.</li>
    <li><strong>Quadrant 4</strong>: Community-driven apps like PDB, where people vote on which celebrity or character matches which type.</li>
  </ul>

  <p>👉 The <strong>Free business quadrant is empty</strong>, showing a real opportunity.</p>

  <hr>

  <h2>Competitor Analysis</h2>

  <ol>
    <li>
      <strong>16 Personalities</strong>
      <ul>
        <li><em>Strengths</em>: Offers free tests and results, then upsells premium reports. It is the default for everyone and is the king of SEO and word-of-mouth.</li>
        <li><em>Weaknesses</em>: It is a false MBTI type test because it is based more on Big Five instead of cognitive functions. The descriptions are vague to please most people.</li>
      </ul>
    </li>
    <li>
      <strong>Crystal Knows</strong>
      <ul>
        <li><em>Strengths</em>: Provides HR analysis using public LinkedIn profile data of potential hires. Offers Big Five and DISC results. It is very well integrated with CRM tools.</li>
        <li><em>Weaknesses</em>: Very costly and works on a subscription model.</li>
      </ul>
    </li>
    <li>
      <strong>PDB</strong>
      <ul>
        <li><em>Strengths</em>: Cultivated a high level of community engagement and participation.</li>
        <li><em>Weaknesses</em>: Based on user votes and can be highly inaccurate.</li>
      </ul>
    </li>
    <li>
      <strong>Personality Reveal.ai</strong>
      <ul>
        <li><em>Strengths</em>: Direct competitor that also reveals personality using text, presented in a chat interface. Very simple and straightforward approach.</li>
        <li><em>Weaknesses</em>: Limited by input data and can change depending on the user’s mood.</li>
      </ul>
    </li>
  </ol>

  <hr>

  <h2>Insights Based on Competitor Analysis</h2>
  <ul>
    <li>There is a gap between casual users of <em>16 Personalities</em> and hardcore users of PDB and Reddit communities. There is <strong>no solution for mid-core users</strong> who want to go deeper but don’t have the time or energy.</li>
    <li>I can offer healthcare professionals and companies compatibility and personality analysis of their teams at a much cheaper, more affordable price.</li>
    <li>I can use subtitles of shows to analyze characters — a creative marketing opportunity.</li>
    <li>For users concerned about uploading chats, I can give them a chatbot to get their results.</li>
  </ul>

  <hr>

  <h2>Buyer Persona: Alex, The Reflective Achiever</h2>

  <p><strong>Overview</strong><br>
  Alex is a digitally native, intellectually curious professional invested in personal growth as a path to effectiveness and fulfillment.</p>

  <p><strong>Demographics</strong></p>
  <ul>
    <li>Age: 25–38</li>
    <li>University-educated, employed in knowledge industries (tech, marketing, design, education)</li>
    <li>Urban/suburban, household income $75K+</li>
    <li>Has disposable income for high-value digital products</li>
  </ul>

  <p><strong>Psychographics &amp; Values</strong></p>
  <ul>
    <li>Values authenticity, continuous self-improvement, efficiency, and intellectual rigor</li>
    <li>Progressive in social/political views; supports value-aligned brands</li>
    <li>Busy professional, protective of leisure time, invests in tools with tangible benefits</li>
    <li>Interests: non-fiction, psychology/productivity podcasts, strategic/creative hobbies</li>
    <li>Personality (Big Five): High Openness (curious), High Conscientiousness (organized, disciplined), Moderate Extraversion (prefers deep over broad connections)</li>
  </ul>

  <p><strong>Motivations &amp; Goals</strong></p>
  <ul>
    <li>Seeks deeper self-awareness for better decisions in career, relationships, and personal growth</li>
    <li>Desires a coherent framework to explain recurring thought/behavior patterns</li>
    <li>Craves validation — being accurately “seen” by an objective system</li>
  </ul>

  <p><strong>Frustrations &amp; Pain Points</strong></p>
  <ol>
    <li><em>Horoscope Effect</em>: Frustrated by vague, flattering, pseudoscientific tests; wants evidence-based insights</li>
    <li><em>Performance Paradox</em>: Distrusts self-report bias; resents “performing” for tests or outcomes</li>
    <li><em>Label Limbo</em>: Wants frameworks, but not rigid, oversimplified labels</li>
    <li><em>Privacy Concerns</em>: Data-savvy; skeptical of opaque terms, excessive permissions, or misuse of personal info</li>
  </ol>

  <hr>

  <h2>Unique Value Proposition</h2>

  <p><strong>Core Problem</strong><br>
  "I want deep, accurate self-knowledge to improve my life, but current tools force me to choose between superficial, free quizzes that I don't trust, and complex, time-consuming theories I don't have time to master."</p>

  <p><strong>TypeMyVibe’s UVP</strong><br>
  For the self-aware individual seeking genuine personal insight, <em>TypeMyVibe</em> is the only AI-powered personality analysis service that uses your authentic, real-world conversations to deliver a deep, multi-faceted report with absolute privacy. Unlike questionnaire-based tests, we reveal who you truly are, not who you think you should be.</p>

  <p><strong>Pillars</strong></p>
  <ol>
    <li>
      <strong>Unquestionable Authenticity</strong><br>
      <em>Message</em>: "Your True Personality, Revealed from Your Real Conversations."<br>
      <em>Proof</em>: Grounded in the objective reality of a user's linguistic patterns, tone, and communication style over time. Not based on biased, aspirational, or situational self-reporting.
    </li>
    <li>
      <strong>Absolute Privacy</strong><br>
      <em>Message</em>: "Deep Insights. Zero Data Footprint."<br>
      <em>Proof</em>: TypeMyVibe never stores user chat data.
    </li>
    <li>
      <strong>Actionable Depth</strong><br>
      <em>Message</em>: "Beyond the Label. A 360° View of Your Vibe."<br>
      <em>Proof</em>: Reports are comprehensive and multi-model (MBTI, Enneagram, Big Five/OCEAN). The OCEAN model adds scientific credibility. A custom <strong>Vibe Card</strong> provides a nuanced, visually rich summary beyond a simple four-letter code.
    </li>
  </ol>

  <p><strong>Strategic Messaging &amp; Tone of Voice</strong></p>
  <ul>
    <li><strong>Key Phrases to Use</strong>: "Evidence-based insights," "Your authentic communication style," "Discover the patterns in your words," "Beyond the stereotypes," "A private space for self-discovery."</li>
    <li><strong>Key Phrases to Avoid</strong>: "Find your true self" (too vague), "The most accurate test ever" (unprovable, arrogant), "Unlock your destiny" (overly dramatic, misaligned with science).</li>
  </ul>

  <p><strong>Pricing Strategy</strong><br>
  The $20 one-time fee is a quality signal in a market saturated with free alternatives. The landing page must frame this as a <em>worthwhile investment in genuine, private self-discovery</em>.</p>

  <hr>

  <h2>Landing Page</h2>

  <p><strong>Hero Section</strong></p>
  <ul>
    <li><em>Headline</em>: <em>Discover your true personality — no test, no bias, just the real you!</em></li>
    <li>With an image of the Vibe Card and a link to “My Vibe Report.”</li>
    <li><em>Subheadline</em>: <em>Upload your chats and get your real MBTI, Enneagram, alignment, strengths, weaknesses, career fit, and more — in minutes.</em></li>
    <li>CTA: "Get My Report"</li>
    <li>Metrics: <em>Vibes typed (total, this month, today)</em></li>
  </ul>

  <p><strong>Value Section</strong></p>
  <ul>
    <li>Visual: All types pointing an arrow toward the user.</li>
    <li>Text: <em>We show a complete and truly personal picture. Truly personalized reports about relationships, career, productivity, etc. You are one in a million, not one in 16.</em></li>
  </ul>

  <p><strong>Comparison Table</strong></p>
  <table border="1" cellpadding="6">
    <thead>
      <tr>
        <th>Feature</th>
        <th>TypeMyVibe</th>
        <th>Traditional Quizzes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Basis of Analysis</td>
        <td>Your Real Conversations</td>
        <td>Your Biased Answers</td>
      </tr>
      <tr>
        <td>Data Privacy</td>
        <td>Never Stored</td>
        <td>Stored in User Profiles</td>
      </tr>
      <tr>
        <td>Result</td>
        <td>Objective &amp; Nuanced</td>
        <td>Stereotypical &amp; Vague</td>
      </tr>
      <tr>
        <td>Insight</td>
        <td>Evidence-Based</td>
        <td>Aspirational</td>
      </tr>
    </tbody>
  </table>

  <p><strong>How Section</strong></p>
  <ul>
    <li>The three steps: Upload Chat → Analyze → Report.</li>
    <li>Animation idea: Chats go into open-source AI for analysis → report generated → chats deleted.</li>
  </ul>

  <p><strong>Other Sections</strong></p>
  <ul>
    <li>Supported Apps</li>
    <li>Social Proof</li>
    <li>Quote: <em>"There are three things extremely hard: steel, a diamond, and to know one's self." – Benjamin Franklin</em> — <em>Not anymore.</em></li>
    <li>Price</li>
    <li>FAQ</li>
  </ul>

  <hr>

  <h2>Practical Lessons from X and YouTube</h2>

  <ul>
    <li>Consistency is the key.</li>
    <li>Marketing is both art and science, requiring experimentation and iterations.</li>
  </ul>

  <p><strong>Checklist</strong></p>
  <ul>
    <li>[ ] Get VPN</li>
    <li>[ ] Get domain email ID</li>
    <li>[ ] Make accounts on Shorts, Reels, and TikTok</li>
    <li>[ ] Follow psychology, growth, and self-help influencers</li>
    <li>[ ] Warm up accounts by watching their content and gaining inspiration (Good artists copy, great artists steal)</li>
    <li>[ ] Make a list of influencers who can market the product</li>
    <li>[ ] Start posting content daily</li>
  </ul>

  <hr>

  <h2>Planned Campaigns</h2>

  <ol>
    <li>TV show dialogue analysis → personality types of characters (blog, Reddit post in TV show subreddit and MBTI subreddit)</li>
    <li>Reddit free analysis in MBTI subreddits (for initial testimonials)</li>
    <li>Top X influencers analysis (blog + X thread)</li>
    <li>Top LinkedIn influencers (maybe later)</li>
    <li>Quora: answer key questions, also use for content ideas</li>
    <li>Free compatibility report if you invite your friend or special someone 😉 (for organic growth)</li>
    <li>Community hook: "Most of you are mistyped — do you actually believe you are just one of 16?" (polarizing to grab attention)</li>
    <li>Productivity subreddits: "Knowing yourself is the most important step."</li>
    <li>Emotional ads about finding yourself (experimental)</li>
    <li>Possible future markets: health coaches, therapists, teams</li>
  </ol>

  <hr>
          `
        },
        {
          id:21,
          title:'100 days of entrepreneurship day 26',
          slug:'100-days-of-entrepreneurship-day-26',
          day:'26',
          date:'August 23, 2025',
          snippet:"Things never work out the way you actually plan them",
          content:`
          <p>Things never work out the way you actually plan them. I thought implementing the app would be straightforward, but as luck would have it, LangChain’s chat loaders don’t work anymore. I wasted a lot of time trying to figure out how they worked, with no results. So now, I’ll have to build custom chat loaders, which is going to be a long and tedious task. Because of this, I’m cutting down the scope of my product.</p>

  <p>For the MVP, I’ll only include 4 options: Reddit and X for public social media content, and Instagram and WhatsApp for chats. I chose Instagram and WhatsApp because they’re the most widely used text apps among Gen-Z and millennials. That should be good enough for now.</p>

  <p>I also tried making the “vibe card” concept along with a report based on my types—and I loved it. It felt like a Pokémon card, but about me. I shared it with a few people and got mixed reviews: some liked it horizontal, some preferred borders, others without borders—but everyone loved the concept. Honestly, it was confusing as hell. So I’ve decided to just give users two versions.</p>

  <p>I’ve also been more active on Reddit and X recently, and I’m starting to get the hang of it. I get a lot of engagement on Reddit, but X is tough. Still, it seems like consistency is the key. I even found an Australian guy who’s super hardcore into typology, and he’ll probably be really helpful in my journey. Thanks, Reddit!</p>

  <p>One more thing—I’ve decided I won’t write or count Sundays anymore. That’s going to be my day off.</p>

          `
        },
        {
          id:22,
          title:'100 days of entrepreneurship day 27',
          slug:'100-days-of-entrepreneurship-day-27',
          day:'27',
          date:'August 25, 2025',
          snippet:"Alcohol is poison.",
          content:`
          <p>Hello readers, </p>
          <p>Alcohol is poison. Yesterday, I drank about three large glasses of whiskey. Today, I woke up at 4:30 with a headache and couldn’t fall back asleep for about two hours. After that, I woke up again at 11 a.m., and the headache was still there. I didn’t feel like doing anything, and even my Whoop band showed 1% recovery, telling me to take a relaxing day. I honestly don’t even know how the day passed&mdash;it feels like I just woke up, and now it’s already over. I hate alcohol. I used to be able to drink without any problems, but nowadays it’s not the same.</p>

  <p>As for work, I didn’t do much. I just checked out Peerlist, Product Hunt, Indie Hackers, and other product launch websites, and I made accounts on them. I plan to be a little active there so that when I launch my product, I can get some good traction. I’m planning to launch <strong>Sitchat</strong> on Product Hunt just to see what it’s like. I can’t launch it right now though, since you can only launch a week after joining.</p>

  <p>I also had two more wild ideas. My current product, <strong>VibeMyType</strong>, does personality analysis based on personal chats or public posts/comments on Reddit/X. If this works, I could create a competitor called <strong>MyVibeType</strong>, where you can just chat with an AI for a few minutes and get your personality type without compromising your privacy.</p>

  <p>The other idea is <strong>Vibe Dating</strong>, where users swipe “vibe cards” with personalized avatars and compatibility ratings. I think VibeMyType, if it works, could be a $1&ndash;2M ARR business. But Vibe Dating could easily reach $100M.</p>

  <p>Today felt wasted, but I’m going to work hard tomorrow. I’ve also realized something: the reason I’ve been having trouble sleeping is because I overthink what I want to do and what I could do with my products. I think I do this because I’m not working as much as I should during the day. I procrastinate a lot, and then I overthink at night to make myself feel like I’m working. So tomorrow, I’m going to try working harder and see if this theory is right.</p>
</body>
          `
        },
        {
          id:23,
          title:'100 days of entrepreneurship day 28',
          slug:'100-days-of-entrepreneurship-day-28',
          day:'28',
          date:'August 26, 2025',
          snippet:"It was a somewhat productive day.",
          content:`
          <p>Hello readers, </p>
           <p>It was a somewhat productive day. I finally got the second-to-last piece to work, and now I can move on to the final part—making the report and the vibe card. I’m really excited to see it come together, but also a bit scared that it might not work and the results could just turn out to be random hallucinations.</p>

    <p>On Twitter, I’ve crossed 20 followers just by posting every day, which is nice. On Reddit, I’m engaging more and starting to get somewhat known in the community. I just hope that when I begin marketing there, I don’t get banned.</p>

    <p>I’ve still been procrastinating a lot, and most of my mornings are wasted by lazing around. My nights often go into meeting friends and talking with my girlfriend. I think the only way to be more productive is to optimize my mornings for work. I don’t want to stop meeting friends or talking to my girlfriend, since I see that as an important part of life.</p>

    <p>This Sunday I have exams, so I need to start preparing for them too. That means product progress will slow down a little, but I still think I’ll be able to launch by the end of the first week of September.</p>
          `
        },
        {
          id:24,
          title:'100 days of entrepreneurship day 29',
          slug:'100-days-of-entrepreneurship-day-29',
          day:'29',
          date:'August 27, 2025',
          snippet:"Today I had some other work aside from my product.",
          content:`
              <p>Hello readers,</p>

    <p>Today I had some other work aside from my product. First of all, Rajesh uncle called me to discuss some potential projects. The ideas he wants me to work on are interesting and fun. He wants me to build an AI toy for kids that can voice-clone their parents and teach them. Another project is about extracting leads from LinkedIn, Yellow Pages, and other sources, and then reaching out to them using AI—making the outreach more personal and increasing conversion rates. I want to work on both of these and have told him I’ll commit 2–3 hours a day to them once I’m back to full health.</p>

    <p>For these tasks, I’ll have access to his team, so my role will be more like a product manager. This will also give me the chance to develop some management skills.</p>

    <p>As for my current product, I had some authentication issues, so I spent a good amount of time fixing those. After that, I developed a reports page where the user will be redirected after making a payment. I also did a lot of research on how I can analyze different personality types using AI, and specifically, what the minimum amount of text is that I need for a good analysis.</p>

    <p>Based on my research, here’s the plan: I’ll chunk the messages using semantic chunking and then add contextual data. Each chunk will then be analyzed for typologies. After that, I’ll combine the results using both mathematical methods and LLM-based analysis to produce a final personality typology. Finally, I’ll use this typology to create a holistic report for the user. This system should significantly increase accuracy and actually provide meaningful insights.</p>

    <p>On the social side, Twitter and Reddit engagement is ongoing, but the results aren’t that great yet.</p>
          `
        },
        {
          id:25,
          title:'100 days of entrepreneurship day 30',
          slug:'100-days-of-entrepreneurship-day-30',
          day:'30',
          date:'August 28, 2025',
          snippet:"After having a somewhat consistent streak of work, I relapsed today.",
          content:`
          <p>Hello readers</p>

            <p>After having a somewhat consistent streak of work, I relapsed today. I wasted the whole day doing nothing but scrolling Twitter, Reddit, and watching TV shows while constantly thinking that I should have been working. It’s not like I was getting a lot done before, but still, something is better than nothing. I don’t know why I do this. I have big ambitions, I want to achieve great things, and I have the ability to do so — then why do I choose inaction? Why do I keep wasting time instead of working toward my goals? I have no idea.</p>

  <p>Is it because we are animals and tend to follow habits, and I’ve built up very bad ones? Is it because I’ve never really had to work hard to get by in life — exams and everything else always came easily to me? Is it because we tend to flow into things, and I often choose to start with the wrong activities? Is it because I was suicidal until the age of 20 and remain somewhat nihilistic, so I don’t see much value in long-term things? Is it because I fear failure? Or is it because I want to maintain the illusion of the potential I believe I have?</p>

  <p>Why is it that when a new episode of a show drops, I feel an urgency to watch it immediately, but when it comes to my ambitions, I tell myself I’ll do it tomorrow? It doesn’t make sense.</p>

  <p>I don’t have answers to any of these questions. I don’t understand why I am like this. Why can’t I be like my idols, who work at least 8–10 hours a day to achieve what they want in life? Why can’t I do that?</p>

  <p>It’s not that I’m not interested in coding or working — because when I do work, I get very excited and lost in it. But then I take a break due to exhaustion, and that’s when I derail.</p>

  <p>I have no sense of urgency in my life to achieve my goals as quickly as possible, and I don’t know why. I’m working on one feature at a speed that feels painfully slow, especially in this era of AI where people can build apps like mine in just a few hours. Why don’t I have that same sense of urgency? Is it because my father still supports me financially at the age of 25? If I moved out, would I develop that urgency? Maybe. Maybe not. I don’t know.</p>

  <p>I’m just fed up with myself. Why can’t I do what needs to be done? Why am I my own worst enemy? How are other people so responsible?</p>

  <p>I want to be able to work at least 8 hours a day, but I don’t know how to make that happen.</p>

  <p>I have an exam on Sunday, so I’ll be preparing for it over the next two days. The next blog I write will be on Monday.</p>
          `  
        },
        {
          id:26,
          title:'100 days of entrepreneurship day 31',
          slug:'100-days-of-entrepreneurship-day-31',
          day:'31',
          date:'Settember 2, 2025',
          snippet:"I’ve been so locked in that I almost forgot I even write a blog. ",
          content:`
          <p>Hello readers</p>
          <p>I’ve been so locked in that I almost forgot I even write a blog. I don’t know exactly what’s happening, but I’ve been able to work the whole day and actually enjoy it. The only problem is I can’t seem to sleep more than 6 hours. This started on Thursday when I began using Quorogel ointment for my wound. Maybe I’m just making baseless theories, but I can’t help wondering if there’s a connection.</p>

  <p>I used to think my sleep struggles came from not being productive enough during the day, but back then if I worked hard, I could sleep 8 hours. Now I’m productive the whole day, yet I’m still struggling to fall asleep—and staying asleep has also become a challenge. I don’t know what’s going on.</p>

  <p>That said, I wish every day felt like this. I’m so happy being this productive instead of wasting my days. If only I could crack the sleep part.</p>

  <p>On another note, my exam went 10/10. There was even a meme question as an optional one, and I chose to answer it because it felt more challenging and fun.</p>

  <p>I also bought X Premium and ChatGPT Premium to increase my reach and speed up development. I thought X Premium would help me gain followers, but it’s been two days and nothing has changed 😭.</p>

  <p>Recently, I’ve been active on Product Hunt and enjoying it. I decided to launch <b>Sitchat</b> there just to see how it works. The launch failed and ended up in 90th place. I noticed that the products doing well on Product Hunt usually have proper planning and strategy behind them. So for <b>VibeMyType</b>, I’ll need to figure out a solid plan before launch to maximize my reach.</p>

  <p>Meanwhile, there’s been a lot of progress on the product. I analyzed a few chats, and it’s working really well. When I read my description, it felt very accurate—though I still need a few more iterations to perfect it.</p>

  <p>I think the MVP will be ready this week. Next week, I’ll need to focus on SEO, payments, and building a GTM strategy to make sure the launch is successful.</p>
          `
        },
        {
          id:27,
          title:'100 days of entrepreneurship day 32',
          slug:'100-days-of-entrepreneurship-day-32',
          day:'32',
          date:'Settember 3, 2025',
          snippet:"Still locked in today, but I got a good night’s sleep.",
          content:`
          <p>Hello readers</p>
          <p>Still locked in today, but I got a good night’s sleep. I don’t know why, but after sleeping well I was more relaxed and okay with not working as much as I do when I’m sleep-deprived. I think being in crisis mode can make you more productive, but I can’t sleep-deprive myself for that—it’s not good long term.</p>

  <p>I spent the whole day improving my reports. It was tedious—tweak, read, tweak again—but the report is now in a good enough place that I can move forward with integrating it with the frontend and implementing the vibe-card feature. I’m really excited about this. I’ll try to complete it tomorrow. After that, the only things left for the MVP will be integrating X, Reddit, and Instagram; a few blogs; SEO optimization; and payments. I think I can finish all of this by next weekend and be ready for launch. The rest I can keep implementing afterward.</p>

  <p>My follower count on X increased from 23 to 30 in two days, which is awesome. On Reddit, I’m getting a lot of recognition for my comments as well.</p>

  <p>I’m anxious about the launch, though, since my marketing plans for Sitchat were a big flop when I expected them to work easily.</p>

  <p>My plan is to post the vibe card on relevant subreddits and on X, and write about what I’ve made. That’ll be the first step. Next, I’ll analyze content from famous people and characters, create their vibe card and report, and share them in the right places. I’ll also write in self-help subreddits about how useful personality types are. I may even make some rage-bait content in MBTI subreddits. I’ll focus on X and Reddit for the first month. In the second month I’ll start short-form content marketing, and if I make some revenue I’ll definitely do influencer marketing, then post that content from my account and boost it with ads.</p>

  <p>Let’s see how the second product’s distribution goes.</p>

  <p>That’s it for today’s blog.</p>
          `
        },
        {
          id:28,
          title:'100 days of entrepreneurship day 33',
          slug:'100-days-of-entrepreneurship-day-33',
          day:'33',
          date:'Settember 4, 2025',
          snippet:"I accomplished everything I said I would in yesterday’s blog! Well, that’s a first. What a great feeling.",
          content:`
          <p>Hello readers</p>
          <p>I accomplished everything I said I would in yesterday’s blog! Well, that’s a first. What a great feeling. Well, almost everything—because vibe cards aren’t working yet, but the code is there.</p>

  <p>There’s something really crazy about community and movement. One person tweeted that from September 1st until the end of the year, it’s time to be locked in—and a bunch of other people joined him, including me. I think one of the main reasons I’m working this hard right now is because of that.</p>

  <p>I started reading <em>The Mom Test</em> yesterday, which is about how to talk to customers. The concept is basically this: if you ask your mom directly, <em>“Mom, I have a business idea,”</em> then tell her what it is and ask if it’s good, she’ll say yes because she loves you. And most other people will also say yes just to make you feel good. So the book teaches how to ask better questions. The first rule is: don’t talk about the idea or the problem—talk about the customer’s life and experiences.</p>

  <p>There were some examples that sparked an idea in me, so I posted in the MBTI subreddit asking people how and why they got into MBTI. I got a lot of answers, which gave me a better idea of how to position my product. Now I’m wondering: what should I include on my landing page to convert properly? I’m going to keep posting questions like this to learn more about people who are into MBTI. Next, I’ll ask about what tests they’ve tried, which ones they found best, and which ones they thought were the worst.</p>

  <p>Man, I’ve been rapidly gaining followers on X. Yesterday I had 30, today I have 39—that’s crazy.</p>

  <p>Now for the sad part. Although the momentum of my work has been going really well for the last 3–4 days, I’ll have to pause this weekend because one of my close friends, Tada, is coming to town. I was the one who invited him, so I’ve got to receive him and keep him company until Sunday. I’m really happy he’s coming—we’re meeting after 3–4 years—but I still didn’t want to break the momentum.</p>

  <p>The next things I need to implement are: report-to-PDF and email, then integration of X, Reddit, and Twitter, and finally payments and SEO. That should take 3–4 days max, so I should still be able to launch next week. I’ve been hyping my mystery product launch on X, so I have to follow through. I think that’s also why I’ve been gaining so many followers.</p>

          `
        },
        {
          id:29,
          title:'100 days of entrepreneurship day 34',
          slug:'100-days-of-entrepreneurship-day-34',
          day:'34',
          date:'Settember 11, 2025',
          snippet:"Shit, I did it again—another 5-day break. As I mentioned in my last blog, my friend was coming over and I wasn’t planning to work on the blog for the next 3 days, but it ended up turning into 5. :(",
          content:`
          <p>Hello readers</p>
          <!DOCTYPE html>
<html>
<head>
  <title>Blog Update</title>
</head>
<body>

  <p>Shit, I did it again—another 5-day break. As I mentioned in my last blog, my friend was coming over and I wasn’t planning to work on the blog for the next 3 days, but it ended up turning into 5. :(</p>

  <p>It was really nice meeting Tada after so many years. Our friendship felt exactly the same as it did back in college. It didn’t feel like we were meeting after such a long time—it was just like the day we left. But that was also part of the problem. Back in college we partied hard, and even though we’d left that behind, as soon as we met we kept saying “for old time’s sake” and pushed way beyond our limits. The 3 days were hardcore.</p>

  <p>After he left, I slept straight for 15 hours and woke up with both a hangover and a fever. Tada texted me saying the same thing happened to him. I guess we’re not 21 anymore.</p>

  <p>On the brighter side, I went to the doctor today and I don’t need to wear a dressing anymore. Finally—after 3 months since my surgery, I’m free. The bedrest was rough, but it’s done, and I can get back to normal life now.</p>

  <p>Yesterday I started working again, but I forgot about the blog. So, it starts again from today.</p>

  <p>I’ve made a lot of progress with my product. All the features are now done. What’s left is X, Reddit, and IG integration, SEO optimization, blogs, and payments. Hopefully, I’ll complete all of this over the weekend and launch next Monday.</p>

  <p>For the launch, I’m planning a breaking-news style video using AI models. It’ll go something like: <em>“Breaking news: AI can now decode your personality. In the wrong hands, this can be disastrous—but in your hands, it can be immensely powerful.”</em> Then I’ll do a breakdown of Elon Musk’s (or someone else’s) personality. I’ll boost it on X. Launch videos are big these days, and this will be a fun experiment.</p>

  <p>On top of that, I’ve started another product with my friend Deepankar: <strong>BananaPPT</strong>. Everyone’s been using the NanoBanana image model for amazing things, but no one’s using it to make out-of-this-world presentations. We’re targeting MBA and BBA students who have to give hundreds of presentations every semester. We’ll handle the research, create the presentations, and even provide speaker notes. It should be fun and (hopefully) work. More importantly, this is my first time working with another programmer. He’s a professional, so I’ll get to learn a lot.</p>

  <p>My new (and final) term is about to start. I’ve taken three subjects:</p>

  <ul>
    <li><strong>Web Dev Labs</strong>: Full-stack app development using Node.js, React, Express, PostgreSQL, and JWT auth.</li>
    <li><strong>Data Science Labs</strong>: Data cleaning, processing, pipelines, ML, deep learning, computer vision, LLMs, etc.</li>
    <li><strong>MLOps</strong>: Everything from DevOps to data versioning, model versioning, and serverless.</li>
  </ul>

  <p>Most of this will be a revision for me, except Node, React, and the MLOps part. But I’m excited—it’ll be fun.</p>

  <p>With all this, I’m basically becoming a one-man IT department. I’ll be learning, building, doing marketing for my product, and handling accounting for my company. A walking corporate. Like in <em>Foundation</em> where Cleons say, <em>“I am Empire.”</em> I’m like, <em>“I am Corporate.”</em></p>

  <p>Let’s see how everything pans out. I’m both scared and excited for what’s ahead.</p>

</body>
</html>

          `
        },
        {
          id:30,
          title:'100 days of entrepreneurship day 35',
          slug:'100-days-of-entrepreneurship-day-35',
          day:'35',
          date:'Settember 12, 2025',
          snippet:"<p>For my second product, I tried the new GitHub Copilot Speckit. ",
          content:`
          <p>Hello readers</p>
            <p>For my second product, I tried the new GitHub Copilot Speckit. The concept is fascinating: first, you describe what you want and why you want it. Then you decide how to do it—what tech stack to use, etc. It forms a list of tasks and then executes them, some even in parallel. So for the second product, Deepankar and I used it today, and the product was ready in 30 minutes. It was crazy. But I didn’t want to run it because I knew it wouldn’t work and would just be frustrating. So I told Deepankar to run it. As expected, the backend server didn’t start, the frontend server didn’t start, and he couldn’t even set up the virtual environment. That made me doubt his technical abilities—I may have overestimated him. There were already other signals, but this experiment is exactly for testing whether we can actually work together.</p>

  <p>For my main product, everything is basically ready. All the features are working. Now I get an email with the vibe cards, the analysis report, and the vibe report. All that’s left is to integrate with X, Instagram, and Reddit; then add character and celebrity analysis as content examples for users; handle SEO; and set up payments. After that, I can launch. I think I’ll be able to cover all of this over the weekend. Lastly, I need to do “benefit maxxing” for the landing page. Then I’ll be ready to launch.</p>

  <p>I updated the vibe card prompt today, and it’s good now.</p>

  <p>But it’s not all smooth. The analysis isn’t working properly. Different chats are showing different personalities, but today I noticed it gave the same typology for both participants. That means keeping the other person’s chat as context is doing more harm than good. I’ll remove the context and try again. Maybe that was the cause of the problem, and now it’ll show the types much more accurately.</p>

  <p>At this point, I started having second thoughts—what if it’s useless and no one shows up? What if no one buys, and I become a laughing stock for making something so stupid? Launching is giving me anxiety, but I guess that’s part of the process. This might work, it might not—but I’ve been optimistic until now, so I should keep the optimism up. Being a little delusional is part of the job.</p>

  <p>I don’t know why I’m scared, but I have to go through this. If I’m going to fail, I’d rather fail fast. I don’t have much time left—I need to settle down soon.</p>
          `
        },
        {
          id:31,
          title:'100 days of entrepreneurship day 36',
          slug:'100-days-of-entrepreneurship-day-36',
          day:'36',
          date:'Settember 15, 2025',
          snippet:"As I get closer to launch, I’ve started having second thoughts—really bad ones.",
          content:`
          <p>Hello readers</p>
          <p>As I get closer to launch, I’ve started having second thoughts—really bad ones. On Saturday and Sunday, I spent the whole time just tweaking prompts and chunking strategies. My thought was that since different chats were giving different results, they should all be consistent. To fix this, I ended up over-optimizing the prompt so much that it actually got worse. By Sunday, I simplified it again but kept a few useful tweaks. Now I usually get ENTP, INTP, or INFP, which makes sense. Honestly, the simplest solution is just to add a note saying: <em>“Upload a chat where you’re most authentic to get the most accurate results.”</em> But because of my anxiety, I overdid everything.</p>

  <p>Today, I spent the entire day researching and implementing Reddit and X integrations. It was a nightmare. X’s API costs $200/month—which I can’t afford—and most alternatives don’t work because of recent changes. After hours of struggle, I finally found one that works. Reddit was simple in comparison. Still, my whole day was wasted.</p>

  <p>My plan was to launch today, but I still need to deploy, integrate Instagram, implement payments, and refine my landing page. My new target is Wednesday. Tomorrow morning, I’ll deploy and implement payments by the afternoon. Then I’ll integrate Instagram by night. The day after, I’ll optimize my landing page for benefits and SEO. After that, I’ll do a soft launch across subreddits and X.</p>

  <p>Hopefully, it works out. Right now, I’m constantly swinging between <em>“this won’t work”</em> and <em>“this is the best idea ever.”</em> I’m finally starting to understand why people say entrepreneurship is hard—and I haven’t even properly started yet.</p>
          `
        },
        {
          id:32,
          title:'100 days of entrepreneurship day 37',
          slug:'100-days-of-entrepreneurship-day-37',
          day:'37',
          date:'Settember 17, 2025',
          snippet:"I wasted two whole days because of my ignorance and over-reliance on AI.",
          content:`
          <p>Hello readers</p>
            <p>I wasted two whole days because of my ignorance and over-reliance on AI. My Codex limit was over, so I had to take a three-day break for it to reset. During that time, I decided to finally deploy. The plan was simple: create Docker images, write a Docker YAML, and deploy using Coolify. Easy, right? Nope.</p>

  <p>First problem: the server wouldn’t connect. It should’ve been a simple process—paste the private key into Coolify and the public key into the server’s <code>ssh/authorized_keys</code>. Last time I did this, it worked instantly. This time, no luck. I went to AI for help, and it kept giving me different “solutions.” I tried every variant for hours, only to realize that the very first thing I tried had actually worked, even though it hadn’t worked in the last 2–3 attempts.</p>

  <p>But it didn’t end there. Next was the CI/CD pipeline. The pipeline was created, the site deployed, and it was live—but I had forgotten to change the API URL in the frontend. When I redeployed, the deployment failed due to server connection issues. At that point, I gave up. The next day, I tried again—same error. I fell back into the same loop: AI suggestions, hours wasted, nothing working. I was on the verge of tears.</p>

  <p>Finally, I opened an issue in the Coolify Discord. I explained the problem, but again, I got the same recycled advice I had already tried. Luckily, the founder saw the thread, emailed me, and said he was looking into it. Four to five hours later, it was fixed.</p>

  <p>Then came the real pain: a certificate error between the frontend and backend API. Again, I fell into the loop of trying random fixes until 1 a.m. Out of desperation, I checked the Docker logs for the backend and—boom—turns out it was just a missing environment variable. I fixed it, and everything worked. Two days of blood, sweat, and no results… all because of one missing env variable.</p>

  <p>I had even announced on X that I’d launch “tomorrow,” but that’s not happening anymore. Now I’m locking in <strong>Monday</strong> as the final launch date.</p>

  <p>What’s left:</p>
  <ul>
    <li>IG and Discord integration</li>
    <li>Payments and resources</li>
    <li>SEO optimization</li>
    <li>A bit of marketing content</li>
  </ul>

  <p>Then I can finally launch. What I thought would be a 2-week sprint has dragged into a month.</p>

  <p>But hey—it’s deployed now. That alone is a blissful feeling. Time to push through and get ready for Monday’s launch.</p>
          `,
        },
                {
          id:33,
          title:'100 days of entrepreneurship day 38',
          slug:'100-days-of-entrepreneurship-day-38',
          day:'38',
          date:'Settember 19, 2025',
          snippet:"I missed a day again. After the deployment was successful, I spent the whole day optimizing the landing page to the best of my understanding. ",
          content:`
          <p>Hello Readers,</p>
            <p>I missed a day again. After the deployment was successful, I spent the whole day optimizing the landing page to the best of my understanding. I believe the landing page is the most important part, as it’s my 24/7 salesperson. I think I’ve done a good job, but only time will tell. Sadly, I ended up spending the entire day on this. After that, I worked on SEO optimization, and the day was over.</p>

  <p>Today, I added some blogs and built a personality database where analyses and reports on TV show characters, anime characters, celebrities, etc. will be available. I think this will be really useful as marketing content. I can post these in their respective subreddits and also in different typology subreddits, leading to a lot of views and hopefully some conversions.</p>

  <p>I also got approval from Dodopayments to accept payments. So, I started learning how the payment process works and how to implement it. It looks straightforward: the frontend sends the details to the backend, the backend creates a checkout link, and once the payment is complete, they send a callback to my webhook to update the status. Now I just need to code it out. I’ll do this tomorrow along with Discord and Instagram integration.</p>

  <p>After that, I’ll create a lot of marketing content on Sunday. The launch is planned for Monday. <strong>That’s the plan—let’s see how it goes.</strong></p>
          `
        },
        {
          id:34,
          title:'100 days of entrepreneurship day 39',
          slug:'100-days-of-entrepreneurship-day-39',
          day:'39',
          date:'Settember 22, 2025',
          snippet:"I’m getting launch anxiety. I keep optimizing random things, and I’ve changed my prompts at least 20 times.",
          content:`
          <p>Hello readers</p>
             <p>I’m getting launch anxiety. I keep optimizing random things, and I’ve changed my prompts at least 20 times. Now I don’t even know if the results are better or worse. On top of that, I’m procrastinating. I need to make an ad, but I’m not doing it.</p>

  <p>I already spent a month building this, and I know I should be focusing on marketing now.</p>

  <p>My original plan was to create a “breaking news” style video about how AI can decode your personality. I also wanted to make posts in self-help groups about how knowing yourself is the most important thing, and then plug my product in between. Another plan was to do personality analyses of celebrities and fictional characters—using their tweets, TV shows, anime, movies with subtitles, or YouTube videos. I could post those daily in relevant subreddits and typology communities.</p>

  <p>But instead of moving ahead with any of this, I’m stuck optimizing my site, when I should have already started marketing. Launch anxiety feels very real, and it’s hard.</p>

  <p><strong>The good news is payments are working—and I already got one payment from a friend!</strong></p>
  `
        },
        {
          id:35,
          title:'100 days of entrepreneurship day 40',
          slug:'100-days-of-entrepreneurship-day-40',
          day:'40',
          date:'Settember 22, 2025',
          snippet:"I thought launch videos were a big thing these days, so I decided to make one too. ",
          content:`
          <p>Hello readers</p>
             <p>
    I thought launch videos were a big thing these days, so I decided to make one too. 
    My idea was to create a news-style video: <i>“Breaking news—the AI can decode your personality”</i> 
    and then explain the product.
  </p>

  <p>
    It took me six hours to make a 40-second clip using Veo 3 and Nano Banana. 
    It was frustrating—the image model rarely worked as expected. 
    I had to retry 4–5 times before getting anything decent, 
    and the same thing happened with the video model. 
    Eventually, it worked.
  </p>

  <p>
    The final video wasn’t the <i>“banger”</i> I had imagined. 
    I debated whether to post it, but in the end, I shared it with an honest story. 
    It didn’t perform too well: <b>200 views, 6 likes, 10–20 site visitors, and 2 sign-ups—no sales.</b>
  </p>

  <p>
    The good thing is that I’m done with the launch. 
    The anxiety is gone, and now I can focus on consistent posting and daily marketing.
  </p>

  <p>
    My current plan is to analyze the personalities of famous people using their Twitter accounts 
    and share the results on Twitter, their subreddits, the MBTI subreddit, and other related communities daily. 
    Hopefully, this will attract readers, and some of them will decide to get their vibe checked. 
    Let’s see how this strategy goes.
  </p>
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
    },
    sortedPosts() {
      return this.posts.sort((a, b) => b.id - a.id);
    }
  },
  // We no longer need the 'methods' block for selectPost/goBack
}
</script>

<template>
  <div class="min-h-screen relative overflow-hidden bg-background py-20 md:py-24">
    <div class="container mx-auto px-4">
      <main class="max-w-6xl mx-auto">
        <div v-if="currentPost">
          <Button as-child variant="outline" class="mb-8 gap-2">
            <RouterLink to="/blog">
              <ArrowLeft class="h-4 w-4" />
              Back to Blog List
            </RouterLink>
          </Button>
          <Card class="w-full shadow-lg">
            <CardHeader class="p-8 md:p-12">
              <CardTitle
                class="text-4xl md:text-5xl font-bold text-center mb-4 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent"
                id="text"
              >
                {{ currentPost.title }}
              </CardTitle>
              <div
                class="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-muted-foreground mt-4"
              >
                <span>By Hritik Gupta</span>
                <span class="hidden md:inline">|</span>
                <span>Published on {{ currentPost.date }}</span>
                <Badge variant="secondary" class="ml-2">Day {{ currentPost.day }}</Badge>
              </div>
            </CardHeader>
            <CardContent
              class="p-8 md:p-12 text-lg text-foreground/90 leading-relaxed space-y-6"
              v-html="currentPost.content"
              id="text"
            >
            </CardContent>
          </Card>
        </div>

        <!-- Blog list -->
        <div v-else>
          <h1
            class="text-5xl font-bold text-center mb-12 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent"
            id="text"
          >
            My Blog
          </h1>

          <!-- Grid layout -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card
              v-for="post in sortedPosts"
              :key="post.id"
              class="hover:shadow-xl transition-shadow duration-300"
            >
              <RouterLink :to="'/blog/' + post.slug" class="block">
                <CardHeader>
                  <CardTitle
                    class="text-2xl font-bold group-hover:text-primary"
                    id="text"
                  >
                    {{ post.title }}
                  </CardTitle>
                  <div
                    class="flex items-center gap-4 text-sm text-muted-foreground pt-2"
                  >
                    <span>{{ post.date }}</span>
                    <Badge variant="outline">Day {{ post.day }}</Badge>
                  </div>
                </CardHeader>
                <CardContent>
                  <p class="text-muted-foreground" id="text">
                    {{ post.snippet }}
                  </p>
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

    <!-- background decoration -->
    <div class="absolute inset-0 -z-10 overflow-hidden pointer-events-none">
      <div
        class="absolute right-20 top-1/3 h-72 w-72 rounded-full bg-primary/10 blur-3xl"
      ></div>
      <div
        class="absolute left-32 bottom-1/4 h-64 w-64 rounded-full bg-secondary/10 blur-3xl"
      ></div>
    </div>
  </div>
</template>
