from unittest import TestCase
import sys
from os import getcwd
sys.path.insert(0, getcwd() + '/backend')
from bus import Bus


class TestBus(TestCase):

    def test_route_id_to_dict_valid_route(self):
        self.assertTrue(isinstance(Bus.route_id_to_dict(639), dict),
                        "Bus.route_id_to_dict(int) should return a dictionary")

    def test_route_id_to_dict_invalid_route(self):
        self.assertTrue(isinstance(Bus.route_id_to_dict(-1), dict),
                        "Bus.route_id_to_dict(int) should return a dictionary")

    def test_convert_heading_stopped(self):
        self.assertTrue(Bus.convert_heading(0) == '',
                        "Bus.convert_heading(0) should return \'\' because the bus is stopped")

    def test_convert_heading_not_stopped(self):
        self.assertTrue(Bus.convert_heading(360) == 'N',
                        "Bus.convert_heading(360) should return \'N\'")

    def test_stop_id_to_dict_valid_stop(self):
        self.assertTrue(isinstance(Bus.stop_id_to_dict(22), dict),
                        "Bus.stop_id_to_dict(int) should return a dictionary")

    def test_stop_id_to_dict_invalid_stop(self):
        self.assertTrue(isinstance(Bus.stop_id_to_dict(-1), dict),
                        "Bus.stop_id_to_dict(int) should return a dictionary")

    def test_get_time_since_last_update(self):
        self.assertTrue(isinstance(Bus.get_time_since_last_update(1), int),
                        "Bus.get_time_since_last_update(int) should return an integer")

    def test_to_dict(self):
        bus = Bus(0, "name", 0, (0, 0), 0, 0, 0, 0)
        self.assertTrue(isinstance(bus.to_dict(), dict), "Bus.to_dict() should return a dictionary")
