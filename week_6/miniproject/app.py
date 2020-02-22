from flask import Flask
from flask import render_template
from flask import request, redirect
from forms import *
from flask_socketio import SocketIO, send

import db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'no-corona-here'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = db.load_database()

    return render_template('products.html', product=products)

@app.route('/product_specs/<int:product_id>')
def product_specs(product_id):
    products = db.load_database()

    return render_template('product_specs.html', product=products[product_id])


@app.route('/buy/<int:product_id>')
def buy(product_id):

    products = db.load_database()
    products[product_id]['stock'] -= 1
    db.update_database(products)

    return redirect(f'/product_specs/{product_id}')

@app.route('/products/eye care')
def eyecare():
    all_data = db.load_database()
    eyecare_list = []
    for product in all_data['products']:
        if product['category'] == 'eye care':
            eyecare_list.append(product)

    return render_template('products.html', product=eyecare_list)

@app.route('/products/moisturizers')
def moisturizers():
    all_data = db.load_database()['products']
    moisturizers_list = []
    for product in all_data['products']:
        if product['category'] == 'moisturizer':
            moisturizers_list.append(product)

    return render_template('products.html', product=moisturizers_list)

@app.route('/products/allinone')
def allinone():
    all_data = db.load_database()
    allinone_list = []
    for product in all_data['products']:
        if product['category'] == 'allinone':
            allinone_list.append(product)

    return render_template('products.html', product=allinone_list)

@app.route('/products/masks')
def masks():
    all_data = db.load_database()
    masks_list = []
    for product in all_data['products']:
        if product['category'] == 'masks':
           masks_list.append(product)

    return render_template('products.html', product=masks_list)


@app.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form = login_form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        if username == "Rachel" and password == "blue":
            return f"<h1>Welcome Rachel! You've taken your next step to healthier and brighter looking skin!</h1>"
        else:
            return "<h1>Access Denied. Please enter the correct username and password.</h1>"
    else:
        return "<h1>Failed Validation. Please enter the correct username and password.</h1>"

if __name__ == "__main__":
    app.run()
