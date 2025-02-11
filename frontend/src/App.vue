<script setup>
import { RouterLink, RouterView } from 'vue-router'
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from '@/components/ui/navigation-menu'
import { Input } from '@/components/ui/input'
import { useColorMode } from '@vueuse/core'
import { Button } from '@/components/ui/button'

const mode = useColorMode('dark')

</script>

<template>
  <div class="w-full h-screen flex flex-col">
    <div class="w-full bg-gray-900 fixed top-0 left-0 right-0 z-50">
      <NavigationMenu class="w-full">
        <NavigationMenuList class="w-full p-4 flex items-center">
          <div class="flex items-center pl-6 pr-20 mr-20">
            <NavigationMenuItem>
              <NavigationMenuLink asChild>
                <RouterLink to="/" class="text-xl font-bold tracking-wide text-white">HG</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>
          </div>

          <div class="flex items-center gap-6 ml-auto pl-20 pr-6 ml-10">
            <NavigationMenuItem>
              <NavigationMenuLink asChild>
                <RouterLink to="/about" class="text-white">About</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <NavigationMenuLink asChild>
                <RouterLink to="/products" class="text-white">Products</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <NavigationMenuLink asChild>
                <RouterLink to="/projects" class="text-white">Projects</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <NavigationMenuLink asChild>
                <RouterLink to="/contact" class="text-white">Contact</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>

            <NavigationMenuItem>
              <NavigationMenuLink asChild>
                <RouterLink to="/blog" class="text-white">Blog</RouterLink>
              </NavigationMenuLink>
            </NavigationMenuItem>

            <Input 
              class="bg-gray-800 border-gray-700 text-white w-48"
              placeholder="Enter tone..." 
            />
            <Button variant="default">Change Tone</Button>
            
            <Input 
              class="bg-gray-800 border-gray-700 text-white w-48"
              placeholder="Enter style..." 
            />
            <Button variant="default">Change Style</Button>
          </div>
        </NavigationMenuList>
      </NavigationMenu>
    </div>

    <main class="flex-grow w-full pt-[80px]">
      <RouterView class="w-full h-full" />
    </main>
  </div>
</template>