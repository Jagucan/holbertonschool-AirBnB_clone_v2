#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Handles the Route / to the Flask application """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Handles the Route /hbnb to the Flask application """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Handles the Route /c/<text> to the Flask application """
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
