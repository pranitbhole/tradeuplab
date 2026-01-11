import random
from collections import Counter


def run_tradeup_simulation(
    probabilities: dict[str, float],
    runs: int = 10000
) -> dict:
    """
    Monte Carlo simulation of trade-up outcomes.
    Returns empirical probabilities.
    """

    if not probabilities:
        return {}

    skins = list(probabilities.keys())
    weights = list(probabilities.values())

    results = random.choices(
        skins,
        weights=weights,
        k=runs
    )

    counts = Counter(results)

    return {
        skin: {
            "count": count,
            "probability": round(count / runs, 6)
        }
        for skin, count in counts.items()
    }
