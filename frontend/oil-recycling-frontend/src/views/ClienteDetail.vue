<template>
  <div class="container mt-4">
    <h1>Dettaglio Cliente</h1>
    <div v-if="cliente">
      <p><strong>Ragione Sociale:</strong> {{ cliente.ragionesociale }}</p>
      <p><strong>Indirizzo:</strong> {{ cliente.indirizzo }}</p>
      <p><strong>CAP:</strong> {{ cliente.cap }}</p>
      <p><strong>Città:</strong> {{ cliente.city }}</p>
      <p><strong>Provincia:</strong> {{ cliente.provincia }}</p>
      <p>
        <strong>Sito Web:</strong>
        <a v-if="cliente.sito_web" :href="cliente.sito_web" target="_blank">
          {{ cliente.sito_web }}
        </a>
      </p>
      <p><strong>E-mail:</strong> {{ cliente.e_mail }}</p>
      <!-- Aggiungi altri campi o un form per modificare il cliente -->
      <button class="btn btn-primary" @click="editCliente">
        Modifica Cliente
      </button>
    </div>
    <div v-else>Caricamento in corso...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const cliente = ref(null);
const clienteId = route.params.id;

console.log('clienteId:', clienteId); // Debug

onMounted(async () => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/cliente/${clienteId}/`
    );
    cliente.value = response.data;
  } catch (error) {
    console.error('Errore nel recuperare il cliente:', error);
  }
});

function editCliente() {
  // Qui potresti navigare verso una pagina di modifica oppure aprire un form modale
  // Per esempio:
  router.push({ name: 'cliente-edit', params: { id: clienteId } });
  // Oppure, se non hai ancora definito una rotta per l'edit, implementa il form direttamente in questa pagina
}
</script>

<style scoped>
/* Aggiungi eventuali stili per il dettaglio del cliente */
</style>
