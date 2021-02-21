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

# Example item in list
#
# {
#     "date": "2021-02-19",
#     "minute": "15:59",
#     "label": "3:59 PM",
#     "high": 129.945,
#     "low": 129.815,
#     "open": 129.88,
#     "close": 129.815,
#     "average": 129.885,
#     "volume": 11861,
#     "notional": 1540568.095,
#     "numberOfTrades": 111
# }