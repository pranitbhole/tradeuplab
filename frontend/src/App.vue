<script setup>
import { ref, onMounted } from 'vue'
import { fetchSkinAnalytics } from './services/api'

import LiquidityScore from './components/LiquidityScore.vue'
import RiskMeter from './components/VolatilityMeter.vue'
import TradeUpEV from './components/TradeUpEV.vue'
import TradeUpSimulator from './components/TradeUpSimulator.vue'

const skinName = 'AK-47 | Redline (Field-Tested)'

const analytics = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    analytics.value = await fetchSkinAnalytics(skinName)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="min-h-screen bg-neutral-900 text-white p-8">
    <h1 class="text-3xl font-bold mb-2 text-center">
      TradeUpLab
    </h1>

    <h2 class="text-xl mb-6 text-center text-gray-300">
      {{ skinName }}
    </h2>

    <div v-if="loading" class="text-gray-400 text-center">
      Loading analytics…
    </div>

    <div v-else-if="error" class="text-red-400 text-center">
      {{ error }}
    </div>

    <div
      v-else
      class="max-w-md mx-auto space-y-6"
    >
      <!-- Analytics Cards -->
      <LiquidityScore :data="analytics.liquidity" />
      <RiskMeter :data="analytics.risk" />
      <TradeUpEV
        :risk="analytics.risk"
        :liquidity="analytics.liquidity"
      />

      <!-- Trade-Up Simulator -->
      <TradeUpSimulator />
    </div>
  </div>
</template>
