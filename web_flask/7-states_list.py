#!/usr/bin/python3
""" Starts a Flask web application """
import os
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """Displays a list of all State objects present in the DBStorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ Closes the database session """
    storage.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
