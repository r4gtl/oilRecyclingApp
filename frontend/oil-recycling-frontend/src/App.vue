<template>
  <div>
    <!-- Include la navbar -->
    <Navbar />
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script setup>
// Se necessario, importa altri componenti o configurazioni
import Navbar from './components/Navbar.vue';
</script>

<style scoped></style>
