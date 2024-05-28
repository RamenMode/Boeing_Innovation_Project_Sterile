from flask import Flask, request, jsonify, make_response
import json
import urllib.parse
import os
from flask_cors import CORS

from io import StringIO
import pandas as pd
import numpy as np

from main import Mainframe

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# initialize and train classifiers using function from main.py
mainframe = Mainframe()

@app.route('/', methods=['GET'])
def home():
    return "This is the backend server for Notre Dame X Boeing NLP"

@app.route('/getTranscript', methods=['POST'])
def getTranscript():
    plain_text = request.data.decode('ascii')
    output = predict(plain_text)
    json_serializable_data = {key: value.tolist() if isinstance(value, np.ndarray) else value for key, value in output.items()}
    return jsonify(json_serializable_data), 200

def predict(user_input):
    output = mainframe.get_datalog([user_input])
    return output

if __name__ == '__main__':
    app.run(port=8000)