from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

from request import describe_image, speech_to_text, text_to_speech
from dotenv import load_dotenv
import os

load_dotenv()
replicate_token = os.environ['REPLICATE_API_KEY']
openai_token = os.environ['OPENAI_API_KEY']

app = Flask(__name__)
CORS(app)

#temp
transcript = "describe the image as if you were talking to a blind person"
result = ""

@app.route("/")
def helloWorld():
  return '{"text": "Hello, World!"}'

@app.route('/record', methods = ['POST'])
def record():
    # Open file and write binary (blob) data
    f = open('./file.wav', 'wb')
    f.write(request.data)
    f.close()
    transcript = speech_to_text('./file.wav', openai_token)
    return '{"text": "' + transcript + '"}'

@app.route('/capture', methods = ['POST'])
def capture():
    f = open('./image.jpeg', 'wb')
    f.write(request.data)
    f.close()
    result = describe_image('./image.jpeg', replicate_token, transcript)
    return '{"text": "' + result + '"}'

@app.route('/texttospeech', methods = ['POST'])
def textToSpeech():
    outputText = text_to_speech(result)
    return '{"text": "' + outputText + '"}'

@app.route('/test', methods = ['POST'])
def test():
    print("TEST")
    return '{"text": "TEST!"}'
