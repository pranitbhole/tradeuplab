from app.db import SessionLocal
from app.analytics.volatility import calculate_volatility

if __name__ == "__main__":
    db = SessionLocal()

    skin = "AK-47 | Redline (Field-Tested)"

    print("7D Volatility:", calculate_volatility(db, skin, 7))
    print("30D Volatility:", calculate_volatility(db, skin, 30))

    db.close()
