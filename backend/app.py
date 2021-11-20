from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

from stock_service import Stock
from reddit_service import Reddit

app = Flask(__name__)
CORS(app)

@app.route('/stock-data', methods=['POST'])
def stock_data():
    params = request.json
    ticker = params["ticker"]
    full_data = {}
    try:
        stock = Stock()
        data_open, data_close, percent_change = stock.get_stock_data(ticker)
        full_name = stock.get_full_name(ticker)
        full_data["open"] = data_open
        full_data["close"] = data_close
        full_data["fullName"] = full_name
        full_data["percentChange"] = percent_change
        print("--------------------")
        print(ticker)
        print(full_data)
        print("--------------------")
        return jsonify(full_data)
    except:
        return jsonify("Invalid ticker")


@app.route('/reddit-data', methods=['POST'])
def reddit_data():
    params = request.json
    ticker = params["ticker"]
    time = "1d"
    reddit = Reddit()
    num_subs = reddit.num_subs(ticker, time)
    print("NUMBER OF REDDIT POSTS: " + str(num_subs))
    return jsonify(num_subs)

