<script setup>
import { ref } from 'vue'
import { simulateTradeup } from '../services/tradeupApi'

const result = ref(null)
const loading = ref(false)
const error = ref(null)

const run = async () => {
  loading.value = true
  error.value = null

  try {
    const payload = {
      inputs: Array(10).fill('AK-47 | Redline (Field-Tested)')
    }
    result.value = await simulateTradeup(payload)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="bg-neutral-800 border border-neutral-700 rounded-xl p-5">
    <h3 class="text-lg font-semibold mb-3">Trade-Up Simulator (API Test)</h3>

    <button
      class="px-4 py-2 bg-blue-600 rounded mb-3"
      @click="run"
    >
      Run Trade-Up
    </button>

    <div v-if="loading" class="text-gray-400">Running simulation…</div>
    <div v-if="error" class="text-red-400">{{ error }}</div>

    <pre
      v-if="result"
      class="mt-3 text-xs bg-black/40 p-3 rounded overflow-x-auto"
    >
{{ result }}
    </pre>
  </div>
</template>
