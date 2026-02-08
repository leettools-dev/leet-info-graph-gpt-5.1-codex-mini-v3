<script setup>
import { onMounted, ref } from 'vue'
import i18n from '@/i18n'
import api from '@/utils/request'

const backendStatus = ref('loading')

const checkBackend = async () => {
  try {
    await api.get('/health')
    backendStatus.value = 'connected'
  } catch (error) {
    backendStatus.value = 'disconnected'
  }
}

onMounted(() => {
  checkBackend()
})
</script>

<template>
  <div class="min-h-screen bg-[var(--color-bg)] text-[var(--color-text)] font-sans">
    <header class="p-6 border-b border-[var(--color-border)]">
      <div class="flex justify-between items-center">
        <div>
          <h1 class="text-2xl font-semibold">Research Infograph Assistant</h1>
          <p v-if="backendStatus === 'connected'" class="text-sm text-[var(--color-primary)]">
            {{ i18n.t('common.backendConnected') }}
          </p>
          <p v-else-if="backendStatus === 'disconnected'" class="text-sm text-red-400">
            {{ i18n.t('common.backendDisconnected') }}
          </p>
          <p v-else class="text-sm text-gray-400">Checking backend...</p>
        </div>
        <nav class="space-x-4">
          <router-link to="/chat" class="text-[var(--color-text)] hover:text-[var(--color-primary)]">Chat</router-link>
          <router-link to="/history" class="text-[var(--color-text)] hover:text-[var(--color-primary)]">History</router-link>
        </nav>
      </div>
    </header>
    <router-view />
  </div>
</template>
