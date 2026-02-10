import { afterEach, beforeEach, describe, expect, test, vi } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'

const mockExchangeToken = vi.fn()
const mockFetchUser = vi.fn()
vi.mock('@/api/auth', () => ({
  exchangeGoogleToken: mockExchangeToken,
  fetchCurrentUser: mockFetchUser,
}))

const mockSetAuthToken = vi.fn()
vi.mock('@/utils/request', () => ({
  setAuthToken: mockSetAuthToken,
}))

import { useAuthStore } from '../index'
import { exchangeGoogleToken, fetchCurrentUser } from '@/api/auth'
import { setAuthToken } from '@/utils/request'

const createMockStorage = () => {
  const storage = new Map()
  return {
    getItem: vi.fn((key) => storage.get(key) ?? ''),
    setItem: vi.fn((key, value) => storage.set(key, value)),
    removeItem: vi.fn((key) => storage.delete(key)),
  }
}

describe('auth store', () => {
  let mockStorage

  beforeEach(() => {
    vi.clearAllMocks()
    mockStorage = createMockStorage()
    global.localStorage = mockStorage
    setActivePinia(createPinia())
  })

  afterEach(() => {
    delete global.localStorage
  })

  test('loginWithGoogle persists token and user', async () => {
    const store = useAuthStore()
    mockExchangeToken.mockResolvedValue({
      data: {
        token: 'jwt-test',
        user: {
          user_id: 'abc',
          email: 'test@example.com',
          name: 'Test User',
          google_id: 'g123',
          created_at: 0,
          updated_at: 0,
        },
      },
    })

    await store.loginWithGoogle('credential')

    expect(mockExchangeToken).toHaveBeenCalledWith('credential')
    expect(mockSetAuthToken).toHaveBeenCalledWith('jwt-test')
    expect(mockStorage.setItem).toHaveBeenCalledWith('auth_token', 'jwt-test')
    expect(store.user.value.email).toBe('test@example.com')
  })

  test('hydrate refreshes user when token exists', async () => {
    mockStorage.getItem.mockReturnValue('persisted-token')
    const store = useAuthStore()
    mockFetchUser.mockResolvedValue({
      data: {
        user_id: 'abc',
        email: 'hydrate@example.com',
        name: 'Hydrate User',
        google_id: 'g-hydrate',
        created_at: 0,
        updated_at: 0,
      },
    })

    await store.hydrate()

    expect(mockSetAuthToken).toHaveBeenCalledWith('persisted-token')
    expect(mockFetchUser).toHaveBeenCalled()
    expect(store.user.value.email).toBe('hydrate@example.com')
  })
})
