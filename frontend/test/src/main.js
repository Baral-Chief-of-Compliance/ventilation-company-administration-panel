/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Plugins
import { registerPlugins } from '@/plugins'

import ymapPlugin from 'vue-yandex-maps'


const pinia = createPinia()
const app = createApp(App)
const settings = {
    apiKey: 'aaca613a-fe9d-47d2-95f3-cd1714593fff'
}
registerPlugins(app)
app.use(ymapPlugin, settings)
app.use(pinia)

app.mount('#app')
