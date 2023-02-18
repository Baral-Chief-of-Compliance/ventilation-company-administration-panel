/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

import ymapPlugin from 'vue-yandex-maps'

const app = createApp(App)

registerPlugins(app)
app.use(ymapPlugin)

app.mount('#app')
