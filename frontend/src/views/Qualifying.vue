<script setup lang="ts">
import DriverList from '../components/DriverList.vue'
import SectorGrid from '../components/SectorGrid.vue'
import { useRaceStore } from '../stores/race'

const store = useRaceStore()
</script>

<template>
  <div class="p-6 max-w-7xl mx-auto">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-f1-red uppercase italic tracking-tighter">Qualifying</h1>
      <div class="bg-f1-dark px-4 py-2 rounded border border-gray-700">
        <span class="text-gray-400 mr-2">SESSION</span>
        <span class="font-bold text-xl">{{ store.data?.status || 'Q1' }}</span>
      </div>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Driver List -->
      <div class="lg:col-span-4">
        <DriverList />
      </div>
      
      <!-- Sector Grid -->
      <div class="lg:col-span-8">
        <SectorGrid />
      </div>
    </div>
  </div>
</template>
