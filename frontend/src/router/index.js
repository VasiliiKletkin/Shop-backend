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
      path: '/signin',
      name: 'signin',
      component: () => import('../views/SignInView.vue'),
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: () => import('../views/SignUpView.vue'),
    },
    {
      path: '/profile',
      name: 'Profile',
      component: () => import('../views/ProfileView.vue'),
    },
    // {
    //   path: '/admin',
    //   name: 'Admin',
    //   component: () => import('./views/BoardAdminView.vue')
    // },
    // {
    //   path: '/mod',
    //   name: 'Moderator',
    //   component: () => import('./views/BoardModeratorView.vue')
    // },
    // {
    //   path: '/user',
    //   name: 'User',
    //   component: () => import('./views/BoardUserView.vue')
    // }
  ]
})

export default router
