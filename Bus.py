class Bus:

    def __init__(self, id, name='', route=-1, location=(), heading=-1, speed=-1, last_stop=-1, last_update=-1):
        self.id = id
        self.name = name
        self.route = route
        self.location = location
        self.heading = heading
        self.speed = speed
        self.last_stop = last_stop
        self.last_update = last_update

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_route(self, route):
        self.route = route

    def get_route(self):
        return self.route

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_heading(self, heading):
        self.heading = heading

    def get_heading(self):
        return self.heading

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_last_stop(self, last_stop):
        self.last_stop = last_stop

    def get_last_stop(self):
        return self.last_stop

    def set_last_update(self, last_update):
        self.last_update = last_update

    def get_last_update(self):
        return self.last_update
