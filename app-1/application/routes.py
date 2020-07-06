from flask import render_template, redirect, url_for, request
from application import app
from application.forms import AnimalForm
import requests

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = AnimalForm()
    if form.validate_on_submit():
        return redirect(url_for('generate'))
    
    return render_template('home.html', title='Home', form=form)

@app.route('/generate', methods = ['GET', 'POST'])
def generate():
    animal = requests.get("http://app-2:5001")
    noise = requests.post("http://app-2:5001/noise", data=animal.text)
    


    return render_template('generate.html', title='Generate', animal=animal, noise=noise)
