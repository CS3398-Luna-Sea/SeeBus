import BusTracker
import time


class DisplayCommandLine:

    __table_header    = "| ID  | Route | Location      | Heading | Speed | Last Stop | Last Update |"
    __table_separator = "|-----|-------|---------------|---------|-------|-----------|-------------|"

    def __init__(self):
        self.__bt = BusTracker.BusTracker()

    def loop(self):
        while True:
            self.__bt.update_buses()
            self.__bt.calculate_speeds()
            DisplayCommandLine.__display_buses(self.__bt.get_buses())

    @staticmethod
    def bus_format_table(bus):
        speed_str = ('{: >5.2f}'.format(bus.get_speed()) if bus.get_speed() != -1 else '     ')
        return "| {:3d} | {:5d} | {:2.2f}, {:2.2f} | {:>2s}  {:3d} | {:s} | {:9d} | {:11d} |".format(
            bus.get_id(), bus.get_route(), bus.get_location()[0], bus.get_location()[1], bus.get_heading_cardinal(),
            bus.get_heading(), speed_str, bus.get_last_stop(), bus.get_last_update()
        )

    @staticmethod
    def __display_buses(buses):
        print(DisplayCommandLine.__table_header)
        print(DisplayCommandLine.__table_separator)
        for bus in buses:
            print(DisplayCommandLine.bus_format_table(bus))
        print(DisplayCommandLine.__table_separator)
        print()
        time.sleep(3)


if __name__ == '__main__':
    dcl = DisplayCommandLine()
    dcl.loop()
