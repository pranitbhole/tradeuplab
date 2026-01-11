import requests


STEAM_PRICE_URL = "https://steamcommunity.com/market/priceoverview/"


def fetch_skin_price(
    market_hash_name: str,
    currency: int = 1,
    appid: int = 730
):
    """
    Fetch current Steam market price snapshot for a skin.

    currency=1 -> USD
    appid=730 -> CS2
    """

    params = {
        "country": "US",
        "currency": currency,
        "appid": appid,
        "market_hash_name": market_hash_name
    }

    headers = {
        "User-Agent": "TradeUpLab/1.0 (contact: dev)"
    }

    response = requests.get(
        STEAM_PRICE_URL,
        params=params,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return {
        "success": data.get("success"),
        "lowest_price": data.get("lowest_price"),
        "median_price": data.get("median_price"),
        "volume": data.get("volume")
    }
