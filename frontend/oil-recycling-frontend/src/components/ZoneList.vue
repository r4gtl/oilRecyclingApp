<template>
  <div class="container mt-4">
    <h1 class="mb-3">Elenco Zone</h1>
    <div class="table-responsive">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Zona</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="zona in zone"
            :key="zona.id"
            @click="goToDetail(zona.id)"
            style="cursor: pointer"
          >
            <td>{{ zona.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const zone = ref([]);

function goToDetail(id) {
  // Naviga alla rotta per il dettaglio del cliente
  // router.push({ name: 'cliente-detail', params: { id } });
  router.push({ name: 'zona-edit', params: { id } });
}

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/zone/');
    zone.value = response.data;
  } catch (error) {
    console.error('Errore nel recuperare le zone:', error);
  }
});
</script>

<style scoped>
/* Puoi aggiungere stili personalizzati se necessario */
</style>
