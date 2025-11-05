def estimate_profit(trade: int, retail: int, listing_price: int):
    avg_value = (trade + retail) / 2
    profit = avg_value - listing_price
    margin = (profit / avg_value) * 100 if avg_value else 0
    return round(profit), round(margin, 1)
