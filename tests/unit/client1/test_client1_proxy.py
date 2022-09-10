from unittest import TestCase
from broker_pattern.client1.client1_proxy import Client1Proxy


class TestClient1Proxy(TestCase):
    def test_add_two_integers(self):
        client_proxy = Client1Proxy()
        self.assertEqual(client_proxy.add_two_integers(1, 3), 4)
        self.assertEqual(client_proxy.add_two_integers(0, 0), 0)
        self.assertEqual(client_proxy.add_two_integers(-10, 10), 0)
        self.assertEqual(client_proxy.add_two_integers(-10, -10), -20)

        with self.assertRaises(TypeError):
            client_proxy.add_two_integers(1234)
            client_proxy.add_two_integers('1234')

        # TODO
        # with self.assertRaises(AttributeError):
        #     self.assertEqual(client_proxy.add_two_integers(1.5, 1.5), 3)
        #     client_proxy.add_two_integers('1234', 'abc')
        #     client_proxy.add_two_integers(1234, True)

    def test_find_maximum_element(self):
        client_proxy = Client1Proxy()
        self.assertEqual(client_proxy.find_maximum_element([1, 2, 3]), 3)
        self.assertEqual(client_proxy.find_maximum_element([-1, -2, 0]), 0)
        self.assertEqual(client_proxy.find_maximum_element([-1, -2, -10]), -1)

        with self.assertRaises(TypeError):
            client_proxy.find_maximum_element(['a', 1, 10])
            client_proxy.find_maximum_element(1234)
            client_proxy.find_maximum_element(True)
            client_proxy.find_maximum_element(1.234)

        with self.assertRaises(ValueError):
            client_proxy.find_maximum_element([])