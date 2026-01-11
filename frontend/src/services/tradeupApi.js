export async function runTradeUpSimulation(payload) {
  const res = await fetch('http://127.0.0.1:8000/tradeup/simulate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })

  if (!res.ok) {
    const text = await res.text()
    throw new Error(text)
  }

  return res.json()
}
