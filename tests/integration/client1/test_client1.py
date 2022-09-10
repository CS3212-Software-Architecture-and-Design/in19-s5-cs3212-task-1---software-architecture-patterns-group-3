from unittest import TestCase
from broker_pattern.client1.client1 import add_two_integers, find_max_element


class TestClient1(TestCase):
    def test_add_two_integers(self):
        self.assertEqual(add_two_integers(3, 5), 8)
        self.assertEqual(add_two_integers(1, -1), 0)
        self.assertEqual(add_two_integers('ac', 'v'), "Invalid")

    def test_find_max_element(self):
        self.assertEqual(find_max_element([1, 2, 3]), 3)
        self.assertEqual(find_max_element([-1, 20, 3]), 20)
