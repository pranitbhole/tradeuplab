from app.db import SessionLocal
from app.tradeup.simulator import simulate_tradeup

ALL_SKINS = [
    "AK-47 | Redline (Field-Tested)",
    "AWP | Asiimov (Field-Tested)",
    "AUG | Chameleon (Factory New)"
]

INPUT_SKINS = ["AK-47 | Redline (Field-Tested)"] * 10


if __name__ == "__main__":
    db = SessionLocal()

    result = simulate_tradeup(
        db=db,
        input_skins=INPUT_SKINS,
        all_skins=ALL_SKINS
    )

    db.close()

    print("\nTRADE-UP RESULT\n")
    for k, v in result.items():
        print(f"{k}: {v}")
