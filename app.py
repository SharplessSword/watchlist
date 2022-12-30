import os.path

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

name = '高敬儒'
movies = [
    {'title': '阿凡达2', 'year': '2022'},
]


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', name=name, movies=movies)


if __name__ == '__main__':
    app.run()
