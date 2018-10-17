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

    def get_heading_cardinal(self):
        """
        Converts the integer heading (0-360) to a cardinal direction (N, NE, E, SE, etc).
        :return: The cardinal direction the bus is driving.
        """
        a = self.get_heading()
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

    def get_last_stop(self):
        """
        Gets the integer last stop of the bus.
        :return: The last stop of the bus.
        """
        return self.__last_stop

    def get_last_update(self):
        """
        Gets the unix timestamp corresponding to when the bus was last updated in the API.
        :return: The last time the bus was updated.
        """
        return self.__last_update

    def get_time_since_last_update(self):
        """
        Converts the last_update field to time since last update by getting the difference from the current time.
        :return: The number of seconds since the bus was last updated.
        """
        return int(time.time() - self.__last_update)

    def is_stopped(self):
        """
        Sees if the bus is currently not moving.
        :return: True if the bus is stopped, false otherwise.
        """
        return self.__heading == 0 or self.__speed < 0.5

    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'route': self.__route,
            'location': self.__location,
            'heading': self.__heading,
            'speed': self.__speed,
            'last_stop': self.__last_stop,
            'last_update': self.__last_update
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
