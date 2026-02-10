import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

import { createSession, deleteSession, listSessions } from '@/api/session'

export const useSessionStore = defineStore('session', () => {
  const sessions = ref([])
  const loading = ref(false)
  const error = ref(null)
  const creating = ref(false)

  const fetchSessions = async () => {
    loading.value = true
    try {
      const response = await listSessions()
      sessions.value = response.data
    } catch (err) {
      error.value = err
    } finally {
      loading.value = false
    }
  }

  const addSession = async (prompt) => {
    creating.value = true
    try {
      const response = await createSession({ prompt })
      sessions.value = [response.data, ...sessions.value]
    } catch (err) {
      error.value = err
      throw err
    } finally {
      creating.value = false
    }
  }

  const removeSession = async (sessionId) => {
    try {
      await deleteSession(sessionId)
      sessions.value = sessions.value.filter((session) => session.session_id !== sessionId)
    } catch (err) {
      error.value = err
      throw err
    }
  }

  const sessionCount = computed(() => sessions.value.length)

  return {
    sessions,
    loading,
    error,
    creating,
    fetchSessions,
    addSession,
    removeSession,
    sessionCount,
  }
})
