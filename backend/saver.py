from backend.bus_tracker import BusTracker
from datetime import datetime
import json


class Saver:

    def __init__(self, start_hour, end_hour):
        self.__bt = BusTracker()
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        self.__buses = {}
        self.__data = {
            "date": str(datetime.now().date()),
            "buses": {}
        }

    def loop(self):
        try:
            while self.__start_hour <= datetime.now().hour < self.__end_hour:
                self.__update_data()
        except KeyboardInterrupt:
            pass
        self.__after()
        quit()

    def __update_data(self):
        self.__bt.update_buses()

        for bus in self.__bt.get_buses():
            id = bus.get_id()

            # if bus doesn't have a list, make one
            if id not in self.__buses:
                self.__buses[id] = -1
                self.__data["buses"][id] = []

            curr_stop = bus.get_last_stop()
            prev_stop = self.__buses[bus.get_id()]

            # if stops not same, update data
            if curr_stop != prev_stop:
                self.__data["buses"][id].append({
                    'route': bus.get_route(),
                    'stop': curr_stop,
                    'arrival time': datetime.now().timestamp()
                })
                self.__buses[id] = curr_stop

    def __after(self):
        with open('data.json', 'w+') as f:
            f.write(json.dumps(self.__data, indent=2))


if __name__ == '__main__':
    s = Saver(7, 20)
    s.loop()
