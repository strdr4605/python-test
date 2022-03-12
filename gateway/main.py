import os
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '/service1, /service2'

@app.route('/<service>')
def serv(service):
    r = requests.get('http://' + service + ':5001')
    return r.text

app.run(host='0.0.0.0', port=5001)
