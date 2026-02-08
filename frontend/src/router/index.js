import { createRouter, createWebHistory } from 'vue-router'

import LoginPage from '@/pages/auth/LoginPage.vue'
import ChatPage from '@/pages/chat/ChatPage.vue'
import HistoryPage from '@/pages/history/HistoryPage.vue'

const routes = [
  {
    path: '/',
    redirect: '/chat',
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    meta: { title: 'Login' },
  },
  {
    path: '/chat',
    name: 'Chat',
    component: ChatPage,
    meta: { title: 'Chat' },
  },
  {
    path: '/history',
    name: 'History',
    component: HistoryPage,
    meta: { title: 'History' },
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/chat',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
