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
            <button @click="toggleLayer('Cykelpump_Punkt')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Bicycle pump
            </button>
            <button @click="toggleLayer('Elsparkcykelplats_Yta')"
                    class="bg-gray-500 hover:bg-gray-700 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate">
              Electric bike parking area
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
import userIcon from '@/store/here.png';
import axios from "axios";

export default {
  name: 'MapWithContent',
  data() {
    return {
      userLocationMarker: null,
      layerVisibility: {
        CityBikes_Punkt: false,
        Cykelparkering_Punkt: false,
        // Add other layers here if needed
      },
      wmsLayers: {},
      geoJsonLayers: {} // Maintain GeoJSON layers
    };
  },
  mounted() {
    this.loadMapQuestAPI().then(() => {
      this.initializeMap();
      this.CityBikes_Punkt();
      this.Cykelparkering_Punkt();
      this.Cykelpump_Punkt();
      this.Elsparkcykelplats_Yta();

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

      // Initially add all layers to the map
      if (this.map) {
        Object.values(this.wmsLayers).forEach(layer => {
          layer.addTo(this.map);
          layer.setOpacity(this.layerVisibility[layer.options.layers] ? 1 : 0);
        });
      } else {
        console.error("Leaflet map instance is not defined.");
      }
    },
    CityBikes_Punkt() {
      const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:CityBikes_Punkt&srsname=EPSG:4326&outputFormat=json';

      axios.get(url)
          .then(response => {
            this.addGeoJsonLayer(response.data, 'CityBikes_Punkt');
          })
          .catch(error => {
            console.error('Error fetching GeoJSON data:', error);
          });
    },
    Cykelparkering_Punkt() {
      // Example URL for fetching additional GeoJSON data
      const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:Cykelparkering_Punkt&srsname=EPSG:4326&outputFormat=json';

      axios.get(url)
          .then(response => {
            this.addGeoJsonLayer(response.data, 'Cykelparkering_Punkt');
          })
          .catch(error => {
            console.error('Error fetching additional GeoJSON data:', error);
          });
    },
    Cykelpump_Punkt() {
    const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:Cykelpump_Punkt&srsname=EPSG:4326&outputFormat=json';

    axios.get(url)
        .then(response => {
          this.addGeoJsonLayer(response.data, 'Cykelpump_Punkt');
        })
        .catch(error => {
          console.error('Error fetching Cykelpump_Punkt GeoJSON data:', error);
        });
  },
  Elsparkcykelplats_Yta() {
    const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:Elsparkcykelplats_Yta&srsname=EPSG:4326&outputFormat=json';

    axios.get(url)
        .then(response => {
          this.addGeoJsonLayer(response.data, 'Elsparkcykelplats_Yta');
        })
        .catch(error => {
          console.error('Error fetching Elsparkcykelplats_Yta GeoJSON data:', error);
        });
  },
    addGeoJsonLayer(geoJsonData, layerName) {
      const geoJsonLayer = L.geoJSON(geoJsonData, {
        pointToLayer: function (feature, latlng) {
          // Customize marker icon
          const customIcon = L.icon({
            iconUrl: markerIconPng,
            shadowUrl: markerShadowPng,
            iconSize: [25, 41], // Size of the icon
            shadowSize: [41, 41], // Size of the shadow
            iconAnchor: [12, 41], // Point of the icon which will correspond to marker's location
            shadowAnchor: [12, 41], // The same for the shadow
            popupAnchor: [1, -34] // Point from which the popup should open relative to the iconAnchor
          });
          const marker = L.marker(latlng, {icon: customIcon});
          // Add popup with coordinates
          const coordinates = latlng.lat.toFixed(5) + ", " + latlng.lng.toFixed(5);
          marker.bindPopup("Coordinates: " + coordinates).openPopup();
          return marker;
        }
      });

      this.geoJsonLayers[layerName] = geoJsonLayer;

      if (this.layerVisibility[layerName]) {
        geoJsonLayer.addTo(this.map);
      }
    },
    toggleLayer(layerName) {
      this.layerVisibility[layerName] = !this.layerVisibility[layerName];

      if (this.geoJsonLayers[layerName]) {
        if (this.layerVisibility[layerName]) {
          this.geoJsonLayers[layerName].addTo(this.map);
        } else {
          this.map.removeLayer(this.geoJsonLayers[layerName]);
        }
      }
    },
    showMyLocation() {
      this.map.locate({setView: true, maxZoom: 13});
      this.map.on('locationfound', this.onLocationFound);
      this.map.on('locationerror', this.onLocationError);
    },
onLocationFound(e) {
  const radius = e.accuracy / 2;

  // Clear previous markers and popups
  this.map.eachLayer(layer => {
    if (layer instanceof L.Marker && layer !== this.userLocationMarker) {
      this.map.removeLayer(layer);
    }
  });

  // Update user location marker or create new if not exists
  if (!this.userLocationMarker) {
    const customIcon = L.icon({
      iconUrl: userIcon,
      shadowUrl: markerShadowPng,
      iconSize: [40, 41],
      shadowSize: [41, 41],
      iconAnchor: [12, 41],
      shadowAnchor: [12, 41],
      popupAnchor: [1, -34],
    });
    this.userLocationMarker = L.marker(e.latlng, {icon: customIcon}).addTo(this.map);
    L.circle(e.latlng, radius).addTo(this.map);
  } else {
    this.userLocationMarker.setLatLng(e.latlng);
  }

  // Initialize variables for nearest points
  let nearestPoints = [];

  // Iterate through each visible layer
  for (const layerName of Object.keys(this.layerVisibility)) {
    if (this.layerVisibility[layerName] && this.geoJsonLayers[layerName]) {
      const geoJsonLayer = this.geoJsonLayers[layerName];
      let nearestDistance = Infinity;
      let nearestFeature = null;

      // Iterate through each feature in the GeoJSON layer
      geoJsonLayer.eachLayer(featureLayer => {
        const distance = e.latlng.distanceTo(featureLayer.getLatLng());
        if (distance < nearestDistance) {
          nearestDistance = distance;
          nearestFeature = featureLayer;
        }
      });

      // Store the nearest point for this layer
      nearestPoints.push({
        layerName: layerName,
        nearestDistance: nearestDistance,
        nearestFeature: nearestFeature
      });
    }
  }

  // Display markers and popups for the nearest points
  nearestPoints.forEach(nearestPoint => {
    const nearestLatLng = nearestPoint.nearestFeature.getLatLng();
    const nearestMarker = L.marker(nearestLatLng, {
      title: "Nearest Point"
    }).addTo(this.map);

    nearestMarker.bindPopup(`Nearest Point from ${nearestPoint.layerName} is ${nearestPoint.nearestDistance.toFixed(2)} meters away.`).openPopup();
  });
},



    onLocationError(e) {
      alert(e.message);
    },
  },
};
</script>
