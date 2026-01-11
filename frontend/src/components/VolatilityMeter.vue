<script setup>
defineProps({
  data: Object
})
</script>

<template>
  <div class="bg-neutral-800 border border-neutral-700 rounded-xl p-5">
    <h3 class="text-lg font-semibold mb-3">Risk</h3>

    <div
      class="text-xl font-bold mb-2"
      :class="{
        'text-green-400': data.risk_level === 'Stable',
        'text-yellow-400': data.risk_level === 'Medium',
        'text-red-400': data.risk_level === 'High'
      }"
    >
      {{ data.risk_level }} Risk
    </div>

    <div class="text-sm text-gray-400 space-y-1">
      <div>7D Volatility: {{ data.volatility_7d }}</div>
      <div>30D Volatility: {{ data.volatility_30d }}</div>
      <div>Liquidity Score: {{ data.liquidity_score }}</div>
    </div>
  </div>
</template>
