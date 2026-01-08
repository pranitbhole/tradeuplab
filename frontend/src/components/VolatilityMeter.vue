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
  <div
    style="
      border: 1px solid #ddd;
      padding: 16px;
      border-radius: 8px;
      max-width: 320px;
    "
  >
    <h3 style="margin-bottom: 8px;">Risk</h3>

    <div
      :style="{
        color: riskUI.color,
        fontWeight: 'bold',
        fontSize: '18px',
        marginBottom: '10px'
      }"
    >
      {{ riskUI.emoji }} {{ riskUI.label }}
    </div>

    <div style="font-size: 13px; color: #555;">
      <div>7D Volatility: {{ (risk.volatility_7d * 100).toFixed(2) }}%</div>
      <div>30D Volatility: {{ (risk.volatility_30d * 100).toFixed(2) }}%</div>
      <div>Max Drawdown (90D): {{ risk.max_drawdown_90d }}%</div>
    </div>
  </div>
</template>
