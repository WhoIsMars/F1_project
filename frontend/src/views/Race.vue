<script setup lang="ts">
import DriverList from '../components/DriverList.vue'
import RaceMap from '../components/RaceMap.vue'
import { useRaceStore } from '../stores/race'

const store = useRaceStore()
</script>

<template>
  <div class="h-screen w-screen flex flex-col overflow-hidden bg-f1-black">
    <!-- Header - Fixed Height -->
    <div class="flex-shrink-0 px-4 py-2 border-b border-gray-800">
      <div class="flex justify-between items-center">
        <h1 class="text-2xl font-bold text-f1-red uppercase italic tracking-tighter">Race</h1>
        <div class="bg-f1-dark/80 backdrop-blur-md px-3 py-1 rounded-lg border border-gray-800/50">
          <span class="text-gray-400 mr-2 text-xs">LAP</span>
          <span class="font-bold text-lg text-white">{{ store.data?.lap || '--' }}</span>
          <span class="text-gray-500 mx-1">/</span>
          <span class="font-bold text-sm text-gray-400">{{ store.data?.totalLaps || 50 }}</span>
        </div>
      </div>
    </div>

    <!-- Main Content - Takes Remaining Height -->
    <div class="flex-1 overflow-hidden px-4 py-2">
      <div class="grid grid-cols-12 gap-3 h-full">
        <!-- Driver List - Left Column (25%) - Scrollable Internally -->
        <div class="col-span-3 h-full max-h-full overflow-hidden">
          <DriverList />
        </div>
        
        <!-- Main Content - Right Column (75%) -->
        <div class="col-span-9 h-full max-h-full flex flex-col gap-3 overflow-hidden">
          <!-- Stats Grid - Compact & Fixed -->
          <div class="flex-shrink-0 grid grid-cols-3 gap-3">
            <div class="bg-f1-dark/80 backdrop-blur-md p-2 rounded-lg border border-gray-800/50">
              <h3 class="text-[10px] font-medium text-gray-400 uppercase">Weather</h3>
              <div class="flex items-baseline gap-1 mt-0.5">
                <span class="text-sm font-bold">{{ store.data?.weather?.condition || 'Clear' }}</span>
                <span class="text-f1-orange text-xs">{{ store.data?.weather?.temp || '21' }}°C</span>
              </div>
            </div>
            <div class="bg-f1-dark/80 backdrop-blur-md p-2 rounded-lg border border-gray-800/50">
              <h3 class="text-[10px] font-medium text-gray-400 uppercase">Track</h3>
              <div class="flex items-baseline mt-0.5">
                <span class="text-sm font-bold">{{ (store.data?.weather?.temp ? store.data.weather.temp + 4 : 25).toFixed(1) }}°C</span>
              </div>
            </div>
            <div class="bg-f1-dark/80 backdrop-blur-md p-2 rounded-lg border border-gray-800/50">
              <h3 class="text-[10px] font-medium text-gray-400 uppercase">Status</h3>
              <div class="flex items-baseline mt-0.5">
                <span class="text-sm font-bold text-green-500">{{ store.data?.status || 'RACE' }}</span>
              </div>
            </div>
          </div>
          
          <!-- Map - Takes Remaining Space -->
          <div class="flex-1 overflow-hidden min-h-0">
            <RaceMap />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
