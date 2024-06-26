#!/usr/bin/python3
"""web flask module"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """display C followed by varibale text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """display C followed by varibale text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
