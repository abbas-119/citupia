<template>
  <div class="bg-gradient-to-r from-orange-100 to-orange-400 flex flex-col items-center justify-start min-h-screen bg-gray-100 pt-20">
    <div>
      <h1 class="text-xl font-semibold mb-10">Select the Country</h1>
      <div class="flex flex-col space-y-2">
        <select v-model="selectedOptionC" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded">
          <option value="">Please select one</option>
          <option value="Portugal">Portugal</option>
          <option value="Sweden">Sweden</option>
        </select>
        <br><br><br>
        </div>
        <h1 class="text-xl font-semibold mb-10">Select the City</h1>
      <div class="flex flex-col space-y-2">
        <select v-model="selectedOption" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded">
          <option value="">Please select one</option>
          <option value="Stolkholm">Portugal</option>
          <option value="Braga">Sweden</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      selectedOptionC: '',
      selectedOption: '',
    };
  },
  methods: {
    navigateToSelectedOption() {
      if (this.selectedOption) {
        this.$router.push(this.selectedOption);
      }
    },
  },
};
</script>

