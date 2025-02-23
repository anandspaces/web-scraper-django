<template>
  <DefaultLayout>
    <div class="min-h-screen flex justify-center items-center p-6 bg-gray-100">
      <div class="w-full max-w-3xl bg-white shadow-lg rounded-lg p-6">
        <h1 class="text-4xl font-bold mb-4 text-blue-600 text-center">Web Scraper</h1>
        <p class="text-gray-600 mb-6 text-center">Enter a website URL to scrape its content.</p>
        
        <input 
          v-model="url" 
          type="text" 
          placeholder="Enter website URL" 
          class="border border-gray-300 rounded w-full p-3 mb-4 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        
        <button 
          @click="scrapeSite"
          :disabled="loading"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline disabled:opacity-50"
        >
          {{ loading ? 'Scraping...' : 'Scrape' }}
        </button>

        <Loader v-if="loading" class="mt-4" />

        <div v-if="data" class="mt-6 bg-gray-50 p-4 rounded-lg shadow-md overflow-auto max-h-96">
          <h2 class="text-2xl font-semibold text-gray-800 mb-2">Scraped Data:</h2>
          <pre class="text-sm text-gray-700 whitespace-pre-wrap">{{ data }}</pre>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script lang="ts">
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import { defineComponent, ref } from 'vue'
import { scrapeSite } from '@/api/scraper'
import Loader from '@/components/Loader.vue'

export default defineComponent({
  name: 'HomeView',
  components: {
    DefaultLayout,
    Loader
  },
  setup() {
    const url = ref('')
    const data = ref('')
    const loading = ref(false)

    const scrapeSiteData = async () => {
      if (!url.value) {
        alert('Please enter a URL')
        return
      }
      loading.value = true
      try {
        const response = await scrapeSite(url.value)
        data.value = response.data.data.content // Display only the content
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
