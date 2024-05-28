import requests
import json
'''
import json
import urllib.parse
import os

from io import StringIO
import pandas as pd

from main import Mainframe

mainframe = Mainframe()
print(mainframe.get_datalog(['PERFORMED HARD-LANDING INSPECTION ACCORDING TO STANDARD PROTOCOL']))
'''
'''
print(requests.get('http://127.0.0.1:105/getPrediction').text)

res = requests.get('http://127.0.0.1:105/hello')
response = res.content.decode('utf-8')
print(response)

with open('preamble.wav', 'rb') as fobj:
    requests.post('http://127.0.0.1:105/storeAudio', files={'fieldname': fobj})
res = requests.get('http://127.0.0.1:105/getAudio', params={'name': 'uploaded_audio.wav'})
print(res.content)

with open("audio.wav", 'wb') as file:
    file.write(res.content)

'''


# The URL of your Flask server
url = 'http://127.0.0.1:8000/getTranscript'

# Data to send in the request
formData = {'text': 'PERFORMED HARD-LANDING INSPECTION ACCORDING TO STANDARD PROTOCOL'}

# Send a POST request to the endpoint with JSON data
response = requests.post(url, data=formData)

# Print the response
print(response.status_code)
print(response.text)
