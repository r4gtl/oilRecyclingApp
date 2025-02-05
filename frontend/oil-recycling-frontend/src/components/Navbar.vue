<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">ItineraTruck</router-link>
      <button
        class="navbar-toggler"
        type="button"
        @click="toggleNavbar"
        :aria-expanded="isCollapsed.toString()"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <!-- Applichiamo la classe "show" in base alla variabile reattiva -->
      <div
        class="collapse navbar-collapse"
        :class="{ show: isCollapsed }"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="#">Clienti</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';

const isCollapsed = ref(false);

function toggleNavbar() {
  isCollapsed.value = !isCollapsed.value;
}
</script>

<style scoped>
/* Puoi aggiungere eventuali personalizzazioni, se necessario */
</style>
