from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/get_films')
def get_films():

    return NotImplementedError


app.run(host='0.0.0.0', port=81)
