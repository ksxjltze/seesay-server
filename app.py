from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return '{"text": "Hello, World!"}'

@app.route('/record', methods = ['POST'])
def record():
    # Open file and write binary (blob) data
    f = open('./file.wav', 'wb')
    f.write(request.data)
    f.close()
    return '{"text": "Audio file saved!"}'

@app.route('/capture', methods = ['POST'])
def capture():
    f = open('./image.jpeg', 'wb')
    f.write(request.data)
    f.close()
    return '{"text": "Image file saved!"}'

@app.route('/test', methods = ['POST'])
def test():
    print("TEST")
    return '{"text": "TEST!"}'
