from flask import Flask
import pizza
from flask import request

#Create Flask App
app = Flask(__name__)

#Routes
@app.route('/')
def hello_world():
    return 'Hello, Jon'

@app.route('/home', defaults={'name': 'Stranger'} )
@app.route('/home/<string:name>')
def home(name):
    html = f"<h1 style='color: red;'>Welcome {name}</h1>"
    return html


@app.route('/pizza/<int:size>/<string:top1>/<string:top2>')
def pizza1(size, top1, top2):
    return pizza.make_pizza(size, top1, top2)


@app.route('/custompizza/<path:args>')
def order_custom_pizza(args):
    args = args.split('/')
    return pizza.make_pizza(args[0], *args[1:])


@app.route('/getpizza', methods=['GET'])
# /getpizza?size=10&topping1=olives ... etc
def get_pizza():
    size = request.args.get("size")
    topping1 = request.args.get("topping1")
    topping2 = request.args.get("topping2")
    topping3 = request.args.get("topping3")
    return pizza.make_pizza(size, topping1, topping2, topping3)



@app.route('/menu', defaults={'username': 'Stranger'} )
@app.route('/menu/<string:username>')
def menu(username):
    html = render_template('menu.html', name=username, items=["Streetcats"])
    return html


if __name__ == "__main__":
    app.run()


# #creates a flask app
# app = Flask(__name__)
#
# #routes, decorator. the / is our index.
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
# #how to map a url to a particular method, how to connect it.
# #this is a fx, and passing a paramter in it.
# @app.route('/home', defaults={'name', 'Stranger'})
# @app.route('/home/<string:name>') #can add a variable. here that is string
# def home(name):
#       html = f"<h1 style= 'color: red;'>Welcome {name}</h1>"
#       return html

# @app.route('/home')
# def home(name):
#     return """<h1 style="color:red;">Welcome Home</h1>
#             <p>This is a para</p>
#             <p>This is para2</p>"""


# @app.route('/pizza/'):
# def pizza1():
#     return pizza.make_pizza("32", "tomato", "olives", "cheese")

