<template>
  <div class="container mt-4">
    <h1 class="mb-3">Elenco Clienti</h1>
    <div class="table-responsive">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Ragione Sociale</th>
            <th>Indirizzo</th>
            <th>CAP</th>
            <th>Città</th>
            <th>Provincia</th>
            <th>Sito Web</th>
            <th>E-mail</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="cliente in clienti"
            :key="cliente.id"
            @click="goToDetail(cliente.id)"
            style="cursor: pointer"
          >
            <td>{{ cliente.ragionesociale }}</td>
            <td>{{ cliente.indirizzo }}</td>
            <td>{{ cliente.cap }}</td>
            <td>{{ cliente.city }}</td>
            <td>{{ cliente.provincia }}</td>
            <td>
              <a
                v-if="cliente.sito_web"
                :href="cliente.sito_web"
                target="_blank"
                @click.stop
              >
                {{ cliente.sito_web }}
              </a>
            </td>
            <td>{{ cliente.e_mail }}</td>
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
const clienti = ref([]);

function goToDetail(id) {
  // Naviga alla rotta per il dettaglio del cliente
  // router.push({ name: 'cliente-detail', params: { id } });
  router.push({ name: 'cliente-edit', params: { id } });
}

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/clienti/');
    clienti.value = response.data;
  } catch (error) {
    console.error('Errore nel recuperare i clienti:', error);
  }
});
</script>

<style scoped>
/* Puoi aggiungere stili personalizzati se necessario */
</style>
