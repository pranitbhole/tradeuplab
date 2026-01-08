import { createApp } from 'vue'
import App from './App.vue'
import skinData from './mock/skin_sample.json'
import './style.css'

createApp(App).mount('#app')

const app = createApp(App)
app.provide('skinData', skinData)
app.mount('#app')
