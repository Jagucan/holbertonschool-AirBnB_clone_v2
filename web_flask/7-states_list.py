#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    from models import storage

    """Displays a list of all State objects present in the DBStorage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    from models import storage
    """ Closes the database session """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
