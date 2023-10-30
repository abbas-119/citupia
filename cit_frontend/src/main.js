import { createApp } from 'vue';
import App from './App.vue';

// Import Bootstrap and BootstrapVue3 CSS files
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

// Import the BootstrapVue3 plugin
import { BootstrapVue3 } from 'bootstrap-vue-3';

const app = createApp(App);

// Use the BootstrapVue3 plugin
app.use(BootstrapVue3);

app.mount('#app');
