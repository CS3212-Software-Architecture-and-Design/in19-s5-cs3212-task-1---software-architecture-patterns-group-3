from unittest import TestCase
from broker_pattern.passwordServer.server import Server as Server3


class TestPasswordServer(TestCase):

    def test_create_password(self):
        password_server = Server3()
        self.assertEqual(len(password_server.create_password(7)), 7)
        self.assertEqual(len(password_server.create_password(10)), 10)
        self.assertEqual(len(password_server.create_password(3)), 3)
