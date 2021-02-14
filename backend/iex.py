import requests
import json

base_intraday_url = "https://cloud.iexapis.com/stable/stock/{}/intraday-prices?token=pk_efe8ccaa56f640648313551f6afa5cb8"
ticker = "aapl"
full_intraday_url = base_intraday_url.format(ticker)
response = requests.get(full_intraday_url)
data = response.json()
print(data[0]["minute"])
# data_formatted = json.dumps(data, indent=2)
# print(data_formatted)
