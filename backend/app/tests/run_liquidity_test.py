from app.db import SessionLocal
from app.analytics.liquidity import calculate_liquidity

if __name__ == "__main__":
    db = SessionLocal()

    skin = "AK-47 | Redline (Field-Tested)"
    result = calculate_liquidity(db, skin)

    db.close()

    print("Liquidity analytics:")
    for k, v in result.items():
        print(f"  {k}: {v}")
