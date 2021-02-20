from flask import Flask
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/price', methods=['POST'])
def getPrice():
    print(request.json)
    return request.json
