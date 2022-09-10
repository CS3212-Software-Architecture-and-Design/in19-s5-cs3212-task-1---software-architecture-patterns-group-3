from unittest import TestCase
from broker_pattern.statServer.server import Server as Server1


class TestStatServer(TestCase):
    def test_add_two_numbers(self):
        stat_server = Server1()
        self.assertEqual(stat_server.add_two_numbers(2, 4), 6)
        self.assertEqual(stat_server.add_two_numbers(0, 10), 10)
        self.assertEqual(stat_server.add_two_numbers(-2, 4), 2)
        with self.assertRaises(Exception):
            stat_server.add_two_numbers(3, 'ad')

    def test_find_maximum_element(self):
        stat_server = Server1()
        self.assertEqual(stat_server.find_maximum_element([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(stat_server.find_maximum_element([1, -2, -3, -4, 0]), 1)
        self.assertEqual(stat_server.find_maximum_element([-1, 12, 3, 4, -5]), 12)
