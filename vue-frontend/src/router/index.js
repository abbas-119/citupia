import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from "@/views/AboutView.vue";
import PrivacyView from "@/views/PrivacyView.vue";
import LoginView from "@/views/LoginView.vue";
import SignUpView from "@/views/SignUpView.vue";
import ForgotPasswordView from "@/views/ForgotPasswordView.vue";
import ResetPasswordView from "@/views/ResetPasswordView.vue";
import ActivationView from "@/views/ActivationView";
import SettingsView from "@/views/SettingsView";
import Monitoring from "@/views/Monitoring.vue";

const routes = [
  {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUpView
    },
    {
    path: '/',
    name: 'home',
    component: HomeView
  },
    {
        path: '/privacy',
        name: 'privacy',
        component: PrivacyView
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LoginView
    },
    {
        path: '/password/reset',
        name: 'ForgotPassword',
        component: ForgotPasswordView
    },
    {
        path: '/password/reset/confirm/:uid/:token',
        name: 'ResetPassword',
        component: ResetPasswordView
    },

    {
        path: '/activate/:uid/:token',
        name: 'Activation',
        component: ActivationView
    },
    {
        path: '/settings/',
        name: 'settings',
        component: SettingsView
    },
    {
        path: '/monitoring/',
        name: 'monitoring',
        component: Monitoring
    },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: AboutView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
