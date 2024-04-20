#!/usr/bin/python3

"""A script to start the flask web application"""


from flask import Flask

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


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")
