<script setup>
import PriceChart from './components/PriceChart.vue'
import VolumeChart from './components/VolumeChart.vue'
import LiquidityScore from './components/LiquidityScore.vue'
import VolatilityMeter from './components/VolatilityMeter.vue'
import TradeUpEV from './components/TradeUpEV.vue'
import skinData from './mock/skin_sample.json'
</script>

<template>
  <div style="padding: 40px; font-family: Arial;">
    <h1 class="text-red-500 text-3xl font-bold">
  TradeUpLab
</h1>

    <h2>{{ skinData.skin_name }}</h2>

    <p>
      <strong>Current Price:</strong>
      {{ skinData.price_stats.current_price }}
      {{ skinData.currency }}
    </p>

    <div style="display: flex; gap: 40px;">
      <!-- Charts -->
      <div>
        <PriceChart />
        <div style="margin-top: 20px;">
          <VolumeChart />
        </div>
      </div>

      <!-- Analytics -->
      <div style="display: flex; flex-direction: column; gap: 20px;">
        <LiquidityScore />
        <VolatilityMeter />
        <TradeUpEV />
      </div>
    </div>
  </div>
</template>
