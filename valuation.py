def get_valuation(car: dict) -> dict:
    base_trade = 5200
    base_retail = 6800

    age_penalty = max(0, (2025 - car["year"] - 5)) * 150
    miles_penalty = max(0, (car["mileage"] - 60000) // 5000) * 120

    trade = max(1000, base_trade - age_penalty - miles_penalty)
    retail = max(trade + 400, base_retail - age_penalty - miles_penalty + 300)

    return {"trade": int(trade), "retail": int(retail)}
