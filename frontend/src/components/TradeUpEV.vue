<script setup>
import skinData from '../mock/skin_sample.json'

// ---- MOCK trade-up calculation (frontend only) ----

// Cost to perform trade-up (10 inputs)
const tradeUpCost = 10 * skinData.price_stats.current_price

// Simulated outputs (later comes from backend)
const outcomes = [
  { name: 'AK-47 | Vulcan', price: 42, probability: 0.25 },
  { name: 'M4A4 | Asiimov', price: 38, probability: 0.25 },
  { name: 'AWP | Redline', price: 34, probability: 0.25 },
  { name: 'FAMAS | Pulse', price: 18, probability: 0.25 }
]

// Expected value
const expectedReturn = outcomes.reduce(
  (sum, o) => sum + o.price * o.probability,
  0
)

const ev = expectedReturn - tradeUpCost

const evLabel = ev > 0 ? 'Positive EV' : 'Negative EV'
const evColor = ev > 0 ? '#2ecc71' : '#e74c3c'
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
    <h3 style="margin-bottom: 10px;">Trade-Up EV</h3>

    <div style="font-size: 14px; margin-bottom: 8px;">
      <strong>Cost:</strong>
      {{ tradeUpCost.toFixed(2) }} {{ skinData.currency }}
    </div>

    <div style="font-size: 14px; margin-bottom: 8px;">
      <strong>Expected Return:</strong>
      {{ expectedReturn.toFixed(2) }} {{ skinData.currency }}
    </div>

    <div
      style="font-size: 18px; font-weight: bold;"
      :style="{ color: evColor }"
    >
      {{ evLabel }} ({{ ev.toFixed(2) }} {{ skinData.currency }})
    </div>

    <div style="font-size: 12px; margin-top: 10px; color: #555;">
      Demand Score: {{ skinData.tradeup_profile.tradeup_demand_score }}
      <br />
      EV Sensitivity: {{ skinData.tradeup_profile.ev_sensitivity }}
    </div>
  </div>
</template>
