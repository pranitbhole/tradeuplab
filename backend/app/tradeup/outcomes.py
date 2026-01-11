from collections import defaultdict
from app.tradeup.metadata import (
    get_skin_meta,
    get_all_metadata,
    next_rarity
)


def generate_outcomes(input_skins: list[str]) -> dict[str, list[str]]:
    """
    Generates possible trade-up outcomes grouped by collection.
    """

    collections = defaultdict(int)

    # Count how many skins from each collection
    for skin in input_skins:
        meta = get_skin_meta(skin)
        collections[meta["collection"]] += 1

    outcome_pool = {}

    for collection, count in collections.items():
        # Trade-up rules: need at least 1 skin from a collection
        # Higher count => higher probability (handled later)
        higher_rarity = next_rarity(
            get_skin_meta(input_skins[0])["rarity"]
        )

        # Get all skins in this collection with next rarity
        possible = [
            name
            for name, meta in get_all_metadata().items()
            if meta["collection"] == collection
            and meta["rarity"] == higher_rarity
        ]

        if possible:
            outcome_pool[collection] = possible

    if not outcome_pool:
        raise ValueError("No valid trade-up outcomes found")

    return outcome_pool
