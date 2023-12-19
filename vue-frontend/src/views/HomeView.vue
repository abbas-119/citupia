<template>
  <div class="bg-gradient-to-r from-orange-100 to-orange-400 flex flex-col items-center justify-start min-h-screen bg-gray-100 pt-20">
    <div>
      <h1 class="text-xl font-semibold mb-10">Select from the following:</h1>
      <div class="flex flex-col space-y-2">
        <button href="/monitoring/" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded mb-3">Monitoring</button>
        <button href="/Planning/" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded">Planning</button>
      </div>
    </div>

  </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";
import {formatDay, formatPubDate, formatMonthYear} from "./dateUtils";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  methods: {


    user() {
      axiosClient.get("/v1/users/me").then((response) => {
        this.user = response.data;
      });
    },
  },
  updated() {
    if (localStorage.getItem("largeFont") === "true") {
      // remove all different text size class
      document.querySelectorAll('.text-xs').forEach(e => e.classList.remove('text-xs'));
      document.querySelectorAll('.text-sm').forEach(e => e.classList.remove('text-sm'));
      document.querySelectorAll('.text-base').forEach(e => e.classList.remove('text-base'));
      document.querySelectorAll('.text-lg').forEach(e => e.classList.remove('text-lg'));
      document.querySelectorAll('.text-xl').forEach(e => e.classList.remove('text-xl'));
      document.body.classList.add('text-xl')
    }
  },
};
</script>
