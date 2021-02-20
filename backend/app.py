from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route('/price', methods=['POST'])
def getPrice():
    params = request.json
    print(params)
    return jsonify(params)
