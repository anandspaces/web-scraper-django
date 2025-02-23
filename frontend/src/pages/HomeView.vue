<template>
  <DefaultLayout>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Web Scraper</h1>
      <input 
        v-model="url" 
        type="text" 
        placeholder="Enter website URL" 
        class="border rounded w-full p-2 mb-4"
      />
      <button 
        @click="scrapeSite"
        class="bg-blue-500 text-white rounded px-4 py-2"
      >Scrape</button>

      <Loader v-if="loading" />

      <div v-if="data" class="mt-4">
        <h2 class="text-xl font-semibold">Scraped Data:</h2>
        <pre>{{ data }}</pre>
      </div>
    </div>
  </DefaultLayout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { scrapeSite } from '@/api/scraper'
import Loader from '@/components/Loader.vue'

export default defineComponent({
  name: 'HomeView',
  components: {
    Loader
  },
  setup() {
    const url = ref('')
    const data = ref('')
    const loading = ref(false)

    const scrapeSiteData = async () => {
      if (!url.value) return alert('Please enter a URL')
      loading.value = true
      try {
        const response = await scrapeSite(url.value)
        data.value = response.data.data
      } catch (error) {
        console.error(error)
        alert('Failed to scrape site.')
      } finally {
        loading.value = false
      }
    }

    return {
      url,
      data,
      loading,
      scrapeSite: scrapeSiteData
    }
  }
})
</script>
