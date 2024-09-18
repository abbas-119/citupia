<template>
  <div class="flex flex-col md:flex-row h-screen w-screen">
    <div ref="map" class="flex-grow md:border-r-2 border-black"></div>
    <div class="w-full md:w-1/4 bg-gray-900 p-4 md:p-6 overflow-auto">
      <h1 class="text-2xl md:text-3xl font-bold mb-4 md:mb-8 text-white">Layers</h1>

      <div class="space-y-4">
        <div>
          <button @click="showMyLocation"
                  class="bg-gray-700 hover:bg-gray-800 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out w-full">
            My Location
          </button>
          <br><br>
          <h2 class="text-xl font-semibold mb-2 md:mb-4 text-white">City Bikes</h2>
          <div class="grid grid-cols-2 gap-2 md:gap-3">
            <button
    @click="toggleLayer('CityBikes_Punkt')"
    :class="activeButtons['CityBikes_Punkt'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
    class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full flex items-center space-x-2">
    <img src="@/store/map-pink.png" alt="City Bikes Icon" class="w-6 h-6">
    <span>City Bikes Point</span>
  </button>
            <button
                @click="toggleLayer('Cykelparkering_Punkt')"
                :class="activeButtons['Cykelparkering_Punkt'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full flex items-center space-x-2">
              <img src="@/store/map-red.png" alt="City Parking" class="w-6 h-6">
              Bicycle Parking Point
            </button>

            <button
                @click="toggleLayer('Cykelpump_Punkt')"
                :class="activeButtons['Cykelpump_Punkt'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full flex items-center space-x-2">
              <img src="@/store/map-brown.png" alt="City Parking" class="w-6 h-6">
              Bicycle Pump Point
            </button>
            <button
                @click="toggleLayer('Cykelraknare')"
                :class="activeButtons['Cykelraknare'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full flex items-center space-x-2">
              <img src="@/store/map-blue.png" alt="City Parking" class="w-6 h-6">
              Bicycle counter
            </button>
            <button
                @click="toggleLayer('Elsparkcykelplats_Yta')"
                :class="activeButtons['Elsparkcykelplats_Yta'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate relative">
              <span class="absolute bottom-0 left-0 w-full h-1 bg-black"></span>
              Electric bike Parking
            </button>
            <button
    @click="toggleLayer('Cykelstrak_Linje')"
    :class="activeButtons['Cykelstrak_Linje'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
    class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full relative">
    <span class="absolute bottom-0 left-0 w-full h-1" style="background-color: #e8718d"></span>
    <span>Cycle Line</span>
  </button>
<!--            <button-->
<!--                @click="toggleLayer('Cykelplan_Linje')"-->
<!--                :class="activeButtons['Cykelplan_Linje'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"-->
<!--                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full">-->
<!--              Bicycle plan Line-->
<!--            </button>-->
            <!--            <button-->
            <!--                @click="toggleLayer('Markupplatelse_Punkt')"-->
            <!--                :class="activeButtons['Markupplatelse_Punkt'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"-->
            <!--                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full">-->
            <!--              Markupplatelse Point-->
            <!--            </button>-->
          </div>
<!--          <br>-->
<!--          <h2 class="text-xl font-semibold mb-2 md:mb-4 text-white">Pedestrian Network</h2>-->
<!--          <div class="grid grid-cols-2 gap-2 md:gap-3">-->
<!--            <button-->
<!--                @click="toggleLayer('NVDB_Gangfartsomrade')"-->
<!--                :class="activeButtons['NVDB_Gangfartsomrade'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"-->
<!--                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full">-->
<!--              Pedestrian Area-->
<!--            </button>-->
<!--            <button-->
<!--                @click="toggleLayer('NVDB_Gagata')"-->
<!--                :class="activeButtons['NVDB_Gagata'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"-->
<!--                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full">-->
<!--              Pedestrian Street-->
<!--            </button>-->
<!--          </div>-->
          <br>
<!--          <h2 class="text-xl font-semibold mb-2 md:mb-4 text-white">Motor vehicle traffic</h2>-->
<!--          <div class="grid grid-cols-2 gap-2 md:gap-3">-->
<!--          <button-->
<!--              @click="toggleLayer('Trafikflode_Motorfordon')"-->
<!--              :class="activeButtons['Trafikflode_Motorfordon'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"-->
<!--              class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full">-->
<!--            Motor Traffic-->
<!--          </button>-->
<!--        </div>-->
<!--          <br>-->
        <h2 class="text-xl font-semibold mb-2 md:mb-4 text-white">Traffic flow</h2>

          <div class="grid grid-cols-2 gap-2 md:gap-3">
            <button @click="toggleLiveTrafficLayer"
                    :class="activeButtons['liveTraffic'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"
                    class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out w-full">
              {{ activeButtons['liveTraffic'] ? 'Hide Live Traffic' : 'Show Live Traffic' }}
            </button>
          </div>
          <br><br>

          <div>
    <button @click="clearLayers" class="bg-gray-700 hover:bg-gray-800 text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out w-full">
      Clear Layers
    </button>
  </div>
<!--          <h2 class="text-xl font-semibold mb-2 md:mb-4 text-white">Land Grant</h2>-->
<!--          <div class="grid grid-cols-2 gap-2 md:gap-3">-->
<!--            <button-->
<!--                @click="toggleLayer('Markupplatelse_Punkt')"-->
<!--                :class="activeButtons['Markupplatelse_Punkt'] ? 'bg-green-500 hover:bg-green-600' : 'bg-gray-700 hover:bg-gray-800'"-->
<!--                class="text-white font-semibold py-2 px-4 rounded transition duration-150 ease-in-out truncate w-full">-->
<!--              Land Grant-->
<!--            </button>-->
<!--          </div>-->


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
import red from '@/store/map-red.png';
import pink from '@/store/map-pink.png';
import blue from '@/store/map-blue.png';
import brown from '@/store/map-brown.png';
import axios from "axios";
import 'leaflet-routing-machine/dist/leaflet-routing-machine.css';
import 'leaflet-routing-machine';
import 'leaflet/dist/leaflet.css';


export default {
  name: 'MapWithContent',
  data() {
    return {
      userLocationMarker: null,
      activeButtons: {},
      routingControl: null,

      layerVisibility: {
        CityBikes_Punkt: false,
        Cykelparkering_Punkt: false,
        Cykelpump_Punkt: false,
        Elsparkcykelplats_Yta: false,
        Cykelplan_Linje: false,
        Cykelraknare: false,
        Cykelstrak_Linje: false,
        NVDB_Gagata: false,
        NVDB_Gangfartsomrade: false,
        // Markupplatelse_Punkt: false,
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
      this.Cykelraknare();
      // this.Markupplatelse_Punkt();
      // this.Elsparkcykelplats_Yta();

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
        await this.loadScript("https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-map.js?key=your_key");
        await this.loadScript("https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-traffic.js?key=your_key");
        await this.loadScript("https://www.mapquestapi.com/sdk/leaflet/v2.2/mq-routing.js?key=your_key");

        this.trafficLayer = MQ.trafficLayer();

        console.log("MapQuest API loaded successfully.");
      } catch (error) {
        console.error("Failed to load MapQuest API:", error);
      }
    },
    initializeMap() {
      this.map = L.map(this.$refs.map, {
        center: [59.3293, 18.0686],
        zoom: 12,
      });

      L.tileLayer(
          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
          {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          }
      ).addTo(this.map);

      // if (typeof MQ !== 'undefined') {
      //   MQ.trafficLayer().addTo(this.map);
      //   // MQ.mapLayer().addTo(this.map);
      // }


      // Change the localhost port and layers to match your GeoServer configuration for every wms layer.
      // Citupia:_______ where citupia is my workspace and _______ is the layer name.
      this.wmsLayers = {
        Cykelplan_Linje: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Cykelplan_Linje`,
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
        Trafikflode_Motorfordon: L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
          layers: `Citupia:Trafikflode_Motorfordon`,
          format: "image/png",
          transparent: true,
          attribution: "Your attribution here"
        }),
      };

    },
    CityBikes_Punkt() {
      const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:CityBikes_Punkt&srsname=EPSG:4326&outputFormat=json';
      const iconUrl = pink;

      axios.get(url)
          .then(response => {
            this.addGeoJsonLayer(response.data, 'CityBikes_Punkt', iconUrl);
          })
          .catch(error => {
            console.error('Error fetching GeoJSON data:', error);
          });
    },



    Cykelpump_Punkt() {
      const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:Cykelpump_Punkt&srsname=EPSG:4326&outputFormat=json';
      const iconUrl = brown;
      axios.get(url)
          .then(response => {
            this.addGeoJsonLayer(response.data, 'Cykelpump_Punkt', iconUrl);
          })
          .catch(error => {
            console.error('Error fetching Cykelpump_Punkt GeoJSON data:', error);
          });
    },
    Cykelraknare() {
      const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:Cykelraknare&srsname=EPSG:4326&outputFormat=json';
      const iconUrl = blue;

      axios.get(url)
          .then(response => {
            this.addGeoJsonLayer(response.data, 'Cykelraknare', iconUrl);
          })
          .catch(error => {
            console.error('Error fetching Cykelraknare GeoJSON data:', error);
          });
    },

    Cykelparkering_Punkt() {
      const url = 'https://openstreetgs.stockholm.se/geoservice/api/ba9e5991-379f-4eb4-b6a3-e288a3730b2a/wfs/?version=1.0.0&request=GetFeature&typeName=od_gis:Cykelparkering_Punkt&srsname=EPSG:4326&outputFormat=json';
      const iconUrl = red;

      axios.get(url)
          .then(response => {
            this.addGeoJsonLayer(response.data, 'Cykelparkering_Punkt', iconUrl);
          })
          .catch(error => {
            console.error('Error fetching additional GeoJSON data:', error);
          });
    },

    addGeoJsonLayer(geoJsonData, layerName, iconUrl) {
      const customIcon = L.icon({
        iconUrl: iconUrl,
        shadowUrl: markerShadowPng,
        iconSize: [30, 30], // Adjust the icon size here
        shadowSize: [25, 25], // Adjust the shadow size if needed
        iconAnchor: [7, 25], // Adjust the icon anchor if needed
        shadowAnchor: [7, 25], // Adjust the shadow anchor if needed
        popupAnchor: [1, -18] // Adjust the popup anchor if needed
      });

      const geoJsonLayer = L.geoJSON(geoJsonData, {
        pointToLayer: function (feature, latlng) {
          const marker = L.marker(latlng, {icon: customIcon});
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

    toggleLiveTrafficLayer() {
      if (this.activeButtons['liveTraffic']) {
        if (this.map.hasLayer(this.trafficLayer)) {
          this.map.removeLayer(this.trafficLayer);
        }
        delete this.activeButtons['liveTraffic'];
      } else {
        this.trafficLayer.addTo(this.map);
        this.activeButtons['liveTraffic'] = true;
      }
    },


    toggleLayer(layerName) {
      // Toggle visibility
      this.layerVisibility[layerName] = !this.layerVisibility[layerName];

      // Toggle active state
      if (this.activeButtons[layerName]) {
        // If button is already active, remove it to indicate deactivation
        delete this.activeButtons[layerName];
      } else {
        // Activate button by setting its state to true
        this.activeButtons[layerName] = true;
      }

      // Ensure reactivity
      this.activeButtons = {...this.activeButtons};

      // Add or remove layer from the map based on the updated visibility
      if (this.layerVisibility[layerName]) {
        if (this.geoJsonLayers[layerName]) {
          this.geoJsonLayers[layerName].addTo(this.map);
        }
        if (this.wmsLayers[layerName]) {
          this.wmsLayers[layerName].addTo(this.map);
        }
      } else {
        if (this.geoJsonLayers[layerName]) {
          this.map.removeLayer(this.geoJsonLayers[layerName]);
        }
        if (this.wmsLayers[layerName]) {
          this.map.removeLayer(this.wmsLayers[layerName]);
        }
      }
    },

    displayRoute(from, to) {
    // Remove the previous routing control if it exists
    if (this.routingControl) {
      this.map.removeControl(this.routingControl);
    }

    // Create a new routing control and store it
    this.routingControl = L.Routing.control({
      waypoints: [
        L.latLng(from.lat, from.lng),
        L.latLng(to.lat, to.lng)
      ],
      // Set the waypoints to readonly
      draggableWaypoints: false,
    }).addTo(this.map);
  },

    clearLayers() {
    // Remove all markers and circle markers from the map
    this.map.eachLayer(layer => {
      if (layer instanceof L.Marker || layer instanceof L.CircleMarker) {
        this.map.removeLayer(layer);
      }
    });
    // Remove routing control and routing directions from the map
    if (this.routingControl) {
      this.map.removeControl(this.routingControl);
      this.routingControl = null;
    }
  },




   showMyLocation() {
  this.map.locate({setView: true, maxZoom: 14});
  this.map.once('locationfound', e => {
    this.onLocationFound(e);

    if (this.nearestPoint) {
      L.Routing.control({
        waypoints: [
          L.latLng(e.latlng.lat, e.latlng.lng),
          L.latLng(this.nearestPoint.lat, this.nearestPoint.lng)
        ],
        routeWhileDragging: true
      }).addTo(this.map);
    }
  });
  this.map.on('locationerror', this.onLocationError);
},



   onLocationFound(e) {
  const userLocation = e.latlng;
  // Clear existing markers and routes
  this.map.eachLayer(layer => {
    if (layer instanceof L.Marker || layer instanceof L.Routing.Control || layer instanceof L.CircleMarker) {
      this.map.removeLayer(layer);
    }
  });
  let nearestPoints = [];
  // Iterate through each GeoJSON layer to find the nearest point
  Object.keys(this.geoJsonLayers).forEach(layerName => {
    let nearestDistance = Infinity;
    let nearestFeature = null;
    this.geoJsonLayers[layerName].eachLayer(featureLayer => {
      const featureLatLng = featureLayer.getLatLng();
      const distance = userLocation.distanceTo(featureLatLng);
      if (distance < nearestDistance) {
        nearestDistance = distance;
        nearestFeature = featureLayer;
      }
    });
    if (nearestFeature) {
      nearestPoints.push(nearestFeature);
    }
  });
  // Display only the nearest points on the map
  nearestPoints.forEach(featureLayer => {
    L.marker(featureLayer.getLatLng(), {
      icon: featureLayer.options.icon,
    }).addTo(this.map).on('click', (event) => {
      this.displayRoute(userLocation, event.latlng);
    });
  });
  // Draw a circle marker at the user's location
  L.circleMarker(userLocation, {
    radius: 5, // Adjust the radius of the circle
    color: 'blue', // Adjust the color of the circle
    fillColor: '#3388ff', // Adjust the fill color of the circle
    fillOpacity: 0.8 // Adjust the fill opacity of the circle
  }).addTo(this.map);
},


    getLayerIconUrl(layerName) {
      // Define the icon URLs for each layer
      const iconUrls = {
        CityBikes_Punkt: pink,
        Cykelparkering_Punkt: red,
        Cykelpump_Punkt: brown,
        Elsparkcykelplats_Yta: blue,
        Cykelraknare: blue,
        // Add more layers and their icon URLs if needed
      };

      // Return the icon URL for the specified layer
      return iconUrls[layerName] || null;
    },


    onLocationError(e) {
      alert(e.message);
    },


  },


};
</script>

<style scoped>
/* Add responsive styles here */
@media screen and (min-width: 640px) {
  .h-half {
    height: 50%;
  }
}
</style>
