# CarIQ CLI 🚗

**CarIQ CLI** is a Python-based command-line tool for car traders and enthusiasts.
It models UK vehicle valuation and deal-analysis logic end to end — vehicle lookup, trade/retail value estimation, and profit-margin analysis against sample marketplace listings.

> **Data mode:** the DVLA and MOT lookups currently run against **mock/placeholder data** (`dvla_api.py`, `mot_api.py`) so the tool runs without an API key. The valuation and profit-analysis logic (`valuation.py`, `analytics.py`, `market_scraper.py`) is real and does the actual calculation work. Wiring in the live [DVLA Vehicle Enquiry API](https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html) is a free, ~30-minute follow-up — the placeholder functions are isolated on purpose so that swap is a single-file change.

---

## 🔧 Features

- Vehicle lookup (mock DVLA data; real API integration ready to plug in)
- MOT history lookup (mock; DVSA API integration ready to plug in)
- Calculates estimated **trade** and **retail** values
- Simulates **market listings** with profit margins
- Saves every result to `out/results.csv`

---

## 🧠 Example Output

```
Enter reg: WL68LLX
Fetching...

CAR DETAILS
2017 Ford Focus Zetec • 68000 miles
MOT: Valid until Mar 2026

ESTIMATED VALUE
Trade: £4630 | Retail: £6530

POSSIBLE DEALS
Ford Focus Zetec 2017 - clean — £5400 (AutoTrader)
Potential profit: £180 (3.2%)
```

---

## 🗂️ Project Structure

```
cariq-cli/
├── cariq.py            # main program
├── dvla_api.py         # DVLA Vehicle Enquiry API (currently mock data)
├── mot_api.py          # MOT history API (currently mock data)
├── valuation.py        # valuation logic
├── market_scraper.py   # mock marketplace data
├── analytics.py        # profit analysis
├── out/results.csv     # saved results
├── requirements.txt    # dependencies
└── README.md           # documentation
```

---

## ⚙️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/M77Rahman/cariq-cli.git
   cd cariq-cli
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app**
   ```bash
   python cariq.py
   ```

## 🔑 Live API Setup (optional)

To replace the mock data with real lookups, get free keys from:

| API | Purpose |
|---|---|
| DVLA Vehicle Enquiry API | Vehicle make/model/year/MOT status |
| DVSA MOT History API | Full MOT test history |

Then update `dvla_api.py` / `mot_api.py` to call the live endpoints instead of returning the placeholder dict.
