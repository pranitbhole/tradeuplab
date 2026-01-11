from sqlalchemy.orm import Session
from app.tradeup.price import get_latest_price


def calculate_tradeup_ev(
    db: Session,
    input_skins: list[str],
    probabilities: dict[str, float]
) -> dict:

    input_prices = []
    for skin in input_skins:
        price = get_latest_price(db, skin)
        if price is None:
            raise ValueError(f"Missing price for input skin: {skin}")
        input_prices.append(price)

    input_cost = round(sum(input_prices), 2)

    expected_return = 0.0
    bust_probability = 0.0
    outcomes = []

    for skin, prob in probabilities.items():
        price = get_latest_price(db, skin)
        if price is None:
            continue

        contribution = price * prob
        expected_return += contribution

        if price < input_cost:
            bust_probability += prob

        outcomes.append({
            "skin": skin,
            "probability": prob,
            "price": round(price, 2),
            "expected_value": round(contribution, 2)
        })

    expected_return = round(expected_return, 2)
    ev = round(expected_return - input_cost, 2)
    roi = round((ev / input_cost) * 100, 2)

    return {
        "input_cost": input_cost,
        "expected_return": expected_return,
        "ev": ev,
        "roi_percent": roi,
        "bust_probability": round(bust_probability, 4),
        "outcomes": outcomes
    }
