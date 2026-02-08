<template>
  <div class="min-h-screen flex items-center justify-center bg-[#05080a]">
    <div class="bg-[var(--color-card)] p-10 rounded-2xl shadow-xl w-full max-w-sm text-center">
      <h1 class="text-2xl font-semibold mb-6 text-[var(--color-text)]">Sign in to Research Infograph</h1>
      <slot>
        <button
          class="mt-4 w-full rounded-xl py-3 text-lg font-medium bg-[var(--color-primary)] text-black hover:bg-[var(--color-primary-dark)]"
        >
          Sign in with Google
        </button>
      </slot>
    </div>
  </div>
</template>
