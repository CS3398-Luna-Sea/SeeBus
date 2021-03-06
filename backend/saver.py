from bus_tracker import BusTracker
import translate
from datetime import datetime
import pytz
import json
import pymongo
from datetime import date
import calendar

class Saver:

    def __init__(self, start_hour, end_hour, departure_threshold=5, timezone=pytz.timezone('US/Central')):
        self.__bt = BusTracker()
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        self.__buses = {}
        self.__data = {}
        self.__departure_threshold = departure_threshold
        self.__timezone = timezone

    def loop(self):
        """
        Constantly runs and saves a JSON file with bus data once each day.
        """
        should_save = False
        try:
            while True:
                now = datetime.now(self.__timezone)
                if self.__start_hour <= now.hour < self.__end_hour:
                    self.__data = {
                        "date": str(now.date()),
                        "buses": {}
                    }
                while self.__start_hour <= now.hour < self.__end_hour:
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
        """
        Updates the buses and the data collected regarding their arrival and departure times.
        """
        self.__bt.update_buses()

        for bus in self.__bt.get_buses():
            id = bus.get_id()
            id = str(id)

            # if bus doesn't have a list, make one
            if id not in self.__buses:
                self.__buses[id] = {
                    'stop': None,
                    'speed': None,
                    'stop flag': False
                }
                self.__data["buses"][id] = []

            curr_stop = bus.get_last_stop()
            prev_stop = self.__buses[id]['stop']

            # If new stop
            if bus.is_stopped() and curr_stop != prev_stop:
                try:
                    print('{} on {} arrived at {}'.format(id, translate.route_id_dict[bus.get_route()]['name'],
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
                    print('{} on {} leaving {}'.format(id, translate.route_id_dict[bus.get_route()]['name'],
                                                       translate.stop_id_dict[curr_stop]['name']))
                except KeyError:
                    pass
                self.__buses[id]['stop flag'] = False

    def __save(self):
        """
        Saves a JSON file with the bus data with a unique filename.
        """
        filename = 'backend/bus_data/data{}.json'.format(datetime.now().timestamp())
        with open(filename, 'w+') as f:
            f.write(json.dumps(self.__data, indent=2))
        print(filename)

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["November_27_BusDatabase"]

        my_date = date.today()
        mycol = mydb[calendar.day_name[my_date.weekday()] + "Collection"]
        mycol.insert_one(self.__data)
        print("Inserting a Bus List into :" + calendar.day_name[my_date.weekday()] + "Collection")

if __name__ == '__main__':
    s = Saver(7, 22)
    s.loop()

