<script setup>
import skinData from '../mock/skin_sample.json'

// Convert 0–1 score to 0–5 dots
const totalDots = 5
const filledDots = Math.round(
  skinData.liquidity.liquidity_score * totalDots
)
</script>

<template>
  <div
    style="
      border: 1px solid #ddd;
      padding: 16px;
      border-radius: 8px;
      max-width: 320px;
    "
  >
    <h3 style="margin-bottom: 8px;">Liquidity</h3>

    <!-- Dots -->
    <div style="font-size: 20px; margin-bottom: 6px;">
      <span v-for="i in totalDots" :key="i">
        {{ i <= filledDots ? '🔵' : '⚪' }}
      </span>
    </div>

    <strong>{{ skinData.liquidity.liquidity_label }}</strong>

    <!-- Details -->
    <div style="font-size: 13px; margin-top: 8px; color: #555;">
      <div>Avg Daily Volume: {{ skinData.liquidity.avg_daily_volume }}</div>
      <div>Active Listings: {{ skinData.liquidity.avg_listings }}</div>
      <div>
        Days to Liquidate:
        {{ skinData.liquidity.days_to_liquidate }}
      </div>
    </div>
  </div>
</template>
