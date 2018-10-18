from flask import Flask, render_template
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    t = str(datetime.datetime.now())
    return str(t)


if __name__ == '__main__':
    app.run(debug=True)
