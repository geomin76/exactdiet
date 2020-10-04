import os
import sys
from flask import Flask, request
import requests
import json
import os
import base64
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/analyze', methods=['GET', 'POST'])
@cross_origin(origin='*')
def analyze():
    encoded_string = request.json["data"]
    # print(request.json["data"])

    imgdata = base64.b64decode(encoded_string)
    filename = '/tmp/img.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    # stream = os.popen('./ocr/tesseract /tmp/img.jpg stdout -l eng')
    # output = stream.read()
    # print(output)

    ocr_url = endpoint + "vision/v3.0/ocr"
    image_url = '/tmp/img.png'
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

    os.remove('/tmp/img.png')

    vals = " ".join(res)
    
    # return json.dumps({ 'data': vals })
    return vals


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)