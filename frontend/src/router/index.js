import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import SignUpView from '@/views/SignUpView.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/signup', name: 'SignUp', component: SignUpView.vue},
  // ...add other routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
