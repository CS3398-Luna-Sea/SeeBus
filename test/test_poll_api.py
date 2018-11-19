from unittest import TestCase
import sys
from os import getcwd
sys.path.insert(0, getcwd() + '/backend')
import poll_api as api


class TestPollAPI(TestCase):

    def test_get_buses(self):
        self.assertTrue(isinstance(api.get_buses(), list),
                        "poll_api.get_buses() should return a dictionary")

    def test_get_buses_on_route(self):
        route = 624
        buses = api.get_buses_on_route(route)
        for bus in buses:
            if bus.get_route() != route:
                self.fail("Bus route {} does not match queried route {}".format(bus.get_route(), route))

        self.assertTrue(isinstance(api.get_buses_on_route(0), list),
                        "poll_api.get_buses_on_route(int) should return a dictionary")
