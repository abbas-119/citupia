<template>
  <div class="min-h-screen flex flex-col justify-center items-center relative">
    <div class="absolute inset-0 bg-gradient-to-b from-purple-900 to-indigo-900"></div>
    <div class="absolute inset-0 bg-black opacity-75"></div>
    <div class="absolute inset-0 z-10 flex flex-col justify-center items-center">
      <h1 class="text-4xl font-extrabold text-white mb-8">Select Your Location</h1>
      <div class="flex flex-col space-y-6 items-center">
        <select v-model="selectedOptionC" class="select-dropdown">
          <option value="" disabled>Please select a country</option>
          <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
        </select>
        <select v-model="selectedOption" class="select-dropdown">
          <option value="" disabled>Please select a city</option>
          <option v-for="city in availableCities" :key="city" :value="city">{{ city }}</option>
        </select>
        <button @click="goToMaps" :class="['button', { 'button-disabled': isButtonDisabled }]"
                :disabled="isButtonDisabled" style="text-align: center;">
          Next
        </button>
      </div>
    </div>
    <div class="absolute inset-0 z-0 flex justify-center items-center">
      <img src="@/store/vecteezy_mapa-poligonal-de-suiza_22791598.png" alt="Background Image"
           class="object-cover w-full h-full"/>
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
      countries: ['Sweden'],
      countryCities: {
        Sweden: ['Stockholm']
      },
      availableCities: [],
      isButtonDisabled: true
    };
  },
  watch: {
    selectedOptionC(newCountry) {
      this.availableCities = this.countryCities[newCountry] || [];
      this.selectedOption = '';
      this.checkFields();
    },
    selectedOption() {
      this.checkFields();
    }
  },
  methods: {
    goToMaps() {
      this.$router.push('/plan_maps/');
    },
    checkFields() {
      this.isButtonDisabled = !this.selectedOptionC || !this.selectedOption;
    }
  },
};
</script>

<style scoped>
.select-dropdown {
  appearance: none;
  background-color: #805AD5;
  color: #FFFFFF;
  font-weight: bold;
  padding: 12px 24px;
  border-radius: 10px;
  cursor: pointer;
  border: none;
  width: 300px;
}

.button {
  background-color: #6B46C1;
  color: #000000;
  font-weight: bold;
  padding: 12px 24px;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button-disabled {
  background-color: #FFFFFF;
  cursor: not-allowed;
}

.button:hover {
  background-color: #805AD5;
}
</style>