from fastapi import APIRouter
from app.db import SessionLocal
from app.analytics.volatility import calculate_volatility
from app.analytics.liquidity import calculate_liquidity
from app.analytics.risk import classify_risk

router = APIRouter(prefix="/api/skins", tags=["analytics"])


@router.get("/{skin_name}/analytics")
def get_skin_analytics(skin_name: str):
    db = SessionLocal()

    volatility = {
        "volatility_7d": calculate_volatility(db, skin_name, 7),
        "volatility_30d": calculate_volatility(db, skin_name, 30),
    }

    liquidity = calculate_liquidity(db, skin_name)
    risk = classify_risk(db, skin_name)

    db.close()

    return {
        "skin_name": skin_name,
        "volatility": volatility,
        "liquidity": liquidity,
        "risk": risk,
    }
