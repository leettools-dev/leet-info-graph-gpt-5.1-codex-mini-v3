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
    <p>Chat UI coming soon.</p>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useAuth } from '@/composables/useAuth'

const { user, hydrate, isAuthenticated } = useAuth()
const userData = computed(() => user.value)

onMounted(async () => {
  await hydrate()
  if (!isAuthenticated.value) {
    window.location.href = '/login'
  }
})
</script>
