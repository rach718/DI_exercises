from flask import Flask, redirect
from flask import render_template
from flask import request
from forms import *

import db

app = Flask(__name__)
app.config['SECRET_KEY']="keyinthehole"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = db.load_database()

    return render_template('products.html', products=products)

@app.route('/productdetails/<int:product_id>')
def productdetails(product_id):
    products = db.load_database()

    return render_template('productdetails.html', product=products[product_id])


@app.route('/buy/<int:product_id>')
def buy(product_id):
    products = db.load_database()
    products[product_id]['stock'] -=1
    db.update_database(products)

    return redirect(f'/productdetails/{product_id}')

@app.route('/login', methods=('Get', 'POST'))
def login():
    login_form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form =login_form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        if username == "Rachel" and password == "blue":
            return f"<h1>Welcome Rachel! Hope you enjoy our site!</h1>"
        else:
            return "<h1>Access Denied</h1>"
    else:
        return "<h1>Failed Validation</h1>"

if __name__ == "__main__":
    app.run(port=5001)