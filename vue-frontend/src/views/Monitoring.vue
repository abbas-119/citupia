<template>
  <div class="bg-gradient-to-r from-orange-100 to-orange-400 flex flex-col items-center justify-start min-h-screen bg-gray-100 pt-20">
    <div>
      <h1 class="text-xl font-semibold mb-10">Select the Country</h1>
      <div class="flex flex-col space-y-2">
        <select v-model="selectedOptionC" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded">
          <option value="">Please select one</option>
          <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
        </select>
        <br><br><br>
      </div>
      <h1 class="text-xl font-semibold mb-10">Select the City</h1>
      <div class="flex flex-col space-y-2">
        <select v-model="selectedOption" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded">
          <option value="">Please select one</option>
          <option v-for="city in availableCities" :key="city" :value="city">{{ city }}</option>
        </select>
      </div>
      <br><br><br><br><br><br>
      <div class="flex flex-col space-y-2">
        <button @click="goToMaps" class="bg-orange-200 hover:bg-orange-300 text-black font-bold py-2 px-4 rounded mb-3"> Next </button>
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
      countries: ['Sweden','Portugal'],
      countryCities: {
        Portugal: ['Braga'],
        Sweden: ['Stockholm']
      },
      availableCities: []
    };
  },
  watch: {
    selectedOptionC(newCountry) {
      this.availableCities = this.countryCities[newCountry] || [];
      this.selectedOption = ''; // Reset city selection when country changes
    }
  },
  methods: {
    navigateToSelectedOption() {
      if (this.selectedOption) {
        this.$router.push(this.selectedOption);
      }
    },
    goToMaps() {
      this.$router.push('/stk_maps/');
    },
  },
};
</script>
