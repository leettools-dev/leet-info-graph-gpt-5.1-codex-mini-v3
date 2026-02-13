<template>
  <div class="p-8">
    <header class="flex justify-between items-center mb-6">
      <div>
        <h1 class="text-2xl font-bold">Research Infograph Assistant</h1>
        <p class="text-sm text-slate-500">AI-generated infographics with sources</p>
      </div>
      <div v-if="user" class="text-right">
        <p class="text-sm text-slate-500">Signed in as:</p>
        <p class="font-semibold">{{ user.name }}</p>
        <p class="text-xs text-slate-400">{{ user.email }}</p>
      </div>
    </header>

    <section class="mb-6" v-if="isAuthenticated">
      <div class="flex gap-2 items-start">
        <input
          v-model="prompt"
          type="text"
          placeholder="Enter research prompt"
          class="flex-1 border border-slate-300 rounded px-3 py-2"
        />
        <button
          class="bg-blue-600 text-white px-4 py-2 rounded shadow"
          :disabled="sessionStore.creating"
          @click="handleCreate"
        >
          {{ sessionStore.creating ? 'Creating…' : 'New Research' }}
        </button>
      </div>
      <div class="text-xs text-red-500 mt-2" v-if="sessionStore.error">
        {{ sessionStore.error.message || 'Unable to create session' }}
      </div>
    </section>

    <section v-if="sessionStore.sessionCount">
      <h2 class="text-lg font-semibold mb-2">Recent sessions</h2>
      <ul class="space-y-2">
        <li
          v-for="session in sessionStore.sessions"
          :key="session.session_id"
          class="border p-3 rounded hover:bg-slate-50 cursor-pointer"
        >
          <p class="font-semibold">{{ session.prompt }}</p>
          <p class="text-xs text-slate-500">{{ formatTimestamp(session.created_at) }}</p>
        </li>
      </ul>
    </section>

    <p v-else>No sessions yet.</p>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/modules/auth'
import { useSessionStore } from '@/stores/modules/session'

const authStore = useAuthStore()
const sessionStore = useSessionStore()
const prompt = ref('')

const isAuthenticated = computed(() => authStore.isAuthenticated)
const user = computed(() => authStore.user)

const formatTimestamp = (value) => {
  const date = new Date(value * 1000)
  return date.toLocaleString()
}

const handleCreate = async () => {
  if (!prompt.value.trim()) {
    return
  }
  await sessionStore.addSession(prompt.value.trim())
  prompt.value = ''
}

onMounted(async () => {
  await authStore.hydrate()
  if (!authStore.isAuthenticated) {
    window.location.href = '/login'
    return
  }
  await sessionStore.fetchSessions()
})
</script>
