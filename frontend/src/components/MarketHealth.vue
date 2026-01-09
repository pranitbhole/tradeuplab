<script setup>
import BaseCard from './BaseCard.vue'
import LiquidityScore from './LiquidityScore.vue'
import VolatilityMeter from './VolatilityMeter.vue'
</script>

<template>
  <BaseCard>
    <h3 class="text-lg font-semibold mb-4">
      Market Health
    </h3>

    <div class="space-y-6">
      <LiquidityScore />
      <VolatilityMeter />
    </div>
  </BaseCard>
</template>
