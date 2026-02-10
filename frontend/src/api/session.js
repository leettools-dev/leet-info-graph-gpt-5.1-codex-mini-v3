import request from '@/utils/request'

const DEFAULT_LIMIT = 10

export function listSessions({ limit = DEFAULT_LIMIT, offset = 0 } = {}) {
  return request.get('/api/v1/sessions', {
    params: {
      limit,
      offset,
    },
  })
}

export function createSession(payload) {
  return request.post('/api/v1/sessions', payload)
}

export function deleteSession(sessionId) {
  return request.delete(`/api/v1/sessions/${sessionId}`)
}
