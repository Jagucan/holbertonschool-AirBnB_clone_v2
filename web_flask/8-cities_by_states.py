#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models import storage
import os

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states():
    """Displays a list of all State objects present in the DBStorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = []
        for state in states:
            for city in state.cities:
                cities.append(city)
    else:
        cities = []
        for state in states:
            for city in state.cities():
                cities.append(city)

    sorted_cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=sorted_states, cities=sorted_cities)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the database session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
