<template>
  <div class="flex justify-center items-center h-screen">
    <!-- Categories and Filters Container -->
    <div class="flex flex-col ml-5 w-1/4">
      <!-- Categories Box -->
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

    <!-- Map Container -->
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
  data() {
    return {
      map: null,
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.initMap();
    });
  },
  methods: {
    initMap() {
      // Initialize the map
      this.map = L.map('map').setView([59.3293, 18.0686], 10);

      // Add OpenStreetMap tiles
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
      }).addTo(this.map);
    },
    async addWfsLayer(wfsUrl) {
      try {
        const response = await fetch(wfsUrl);
        const data = await response.json();
        const wfsLayer = L.geoJSON(data, {
          onEachFeature: (feature, layer) => {
            // Optionally add popups or other interactions here
            layer.bindPopup(feature.properties.MAIN_ATTRIBUTE_VALUE);
          }
        }).addTo(this.map);
        this.map.fitBounds(wfsLayer.getBounds());
      } catch (error) {
        console.error('Error loading WFS layer:', error);
      }
    },
    /*async addGeoJsonLayer() {
      try {
        // Adjust the URL to the location of your GeoJSON file
        const response = await fetch('data/mydata.geojson');
        const geojsonData = await response.json();
        L.geoJSON(geojsonData).addTo(this.map);
      } catch (error) {
        console.error('Error loading GeoJSON data:', error);
      }
    },*/
    showBikeStand() {
      const wfsUrl = 'https://openstreetgs.stockholm.se/geoservice/api/24041e9f-a752-4a88-8563-087ab48ce54b/wfs?request=GetFeature&typeName=od_gis:CityBikes_Punkt&outputFormat=JSON';
      this.addWfsLayer(wfsUrl);
    },
    showBikeLane() {
      // Logic to show Bike Lane data on the map
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
