<template>
  <div class="flex justify-center items-center h-screen">
    <!-- Categories and Filters Container (Top and Bottom) -->
    <div class="flex flex-col ml-5 w-1/4">
      <!-- Categories Box (Bigger and More to the Right) -->
      <div class="rounded-lg border p-5 mb-5">
        <div class="mb-5">
          <h2 class="text-lg font-semibold">Categories</h2>
        </div>
        <!-- List of categories -->
        <ul>
          <li class="mb-2">
            <button @click="showBikeLane" class="text-blue-600 hover:underline focus:outline-none">
              Bike lane
            </button>
          </li>
          <li class="mb-2">
            <button @click="showBikeStand" class="text-blue-600 hover:underline focus:outline-none">
              Bike stand
            </button>
          </li>
          <li class="mb-2">
            <button @click="showRentalBikes" class="text-blue-600 hover:underline focus:outline-none">
              Rental Bikes
            </button>
          </li>
        </ul>
      </div>

      <!-- Filters Box -->
      <div class="rounded-lg border p-5">
        <div class="mb-5">
          <h2 class="text-lg font-semibold">Filters</h2>
        </div>
        <ul>
          <li class="mb-2">
            <button @click="showFilter1" class="text-blue-600 hover:underline focus:outline-none">
              Filter 1
            </button>
          </li>
          <li class="mb-2">
            <button @click="showFilter2" class="text-blue-600 hover:underline focus:outline-none">
              Filter 2
            </button>
          </li>
          <li class="mb-2">
            <button @click="showFilter3" class="text-blue-600 hover:underline focus:outline-none">
              Filter 3
            </button>
          </li>
        </ul>
      </div>
    </div>

    <!-- Map (More to the Right) -->
    <div class="flex-1 ml-20">
      <div id="map" class="h-screen w-full max-w-4xl" style="height: 600px;"></div>
    </div>
  </div>
</template>

<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

export default {
  name: 'LeafletMap',
  mounted() {
    // Ensure this code runs after the component mounts
    this.$nextTick(() => {
      this.initMap();
    });
  },
  methods: {
    initMap() {
      // Initialize the map
      const map = L.map('map').setView([59.3293, 18.0686], 9); // Coordinates for Stockholm

      // Add OpenStreetMap tiles
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
      }).addTo(map);

      // Add other map features here...
    },
    showBikeLane() {
      // Logic to show Bike Lane data on the map
    },
    showBikeStand() {
      // Logic to show Bike Stand data on the map
    },
    showRentalBikes() {
      // Logic to show Rental Bikes data on the map
    },
    showFilter1() {
      // Logic for Filter 1
    },
    showFilter2() {
      // Logic for Filter 2
    },
    showFilter3() {
      // Logic for Filter 3
    },
  }
};
</script>
