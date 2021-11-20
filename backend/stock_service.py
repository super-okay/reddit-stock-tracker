import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# load_dotenv()

# base_intraday_url = "https://cloud.iexapis.com/stable/stock/{}/intraday-prices?token=" + os.getenv("IEX_API_KEY")
# base_company_url = "https://cloud.iexapis.com/stable/stock/{}/company?token=" + os.getenv("IEX_API_KEY")

class Stock:

    def __init__(self):
        load_dotenv()
        self.base_intraday_url = "https://cloud.iexapis.com/stable/stock/{}/intraday-prices?token=" + os.getenv("IEX_API_KEY")
        self.base_company_url = "https://cloud.iexapis.com/stable/stock/{}/company?token=" + os.getenv("IEX_API_KEY")


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

    def get_stock_data(self, ticker):
        """ 
        gets data at open and close of specified ticker
        returns tuple of data at open, data at close, and intraday percent change
        """
        full_intraday_url = self.base_intraday_url.format(ticker)
        response = requests.get(full_intraday_url)
        data = response.json()
        data_open = data[0]
        data_close = data[len(data)-1]

        # round prices to two decimal places
        price_open_open = data_open["open"]
        price_open_close = data_open["close"]
        data_open["open"] = round(price_open_open, 2)
        data_open["close"] = round(price_open_close, 2)

        price_close_open = data_close["open"]
        price_close_close = data_close["close"]
        data_close["open"] = round(price_close_open, 2)
        data_close["close"] = round(price_close_close, 2)

        # change date format
        date = data_open["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%B %d, %Y")
        data_open["date"] = formatted_date
        data_close["date"] = formatted_date

        # calculate intraday price change percentage
        price_at_open = data_open["open"]
        price_at_close = data_close["close"]
        price_div = price_at_close / price_at_open
        percent_change = round((price_div - 1) * 100, 2)

        return data_open, data_close, percent_change

    def get_full_name(self, ticker):
        """ returns full name string """
        full_company_url = self.base_company_url.format(ticker)
        response = requests.get(full_company_url)
        data = response.json()
        full_name = data["companyName"]
        return full_name
