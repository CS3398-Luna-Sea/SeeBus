import poll_api as api
import Bus
import time
import pprint
from geopy.distance import geodesic


class BusTracker:

    def __init__(self, delay=3):
        self.__buses = []
        self.__prev = []
        self.__delay = delay

    def update_buses(self):
        self.__prev = self.__buses
        self.__buses = []
        bus_dict = api.get_buses()
        for bus in bus_dict:
            id = bus['id']
            name = bus['name']
            route = bus['route']
            location = (bus['lat'], bus['lon'])
            heading = bus['heading']
            speed = -1
            last_stop = bus['lastStop']
            last_update = bus['lastUpdate']
            b = Bus.Bus(id, name=name, route=route, location=location, heading=heading, speed=speed,
                        last_stop=last_stop, last_update=last_update)
            self.__buses.append(b)
        self.__buses.sort(key=lambda x: x.get_id())

    def loop(self):
        while True:
            self.update_buses()
            pprint.pprint(self.__buses)
            print(len(self.__buses))
            time.sleep(self.__delay)

    def calculate_speeds(self):
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
        return self.__buses


if __name__ == '__main__':
    bt = BusTracker()
    bt.loop()
