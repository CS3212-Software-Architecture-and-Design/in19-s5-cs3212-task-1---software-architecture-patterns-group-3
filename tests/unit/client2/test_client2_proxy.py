from unittest import TestCase
from broker_pattern.client2.client2_proxy import Client2Proxy


class TestClient2Proxy(TestCase):
    def test_get_char_count(self):
        client_proxy = Client2Proxy()
        self.assertEqual(len(client_proxy.create_password(5)), 5)
        self.assertEqual(len(client_proxy.create_password(0)), 0)
        self.assertEqual(type(client_proxy.create_password(10)), str)

        with self.assertRaises(TypeError):
            client_proxy.create_password('1234')
            client_proxy.create_password(True)
            client_proxy.create_password(1.234)

    def test_convert_to_upper_case(self):
        client_proxy = Client2Proxy()
        self.assertEqual(client_proxy.convert_to_upper_case('foo'), 'FOO')
        self.assertEqual(client_proxy.convert_to_upper_case(''), '')
        self.assertEqual(client_proxy.convert_to_upper_case('1234'), '1234')

        with self.assertRaises(AttributeError):
            client_proxy.convert_to_upper_case(1234)
            client_proxy.convert_to_upper_case(True)
            client_proxy.convert_to_upper_case(1.234)

    def test_create_password(self):
        client_proxy = Client2Proxy()
        self.assertEqual(client_proxy.get_char_count('foo'), 3)
        self.assertEqual(client_proxy.get_char_count(''), 0)
        self.assertEqual(client_proxy.get_char_count('1@34'), 4)

        with self.assertRaises(TypeError):
            client_proxy.get_char_count(1234)
            client_proxy.get_char_count(True)
            client_proxy.get_char_count(1.234)