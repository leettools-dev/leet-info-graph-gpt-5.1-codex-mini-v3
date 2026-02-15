import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const request = axios.create({
  baseURL: API_BASE,
  timeout: 10_000,
})

export function setAuthToken(token) {
  if (token) {
    request.defaults.headers.common.Authorization = `Bearer ${token}`
  } else {
    delete request.defaults.headers.common.Authorization
  }
}

export default request
