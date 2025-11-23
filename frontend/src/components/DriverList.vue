<script setup lang="ts">
import { computed } from 'vue'
import { useRaceStore } from '../stores/race'

const store = useRaceStore()
const drivers = computed(() => store.data?.drivers || [])

// Map constructor IDs to Tailwind classes
const getTeamColorClass = (team?: string) => {
  if (!team) return 'border-l-4 border-gray-500'
  
  const map: Record<string, string> = {
    red_bull: 'border-l-4 border-blue-900',
    ferrari: 'border-l-4 border-red-600',
    mercedes: 'border-l-4 border-cyan-500',
    mclaren: 'border-l-4 border-orange-500',
    aston_martin: 'border-l-4 border-green-600',
    alpine: 'border-l-4 border-pink-500',
    williams: 'border-l-4 border-blue-400',
    haas: 'border-l-4 border-white',
    sauber: 'border-l-4 border-green-400',
    rb: 'border-l-4 border-blue-600',
    alphatauri: 'border-l-4 border-blue-600', // Legacy support
  }
  return map[team] || 'border-l-4 border-gray-500'
}
</script>

<template>
  <div class="bg-f1-dark/80 backdrop-blur-md rounded-xl overflow-hidden shadow-2xl border border-gray-800/50 h-full flex flex-col">
    <!-- Header - Compact -->
    <div class="bg-gradient-to-r from-f1-red to-red-700 px-2 py-1.5 font-bold text-white flex justify-between items-center uppercase text-[10px] tracking-wider shadow-md z-10 flex-shrink-0">
      <span class="w-6 text-center">P</span>
      <span class="flex-1 ml-2">Driver</span>
      <span class="w-6 text-center">T</span>
      <span class="w-12 text-right">Gap</span>
    </div>
    
    <!-- Scrollable List - Optimized for 20 drivers -->
    <div class="divide-y divide-gray-800/50 overflow-y-auto custom-scrollbar flex-1">
      <div 
        v-for="driver in drivers" 
        :key="driver.id"
        class="px-2 py-1.5 flex items-center justify-between hover:bg-white/5 transition-all duration-200 cursor-default group relative"
      >
        <!-- Team Color Indicator -->
        <div class="absolute left-0 top-0 bottom-0 w-0.5" :class="getTeamColorClass(driver.team).replace('border-l-4', 'bg-current').replace('border-', 'text-')"></div>

        <span class="font-mono font-bold w-6 text-center text-xs text-gray-400 group-hover:text-white transition-colors pl-1">{{ driver.position }}</span>
        
        <div class="flex-1 ml-2 flex flex-col justify-center">
          <span class="font-bold text-xs tracking-tight leading-none">{{ driver.code || driver.id.substring(0, 3).toUpperCase() }}</span>
          <span class="text-[9px] text-gray-500 uppercase leading-none mt-0.5 truncate">{{ driver.team?.replace('_', ' ') || 'F1' }}</span>
        </div>
        
        <!-- Tyre Icon - Compact -->
        <span class="w-6 flex justify-center">
          <span 
            class="w-4 h-4 rounded-full flex items-center justify-center text-[9px] font-bold border"
            :class="{
              'border-red-500 text-red-500': driver.tyre === 'SOFT',
              'border-yellow-400 text-yellow-400': driver.tyre === 'MEDIUM',
              'border-white text-white': driver.tyre === 'HARD',
              'border-green-500 text-green-500': driver.tyre === 'INTER',
              'border-blue-500 text-blue-500': driver.tyre === 'WET'
            }"
          >
            {{ driver.tyre ? driver.tyre[0] : 'M' }}
          </span>
        </span>

        <span class="font-mono text-f1-light w-12 text-right text-[10px]">{{ driver.lapTime || '+0.0' }}</span>
      </div>
      <div v-if="drivers.length === 0" class="p-6 text-center text-gray-500 italic text-xs">
        Waiting for live data...
      </div>
    </div>
  </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #38383f;
  border-radius: 3px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #e10600;
}
</style>
