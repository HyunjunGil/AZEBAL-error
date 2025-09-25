<template>
  <div id="app" class="min-h-screen bg-neutral-100">
    <header class="bg-white shadow-sm border-b">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <router-link to="/" class="text-2xl font-bold text-primary">
            스포츠몰
          </router-link>
          <nav class="hidden md:flex space-x-8">
            <router-link to="/" class="text-neutral-600 hover:text-primary transition-colors">
              추천받기
            </router-link>
          </nav>
        </div>
      </div>
    </header>
    
    <main class="flex-1">
      <router-view />
    </main>
    
    <footer class="bg-white border-t mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="text-center text-neutral-600">
          <p>&copy; 2025 스포츠 용품 추천 쇼핑몰 프로토타입</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
