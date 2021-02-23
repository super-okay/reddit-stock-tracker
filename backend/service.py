import requests
import json

import config

base_intraday_url = "https://cloud.iexapis.com/stable/stock/{}/intraday-prices?token=" + config.iex_api_key
base_company_url = "https://cloud.iexapis.com/stable/stock/{}/company?token=" + config.iex_api_key

class Stock:

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

    def get_stock_data(ticker):
        full_intraday_url = base_intraday_url.format(ticker)
        response = requests.get(full_intraday_url)
        data = response.json()
        # data_formatted = json.dumps(data, indent=2)
        # print(data_formatted)

        # print(data[0]["average"])
        return data[1]

    def get_full_name(ticker):
        full_company_url = base_company_url.format(ticker)
        response = requests.get(full_company_url)
        data = response.json()
        full_name = data["companyName"]
        return full_name

    def test():
        return "Stock object in service file."
