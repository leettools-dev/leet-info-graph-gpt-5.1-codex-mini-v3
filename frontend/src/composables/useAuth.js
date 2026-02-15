import { computed } from 'vue'
import { useAuthStore } from '@/stores/modules/auth'

export function useAuth() {
  const authStore = useAuthStore()

  return {
    user: computed(() => authStore.user),
    isAuthenticated: computed(() => authStore.isAuthenticated),
    loginWithGoogle: authStore.loginWithGoogle,
    logout: authStore.logout,
    hydrate: authStore.hydrate,
  }
}
