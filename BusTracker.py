import poll_api as api
import Bus
import time
import pprint


class BusTracker:

    def __init__(self, delay=3):
        self.__buses = []
        self.__delay = delay

    def update_buses(self):
        self.__buses = []
        bus_dict = api.get_buses()
        for bus in bus_dict:
            id = bus['id']
            name = bus['name']
            route = bus['route']
            location = (bus['lat'], bus['lon'])
            heading = bus['heading']
            last_stop = bus['lastStop']
            last_update = bus['lastUpdate']
            b = Bus.Bus(id, name=name, route=route, location=location, heading=heading,
                        last_stop=last_stop, last_update=last_update)
            self.__buses.append(b)

    def loop(self):
        while True:
            self.update_buses()
            pprint.pprint(self.__buses)
            print(len(self.__buses))
            time.sleep(self.__delay)

    def get_buses(self):
        return self.__buses


if __name__ == '__main__':
    bt = BusTracker()
    bt.loop()
