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
    data_open, data_close = Stock.get_stock_data(ticker)
    full_name = Stock.get_full_name(ticker)
    full_data["open"] = data_open
    full_data["close"] = data_close
    full_data["fullName"] = full_name
    print("--------------------")
    print(ticker)
    print(full_data)
    print("--------------------")
    return jsonify(full_data)


@app.route('/reddit-data', methods=['POST'])
def reddit_data():
    params = request.json
    ticker = params["ticker"]
    time = "1d"
    num_subs = Reddit.num_subs(ticker, time)
    print("NUMBER OF REDDIT POSTS: " + str(num_subs))
    return jsonify(num_subs)

