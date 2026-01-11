from app.db import SessionLocal
from app.analytics.risk import classify_risk

if __name__ == "__main__":
    db = SessionLocal()

    skin = "AK-47 | Redline (Field-Tested)"
    result = classify_risk(db, skin)

    db.close()

    print("Risk analytics:")
    for k, v in result.items():
        print(f"  {k}: {v}")
