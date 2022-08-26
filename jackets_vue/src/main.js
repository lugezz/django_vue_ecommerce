import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import store from './store'

axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)
app.use(store)
app.use(router, axios)

app.mount('#app')
