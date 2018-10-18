from backend.bus_tracker import BusTracker
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    bt = BusTracker()
    bt.update_buses()
    buses = [bus.to_dict() for bus in bt.get_buses()]
    return render_template('home.html', buses=buses)


if __name__ == '__main__':
    app.run(debug=True)
