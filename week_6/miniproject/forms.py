import flask_wtf
import wtforms
from flask_wtf import FlaskForm
from wtforms import validators, StringField

class LoginForm(flask_wtf.FlaskForm):
    username = StringField("USERNAME", [validators.length(min=4, max=25)])
    password = wtforms.PasswordField("PASSWORD")
    submit = wtforms.SubmitField("SUBMIT")