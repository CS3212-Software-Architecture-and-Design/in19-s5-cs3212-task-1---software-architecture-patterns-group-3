import json
from unittest import TestCase
from broker_pattern.broker.get_broker import get_broker


class TestBroker(TestCase):

    def test__on_request_receive(self):
        self.broker = get_broker()

        # test1
        payload1 = {
            "method_name": "addTwoNumbers",
            "num1": 1,
            "num2": 2
        }
        result = json.loads(self.broker._on_request_receive("StatService", json.dumps(payload1)))
        self.assertEqual(result["data"], 3)

        # test2
        payload2 = {
            "method_name": "addTwo",
            "num1": 1,
            "num2": 2
        }
        result = self.broker._on_request_receive("StatService", json.dumps(payload2))
        self.assertEqual(result, None)

        # test5
        payload5 = {
            "method_name": "getCharCount",
            "string": 'Hello World',
        }
        result = json.loads(self.broker._on_request_receive("StringService", json.dumps(payload5)))
        self.assertEqual(result['data'], 11)

        # test6
        payload6 = {
            "method_name": "getCharCount",
            "string": ''
        }
        result = json.loads(self.broker._on_request_receive("StringService", json.dumps(payload6)))
        self.assertEqual(result['data'], 0)

        # test7
        payload7 = {
            "method_name": "convertToUpperCase",
            "string": 'Hello World'
        }
        result = json.loads(self.broker._on_request_receive("StringService", json.dumps(payload7)))
        self.assertEqual(result['data'], "HELLO WORLD")

        # test8
        payload8 = {
            "method_name": "createPassword",
            "length": 10
        }
        result = json.loads(self.broker._on_request_receive("PasswordService", json.dumps(payload8)))
        self.assertTrue(len(result['data']) == 10)

    def test_register_service(self):
        from broker_pattern.strServer.server_proxy import ServerBProxy
        self.broker = get_broker()
        self.broker.register_service('StringService', ServerBProxy())

        self.assertTrue('StringService' in self.broker._servers)
