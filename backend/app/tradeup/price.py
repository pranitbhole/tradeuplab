from sqlalchemy.orm import Session
from app.models.price_snapshot import PriceSnapshot


def get_latest_price(db: Session, skin_name: str) -> float | None:
    row = (
        db.query(PriceSnapshot.median_price)
        .filter(
            PriceSnapshot.skin_name == skin_name,
            PriceSnapshot.median_price.isnot(None)
        )
        .order_by(PriceSnapshot.fetched_at.desc())
        .first()
    )
    return float(row[0]) if row else None
