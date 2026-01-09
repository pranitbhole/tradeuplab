<script setup>
import { ref, onMounted } from 'vue'
import { useMotion } from '@vueuse/motion'
import BaseCard from './BaseCard.vue'
import skinData from '../mock/skin_sample.json'

// --- Mock EV calculation ---
const tradeUpCost = 10 * skinData.price_stats.current_price

const outcomes = [
  { price: 42, probability: 0.25 },
  { price: 38, probability: 0.25 },
  { price: 34, probability: 0.25 },
  { price: 18, probability: 0.25 }
]

const expectedReturn = outcomes.reduce(
  (sum, o) => sum + o.price * o.probability,
  0
)

const ev = expectedReturn - tradeUpCost
const isPositive = ev > 0

// Motion ref for EV emphasis
const evRef = ref(null)

onMounted(() => {
  useMotion(evRef, {
    initial: {
      opacity: 0,
      y: 6
    },
    enter: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 250,
        ease: 'easeOut'
      }
    }
  })
})
</script>

<template>
  <BaseCard
    :class="isPositive ? 'border-green-500' : 'border-red-500'"
  >
    <!-- Title -->
    <h3 class="text-xl font-semibold mb-3">
      Trade-Up Expected Value
    </h3>

    <!-- EV RESULT (Animated) -->
    <div
      ref="evRef"
      class="text-2xl font-bold mb-2"
      :class="isPositive ? 'text-green-400' : 'text-red-400'"
    >
      {{ isPositive ? 'Positive EV' : 'Negative EV' }}
      ({{ ev.toFixed(2) }} {{ skinData.currency }})
    </div>

    <!-- Numbers -->
    <div class="text-sm text-gray-300 space-y-1 mb-4">
      <div>
        Cost:
        <span class="font-medium">
          {{ tradeUpCost.toFixed(2) }} {{ skinData.currency }}
        </span>
      </div>
      <div>
        Expected Return:
        <span class="font-medium">
          {{ expectedReturn.toFixed(2) }} {{ skinData.currency }}
        </span>
      </div>
    </div>

    <!-- WHY BLOCK -->
    <div
      class="text-sm rounded-lg p-3"
      :class="isPositive
        ? 'bg-green-500/10 text-green-300'
        : 'bg-red-500/10 text-red-300'"
    >
      <p class="font-semibold mb-1">Why?</p>
      <ul class="list-disc list-inside space-y-1">
        <li>
          {{ isPositive
            ? 'Expected return exceeds input cost'
            : 'Expected return is lower than input cost' }}
        </li>
        <li>
          Risk level: {{ skinData.risk.risk_level }}
        </li>
        <li>
          Liquidity: {{ skinData.liquidity.liquidity_label }}
        </li>
      </ul>
    </div>

    <!-- Meta -->
    <div class="text-xs text-gray-400 mt-3">
      Demand Score: {{ skinData.tradeup_profile.tradeup_demand_score }} ·
      EV Sensitivity: {{ skinData.tradeup_profile.ev_sensitivity }}
    </div>
  </BaseCard>
</template>