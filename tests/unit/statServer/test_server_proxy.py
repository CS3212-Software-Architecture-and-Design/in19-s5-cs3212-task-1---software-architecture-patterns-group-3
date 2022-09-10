from unittest import TestCase
from broker_pattern.statServer.server_proxy import ServerAProxy
import json


class TestServerAProxy(TestCase):
    def test_handle_request(self):
        self.serverAProxy = ServerAProxy()

        # test1
        payload1 = {
            "method_name": "addTwoNumbers",
            "num1": 1,
            "num2": 2
        }
        result = json.loads(self.serverAProxy.handle_request(json.dumps(payload1)))
        self.assertEqual(result["data"], 3)

        # test2
        payload2 = {
            "method_name": "addTwo",
            "num1": 1,
            "num2": 2
        }
        result = self.serverAProxy.handle_request(json.dumps(payload2))
        self.assertEqual(result, None)

        # test3
        payload3 = {
            "method_name": "findMaximumElement",
            "numbers": [1, 2, 3, 4, 5]
        }
        result = json.loads(self.serverAProxy.handle_request(json.dumps(payload3)))
        self.assertEqual(result["data"], 5)
