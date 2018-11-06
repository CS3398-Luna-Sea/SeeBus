import sys
from os import getcwd
sys.path.insert(0, getcwd() + '/backend')
import poll_api as api
from bus import Bus
import time
import pprint
from geopy.distance import geodesic
import re


class BusTracker:

    def __init__(self, delay=3):
        """
        Creates a BusTracker object initializing all fields.
        :param delay: The time between polling the API.
        """
        self.__buses = []
        self.__prev = []
        self.__delay = delay

    def update_buses(self):
        """
        Polls the API and creates and adds Bus objects to the current bus list. Puts the buses in the current list to
        the previous bus list. Then sorts the current list by Bus ID.
        """
        self.__prev = self.__buses
        self.__buses = []
        raw_bus_list = api.get_buses()

        # raw_bus_list = api.get_buses_on_route(633)

        for raw_bus in raw_bus_list:
            id = raw_bus['id']
            name = raw_bus['name']
            route = raw_bus['route']
            location = (raw_bus['lat'], raw_bus['lon'])
            heading = raw_bus['heading']
            speed = -1

            last_stop = raw_bus['lastStop']
            last_update = raw_bus['lastUpdate']

            b = Bus(id, name=name, route=route, location=location, heading=heading, speed=speed,
                        last_stop=last_stop, last_update=last_update)
            self.__buses.append(b)

        self.__buses.sort(key=lambda x: x.get_id())
        self.calculate_speeds()

    def loop(self):
        """
        Continuously updated the buses, prints them and how many there are, then delays before looping again.
        """
        while True:
            self.update_buses()
            pprint.pprint(self.__buses)
            print(len(self.__buses))
            time.sleep(self.__delay)

    def calculate_speeds(self):
        """
        Updated the speeds of all buses based on their change in distance/time.
        """
        for i, (prev, curr) in enumerate(list(zip(self.__prev, self.__buses))):

            prev_location = (prev.get_location()[0], prev.get_location()[1])
            curr_location = (curr.get_location()[0], curr.get_location()[1])
            prev_time = prev.get_last_update()
            curr_time = curr.get_last_update()

            delta_d = geodesic(prev_location, curr_location).miles
            delta_t = curr_time - prev_time
            if delta_t != 0:
                speed = (delta_d / delta_t) * 60 * 60
                self.__buses[i].set_speed(speed)
            else:
                self.__buses[i].set_speed(self.__prev[i].get_speed())

    def get_buses(self):
        """
        Returns the current list of buses.
        :return: The current list of buses.
        """
        return self.__buses

    def get_buses_sorted(self, f):
        """
        Returns the current list of buses sorted by a 'get_' function in Bus.
        :param f: The attribute of Bus to sort by, passed as a function of the form get_buses_sorted(Bus.get_xxxx)
        :return: The sorted list of buses
        """
        m = re.match('<function Bus.(get_.*) at 0x[\w]*>', str(f))
        if m is None:
            raise TypeError("Must sort using a get_xxxx() method from Bus")
        else:
            f_str = m.group(1)

        return sorted(
            self.__buses,
            key=lambda bus: getattr(bus, f_str)()
        )

    def get_delay(self):
        return self.__delay


if __name__ == '__main__':
    bt = BusTracker()
    bt.loop()
