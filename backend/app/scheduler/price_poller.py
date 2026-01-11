from app.db import SessionLocal
from app.models.price_snapshot import PriceSnapshot
from app.services.steam_fetcher import fetch_skin_price
from datetime import datetime


def parse_price(price_str: str | None):
    if not price_str:
        return None
    return float(price_str.replace("$", "").replace(",", ""))


def poll_skin_price(skin_name: str):
    data = fetch_skin_price(skin_name)

    db = SessionLocal()

    snapshot = PriceSnapshot(
        skin_name=skin_name,
        lowest_price=parse_price(data["lowest_price"]),
        median_price=parse_price(data["median_price"]),
        volume=int(data["volume"]) if data["volume"] else None,
        fetched_at=datetime.utcnow()
    )

    db.add(snapshot)
    db.commit()
    db.close()

    print(f"[{datetime.utcnow()}] Snapshot saved for {skin_name}")
