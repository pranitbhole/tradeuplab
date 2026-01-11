# tradeup/utils.py

def uniform_probabilities(outcomes):
    """
    Naive probability model.
    NOT Steam-accurate.
    Use only for testing or UI placeholders.
    """
    if not outcomes:
        return {}
    p = 1 / len(outcomes)
    return {o["market_hash_name"]: p for o in outcomes}
