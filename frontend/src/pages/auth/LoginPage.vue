<template>
  <div class="h-screen flex items-center justify-center bg-slate-50">
    <div class="bg-white shadow-lg rounded-xl p-10 w-96 text-center">
      <h1 class="text-3xl font-bold mb-4">Infograph Assistant</h1>
      <p class="mb-6 text-slate-500">Sign in with Google to start researching.</p>
      <div id="google-signin" class="mt-6"></div>
      <p v-if="authStore.error" class="text-xs text-red-500 mt-2">{{ authStore.error.message }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/modules/auth'

const authStore = useAuthStore()

onMounted(async () => {
  const googleClientId = import.meta.env.VITE_GOOGLE_CLIENT_ID
  if (!googleClientId) {
    console.warn('Google client ID is not configured')
    return
  }

  const handleCredentialResponse = async (response) => {
    if (response.credential) {
      try {
        await authStore.loginWithGoogle(response.credential)
        window.location.href = '/chat'
      } catch (error) {
        console.error('Failed to sign in with Google', error)
      }
    }
  }

  window.google?.accounts?.id.initialize({
    client_id: googleClientId,
    callback: handleCredentialResponse,
  })

  window.google?.accounts?.id.renderButton(
    document.getElementById('google-signin'),
    {
      theme: 'outline',
      size: 'large',
    },
  )

  window.google?.accounts?.id.prompt()
})
</script>
