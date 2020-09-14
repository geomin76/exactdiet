import os
import sys
import requests
from flask import Flask

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
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
        "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'language': 'unk', 'detectOrientation': 'true'}
    data = {'url': image_url}
    response = requests.post(ocr_url, headers=headers, params=params, json=data)
    response.raise_for_status()

    analysis = response.json()

    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        print(line)
    #     for word_metadata in line:
    #         for word_info in word_metadata["words"]:
    #             word_infos.append(word_info)
    # print(word_infos)
    return "woo"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)