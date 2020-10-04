import os
import sys
from flask import Flask, request
import json
import os
import base64
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
# cors = CORS(app, resources={r"/analyze": {"origins": "https://gy0s1wfur7.execute-api.us-east-1.amazonaws.com/dev/"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/analyze', methods=['GET', 'POST'])
@cross_origin(origin='*')
def analyze():
    encoded_string = request.json["data"]
    # print(request.json["data"])

    imgdata = base64.b64decode(encoded_string)
    filename = '/tmp/img.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    stream = os.popen('./tesseract /tmp/img.jpg stdout -l eng')
    output = stream.read()
    print(output)
    os.remove('/tmp/img.jpg')

    # return {
    #     'statusCode': 200,
    #     'headers': {
    #         'Access-Control-Allow-Headers':  "*",
    #         'Access-Control-Allow-Origin': '*',
    #         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    #     },
    #     'body': json.dumps({'data': str(output)})
    # }
    
    return json.dumps({'data': str(output)})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)