<template>
  <div class="min-h-screen flex flex-col justify-center items-center relative">
    <div class="absolute inset-0 bg-gradient-to-b from-purple-900 to-indigo-900"></div>
    <div class="absolute inset-0 bg-black opacity-75"></div>
    <div class="absolute inset-0 z-10 flex flex-col justify-center items-center">
      <h1 class="text-center text-3xl sm:text-4xl font-extrabold text-white mb-8">Welcome to Your Dashboard</h1>
      <div class="grid grid-cols-2 gap-4">
        <button @click="goToMonitoring" class="button bg-orange-500 hover:bg-orange-600 py-3 px-6 sm:py-2 sm:px-4">Monitoring</button>
        <button @click="goToPlanning" class="button bg-orange-500 hover:bg-orange-600 py-3 px-6 sm:py-2 sm:px-4">Planning</button>
      </div>
    </div>
    <div class="absolute inset-0 z-0 flex justify-center items-center">
      <img src="@/store/vecteezy_mapa-poligonal-de-suiza_22791598.png" alt="Background Image" class="object-cover w-full h-full" />
    </div>
  </div>
</template>

<script>

import loginView from "@/views/LoginView.vue";
export default {
  name: "HomeView",
  components: {
    loginView,
  },
  methods: {
    goToMonitoring() {
      this.$router.push('/SelectionM/');
    },
    goToPlanning() {
      this.$router.push('/SelectionP/');
    },
  },
};
</script>

<style scoped>
.button {
  background-color: #6B46C1;
  color: #FFFFFF;
  font-weight: bold;
  padding: 12px 24px;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #805AD5;
}
</style>
