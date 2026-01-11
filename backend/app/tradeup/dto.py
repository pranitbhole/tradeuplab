from typing import List
from pydantic import BaseModel

class TradeUpInput(BaseModel):
    market_hash_names: List[str]   # 10 skins
    wear: str                      # FT, MW, FN
    currency: str = "USD"


class TradeUpResult(BaseModel):
    cost: float
    expected_return: float
    ev: float
    roi: float
    risk_level: str
    bust_probability: float
