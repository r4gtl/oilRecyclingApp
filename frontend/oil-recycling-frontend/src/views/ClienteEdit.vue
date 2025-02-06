<template>
  <div class="container mt-4">
    <h1>Modifica Cliente</h1>
    <div v-if="cliente">
      <form @submit.prevent="updateCliente">
        <div class="row">
          <div class="mb-3">
            <label class="form-label">Ragione Sociale</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.ragionesociale"
              required
            />
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4 mb-2">
            <label class="form-label">Indirizzo</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.indirizzo"
            />
          </div>
          <div class="col-sm-1 mb-2">
            <label class="form-label">CAP</label>
            <input type="text" class="form-control" v-model="cliente.cap" />
          </div>
          <div class="col-sm-4 mb-2">
            <label class="form-label">Città</label>
            <input type="text" class="form-control" v-model="cliente.city" />
          </div>
          <div class="col-sm-3 mb-2">
            <label class="form-label">Provincia</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.provincia"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-sm-3 mb-2">
            <label class="form-label">Zona</label>
            <input type="text" class="form-control" v-model="cliente.zona" />
          </div>
          <div class="col-sm-1 mb-2">
            <label class="form-label">Tolleranza meno (gg)</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.tolerance_before"
            />
          </div>
          <div class="col-sm-1 mb-2">
            <label class="form-label">Tolleranza più (gg)</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.tolerance_after"
            />
          </div>
          <div class="col-sm-3 mb-2">
            <label class="form-label">Intervallo di ritiro (gg)</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.pickup_interval"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-sm-3 mb-2">
            <label class="form-label">Sito Web</label>
            <input
              type="text"
              class="form-control"
              v-model="cliente.sito_web"
            />
          </div>
          <div class="col-sm-3 mb-2">
            <label class="form-label">E-mail</label>
            <input type="email" class="form-control" v-model="cliente.e_mail" />
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
const cliente = ref(null);
const clienteId = route.params.id;
console.log('clienteId:', clienteId);

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

async function updateCliente() {
  try {
    const response = await axios.put(
      `http://127.0.0.1:8000/api/cliente/${clienteId}/`,
      cliente.value
    );
    console.log('Cliente aggiornato:', response.data);
    //router.push({ name: 'cliente-detail', params: { id: clienteId } });

    // Dopo l'aggiornamento, torna all'elenco
    router.push({ name: 'clienti-list' });
  } catch (error) {
    console.error("Errore nell'aggiornare il cliente:", error);
  }
}
function goToList() {
  router.push({ name: 'clienti-list' });
}
</script>

<style scoped>
/* Aggiungi eventuali stili personalizzati */
</style>
