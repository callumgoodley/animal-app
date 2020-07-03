from flask import render_template, redirect, url_for, request
from application import app
import random, requests

@app.route('/', methods = ['GET', 'POST'])
def animal():
    animals = ['duck', 'pig', 'cow', 'horse', 'chicken']
    animal = random.choice(animals)
    respsonse = requests.post("http://animal-app_app-2_1/noise:5001", data=animal)
    data = str(response.json()["data"])

    return data
@app.route('/noise', methods = ['GET', 'POST'])
def noise():
    
    data_sent = request.data.decode('utf-8')
    
    if data_sent == 'duck':
        return {'animal': 'duck', 'noise':'quack'}
    elif data_sent == 'pig':
        return {'animal': 'pig', 'noise':'oink'}
    elif data_sent == 'cow':
        return {'animal': 'cow', 'noise':'moo'}


