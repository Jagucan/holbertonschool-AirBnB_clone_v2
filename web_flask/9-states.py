#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a list of all State objects present in the DBStorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def states_cities(id):
    """Displays a list of all cities related to the specified state"""
    state = storage.get(State, id)
    if state is not None:
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state,
                               cities=sorted_cities)
    else:
        not_found = "Not found!"
        return render_template('9-states.html', message=not_found)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
