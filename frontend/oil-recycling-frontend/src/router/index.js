import { createRouter, createWebHistory } from 'vue-router';
import ClientiList from '../components/ClientiList.vue';
import ZoneList from '../components/ZoneList.vue';
import ClienteDetail from '../views/ClienteDetail.vue';
import ClienteEdit from '../views/ClienteEdit.vue';
import ZonaEdit from '../views/ZonaEdit.vue';

const routes = [
  {
    path: '/',
    name: 'clienti-list',
    component: ClientiList,
  },
  {
    path: '/cliente/:id',
    name: 'cliente-detail',
    component: ClienteDetail,
    props: true, // Passa i parametri di rotta come props
  },
  {
    path: '/cliente/:id/edit',
    name: 'cliente-edit',
    component: ClienteEdit,
    props: true,
  },
  {
    path: '/zone/',
    name: 'zone-list',
    component: ZoneList,
  },
  {
    path: '/zona/:id/edit',
    name: 'zona-edit',
    component: ZonaEdit,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
