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
    data_at_open = Stock.get_stock_data(ticker)
    full_name = Stock.get_full_name(ticker)
    data_at_open["fullName"] = full_name
    print("--------------------")
    print(ticker)
    print(full_name)
    print(data_at_open)
    print("--------------------")
    return jsonify(data_at_open)


@app.route('/reddit-data', methods=['POST'])
def reddit_data():
    params = request.json
    ticker = params["ticker"]
    time = "2d"
    num_subs = Reddit.num_subs(ticker, time)
    print("NUMBER OF REDDIT POSTS: " + str(num_subs))
    return jsonify(num_subs)

