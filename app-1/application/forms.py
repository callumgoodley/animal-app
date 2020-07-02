from flask_wtf import FlaskForm
from wtforms import SubmitField

class AnimalForm(FlaskForm):
    submit = SubmitField('get animal... ')
