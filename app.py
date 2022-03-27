from flask import Flask
form flask import url_for
app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    return 'Welcome to %s watchlist!'%name


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
