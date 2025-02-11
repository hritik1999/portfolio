<script>
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
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

  <Avatar class="w-20 h-20">
    <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
    <AvatarFallback>CN</AvatarFallback>
  </Avatar>

</template>