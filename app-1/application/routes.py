from flask import render_template, redirect, url_for, request
from application import app
from application.forms import AnimalForm
import random, requests

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = AnimalForm()

    if form.validate_on_submit():
        return redirect(url_for('generate'))
    
    return render_template('home.html', title='Home', form=form)

@app.route('/generate', methods = ['GET', 'POST'])
def generate():
    response = requests.get("http://animal-app_app-2_1:5001")
    # animal_dict = str(response.json()["data"])
    animal = "animal"
    noise = "noise"


    return render_template('generate.html', title='Generate', animal=animal, noise=noise, response=response)
