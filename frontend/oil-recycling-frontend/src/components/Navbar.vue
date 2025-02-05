<!-- src/components/Navbar.vue -->
<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">ItineraTruck</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="#">Clienti</router-link>
          </li>
          <!-- Aggiungi altre voci del menu se necessario -->
        </ul>
      </div>
    </nav>
  </div>
</template>

<script setup>
// Se hai logica da aggiungere, puoi farlo qui
</script>

<style scoped>
/* Stili specifici per la navbar, se necessario */
</style>
