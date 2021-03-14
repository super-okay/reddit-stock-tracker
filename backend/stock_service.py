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
        """ 
        gets data at open and close of specified ticker
        returns tuple of data at open, data at close
        """
        full_intraday_url = base_intraday_url.format(ticker)
        response = requests.get(full_intraday_url)
        data = response.json()
        data_open = data[0]
        data_close = data[len(data)-1]
        price_open = data_open["open"]
        price_close = data_close["open"]

        price_div = price_close / price_open
        # percent_change = 0
        # if price_div > 1:
        #     percent_change = (price_div - 1) * 100
        # elif price_div < 1:
        #     percent_change = (1 - price_div) * 100
        percent_change = round((price_div - 1) * 100, 2)

        return data_open, data_close, percent_change

    def get_full_name(ticker):
        full_company_url = base_company_url.format(ticker)
        response = requests.get(full_company_url)
        data = response.json()
        full_name = data["companyName"]
        return full_name
