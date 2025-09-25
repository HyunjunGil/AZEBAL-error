import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

// Import views
import ProfileSelection from './views/ProfileSelection.vue'
import RecommendationResults from './views/RecommendationResults.vue'
import ProductDetail from './views/ProductDetail.vue'
import PurchaseComplete from './views/PurchaseComplete.vue'

// Router configuration
const routes = [
  { path: '/', component: ProfileSelection },
  { path: '/recommendations', component: RecommendationResults },
  { path: '/product/:id', component: ProductDetail },
  { path: '/purchase-complete', component: PurchaseComplete }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
