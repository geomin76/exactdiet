import os
import sys
import requests
from flask import Flask
import json

app = Flask(__name__)

subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/analyze')
def test():
    ocr_url = endpoint + "vision/v3.0/ocr"
    image_url = "./Capture.PNG"

    image_data = open(image_url, "rb").read()

    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'language': 'en', 'detectOrientation': 'true'}
    response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    analysis = response.json()

    res = []
    for region in analysis["regions"]:
        for lines in region["lines"]:
            s = " ".join(words["text"] for words in lines["words"])
            res.append(s)
    print(res)
    return "woo"
