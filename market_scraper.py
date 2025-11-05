def find_deals(car: dict) -> list:
    return [
        {
            "title": f"{car['make']} {car['model']} {car['year']} - clean",
            "price": 5400,
            "source": "AutoTrader",
        },
        {
            "title": f"{car['make']} {car['model']} {car['year']} - needs tyres",
            "price": 4900,
            "source": "FB Marketplace",
        },
    ]
