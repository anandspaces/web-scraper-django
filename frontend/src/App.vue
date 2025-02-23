<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HomeView from "./pages/HomeView.vue"
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
  </header>

  <RouterView />
</template>