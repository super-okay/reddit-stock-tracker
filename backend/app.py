from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

from service import Stock

app = Flask(__name__)
CORS(app)

@app.route('/price', methods=['POST'])
def getData():
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
