import { describe, expect, test, vi } from 'vitest'
import { ref, computed } from 'vue'

// Mock the auth store module
const mockLogin = vi.fn()
const mockLogout = vi.fn()
const mockHydrate = vi.fn()
const mockUserRef = ref({ email: 'test@example.com' })
const mockIsAuthenticated = computed(() => true)

vi.mock('@/stores/modules/auth', () => ({
  useAuthStore: () => ({
    user: mockUserRef,
    isAuthenticated: mockIsAuthenticated,
    loginWithGoogle: mockLogin,
    logout: mockLogout,
    hydrate: mockHydrate,
  }),
}))

import { useAuth } from '@/composables/useAuth'

describe('useAuth composable', () => {
  test('exposes store state and actions', () => {
    const { user, isAuthenticated, loginWithGoogle, logout, hydrate } = useAuth()

    expect(user.value).toEqual({ email: 'test@example.com' })
    expect(isAuthenticated.value).toBe(true)
    expect(loginWithGoogle).toBeInstanceOf(Function)
    expect(logout).toBeInstanceOf(Function)
    expect(hydrate).toBeInstanceOf(Function)

    // ensure functions map to the mocked implementations
    loginWithGoogle('cred')
    expect(mockLogin).toHaveBeenCalledWith('cred')

    logout()
    expect(mockLogout).toHaveBeenCalled()

    hydrate()
    expect(mockHydrate).toHaveBeenCalled()
  })
})