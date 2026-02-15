import request from '@/utils/request'

export function exchangeGoogleToken(credential) {
  return request.post('/api/v1/auth/google', { credential })
}

export function fetchCurrentUser() {
  return request.get('/api/v1/auth/me')
}
