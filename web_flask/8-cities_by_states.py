#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models import storage
import os

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays a list of all State objects present in the DBStorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = {}
        for state in states:
            cities[state] = state.cities
    else:
        cities = {}
        for state in states:
            cities[state] = state.cities()

    return render_template('8-cities_by_states.html',
                           states=sorted_states,
                           cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the database session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
