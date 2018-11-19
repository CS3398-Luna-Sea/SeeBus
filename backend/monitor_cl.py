from bus_tracker import BusTracker
import time


class DisplayCommandLine:

    __table_header    = "| Name | Route                           " \
                        "| Location      | Heading | Speed   | Last Stop                | Last Updated |"
    __table_separator = "|------|---------------------------------" \
                        "|---------------|---------|---------|--------------------------|--------------|"
    __stopped_character = u"\u25A0"

    def __init__(self):
        """
        Initializes a BusTracker object to update and display information.
        """
        self.__bt = BusTracker()

    def loop(self):
        """
        Continuously updates the buses, displays them in the command line, and delays the appropriate amount.
        """
        while True:
            self.__bt.update_buses()
            self.__display_buses()
            time.sleep(self.__bt.get_delay())

    def __display_buses(self):
        """
        Displays the buses in a neatly formatted table in the command line
        :param buses:
        :return:
        """
        print(DisplayCommandLine.__table_header)
        print(DisplayCommandLine.__table_separator)
        for bus in self.__bt.get_buses():
            print(self.bus_format_table(bus))
        print(DisplayCommandLine.__table_separator)
        print()

    @staticmethod
    def bus_format_table(bus):
        """
        Formats the fields of a Bus into a table format.
        :param bus: The Bus to format.
        :return: A string containing all the fields of a Bus in a table format.
        """
        name = bus.get_name()
        route_id = bus.get_route()
        route_str = bus.route_id_to_dict(route_id)['name']
        route_txst_id = str(bus.route_id_to_dict(route_id)['txst_id'])
        loc_lat = bus.get_location()[0]
        loc_lon = bus.get_location()[1]
        heading = bus.get_heading()
        heading_cardinal = bus.convert_heading(heading)
        speed_str = bus.validate_speed(bus.get_speed())
        stopped_char = DisplayCommandLine.__stopped_character if bus.is_stopped() else ' '
        last_stop_id = bus.get_last_stop()
        last_stop_str = bus.stop_id_to_dict(last_stop_id)['name']
        last_update = bus.get_last_update()
        time_since_last_update = bus.get_time_since_last_update(last_update)

        #       | Name   | Route        | Location         | Head   | Sped      | LStop        | LUpdated        |
        return "| {:>4s} | {:2s} {:28s} | {:2.2f}, {:2.2f} | {:>7s} | {:s} {:s} | {:24s} |   {:2d} sec ago |" \
            .format(name, route_txst_id, route_str, loc_lat, loc_lon, heading_cardinal, speed_str, stopped_char,
                    last_stop_str,
                    time_since_last_update
                    )


if __name__ == '__main__':
    dcl = DisplayCommandLine()
    dcl.loop()
