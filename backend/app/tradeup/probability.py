from collections import Counter
from app.tradeup.metadata import get_skin_meta


def calculate_outcome_probabilities(
    input_skins: list[str],
    outcome_pool: dict[str, list[str]]
) -> dict[str, float]:

    collection_counts = Counter(
        get_skin_meta(s)["collection"] for s in input_skins
    )

    total_inputs = sum(collection_counts.values())
    probabilities = {}

    for collection, count in collection_counts.items():
        outcomes = outcome_pool.get(collection, [])
        if not outcomes:
            continue

        collection_weight = count / total_inputs
        per_skin_prob = collection_weight / len(outcomes)

        for skin in outcomes:
            probabilities[skin] = round(per_skin_prob, 6)

    return probabilities
