from bus_tracker import BusTracker
import translate
from datetime import datetime
import json


class Saver:

    def __init__(self, start_hour, end_hour, departure_threshold=5):
        self.__bt = BusTracker()
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        self.__buses = {}
        self.__data = {}
        self.__departure_threshold = departure_threshold

    def loop(self):
        should_save = False
        try:
            while True:
                if self.__start_hour <= datetime.now().hour < self.__end_hour:
                    self.__data = {
                        "date": str(datetime.now().date()),
                        "buses": {}
                    }
                while self.__start_hour <= datetime.now().hour < self.__end_hour:
                    self.__update_data()
                    should_save = True
                if should_save:
                    self.__save()
        except KeyboardInterrupt:
            print("\nStopping... Saving data...")
            self.__save()
            print("Done.")
            quit(0)

    def __update_data(self):
        self.__bt.update_buses()

        for bus in self.__bt.get_buses():
            id = bus.get_id()

            # if bus doesn't have a list, make one
            if id not in self.__buses:
                self.__buses[id] = {
                    'stop': None,
                    'speed': None
                }
                self.__data["buses"][id] = []

            curr_stop = bus.get_last_stop()
            prev_stop = self.__buses[id]['stop']

            # If new stop
            if bus.is_stopped() and curr_stop != prev_stop:
                try:
                    print('{}, {} on {} arrived at {}'.format(datetime.now().time(), id, translate.route_id_dict[bus.get_route()]['name'],
                                                                 translate.stop_id_dict[curr_stop]['name']))
                except KeyError:
                    pass
                # Add timestamp to data
                self.__data["buses"][id].append({
                    'route': bus.get_route(),
                    'stop': curr_stop,
                    'arrival time': datetime.now().timestamp()
                })

                # Update current stop
                self.__buses[id]['stop'] = curr_stop

                # Set stop flag, watch for speed to go above threshold signalling departure
                self.__buses[id]['stop flag'] = True

            # If bus was stopped and bus is moving now -> departure
            if self.__buses[id]['stop flag'] and bus.get_speed() > self.__departure_threshold:
                self.__data["buses"][id][-1]['departure time'] = datetime.now().timestamp()
                try:
                    print('{}, {} on {} leaving {}'.format(datetime.now().time(), id, translate.route_id_dict[bus.get_route()]['name'],
                                                                 translate.stop_id_dict[curr_stop]['name']))
                except KeyError:
                    pass
                self.__buses[id]['stop flag'] = False

    def __save(self):
        filename = 'bus_data/data{}.json'.format(datetime.now().timestamp())
        with open(filename, 'w+') as f:
            f.write(json.dumps(self.__data, indent=2))
        print(filename)


if __name__ == '__main__':
    s = Saver(7, 22)
    s.loop()
