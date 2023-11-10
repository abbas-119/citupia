import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import SignUpView from '@/views/SignUpView.vue';
import LogInView from "@/views/LogInView.vue";

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/signup', name: 'SignUp', component: SignUpView.vue},
  { path: '/login', name: 'LogIn', component: LogInView.vue}
  // ...add other routes here
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
