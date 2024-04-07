## Overview
The Pedestrian Micro-Mobility Management Platform is a web-based application designed to tackle urban micro-mobility challenges. Leveraging advanced geospatial technologies and data analytics, this platform provides comprehensive tools for planning, monitoring, and managing pedestrian traffic and micro-mobility devices in urban environments.

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://git.cs.bham.ac.uk/projects-2023-24/aam119.git

2. **Navigate to the backend directory and install dependencies:**
   ```bash
   cd cit-backend
   pip install -r requirements.txt
   
3. **Run migrations and start the Django server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   
4. **Navigate to the frontend directory and install dependencies:**
   ```bash
   cd ../vue-frontend
   npm install
   
5. **Start the Vue.js server:**
   ```bash
    npm run serve
   
## GeoServer Installation and Setup

GeoServer plays a crucial role in managing and serving geospatial data for the platform. Follow these steps to install and configure GeoServer:

### Installation

1. **Download GeoServer**: Visit the [GeoServer official website](http://geoserver.org/download/) and download the appropriate version for your operating system.

2. **Install GeoServer**: 
   - For **Windows**, run the installer and follow the on-screen instructions.
   - For **Linux/Mac**, extract the downloaded archive and move it to a preferred directory.

3. **Start GeoServer**:
   - Navigate to the GeoServer directory.
   - For **Windows**, run `startup.bat` located in the `bin` folder.
   - For **Linux/Mac**, execute `sh startup.sh` from the `bin` directory.

4. **Access GeoServer**: Open a web browser and go to `http://localhost:"chosen port in installation"/geoserver`. The default port is `8080`, username is `admin` and password is `geoserver`.

### Adding Shapefiles (Layers)

1. **Shapefiles**: The Shape files are stored at `Shape_files` directory. Copy the shapefiles to a preferred directory.               

2. **Log in to GeoServer Web Admin Panel**: Access the GeoServer web admin panel by navigating to `http://localhost:"chosen port in installation"/geoserver/web/` and log in.

3. **Create a Workspace**: 
   - Go to `Data` > `Workspaces` > `Add new workspace`.
   - Fill in the `Name` and `Namespace URI`, then click `Save`.

4. **Create a Store**:
   - Navigate to `Data` > `Stores` > `Add new Store`.
   - Choose `Directory of spatial files (shapefiles)` as the Data Source.
   - Select the workspace you created earlier.
   - Provide a `Data Source Name` and `Description`.
   - Click `Browse` next to `Connection Parameters` > `URL`, and select your directory containing the shapefiles.
   - Click `Save`.

5. **Publish the Layer**:
   - Navigate to `Data` > `Layers`.
   - Click `Add a new layer`.
   - Select the store you created earlier.
   - GeoServer will recognize and list all the shapefiles in the directory as new layers.
   - Click `Publish` next to each layer you wish to configure.
   - Fill in the necessary details such as `Title`, `Abstract`, and ensure the `Bounding Boxes` are correctly set.
   - Click Save.

6. **Access Your Layer**:
   - Go to `Layer Preview`, find your layer, and choose a format to view it (e.g., OpenLayers, GeoJSON).

### Connecting GeoServer to the Vue.js Frontend

1. **Update the Vue.js Configuration**:
   - Navigate `vue-frontend` directory.
   - Navigate to `src` > `views` > `Mon_maps.vue` and `Plan_maps.vue`.
   - Update the `url` in the `map` object to match your GeoServer configuration.

## Note:
1. For Planning feature, if the user is not located in stockholm, Sweden, please use a VPN to access the feature. The feature is only available for Stockholm.
