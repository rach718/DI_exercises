from flask import Flask
from flask import render_template
import db

app = Flask(__name__)

@app.route('/')
def home():

    products = db.load_database()

    html_home = render_template('home.html', products=products)
    return html_home

if __name__=='__main__':
    app.run()
