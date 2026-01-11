from sqlalchemy.orm import Session
from app.models.price_snapshot import PriceSnapshot
from statistics import stdev
from datetime import datetime, timedelta


def get_price_series(
    db: Session,
    skin_name: str,
    days: int
) -> list[float]:
    since = datetime.utcnow() - timedelta(days=days)

    rows = (
        db.query(PriceSnapshot.median_price)
        .filter(
            PriceSnapshot.skin_name == skin_name,
            PriceSnapshot.fetched_at >= since,
            PriceSnapshot.median_price.isnot(None)
        )
        .order_by(PriceSnapshot.fetched_at.asc())
        .all()
    )

    return [r[0] for r in rows]


def calculate_volatility(
    db: Session,
    skin_name: str,
    days: int
) -> float | None:
    prices = get_price_series(db, skin_name, days)

    if len(prices) < 2:
        return None

    return round(stdev(prices), 4)
