import sys
from os import getcwd
sys.path.insert(0, getcwd() + '/backend')
from bus_tracker import BusTracker
from bus import Bus
from flask import Flask, render_template


app = Flask(__name__)
bt = BusTracker()


@app.route('/')
def index():
    """
    Serves the index page of the website.
    :return: The HTML for the index page.
    """
    return render_template('index.html')


@app.route('/buses')
def buses():
    """
    Serves a table containing realtime information about the buses.
    :return: The HTML for the bus table.
    """
    bt.update_buses()
    buses = [bus.to_dict() for bus in bt.get_buses_sorted(Bus.get_id)]
    return render_template('buses.html', buses=buses)


if __name__ == '__main__':
    app.run(debug=True)
