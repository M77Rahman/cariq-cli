from dvla_api import get_vehicle_info
from mot_api import get_mot_history
from valuation import get_valuation
from market_scraper import find_deals
from analytics import estimate_profit
import csv, os, time


def line():
    print("-" * 50)


def save_results(car, val, deals):
    os.makedirs("out", exist_ok=True)
    path = os.path.join("out", "results.csv")
    write_header = not os.path.exists(path)

    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow([
                "ts", "reg", "year", "make", "model", "mileage",
                "trade", "retail", "deal_title", "deal_price", "source"
            ])
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        for d in deals:
            w.writerow([
                ts, car["reg"], car["year"], car["make"], car["model"],
                car["mileage"], val["trade"], val["retail"],
                d["title"], d["price"], d["source"]
            ])


def main():
    reg = input("Enter reg: ").strip().upper()
    miles_txt = input("Enter mileage (just number or leave blank): ").strip()
    miles = int(miles_txt) if miles_txt else 68000

    print("\nFetching...\n")

    # --- Fetch data from APIs ---
    car = get_vehicle_info(reg)
    car["mileage"] = miles
    mot_history = get_mot_history(reg)
    val = get_valuation(car)
    deals = find_deals(car)

    # --- Display results ---
    line()
    print("CAR DETAILS")
    print(f"{car['year']} {car['make']} {car['model']} • {car['mileage']} miles")
    print(f"MOT: {car['mot_status']}")

    line()
    print("MOT HISTORY")
    if mot_history:
        for t in mot_history[:5]:  # last 5 records
            print(f"{t['completedDate']} – {t['result']} ({t['mileage']} miles)")
    else:
        print("No MOT data found")

    line()
    print("ESTIMATED VALUE")
    print(f"Trade: £{val['trade']}  |  Retail: £{val['retail']}")

    line()
    print("POSSIBLE DEALS")
    if not deals:
        print("No deals found.")
    for d in deals:
        profit, margin = estimate_profit(val['trade'], val['retail'], d['price'])
        print(f"{d['title']} — £{d['price']}  ({d['source']})")
        print(f"Potential profit: £{profit} ({margin}%)\n")

    save_results(car, val, deals)
    print("Saved to out/results.csv")


if __name__ == "__main__":
    main()
