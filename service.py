import os
import sys
import requests
import json
import os
import base64

from classifier import *

subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

def ocr(encoded_string):
    imgdata = base64.b64decode(encoded_string)
    filename = '/tmp/img.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)

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
    
    return vals