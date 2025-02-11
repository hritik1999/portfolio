<script>
export default {
  name: 'Home',
  data() {
    return {
      title: 'Home',
      description: 'Welcome to my portfolio',
    }
  }
}
</script>

<template>
  <div>
    <!-- Hero Section -->
    <section class="container mx-auto px-4 py-20 text-center">
      <div class="flex flex-col items-center space-y-4">
        <Avatar class="h-32 w-32">
          <AvatarImage src="https://github.com/yourusername.png" alt="@yourusername" />
          <AvatarFallback>YN</AvatarFallback>
        </Avatar>
        <h1 class="text-4xl font-bold">Your Name</h1>
        <p class="text-xl text-muted-foreground">Full Stack Developer</p>
        <div class="flex gap-4">
          <Button asChild>
            <RouterLink to="/about">About Me</RouterLink>
          </Button>
          <Button asChild variant="outline">
            <RouterLink to="/projects">View Projects</RouterLink>
          </Button>
        </div>
      </div>
    </section>  
  </div>

</template>