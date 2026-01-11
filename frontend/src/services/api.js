const API_BASE = 'http://127.0.0.1:8000'

export async function fetchSkinAnalytics(skinName) {
  const encoded = encodeURIComponent(skinName)
  const res = await fetch(`${API_BASE}/api/skins/${encoded}/analytics`)

  if (!res.ok) {
    throw new Error('Failed to fetch analytics')
  }

  return await res.json()
}
