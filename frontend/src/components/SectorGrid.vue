<script setup lang="ts">
import { computed } from 'vue'
import { useRaceStore } from '../stores/race'

const store = useRaceStore()
const drivers = computed(() => store.data?.drivers || [])

const getSectorColor = (time: number) => {
  if (time < 22.0) return 'text-f1-purple' // Fastest
  if (time < 23.5) return 'text-f1-green'  // Personal Best
  return 'text-f1-orange'                  // Normal
}
</script>

<template>
  <div class="bg-f1-dark rounded-lg overflow-hidden shadow-lg border border-gray-800">
    <div class="bg-gray-800 px-4 py-3 font-bold text-gray-300 flex justify-between items-center text-xs uppercase tracking-wider">
      <span class="w-12">Driver</span>
      <span class="flex-1 text-center">S1</span>
      <span class="flex-1 text-center">S2</span>
      <span class="flex-1 text-center">S3</span>
    </div>
    <div class="divide-y divide-gray-800 max-h-[calc(100vh-200px)] overflow-y-auto custom-scrollbar">
      <div 
        v-for="driver in drivers" 
        :key="driver.id"
        class="px-4 py-2 flex items-center justify-between hover:bg-gray-800 transition-colors"
      >
        <span class="font-bold w-12 truncate">{{ driver.id.substring(0, 3).toUpperCase() }}</span>
        
        <div class="flex-1 flex justify-between space-x-2 font-mono text-sm">
          <span class="flex-1 text-center" :class="getSectorColor(driver.sectors?.s1 || 0)">
            {{ driver.sectors?.s1?.toFixed(3) || '-' }}
          </span>
          <span class="flex-1 text-center" :class="getSectorColor(driver.sectors?.s2 || 0)">
            {{ driver.sectors?.s2?.toFixed(3) || '-' }}
          </span>
          <span class="flex-1 text-center" :class="getSectorColor(driver.sectors?.s3 || 0)">
            {{ driver.sectors?.s3?.toFixed(3) || '-' }}
          </span>
        </div>
      </div>
      <div v-if="drivers.length === 0" class="p-8 text-center text-gray-500 italic">
        Waiting for sector data...
      </div>
    </div>
  </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: #15151e;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #38383f;
  border-radius: 3px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #e10600;
}
</style>
