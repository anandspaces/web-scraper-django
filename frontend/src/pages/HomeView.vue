<template>
  <DefaultLayout>
    <div class="container mx-auto p-4">
      <div class="bg-white shadow rounded-lg p-6">
        <h1 class="text-3xl font-bold mb-6 text-gray-800">Web Scraper</h1>
        
        <input 
          v-model="url" 
          type="text" 
          placeholder="Enter website URL" 
          class="border rounded w-full p-3 mb-4 text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        
        <button 
          @click="scrapeSite"
          :disabled="loading"
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline disabled:opacity-50"
        >Scrape</button>
        
        <Loader v-if="loading" />

        <div v-if="data" class="mt-6">
          <h2 class="text-2xl font-semibold text-gray-800 mb-4">Scraped Data:</h2>
          <pre class="bg-gray-100 p-4 rounded overflow-auto">{{ data }}</pre>
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
