<script setup>
import skinData from '../mock/skin_sample.json'

const riskMap = {
  Low: { color: '#2ecc71', emoji: '🟢', label: 'Stable' },
  Medium: { color: '#f1c40f', emoji: '🟡', label: 'Medium Risk' },
  High: { color: '#e74c3c', emoji: '🔴', label: 'High Risk' }
}

const risk = skinData.risk
const riskUI = riskMap[risk.risk_level]
</script>

<template>
  <div>
    <h4 class="text-sm font-semibold mb-2 text-gray-300">
      Risk
    </h4>

    <div
      class="font-semibold mb-2"
      :style="{ color: riskUI.color }"
    >
      {{ riskUI.emoji }} {{ riskUI.label }}
    </div>

    <div class="text-sm text-gray-400 space-y-1">
      <div>7D Volatility: {{ (risk.volatility_7d * 100).toFixed(2) }}%</div>
      <div>30D Volatility: {{ (risk.volatility_30d * 100).toFixed(2) }}%</div>
      <div>Max Drawdown (90D): {{ risk.max_drawdown_90d }}%</div>
    </div>
  </div>
</template>

