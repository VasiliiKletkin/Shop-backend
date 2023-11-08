import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component:() => import('../views/HomeView.vue'),
    },
    {
      path: '/products',
      name: 'products',
      component:() => import('../views/ProductsListView.vue'),
    },
    {
      path: '/products/:id',
      name: 'product-detail',
      component: () => import('../views/ProductDetailView.vue'),
    },
    {
      path: '/orders',
      name: 'orders',
      component: () => import('../views/OrdersListView.vue'),
    },
    {
      path: '/orders/:id',
      name: 'order-detail',
      component: () => import('../views/OrderDetailView.vue'),
    },
    
    // {
    //   path: '/profile',
    //   name: 'Profile',
    //   component: () => import('../views/ProfileView.vue'),
    // },

  ]
})

export default router
