from sqlalchemy.orm import Session
from app.analytics.volatility import calculate_volatility
from app.analytics.liquidity import calculate_liquidity


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def classify_risk(db: Session, skin_name: str) -> dict:
    vol_7d = calculate_volatility(db, skin_name, 7)
    vol_30d = calculate_volatility(db, skin_name, 30)

    liquidity = calculate_liquidity(db, skin_name)
    liquidity_score = liquidity.get("liquidity_score", 0.0) or 0.0

    # Normalize volatility (cap at 2.0)
    vol_norm_7d = clamp((vol_7d or 0.0) / 2.0)
    vol_norm_30d = clamp((vol_30d or 0.0) / 2.0)

    # Weighted volatility emphasis on recent movement
    vol_norm = (vol_norm_7d * 0.7) + (vol_norm_30d * 0.3)

    # Risk score: volatility ↑, liquidity ↓
    risk_score = clamp(
        (vol_norm * 0.65) + ((1 - liquidity_score) * 0.35)
    )

    if risk_score <= 0.35:
        label = "Stable"
        color = "green"
    elif risk_score <= 0.65:
        label = "Medium"
        color = "yellow"
    else:
        label = "High"
        color = "red"

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": label,
        "risk_color": color,
        "volatility_7d": vol_7d,
        "volatility_30d": vol_30d,
        "liquidity_score": liquidity_score,
    }
