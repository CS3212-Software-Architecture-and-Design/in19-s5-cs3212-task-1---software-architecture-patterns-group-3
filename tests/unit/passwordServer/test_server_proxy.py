from unittest import TestCase
from broker_pattern.passwordServer.server_proxy import ServerCProxy
import json


class TestServerCProxy(TestCase):
    def test_handle_request(self):
        self.serverCProxy = ServerCProxy()

        # test1
        payload1 = {
            "method_name": "createPassword",
            "length": 10
        }
        result = json.loads(self.serverCProxy.handle_request(json.dumps(payload1)))
        self.assertTrue(len(result['data']) == 10)

