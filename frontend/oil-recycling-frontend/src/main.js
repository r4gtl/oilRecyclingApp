import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';

// Importa il CSS di Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';

// Se vuoi utilizzare i componenti JavaScript di Bootstrap, importa anche il bundle (include Popper)
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

createApp(App).use(router).mount('#app');
