import requests

def get_mot_history(reg: str) -> list:
    """Fetch MOT history for a UK vehicle."""
    url = f"https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests?registration={reg}"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching MOT data: {e}")
        return []

    if not data:
        return []

    tests = data[0].get("motTests", [])
    return [
        {
            "completedDate": t.get("completedDate", "Unknown")[:10],
            "result": t.get("testResult", "Unknown"),
            "mileage": t.get("odometerValue", "Unknown")
        }
        for t in tests
    ]
