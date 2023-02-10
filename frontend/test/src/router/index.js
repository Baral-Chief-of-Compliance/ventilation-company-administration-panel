// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: 'brigades',
        name: 'brigades',
        component: () => import('@/components/brigades/BrigadesInfo.vue')
      },
      {
        path: 'add_brigades',
        name: 'add_brigades',
        component: () => import('@/components/brigades/AddBrigades.vue')
      },
    ],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
