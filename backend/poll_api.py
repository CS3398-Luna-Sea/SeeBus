import requests
import json
import pprint


def get_buses():
    """
    Polls the DoubleMap API.
    :return: A list of dictionaries corresponding to the buses currently in service.
    """
    r = requests.get('http://txstate.doublemap.com/map/v2/buses')
    buses = json.loads(r.text)
    return buses


def get_buses_on_route(route):
    """
    Polls the DoubleMap API and filters the results to buses only on a certain route.
    :param route: The DoubleMap integer route ID
    :return: A list of dictionaries corresponding to the buses currently in service on the specified route.
    """
    buses = get_buses()
    on_route = [bus for bus in buses if bus['route'] == route]
    return on_route


if __name__ == "__main__":
    buses = get_buses()
    # buses = get_buses_on_route(617)
    pprint.pprint(buses)
