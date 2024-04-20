#!/usr/bin/python3

"""A script to start the flask web application"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """The home route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """The hbnb route"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """The c route"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python/")
def python_without_subpath():
    """The python route"""
    return "Python is cool"


@app.route("/python/<text>")
def python_is_cool(text):
    """The python route with text"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>")
def is_number(n):
    """The number route"""
    return f"{escape(n)} is a number"


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
