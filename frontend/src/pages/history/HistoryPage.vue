<template>
  <div class="p-8">
    <header class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold">Your Research History</h1>
      <p class="text-sm text-slate-500">Manage saved prompts and sessions.</p>
    </header>

    <section v-if="sessionStore.loading" class="text-sm text-slate-500">Loading sessions…</section>

    <section v-else>
      <ul class="space-y-3">
        <li
          v-for="session in sessionStore.sessions"
          :key="session.session_id"
          class="border rounded-lg p-4 flex justify-between items-center"
        >
          <div>
            <p class="font-semibold">{{ session.prompt }}</p>
            <p class="text-xs text-slate-500">{{ formatTimestamp(session.created_at) }}</p>
          </div>
          <div class="flex gap-2">
            <button
              class="text-blue-600 text-sm"
              @click="navigateToChat(session.session_id)"
            >
              View
            </button>
            <button
              class="text-red-600 text-sm"
              @click="deleteSession(session.session_id)"
            >
              Delete
            </button>
          </div>
        </li>
      </ul>
      <p v-if="!sessionStore.sessions.length" class="text-sm text-slate-500 mt-2">No sessions found.</p>
    </section>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useSessionStore } from '@/stores/modules/session'
import { useAuthStore } from '@/stores/modules/auth'

const router = useRouter()
const sessionStore = useSessionStore()
const authStore = useAuthStore()

const formatTimestamp = (value) => {
  const date = new Date(value * 1000)
  return date.toLocaleString()
}

const navigateToChat = (sessionId) => {
  router.push({ path: '/chat', query: { session: sessionId } })
}

const deleteSession = async (sessionId) => {
  await sessionStore.removeSession(sessionId)
}

onMounted(async () => {
  await authStore.hydrate()
  if (!authStore.isAuthenticated) {
    router.replace('/login')
    return
  }
  await sessionStore.fetchSessions()
})
</script>
