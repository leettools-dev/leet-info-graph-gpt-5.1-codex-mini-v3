import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/modules/auth'

import LoginPage from '@/pages/auth/LoginPage.vue'
import ChatPage from '@/pages/chat/ChatPage.vue'
import HistoryPage from '@/pages/history/HistoryPage.vue'

const routes = [
  { path: '/', redirect: '/chat' },
  { path: '/login', component: LoginPage, meta: { guestOnly: true } },
  { path: '/chat', component: ChatPage, meta: { requiresAuth: true } },
  { path: '/history', component: HistoryPage, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const authStore = useAuthStore()
  const isAuthenticated = authStore.isAuthenticated

  if (to.meta.requiresAuth && !isAuthenticated) {
    return { path: '/login', query: { redirect: to.fullPath } }
  }

  if (to.meta.guestOnly && isAuthenticated) {
    return { path: '/chat' }
  }
})

export default router
