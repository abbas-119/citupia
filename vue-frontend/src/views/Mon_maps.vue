<template>
  <div class="flex h-screen w-screen">
    <div ref="map" class="flex-grow border-r-2 border-black"></div>
    <div class="w-1/4 bg-gray-100 p-6">
      <h1 class="text-2xl font-bold mb-8">Layers</h1>

      <div class="space-y-6">
        <div>
          <button @click="showMyLocation" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out">
            My Location
          </button>
          <h2 class="text-xl font-semibold mb-4">City Bikes</h2>
          <!-- City Bikes buttons in two columns with grey color -->
          <div class="grid grid-cols-2 gap-3">
            <button @click="toggleLayer('CityBikes_Punkt')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">City Bikes Point</button>
<button @click="toggleLayer('Cykelparkering_Punkt')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Bicycle parking</button>
<button @click="toggleLayer('Cykelplan_Linje')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Bicycle plan Line</button>
<button @click="toggleLayer('Cykelpump_Punkt')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Bicycle pump</button>
<button @click="toggleLayer('Cykelraknare')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Bicycle counter</button>
<button @click="toggleLayer('Cykelstrak_Linje')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Bicycle Line</button>

          </div>
        </div>

        <div>
          <h2 class="text-xl font-semibold mb-4">Pedestrian</h2>
          <!-- Pedestrian buttons in two columns with grey color -->
          <div class="grid grid-cols-2 gap-3">
            <button @click="toggleLayer('NVDB_Gagata')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Pedestrian Street</button>
            <button @click="toggleLayer('NVDB_Gangfartsomrade')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Pedestrian Zone</button>
          </div>
        </div>

        <div>
          <h2 class="text-xl font-semibold mb-4">Electric scooter</h2>
          <!-- Electric scooter button, centered since it's a single button -->
          <div class="flex justify-center">
            <button @click="toggleLayer('Elsparkcykelplats_Yta')" class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">Electric scooter Point</button>
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
      map:null,
      userLocationMarker: null,
      layerVisibility: {
        NVDB_Motortrafikled: false,
        Cykelparkering_Punkt: false,
        Cykelplan_Linje: false,
        NVDB_Motorvag: false
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
    showMyLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
          const { latitude, longitude } = position.coords;
          this.updateUserLocation(latitude, longitude);
        }, () => {
          alert("Unable to retrieve your location");
        });
      } else {
        alert("Geolocation is not supported by this browser.");
      }
    },

    updateUserLocation(lat, lng) {
  const location = [lat, lng];

  // Create a custom icon with a shadow
  const customIcon = L.icon({
    iconUrl: markerIconPng,
    shadowUrl: markerShadowPng,
    iconSize: [25, 41], // Size of the icon
    shadowSize: [41, 41], // Size of the shadow
    iconAnchor: [12, 41], // Point of the icon which will correspond to marker's location
    shadowAnchor: [12, 41], // Point of the shadow which will correspond to the icon anchor
    popupAnchor: [1, -34], // Point from which the popup should open relative to the iconAnchor
  });

  // Check if the marker already exists
  if (!this.userLocationMarker) {
    // Create a new marker with the custom icon and add it to the map
    this.userLocationMarker = L.marker(location, { icon: customIcon });
    this.userLocationMarker.addTo(this.map);

    // Attach a click event to the user location marker
    this.userLocationMarker.on('click', (e) => {
      L.popup()
        .setLatLng(e.latlng)
        .setContent(`Coordinates: ${e.latlng.lat.toFixed(5)}, ${e.latlng.lng.toFixed(5)}`)
        .openOn(this.map);
    });
  } else {
    // Update the marker's position and icon if it already exists
    this.userLocationMarker.setLatLng(location);
    this.userLocationMarker.setIcon(customIcon);
  }

  // Center the map on the new location
  this.map.setView(location, 13); // Adjust the zoom level as needed
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
            attribution:
                '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          }
      ).addTo(this.map);

      // Ensure MQ is defined before using it
      if (typeof MQ !== 'undefined') {
        // MQ.mapLayer().addTo(map);
        // MQ.trafficLayer().addTo(this.map);
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
      Object.values(this.wmsLayers).forEach(layer => {
        layer.addTo(this.map);
        layer.setOpacity(this.layerVisibility[layer.options.layers] ? 1 : 0);
      });

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
    }
  },
};
</script>
