<template>
  <div class="flex h-screen w-screen">
    <div ref="map" class="flex-grow border-r-2 border-black"></div>
    <div class="w-1/4">
      <div class="p-5">
        <h1 class="text-xl font-bold">Content</h1>
        <p>This is the content that will appear on the right side of the page.</p>
      </div>
      <!-- Add additional content here if needed -->
    </div>
  </div>
</template>
<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

export default {
  name: 'MapWithContent',
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
      const map = L.map(this.$refs.map, {
        center: [59.3293, 18.0686],
        zoom: 10,
      });

      L.tileLayer(
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                maxZoom: 19,
                attribution:
                    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            }
        ).addTo(map);

      // Ensure MQ is defined before using it
      if (typeof MQ !== 'undefined') {
        // MQ.mapLayer().addTo(map);
        MQ.trafficLayer().addTo(map);
      }

      L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
      layers: 'demo:NVDB_Motortrafikled',
      format: "image/png",
      transparent: true,

    }).addTo(map);

      // L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
      //       layers: `demo:Cykelparkering_Punkt`,
      //       format: "image/png",
      //       transparent: true,
      //
      //   }).addTo(map);

      L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
            layers: `demo:Cykelplan_Linje`,
            format: "image/png",
            transparent: true,

        }).addTo(map);

        L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
            layers: `demo:NVDB_Motorvag`,
            format: "image/png",
            transparent: true,

        }).addTo(map)

      // Add other layers as before...
    },
  },
}
</script>