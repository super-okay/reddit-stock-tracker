from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

from service import Stock

app = Flask(__name__)
CORS(app)

@app.route('/price', methods=['POST'])
def getPrice():
    params = request.json
    ticker = params["ticker"]
    data_at_open = Stock.get_stock_data(ticker)
    print("--------------------")
    print(ticker)
    print(data_at_open)
    print("--------------------")
    return jsonify(data_at_open)
