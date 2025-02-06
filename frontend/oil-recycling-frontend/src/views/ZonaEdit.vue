<template>
  <div class="container mt-4">
    <h1>Modifica Zona</h1>
    <div v-if="zona">
      <form @submit.prevent="updateZona">
        <div class="row">
          <div class="col-sm mb-2">
            <label class="form-label">Nome</label>
            <input
              type="text"
              class="form-control"
              v-model="zona.name"
              required
            />
          </div>
        </div>
        <div class="row">
          <div class="col-sm mb-2">
            <label class="form-label">Descrizione</label>
            <input
              type="text"
              class="form-control"
              v-model="zona.description"
            />
          </div>
        </div>

        <button type="submit" class="btn btn-primary me-2">Salva</button>
        <!-- Pulsante per tornare all'elenco dei clienti -->
        <button class="btn btn-danger" @click="goToList">Annulla</button>
      </form>
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
const zona = ref(null);
const zonaId = route.params.id;
console.log('clienteId:', zonaId);

onMounted(async () => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/zone/${zonaId}/`
    );
    zona.value = response.data;
  } catch (error) {
    console.error('Errore nel recuperare la zona:', error);
  }
});

async function updateZona() {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/zone/${zonaId}/`,
      zona.value
    );
    console.log('Zona aggiornata:', response.data);
    //router.push({ name: 'cliente-detail', params: { id: clienteId } });

    // Dopo l'aggiornamento, torna all'elenco
    router.push({ name: 'zone-list' });
  } catch (error) {
    console.error("Errore nell'aggiornare la zona:", error);
  }
}
function goToList() {
  router.push({ name: 'zone-list' });
}
</script>

<style scoped>
/* Aggiungi eventuali stili personalizzati */
</style>
