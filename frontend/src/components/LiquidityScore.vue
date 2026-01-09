<script setup>
import { ref, onMounted } from 'vue'
import { useMotion } from '@vueuse/motion'
import skinData from '../mock/skin_sample.json'

const totalDots = 5
const filledDots = Math.round(
  skinData.liquidity.liquidity_score * totalDots
)

// Motion ref
const dotsRef = ref(null)

onMounted(() => {
  useMotion(dotsRef, {
    initial: {
      opacity: 0,
      scale: 0.9
    },
    enter: {
      opacity: 1,
      scale: 1,
      transition: {
        duration: 300,
        ease: 'easeOut'
      }
    }
  })
})
</script>

<template>
  <div>
    <h4 class="text-sm font-semibold mb-2 text-gray-300">
      Liquidity
    </h4>

    <!-- Dots (animated) -->
    <div
      ref="dotsRef"
      class="text-xl mb-1"
    >
      <span
        v-for="i in totalDots"
        :key="i"
      >
        {{ i <= filledDots ? '🔵' : '⚪' }}
      </span>
    </div>

    <p class="font-medium mb-2">
      {{ skinData.liquidity.liquidity_label }}
    </p>

    <div class="text-sm text-gray-400 space-y-1">
      <div>
        Avg Daily Volume: {{ skinData.liquidity.avg_daily_volume }}
      </div>
      <div>
        Listings: {{ skinData.liquidity.avg_listings }}
      </div>
      <div>
        Days to Liquidate: {{ skinData.liquidity.days_to_liquidate }}
      </div>
    </div>
  </div>
</template>
