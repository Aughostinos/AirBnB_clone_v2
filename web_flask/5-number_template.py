#!/usr/bin/python3
"""web flask module"""

from flask import Flask, render_template


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


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py_text(text):
    """display Python followed by varibale text"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    '''display n is a number if n is int'''
    return '{} is a number'.format(n)



@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number(n):
    '''display a HTML page only if n is an integer'''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
