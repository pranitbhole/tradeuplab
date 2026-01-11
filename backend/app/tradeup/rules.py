def validate_tradeup(skins: list):
    if len(skins) != 10:
        raise ValueError("Trade-up requires exactly 10 skins")

    rarities = {s["rarity"] for s in skins}
    if len(rarities) != 1:
        raise ValueError("All skins must be same rarity")

    collections = {s["collection"] for s in skins}
    if len(collections) != 1:
        raise ValueError("All skins must be from same collection")

    return True
