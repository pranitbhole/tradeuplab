from app.tradeup.outcomes import generate_outcomes
from app.tradeup.probability import calculate_outcome_probabilities

ALL_SKINS = [
    "AK-47 | Redline (Field-Tested)",
    "AK-47 | Fire Serpent (Factory New)",
    "AWP | Asiimov (Field-Tested)",
    "AUG | Chameleon (Factory New)"
]

INPUT_SKINS = [
    "AK-47 | Redline (Field-Tested)"
] * 10


if __name__ == "__main__":
    pool = generate_outcomes(ALL_SKINS, INPUT_SKINS)
    probs = calculate_outcome_probabilities(INPUT_SKINS, pool)

    print("Outcome Pool:")
    print(pool)

    print("\nProbabilities:")
    for k, v in probs.items():
        print(f"{k}: {v}")
