<script setup>
import PriceChart from './components/PriceChart.vue'
import VolumeChart from './components/VolumeChart.vue'
import LiquidityScore from './components/LiquidityScore.vue'
import VolatilityMeter from './components/VolatilityMeter.vue'
import TradeUpEV from './components/TradeUpEV.vue'
import skinData from './mock/skin_sample.json'
import MarketHealth from './components/MarketHealth.vue'

</script>

<template>
  <div class="min-h-screen bg-neutral-900 text-white p-8">
    <!-- Header -->
    <header class="mb-8">
      <h1 class="text-4xl font-bold mb-2">TradeUpLab</h1>
      <h2 class="text-xl text-gray-300">
        {{ skinData.skin_name }}
      </h2>
      <p class="mt-2 text-lg">
        <span class="font-semibold">Current Price:</span>
        {{ skinData.price_stats.current_price }} {{ skinData.currency }}
      </p>
    </header>

    <!-- Dashboard Grid -->
    <section class="grid grid-cols-12 gap-8">
      <!-- Charts Section -->
      <div class="col-span-8 space-y-6">
        <PriceChart />
        <VolumeChart />
      </div>

      <!-- Insights Section -->
      <aside class="col-span-4 space-y-6">
  <MarketHealth />
  <TradeUpEV />
</aside>

    </section>
  </div>
</template>
