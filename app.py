import os
import sys
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/analyze')
def test():
    stream = os.popen('./tesseract ok.jpg stdout -l eng')
    output = stream.read()
    print(output)
    return "ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)