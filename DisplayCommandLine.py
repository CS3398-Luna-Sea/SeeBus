import BusTracker
import time


class DisplayCommandLine:

    __table_header    = "| Name | Route                | Location      | Heading | Speed   | Last Stop | Last Update |"
    __table_separator = "|------|----------------------|---------------|---------|---------|-----------|-------------|"
    __stopped_character = u"\u25A0"
    route_id_dict = {
        633: {
            'txst id': 10,
            'type': 'On Campus',
            'name': 'Bobcat Stadium'
        },
        634: {
            'txst id': 12,
            'type': 'On Campus',
            'name': 'Bobcat Village'
        },
        635: {
            'txst id': 14,
            'type': 'On Campus',
            'name': 'Campus Loop'
        },
        636: {
            'txst id': 20,
            'type': 'Off Campus',
            'name': 'Aquarena Springs'
        },
        637: {
            'txst id': 21,
            'type': 'Off Campus',
            'name': 'Blanco River',
        },
        638: {
            'txst id': 22,
            'type': 'Off Campus',
            'name': 'Mill Street'
        },
        639: {
            'txst id': 23,
            'type': 'Off Campus',
            'name': 'Post Road'
        },
        640: {
            'txst id': 24,
            'type': 'Off Campus',
            'name': 'Craddock'
        },
        641: {
            'txst id': 25,
            'type': 'Off Campus',
            'name': 'Ranch Road'
        },
        642: {
            'txst id': 26,
            'type': 'Off Campus',
            'name': 'Wonder World'
        },
        643: {
            'txst id': 28,
            'type': 'Special',
            'name': 'Holland'
        },
        621: {
            'txst id': 30,
            'type': 'Special',
            'name': 'Pathways'
        }
    }

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
        #       | Name   | Route  | Location         | Head   | Sped      | LStop | LUpdat |
        return "| {:>4s} | {:20s} | {:2.2f}, {:2.2f} | {:>7s} | {:s} {:s} | {:9d} | {:11d} |".format(
            bus.get_name(),
            DisplayCommandLine.route_id_dict[bus.get_route()]['name'],
            bus.get_location()[0], bus.get_location()[1],
            bus.get_heading_cardinal(),
            speed_str,
            DisplayCommandLine.__stopped_character if bus.is_stopped() else ' ',
            bus.get_last_stop(),
            bus.get_last_update()
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
