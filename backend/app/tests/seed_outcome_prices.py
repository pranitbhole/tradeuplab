from app.db import SessionLocal
from app.models.price_snapshot import PriceSnapshot
from datetime import datetime

db = SessionLocal()

prices = {
    "AWP | Asiimov (Field-Tested)": 45.0,
    "AUG | Chameleon (Factory New)": 31.4
}

for skin, price in prices.items():
    db.add(
        PriceSnapshot(
            skin_name=skin,
            median_price=price,
            lowest_price=price,
            volume=100,
            fetched_at=datetime.utcnow()
        )
    )

db.commit()
db.close()

print("Outcome prices inserted successfully.")
