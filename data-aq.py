import requests as r
from datetime import date
import json
from sys import argv
headers = {
'user-agent' : 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'
}

def download_data(ticker: str) -> dict:
    ticker = ticker.upper()
    today = date.today()
    start = str(today.replace(year=today.year - 5))
    url = f"https://api.nasdaq.com/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"
    response = r.get(url, headers = headers)
    data = response.json()
    return data


