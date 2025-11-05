# CarIQ CLI 🚗

**CarIQ CLI** is a Python-based command-line tool for car traders and enthusiasts.  
It fetches UK vehicle data, estimates market value, and simulates deal analysis — fast and simple.

---

## 🔧 Features

- Pulls real vehicle info via the **DVLA Vehicle Enquiry API**
- Displays **MOT history** (DVSA API integration ready)
- Calculates estimated **trade** and **retail** values
- Simulates **market listings** with profit margins
- Saves every result to `out/results.csv`

---

## 🧠 Example Output

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

yaml
Copy code

---

## 🗂️ Project Structure

cariq-cli/
│
├── cariq.py # main program
├── dvla_api.py # DVLA Vehicle Enquiry API
├── mot_api.py # MOT history API
├── valuation.py # valuation logic
├── market_scraper.py # mock marketplace data
├── analytics.py # profit analysis
├── out/results.csv # saved results
├── requirements.txt # dependencies
└── README.md # documentation

yaml
Copy code

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/M77Rahman/cariq-cli.git
   cd cariq-cli
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python cariq.py
🔑 API Keys Setup
You’ll need free keys to access live data:

API	Purpose	Registration Link
DVLA Vehicle Enquiry API	Fetch real car details like make, model, and MOT status	DVLA Developer Portal
DVSA MOT History API	Fetch vehicle MOT test history	DVSA Developer Portal

Once approved, paste your keys inside:

dvla_api.py

mot_api.py

🧩 Future Roadmap
 Replace mock valuations with live AutoTrader or Parkers scraping

 Add Streamlit web dashboard version

 Real-time deal alerts via Telegram or Email

 Profit tracking dashboard using Google Sheets or Looker Studio

👨‍💻 Author
Muhammad Emdadur Rahman
Tech-driven developer focused on automation, data, and real-world problem solving.
LinkedIn • GitHub

🪶 License
This project is for educational and portfolio use only.
APIs used are property of the UK DVLA and DVSA.

yaml
Copy code

---