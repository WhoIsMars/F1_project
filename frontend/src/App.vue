<script setup lang="ts">
import { onMounted } from 'vue'
import { useRaceStore } from './stores/race'

const store = useRaceStore()

onMounted(() => {
  store.connect()
})
</script>

<template>
  <div class="min-h-screen bg-f1-black text-white font-sans">
    <nav class="bg-f1-dark border-b border-gray-800 p-4 flex justify-between items-center sticky top-0 z-50">
      <div class="flex items-center space-x-6">
        <span class="text-2xl font-bold italic tracking-tighter select-none">
          <span class="text-white">F1</span><span class="text-f1-red">LIVE</span>
        </span>
        <div class="flex space-x-2">
          <router-link 
            to="/qualifying" 
            class="px-4 py-2 rounded font-medium transition-colors duration-200" 
            active-class="bg-f1-red text-white"
            :class="$route.path === '/qualifying' ? 'bg-f1-red text-white' : 'text-gray-300 hover:bg-f1-gray'"
          >
            Qualifying
          </router-link>
          <router-link 
            to="/race" 
            class="px-4 py-2 rounded font-medium transition-colors duration-200" 
            active-class="bg-f1-red text-white"
            :class="$route.path === '/race' ? 'bg-f1-red text-white' : 'text-gray-300 hover:bg-f1-gray'"
          >
            Race
          </router-link>
        </div>
      </div>
      <div class="flex items-center space-x-2 text-sm">
        <span 
          class="w-2 h-2 rounded-full transition-colors duration-300"
          :class="store.isConnected ? 'bg-f1-green animate-pulse' : 'bg-red-500'"
        ></span>
        <span :class="store.isConnected ? 'text-f1-green' : 'text-red-500'">
          {{ store.isConnected ? 'LIVE' : 'OFFLINE' }}
        </span>
      </div>
    </nav>
    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
