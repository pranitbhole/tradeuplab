# Static metadata (temporary – will be replaced by DB / API later)

SKIN_METADATA = {
    "AK-47 | Redline (Field-Tested)": {
        "collection": "The Phoenix Collection",
        "rarity": "Classified",
        "min_float": 0.10,
        "max_float": 0.70
    },

    "AWP | Asiimov (Field-Tested)": {
        "collection": "The Phoenix Collection",
        "rarity": "Covert",
        "min_float": 0.18,
        "max_float": 1.00
    },

    "AUG | Chameleon (Factory New)": {
        "collection": "The Phoenix Collection",
        "rarity": "Covert",
        "min_float": 0.00,
        "max_float": 0.08
    }
}

RARITY_ORDER = [
    "Consumer",
    "Industrial",
    "Mil-Spec",
    "Restricted",
    "Classified",
    "Covert"
]


def get_skin_meta(skin_name: str) -> dict:
    if skin_name not in SKIN_METADATA:
        raise ValueError(f"Metadata not found for {skin_name}")
    return SKIN_METADATA[skin_name]


def get_all_metadata() -> dict:
    return SKIN_METADATA


def next_rarity(rarity: str) -> str:
    idx = RARITY_ORDER.index(rarity)
    if idx + 1 >= len(RARITY_ORDER):
        raise ValueError("No higher rarity exists")
    return RARITY_ORDER[idx + 1]
