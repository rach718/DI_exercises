from flask import Flask
import datetime


app = Flask(__name__)

@app.route('/time')
def count_down():
    present = datetime.datetime.now()
    newyears = datetime.datetime(2021, 1, 1, 1, 1)
    difference = newyears-present
    return f"the countdown to new years is {difference}"

if __name__ == "__main__":
    app.run()


