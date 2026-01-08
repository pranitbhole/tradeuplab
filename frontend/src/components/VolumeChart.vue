<script setup>
import { onMounted, ref } from 'vue'
import { Chart } from 'chart.js/auto'
import skinData from '../mock/skin_sample.json'

const canvasRef = ref(null)

onMounted(() => {
  const ctx = canvasRef.value.getContext('2d')

  const labels = skinData.price_history.map(p => p.date)
  const volumes = skinData.price_history.map(p => p.volume)

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        {
          label: 'Daily Volume',
          data: volumes
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: true
        }
      },
      scales: {
        y: {
          title: {
            display: true,
            text: 'Volume'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Date'
          }
        }
      }
    }
  })
})
</script>

<template>
  <div style="max-width: 600px;">
    <canvas ref="canvasRef"></canvas>
  </div>
</template>
