<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css">
    <title>Leaflet geoserver request</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
        }
        #map {
            width: 100%;
            height: 100vh;
        }
    </style>
</head>
<body>
    <div id="app">
        <!-- Vue.js App -->
        <div id="app">
            <!-- Categories and Filters Container -->
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
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"></script>
    <script src="../src/L.Geoserver.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14"></script>

    <script>
        new Vue({
            el: '#app',
            methods: {
                showBikeLane() {
                    // Implement logic for showing Bike Lane data on the map
                },
                showBikeStand() {
                    // Implement logic for showing Bike Stand data on the map
                },
                showRentalBikes() {
                    // Implement logic for showing Rental Bikes data on the map
                },
                showFilter1() {
                    // Implement logic for Filter 1
                },
                showFilter2() {
                    // Implement logic for Filter 2
                },
                showFilter3() {
                    // Implement logic for Filter 3
                }
            },
            mounted() {
                // Initialize the map
                var map = L.map("map", { zoomControl: false }).setView([59.3293, 18.0686], 10);
                var osmLayer = L.tileLayer(
                    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    {
                        maxZoom: 19,
                        attribution:
                            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                    }
                ).addTo(map);

                var wms1 = L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
                    layers: `demo:NVDB_Motortrafikled`,
                    format: "image/png",
                    transparent: true,
                    attribution: "CityBikes_Punkt",
                });
                wms1.addTo(map);

                var wms2 = L.tileLayer.wms("http://localhost:8090/geoserver/wms", {
                    layers: `demo:Cykelparkering_Punkt`,
                    format: "image/png",
                    transparent: true,
                    attribution: "CityBikes",
                });
                wms2.addTo(map);
            }
        });
    </script>
</body>
</html>
