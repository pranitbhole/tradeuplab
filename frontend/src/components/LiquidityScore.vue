<script setup>
defineProps({
  data: Object
})
</script>

<template>
  <div class="bg-neutral-800 border border-neutral-700 rounded-xl p-5">
    <h3 class="text-lg font-semibold mb-3">Liquidity</h3>

    <div class="text-2xl mb-2">
      <span v-for="i in 5" :key="i">
        {{ i <= Math.round(data.liquidity_score * 5) ? '🔵' : '⚪' }}
      </span>
    </div>

    <p class="font-medium mb-2">{{ data.liquidity_label }}</p>

    <div class="text-sm text-gray-400 space-y-1">
      <div>Avg Daily Volume: {{ data.avg_daily_volume }}</div>
      <div>Listings (est): {{ data.active_listings_est }}</div>
      <div>Days to Liquidate: {{ data.days_to_liquidate }}</div>
    </div>
  </div>
</template>
