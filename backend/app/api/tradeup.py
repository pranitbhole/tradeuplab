from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.db import SessionLocal
from app.tradeup.outcomes import generate_outcomes
from app.tradeup.probability import calculate_outcome_probabilities
from app.tradeup.simulator import run_tradeup_simulation
from app.tradeup.ev import calculate_tradeup_ev

router = APIRouter(prefix="/tradeup", tags=["Trade-Up"])


class TradeUpRequest(BaseModel):
    inputs: List[str]
    runs: int = 10000


@router.post("/simulate")
def simulate_tradeup(req: TradeUpRequest):
    if len(req.inputs) != 10:
        raise HTTPException(
            status_code=400,
            detail="Exactly 10 input skins required"
        )

    db = SessionLocal()

    try:
        # 1️⃣ Generate outcome pool
        outcome_pool = generate_outcomes(req.inputs)

        # 2️⃣ Calculate theoretical probabilities
        probabilities = calculate_outcome_probabilities(
            input_skins=req.inputs,
            outcome_pool=outcome_pool
        )

        # 3️⃣ Calculate EV
        ev_result = calculate_tradeup_ev(
            db,
            req.inputs,
            probabilities
        )

        # 4️⃣ Monte Carlo simulation
        simulation = run_tradeup_simulation(
            probabilities,
            runs=req.runs
        )

        return {
            "ev": ev_result,
            "simulation": simulation
        }

    finally:
        db.close()
