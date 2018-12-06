import requests
import json
import copy


def get_buses():
    """
    Polls the DoubleMap API.
    :return: A list of dictionaries corresponding to the buses currently in service.
    """
    try:
        r = requests.get('http://txstate.doublemap.com/map/v2/buses')
        buses = json.loads(r.text)
        return buses
    except requests.exceptions.ConnectionError:
        pass
        return []


def get_stops():
    """ Returns a dict of stops indexed by id. """
    stops = {}
    stops_url = "https://txstate.doublemap.com/map/v2/stops"
    stops_response = requests.get(stops_url).json()
    # add each stop to the dict of stops
    for stop in stops_response:
        stop_info = copy.deepcopy(stop)
        stop_info.pop('id', None)
        stops[stop['id']] = stop_info

    return stops


def get_routes():
        """ Returns a dict of routes indexed by id. Only returns active routes """
        routes_dict = {}
        routes_url = "https://txstate.doublemap.com/map/v2/routes"
        routes_response = requests.get(routes_url).json()
        # add each route to the dict of routes
        for route in routes_response:
            route_info = copy.deepcopy(route)
            route_info.pop('id', None)
            routes_dict[route['id']] = route_info

        return routes_dict


def eta(stop_id, route_id):
        """ Get eta (in minutes) about a specific stop id and route_id. """
        etas_url = "https://txstate.doublemap.com/map/v2/eta?stop=" + str(stop_id)
        etas = requests.get(etas_url).json()['etas'][str(stop_id)]['etas']
        for eta in etas:
            if eta['route'] == int(route_id):
                return eta['avg']
        else:
            # if there is no eta information available
            print("No ETA information available.")
            return -1


def get_buses_on_route(route):
    """
    Polls the DoubleMap API and filters the results to buses only on a certain route.
    :param route: The DoubleMap integer route ID
    :return: A list of dictionaries corresponding to the buses currently in service on the specified route.
    """
    buses = get_buses()
    on_route = [bus for bus in buses if bus['route'] == route]
    return on_route


def select_location(stops):
    """ Prompt the user for a location and return the stop_id. """
    for stop_id, stop in stops.items():
        print("%s. %s" % (stop_id, stop['name']))
    try:
        stop_input = input()
    except NameError:
        pass

    return int(stop_input)


def find_route(routes, start, finish):
    """ Find which route the user should take. """
    possible_routes = set()
    for route_id, route in routes.items():
        if start in route['stops']:
            possible_routes.add(route_id)
        if finish in route['stops']:
            possible_routes.add(route_id)

    for route_id in list(possible_routes):
        if start in routes[route_id]['stops'] and \
                finish in routes[route_id]['stops']:
            return route_id
    else:
        print("No possible route.")
        return -1


if __name__ == "__main__":
    buses = get_buses()
    stops = get_stops()
    routes = get_routes()

    print("Please Choose a starting stop: ")
    start = select_location(stops)
    print("Please choose an ending location")
    end = select_location(stops)

    route = find_route(routes, start, end)
    bus_name = routes[route]['name']

    if route != -1:
        bus_arrive_time = eta(start, route)
        print("The %s bus will arrive in %s minute(s)." % (bus_name, bus_arrive_time))
    else:
        print("A single route cannot be taken.")
