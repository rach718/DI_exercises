from flask import Flask
from flask import render_template
import db


app = Flask(__name__)

@app.route('/')
def home(): #controller
    #model
    products = db.load_database()
    #view
    html = render_template("home.html", products=products) #variable called products with key and data
    return html

if __name__ == "__main__":
    app.run()

