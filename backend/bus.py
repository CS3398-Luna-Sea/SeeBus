import translate
import time


class Bus:

    def __init__(self, id, name, route, location, heading, speed, last_stop, last_update):
        """
        Creates a bus object initializing all fields.
        :param id: Integer ID of the bus.
        :param name: String name of the bus.
        :param route: Integer route of the bus.
        :param location: Location of the bus, tuple of float: latitude and longitude.
        :param heading: Integer heading of the bus.
        :param speed: Float speed of the bus in MPH.
        :param last_stop: Integer last stop of the bus.
        :param last_update: Unix timestamp of last time the bus was updated.
        """
        self.__id = id
        self.__name = name
        self.__route = route
        self.__location = location
        self.__heading = heading
        self.__speed = speed
        self.__last_stop = last_stop
        self.__last_update = last_update

    def get_id(self):
        """
        Gets the integer ID of the bus.
        :return: The ID of the bus.
        """
        return self.__id

    def get_name(self):
        """
        Gets the string name of the bus.
        :return: The name of the bus.
        """
        return self.__name

    def get_route(self):
        """
        Gets the integer route of the bus.
        :return: The route of the bus.
        """
        return self.__route

    @staticmethod
    def route_id_to_dict(route_id):
        """
        Converts a route id to a dictionary containing information about it.
        :param route_id: The ID of the route from the DoubleMap API.
        :return: A dictionary containing information about the route ID.
        """
        try:
            return translate.route_id_dict[route_id]
        except KeyError:
            with open('missing.txt', 'w+') as f:
                f.write('Missing route'.format(route_id))
            return {
                'txst id': '',
                'type': '',
                'name': ''
            }

    def get_location(self):
        """
        Gets the location of the bus, tuple of floats.
        :return: The location of the bus.
        """
        return self.__location

    def get_heading(self):
        """
        Gets the integer heading of the bus.
        :return: The heading of the bus.
        """
        return self.__heading

    @staticmethod
    def get_heading_cardinal(heading):
        """
        Converts the integer heading (0-360) to a cardinal direction (N, NE, E, SE, etc).
        :param heading: The integer heading of a bus, 0-360 degrees.
        :return: The cardinal direction the bus is driving.
        """
        a = heading
        if a == 0:
            return ''
        elif 22.5 < a <= 67.5:
            return 'NE'
        elif 67.5 < a <= 112.5:
            return 'E'
        elif 112.5 < a <= 157.5:
            return 'SE'
        elif 157.5 < a <= 202.5:
            return 'S'
        elif 202.5 < a <= 247.5:
            return 'SW'
        elif 247.5 < a <= 292.5:
            return 'W'
        elif 292.5 < a <= 337.5:
            return 'NW'
        elif 337.5 < a < 360 or 0 < a <= 22.5:
            return 'N'

    def set_speed(self, speed):
        """
        Sets the speed of the bus.
        :param speed: The speed in MPH.
        """
        self.__speed = speed

    def get_speed(self):
        """
        Gets the float speed of the bus.
        :return: The speed of the bus.
        """
        return self.__speed

    def is_stopped(self):
        """
        Sees if the bus is currently not moving.
        :return: True if the bus is stopped, false otherwise.
        """
        return self.__heading == 0 or self.__speed < 0.5

    @staticmethod
    def validate_speed(speed):
        """
        Checks the speed of a bus and returns an alternate value if it doesn't make sense.
        :param speed: The speed to validate.
        :return: A validated speed integer.
        """
        if speed != -1 and abs(speed) < 100:
            return '{: >5d}'.format(int(speed))
        else:
            return '     '

    def get_last_stop(self):
        """
        Gets the integer last stop of the bus.
        :return: The last stop of the bus.
        """
        return self.__last_stop

    @staticmethod
    def stop_id_to_dict(stop_id):
        """
        Converts a stop id to a dictionary containing information about it.
        :param stop_id: The ID of the stop from the DoubleMap API.
        :return: A dictionary containing information about the stop ID.
        """
        try:
            return translate.stop_id_dict[stop_id]
        except KeyError:
            with open('missing.txt', 'w+') as f:
                f.write('Missing stop {}'.format(stop_id))
            return {
                'name': ''
            }

    def get_last_update(self):
        """
        Gets the unix timestamp corresponding to when the bus was last updated in the API.
        :return: The last time the bus was updated.
        """
        return self.__last_update

    @staticmethod
    def get_time_since_last_update(timestamp):
        """
        Converts a unix timestamp to time since last update by getting the difference from the current time.
        :param timestamp: A unix timestamp corresponding to the last time a bus was updated.
        :return: The number of seconds since timestamp.
        """
        return int(time.time() - timestamp)

    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'route_id': self.__route,
            'route_dict': Bus.route_id_to_dict(self.__route),
            'location': self.__location,
            'latitude': self.__location[0],
            'longitude': self.__location[1],
            'heading': self.__heading,
            'heading_cardinal': Bus.get_heading_cardinal(self.__heading),
            'speed': self.__speed,
            'validated_speed': Bus.validate_speed(self.__speed),
            'last_stop': self.__last_stop,
            'last_stop_dict': Bus.stop_id_to_dict(self.__last_stop),
            'last_update': self.__last_update,
            'time_since_last_update': Bus.get_time_since_last_update(self.__last_update)
        }

    def __repr__(self):
        """
        Converts a Bus object to a string.
        :return: A string containing all fields of the bus in a formatted manner.
        """
        return "{{\n" \
               "  ID:          {}\n" \
               "  Name:        {}\n" \
               "  Route:       {}\n" \
               "  Location:    {}, {}\n" \
               "  Heading:     {}\n" \
               "  Speed:       {}\n" \
               "  Last Stop:   {}\n" \
               "  Last Update: {}\n" \
               " }}".format(
                        self.__id, self.__name, self.__route, self.__location[0], self.__location[1],
                        self.__heading, self.__speed, self.__last_stop, self.__last_update
        )
