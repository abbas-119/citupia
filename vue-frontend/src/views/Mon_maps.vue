<template>
  <div class="flex h-screen w-screen">
    <div ref="map" class="flex-grow border-r-2 border-black"></div>
    <div class="w-1/4 bg-gray-100 p-6">
      <h1 class="text-2xl font-bold mb-8">Layers</h1>

      <div class="space-y-6">
        <div>
          <button @click="showMyLocation"
                  class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out">
            My Location
          </button>
          <br><br>
          <h2 class="text-xl font-semibold mb-4">City Bikes</h2>
          <!-- City Bikes buttons in two columns with grey color -->
          <div class="grid grid-cols-2 gap-3">
            <button @click="toggleLayer('CityBikes_Punkt')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              City Bikes Point
            </button>
            <button @click="toggleLayer('Cykelparkering_Punkt')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Bicycle parking
            </button>
            <button @click="toggleLayer('Cykelplan_Linje')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Bicycle plan Line
            </button>
            <button @click="toggleLayer('Cykelpump_Punkt')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Bicycle pump
            </button>
            <button @click="toggleLayer('Cykelraknare')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Bicycle counter
            </button>
            <button @click="toggleLayer('Cykelstrak_Linje')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Bicycle Line
            </button>

          </div>
        </div>

        <div>
          <h2 class="text-xl font-semibold mb-4">Pedestrian</h2>
          <!-- Pedestrian buttons in two columns with grey color -->
          <div class="grid grid-cols-2 gap-3">
            <button @click="toggleLayer('NVDB_Gagata')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Pedestrian Street
            </button>
            <button @click="toggleLayer('NVDB_Gangfartsomrade')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Pedestrian Zone
            </button>
          </div>
        </div>

        <div>
          <h2 class="text-xl font-semibold mb-4">Electric scooter</h2>
          <!-- Electric scooter button, centered since it's a single button -->
          <div class="flex justify-center">
            <button @click="toggleLayer('Elsparkcykelplats_Yta')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Electric scooter Point
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import markerIconPng from '@/store/marker-icon.png';
import markerShadowPng from '@/store/marker-shadow.png';

export default {
  name: 'MapWithContent',
  data() {
    return {
      userLocationMarker: null,
      layerVisibility: {
        CityBikes_Punkt: false,
        Cykelparkering_Punkt: false,
        Cykelplan_Linje: false,
        Cykelpump_Punkt: false,
        Cykelraknare: false,
        Cykelstrak_Linje: false,
        NVDB_Gagata: false,
        NVDB_Gangfartsomrade: false,
        Elsparkcykelplats_Yta: false,

      },
      wmsLayers: {}
    };
  },
  mounted() {
    this.loadMapQuestAPI().then(() => {
      this.initializeMap();
    });
  },
  methods: {
    loadScript(src) {
      return new Promise((resolve, reject) => {
        let script = document.createElement('script');
        script.src = src;
        script.onload = () => resolve(script);
        script.onerror = () => reject(new Error(`Script load error for ${src}`));
        document.head.appendChild(script);
      });
    },
    async loadMapQuestAPI() {
      try {
        await this.loadScript("https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-map.js?key=eg5NU7KjmX1dKGFERROvoPhsBAMooVH1");
        await this.loadScript("https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-traffic.js?key=eg5NU7KjmX1dKGFERROvoPhsBAMooVH1");
        console.log("MapQuest API loaded successfully.");
      } catch (error) {
        console.error("Failed to load MapQuest API:", error);
      }
    },
    initializeMap() {
      this.map = L.map(this.$refs.map, {
        center: [59.3293, 18.0686],
        zoom: 9,
      });

      L.tileLayer(
          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
          {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          }
      ).addTo(this.map);

      if (typeof MQ !== 'undefined') {
        MQ.trafficLayer().addTo(this.map);
        // MQ.mapLayer().addTo(this.map);
      }

      // Initialize WMS layers
      this.wmsLayers = {
        CityBikes_Punkt: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: 'Citupia:CityBikes_Punkt',
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        Cykelparkering_Punkt: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Cykelparkering_Punkt`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        Cykelplan_Linje: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Cykelplan_Linje`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        Cykelpump_Punkt: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Cykelpump_Punkt`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        Cykelraknare: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Cykelraknare`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        Cykelstrak_Linje: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Cykelstrak_Linje`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        NVDB_Gagata: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:NVDB_Gagata`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        NVDB_Gangfartsomrade: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:NVDB_Gangfartsomrade`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
        Elsparkcykelplats_Yta: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Elsparkcykelplats_Yta`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
      };

      // Initially add all layers to the map
      if (this.map) {
        Object.values(this.wmsLayers).forEach(layer => {
          layer.addTo(this.map);
          layer.setOpacity(this.layerVisibility[layer.options.layers] ? 1 : 0);
        });
      } else {
        console.error("Leaflet map instance is not defined.");
      }

      //     this.map.on('click', (e) => {
      //   const latlng = e.latlng;
      //   L.popup()
      //     .setLatLng(latlng)
      //     .setContent(`Coordinates: ${latlng.lat.toFixed(5)}, ${latlng.lng.toFixed(5)}`)
      //     .openOn(this.map);
      // });
    },
    toggleLayer(layerName) {
      const layer = this.wmsLayers[layerName];
      if (this.layerVisibility[layerName]) {
        layer.setOpacity(0);
      } else {
        layer.setOpacity(1);
      }
      this.layerVisibility[layerName] = !this.layerVisibility[layerName];
    },
    showMyLocation() {
      this.map.locate({setView: true, maxZoom: 13});
      this.map.on('locationfound', this.onLocationFound);
      this.map.on('locationerror', this.onLocationError);
    },
    onLocationFound(e) {
      const radius = e.accuracy / 2;
      if (!this.userLocationMarker) {
        const customIcon = L.icon({
          iconUrl: markerIconPng,
          shadowUrl: markerShadowPng,
          iconSize: [25, 41],
          shadowSize: [41, 41],
          iconAnchor: [12, 41],
          shadowAnchor: [12, 41],
          popupAnchor: [1, -34],
        });
        this.userLocationMarker = L.marker(e.latlng, {icon: customIcon}).addTo(this.map);
      } else {
        this.userLocationMarker.setLatLng(e.latlng);
      }
      L.circle(e.latlng, radius).addTo(this.map);
    },
    onLocationError(e) {
      alert(e.message);
    },
  },
};
</script>