import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

import { exchangeGoogleToken, fetchCurrentUser } from '@/api/auth'
import { setAuthToken } from '@/utils/request'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('auth_token') || '')
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => Boolean(token.value))

  const _persistToken = (value) => {
    token.value = value
    if (value) {
      localStorage.setItem('auth_token', value)
      setAuthToken(value)
    } else {
      localStorage.removeItem('auth_token')
      setAuthToken(null)
    }
  }

  const loginWithGoogle = async (credential) => {
    loading.value = true
    error.value = null
    try {
      const response = await exchangeGoogleToken(credential)
      const { data } = response
      _persistToken(data.token)
      user.value = data.user
    } catch (err) {
      error.value = err
      throw err
    } finally {
      loading.value = false
    }
  }

  const hydrate = async () => {
    if (!token.value) {
      return
    }
    setAuthToken(token.value)
    loading.value = true
    try {
      const response = await fetchCurrentUser()
      user.value = response.data
    } catch (err) {
      console.error('Failed to hydrate auth', err)
      logout()
    } finally {
      loading.value = false
    }
  }

  const logout = () => {
    _persistToken('')
    user.value = null
  }

  return {
    token,
    user,
    loading,
    error,
    isAuthenticated,
    loginWithGoogle,
    hydrate,
    logout,
  }
})
