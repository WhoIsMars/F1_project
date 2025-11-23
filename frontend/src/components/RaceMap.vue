<script setup lang="ts">
import { computed } from 'vue'
import { useRaceStore } from '../stores/race'

const store = useRaceStore()
const drivers = computed(() => store.data?.drivers || [])

const getTeamColor = (team?: string) => {
  if (!team) return '#888888'
  
  const map: Record<string, string> = {
    red_bull: '#0600ef', // RBR
    ferrari: '#dc0000',   // Ferrari
    mercedes: '#00d2be', // Mercedes
    mclaren: '#ff8000', // McLaren
    aston_martin: '#006f62',  // Aston Martin
    alpine: '#ff87bc',
    williams: '#005aff',
    haas: '#ffffff',
    sauber: '#52e252',
    rb: '#469bff',
    alphatauri: '#469bff',
  }
  return map[team] || '#888888'
}
</script>

<template>
  <div class="bg-f1-dark/80 backdrop-blur-md p-4 rounded-xl border border-gray-800/50 h-full relative overflow-hidden group shadow-2xl flex-1">
    <!-- Background Map Image -->
    <div class="absolute inset-0 bg-[url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Circuit_de_Monaco.svg/1200px-Circuit_de_Monaco.svg.png')] bg-contain bg-center bg-no-repeat opacity-20 transition-opacity duration-700 group-hover:opacity-30"></div>
    
    <!-- Driver Dots -->
    <div class="absolute inset-0 pointer-events-none">
      <div 
        v-for="driver in drivers" 
        :key="driver.id"
        class="absolute w-4 h-4 rounded-full border-2 border-white shadow-lg transition-all duration-500 ease-linear transform -translate-x-1/2 -translate-y-1/2 flex items-center justify-center"
        :style="{ 
          left: `${driver.coordinates?.x || 50}%`, 
          top: `${driver.coordinates?.y || 50}%`,
          backgroundColor: getTeamColor(driver.team)
        }"
      >
        <span class="text-[8px] font-bold text-white">{{ driver.position }}</span>
      </div>
    </div>
    
    <div class="absolute bottom-4 right-4 bg-black/50 px-2 py-1 rounded text-xs text-gray-400">
      Live Tracking
    </div>
  </div>
</template>
