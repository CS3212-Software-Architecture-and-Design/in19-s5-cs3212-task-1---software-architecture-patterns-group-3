from unittest import TestCase
from broker_pattern.strServer.server import Server as Server2


class TestStrServer(TestCase):
    def test_convert_to_upper_case(self):
        str_server = Server2()
        self.assertEqual(str_server.convert_to_upper_case('abc'), "ABC")
        self.assertEqual(str_server.convert_to_upper_case('aBc'), "ABC")
        self.assertEqual(str_server.convert_to_upper_case('ABC'), "ABC")

    def test_get_char_count(self):
        str_server = Server2()
        self.assertEqual(str_server.get_char_count('abc'), 3)
        self.assertEqual(str_server.get_char_count('abcdef'), 6)
        self.assertEqual(str_server.get_char_count('123456789'), 9)
