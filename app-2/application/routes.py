from flask import render_template, redirect, url_for, request, Response
from application import app
import random, requests

@app.route('/', methods = ['GET'])
def animal():
    animals = ['duck', 'pig', 'cow']
    animal = random.choice(animals)

    return Response(animal, mimetype='text/plain')


@app.route('/noise', methods = ['POST'])
def noise():
    
    animal = request.data.decode('utf-8')
    
    if animal == 'duck':
        noise = 'quack'
    elif animal == 'pig':
        noise='oink'
    elif animal  == 'cow':
        noise='moo'
    
    return Response(noise, mimetype='text/plain')


