from unittest import TestCase
from broker_pattern.strServer.server_proxy import ServerBProxy
import json


class TestServerBProxy(TestCase):

    def test_handle_request(self):
        self.serverBProxy = ServerBProxy()

        # test1
        payload1 = {
            "method_name": "getCharCount",
            "string": 'Hello World',
        }
        result = json.loads(self.serverBProxy.handle_request(json.dumps(payload1)))
        self.assertEqual(result['data'], 11)

        # test2
        payload2 = {
            "method_name": "getCharCount",
            "string": ''
        }
        result = json.loads(self.serverBProxy.handle_request(json.dumps(payload2)))
        self.assertEqual(result['data'], 0)

        # test3
        payload3 = {
            "method_name": "convertToUpperCase",
            "string": 'Hello World'
        }
        result = json.loads(self.serverBProxy.handle_request(json.dumps(payload3)))
        self.assertEqual(result['data'], "HELLO WORLD")

