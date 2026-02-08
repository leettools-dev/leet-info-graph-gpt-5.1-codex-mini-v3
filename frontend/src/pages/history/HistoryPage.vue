<template>
  <section class="min-h-screen bg-[var(--color-bg)] text-[var(--color-text)] flex flex-col">
    <header class="px-6 py-4 border-b border-[var(--color-border)] flex justify-between items-center">
      <div>
        <p class="text-sm uppercase tracking-[0.3em] text-[var(--color-primary)]">Research Infograph Assistant</p>
        <h1 class="text-2xl font-semibold">History</h1>
      </div>
      <router-link to="/chat" class="text-[var(--color-text)] hover:text-[var(--color-primary)]">Back to Chat</router-link>
    </header>
    <main class="flex-1 p-6">
      <div class="rounded-xl border border-[var(--color-border)] p-6 bg-[var(--color-card)] max-w-4xl mx-auto text-center">
        <p class="text-lg">History listing placeholder content goes here.</p>
      </div>
    </main>
  </section>
</template>
