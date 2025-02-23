<template>
  <div class="min-h-screen flex flex-col bg-gray-100">
    <nav class="bg-blue-600 p-4 shadow-lg">
      <div class="container mx-auto text-white font-bold text-xl">
        <RouterLink to="/" class="hover:text-gray-300">Web Scraper</RouterLink>
      </div>
    </nav>
    <main class="flex-grow container mx-auto p-4">
      <slot />
    </main>
    <footer class="bg-gray-800 text-white text-center py-4">
      &copy; 2025 Web Scraper. All rights reserved.
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { RouterLink } from 'vue-router'

export default defineComponent({
  name: 'DefaultLayout'
})
</script>
