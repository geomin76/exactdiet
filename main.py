import os
import sys
import requests
from flask import Flask
import json

app = Flask(__name__)

subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

@app.route('/')
def world():
    return "Hello World!"

@app.route('/test')
def test():
    ocr_url = endpoint + "vision/v3.0/ocr"

    # Set image_url to the URL of an image that you want to analyze.
    # image_url = "https://lh3.googleusercontent.com/76JllPseCL9WHnBt8bBkA8FaraCi3iEDHDK7-oTi4qN2L5tSy3sYli_3zwoakbCGNcAm_FoB26kDVwmKcVlb9I2f_faFM-iqe9d-20uGg8qI5Deq-XCHltEzBj4EtU2CcMroFwZQ5G0=w600-h315-p-k"
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)