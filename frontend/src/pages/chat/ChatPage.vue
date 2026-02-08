<template>
  <section class="min-h-screen bg-[var(--color-bg)] text-[var(--color-text)] flex flex-col">
    <header class="px-6 py-4 border-b border-[var(--color-border)] flex justify-between items-center">
      <div>
        <p class="text-sm uppercase tracking-[0.3em] text-[var(--color-primary)]">Research Infograph Assistant</p>
        <h1 class="text-2xl font-semibold">Chat</h1>
      </div>
      <nav class="space-x-4">
        <router-link to="/history" class="text-[var(--color-text)] hover:text-[var(--color-primary)]">History</router-link>
        <router-link to="/login" class="text-[var(--color-text)] hover:text-[var(--color-primary)]">Logout</router-link>
      </nav>
    </header>
    <main class="flex-1 p-6">
      <div class="rounded-xl border border-[var(--color-border)] p-6 bg-[var(--color-card)] max-w-4xl mx-auto text-center">
        <p class="text-lg">Chat room placeholder content goes here.</p>
      </div>
    </main>
  </section>
</template>
