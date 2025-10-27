# Golden Stock Dashboard

A simple pipeline that scrapes the live gold price into a CSV file and displays it on a real-time dashboard built with Dash & Plotly.

## Project Structure
dashboard_project/

├─ dash_app.py        # Dash web app (KPIs + historical line chart)

├─ scraper.sh         # Web scraper (appends timestamp + price)

└─ gold.csv           # Stored data (timestamp,price)

## Features
• Automated price scraping with `curl` and `grep`
• Latest price + stats (high, volatility, daily yield)
• Historical price visualization with Plotly
• Auto-refresh every 5 minutes

## Requirements
Python 3.8+
pip (or venv)
curl + grep (PCRE support)
Dash, pandas, plotly

Install dependencies:
pip install dash pandas plotly

## Usage
1. Initialize CSV header (if needed):
echo "timestamp,price" > gold.csv

2. Make scraper executable:
chmod +x scraper.sh

3. Run scraper manually to collect data:
./scraper.sh

4. Launch the Dash app:
python3 dash_app.py
→ Open browser: http://localhost:8080

## Automating Data Collection (cron example)
*/5 * * * * /bin/bash /absolute/path/to/scraper.sh

## Data Format (gold.csv)
timestamp,price
2023-03-26 16:05:01,1979.53
...

## Notes
• HTML scraping may break if website structure changes
• Use relative paths for portability
• For production, run Dash behind a proper web server
