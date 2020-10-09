import os
import sys
from flask import Flask, request, jsonify
import requests
import json
import os
import base64
from flask_cors import CORS, cross_origin

from classifier import *
from service import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/analyze', methods=['GET', 'POST'])
@cross_origin(origin='*')
def analyze():
    encoded_string = request.json["data"]

    vals = ocr(encoded_string)
    
    return jsonify(words=vals)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)