import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/home.vue'
import About from '@/views/about.vue'
import Product from '@/views/Product.vue'
import Blog from '@/views/Blog.vue'
import Projects from '@/views/project.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/products',
    name: 'Product',
    component: Product
  },
  {
    path: '/blog',
    name: 'Blog',
    component: Blog
  },
    {
    path: '/blog/:slug', 
    name: 'blog-post',
    component: Blog
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
