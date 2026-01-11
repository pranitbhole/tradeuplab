from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db import Base


class PriceSnapshot(Base):
    __tablename__ = "price_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    skin_name = Column(String, index=True)
    lowest_price = Column(Float)
    median_price = Column(Float)
    volume = Column(Integer)
    fetched_at = Column(DateTime, default=datetime.utcnow)
