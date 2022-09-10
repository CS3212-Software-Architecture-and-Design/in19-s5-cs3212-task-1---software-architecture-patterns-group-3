from unittest import TestCase
from broker_pattern.client2.client2 import get_char_count, convert_to_upper_case, create_password


class TestClient1(TestCase):
    def test_get_char_count(self):
        self.assertEqual(get_char_count('Hello'), 5)
        self.assertEqual(get_char_count('Hello World'), 11)

    def test_convert_to_upper_case(self):
        self.assertEqual(convert_to_upper_case('Hello'), 'HELLO')
        self.assertEqual(convert_to_upper_case('Hello World'), 'HELLO WORLD')

    def test_create_password(self):
        self.assertEqual(len(create_password(10)), 10)
        self.assertEqual(len(create_password(5)), 5)