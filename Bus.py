class Bus:

    def __init__(self, id, name=None, route=None, location=None, heading=None, speed=None,
                 last_stop=None, last_update=None):
        self.__id = id
        self.__name = name
        self.__route = route
        self.__location = location
        self.__heading = heading
        self.__speed = speed
        self.__last_stop = last_stop
        self.__last_update = last_update

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_route(self, route):
        self.__route = route

    def get_route(self):
        return self.__route

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def set_heading(self, heading):
        self.__heading = heading

    def get_heading(self):
        return self.__heading

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_last_stop(self, last_stop):
        self.__last_stop = last_stop

    def get_last_stop(self):
        return self.__last_stop

    def set_last_update(self, last_update):
        self.__last_update = last_update

    def get_last_update(self):
        return self.__last_update

    def __repr__(self):
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
