import { createApp } from 'vue'
import { createPinia } from 'pinia'

import axios from 'axios'
import VueAxios from 'vue-axios'

import { BootstrapVue, IconsPlugin, CardPlugin} from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App.vue'
import router from './router'
import stores from './stores';

import Vuelidate from 'vuelidate'

const app = createApp(App)
app.config.productionTip = false

app.use(createPinia())
app.use(router)
app.use(stores)
app.use(VueAxios, axios)
app.use(BootstrapVue)
app.use(Vuelidate)

app.mount('#app')


