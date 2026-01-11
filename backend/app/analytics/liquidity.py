from sqlalchemy.orm import Session
from app.models.price_snapshot import PriceSnapshot
from datetime import datetime, timedelta
from statistics import mean


def get_volume_series(
    db: Session,
    skin_name: str,
    days: int
) -> list[int]:
    since = datetime.utcnow() - timedelta(days=days)

    rows = (
        db.query(PriceSnapshot.volume)
        .filter(
            PriceSnapshot.skin_name == skin_name,
            PriceSnapshot.fetched_at >= since,
            PriceSnapshot.volume.isnot(None)
        )
        .all()
    )

    return [r[0] for r in rows if r[0] is not None]


def calculate_liquidity(db: Session, skin_name: str) -> dict:
    volumes = get_volume_series(db, skin_name, days=14)

    if not volumes:
        return {
            "avg_daily_volume": None,
            "days_to_liquidate": None,
            "liquidity_score": 0.0,
            "liquidity_label": "Low"
        }

    avg_daily_volume = round(mean(volumes), 2)

    # Proxy listings: assume listings ~= 7 * avg daily volume
    active_listings_est = avg_daily_volume * 7

    # Days to liquidate = listings / daily volume
    days_to_liquidate = round(
        active_listings_est / avg_daily_volume, 2
    ) if avg_daily_volume > 0 else None

    # Normalize score (cap to avoid over-weighting huge volumes)
    # 0 vol → 0.0, 300+ vol → ~1.0
    liquidity_score = min(avg_daily_volume / 300, 1.0)
    liquidity_score = round(liquidity_score, 2)

    if liquidity_score >= 0.7:
        label = "High"
    elif liquidity_score >= 0.4:
        label = "Medium"
    else:
        label = "Low"

    return {
        "avg_daily_volume": avg_daily_volume,
        "active_listings_est": int(active_listings_est),
        "days_to_liquidate": days_to_liquidate,
        "liquidity_score": liquidity_score,
        "liquidity_label": label
    }
