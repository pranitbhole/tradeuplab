import random


def run_monte_carlo(probabilities: dict[str, float], runs: int = 10000) -> dict:
    results = {}
    skins = list(probabilities.keys())
    weights = list(probabilities.values())

    for _ in range(runs):
        pick = random.choices(skins, weights=weights)[0]
        results[pick] = results.get(pick, 0) + 1

    return {
        skin: round(count / runs, 4)
        for skin, count in results.items()
    }
