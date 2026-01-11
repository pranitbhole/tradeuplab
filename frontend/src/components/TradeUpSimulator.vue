<script setup>
import { ref } from 'vue'
import { runTradeUpSimulation } from '../services/tradeupApi'

const result = ref(null)
const loading = ref(false)
const error = ref(null)

async function runSimulation() {
  loading.value = true
  error.value = null
  result.value = null

  try {
    const inputs = Array(10).fill('AK-47 | Redline (Field-Tested)')

    result.value = await runTradeUpSimulation({
      inputs
    })
  } catch (e) {
    error.value = e.message || 'Simulation failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="bg-neutral-800 border border-neutral-700 rounded-xl p-5">
    <h3 class="text-lg font-semibold mb-3 text-center">
      Trade-Up Simulator
    </h3>

    <button
      @click="runSimulation"
      class="w-full bg-blue-600 hover:bg-blue-500 transition rounded-md py-2 text-sm font-medium"
      :disabled="loading"
    >
      {{ loading ? 'Running…' : 'Run Trade-Up' }}
    </button>

    <div v-if="error" class="mt-3 text-red-400 text-sm">
      {{ error }}
    </div>

    <pre
      v-if="result"
      class="mt-4 text-xs bg-black/40 p-3 rounded overflow-auto max-h-96"
    >
{{ JSON.stringify(result, null, 2) }}
    </pre>
  </div>
</template>
