import BusTracker
import translate
import time


class DisplayCommandLine:

    __table_header    = "| Name | Route                           | Location      | Heading | Speed   | Last Stop                | Last Updated |"
    __table_separator = "|------|---------------------------------|---------------|---------|---------|--------------------------|--------------|"
    __stopped_character = u"\u25A0"

    def __init__(self):
        self.__bt = BusTracker.BusTracker()

    def loop(self):
        while True:
            self.__bt.update_buses()
            self.__bt.calculate_speeds()
            self.__display_buses(self.__bt.get_buses())

    def __display_buses(self, buses):
        print(DisplayCommandLine.__table_header)
        print(DisplayCommandLine.__table_separator)
        for bus in buses:
            print(self.bus_format_table(bus))
        print(DisplayCommandLine.__table_separator)
        print()
        time.sleep(3)

    @staticmethod
    def bus_format_table(bus):
        name = bus.get_name()
        route_id = bus.get_route()
        try:
            route_str = translate.route_id_dict[route_id]['name']
            route_txst_id = translate.route_id_dict[route_id]['txst id']
        except KeyError:
            route_str = ''
            route_txst_id = 0
            print('Missing route {}'.format(route_id))
        loc_lat = bus.get_location()[0]
        loc_lon = bus.get_location()[1]
        heading = bus.get_heading()
        heading_cardinal = bus.get_heading_cardinal()
        speed_str = ('{: >5.2f}'.format(bus.get_speed())
                     if (bus.get_speed() != -1 and abs(bus.get_speed()) < 100) else '     ')
        stopped_char = DisplayCommandLine.__stopped_character if bus.is_stopped() else ' '
        last_stop_id = bus.get_last_stop()
        try:
            last_stop_str = translate.stop_id_dict[last_stop_id]['name']
        except KeyError:
            last_stop_str = ''
            with open('missing_stops.txt', 'w+') as f:
                f.write('Missing stop {} on route {}'.format(last_stop_id, route_id))
        time_since_last_update = bus.get_time_since_last_update()

        #       | Name   | Route        | Location         | Head   | Sped      | LStop        | LUpdated        |
        return "| {:>4s} | {:2d} {:28s} | {:2.2f}, {:2.2f} | {:>7s} | {:s} {:s} | {:24s} |   {:2d} sec ago |" \
            .format(name, route_txst_id, route_str, loc_lat, loc_lon, heading_cardinal, speed_str, stopped_char,
                    last_stop_str, time_since_last_update
                    )




if __name__ == '__main__':
    dcl = DisplayCommandLine()
    dcl.loop()
