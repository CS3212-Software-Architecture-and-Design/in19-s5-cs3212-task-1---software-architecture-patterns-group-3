from broker_pattern.strServer.server import Server
from broker_pattern.broker.service_provider_interface import ServiceProviderInterface
import json


class ServerBProxy(ServiceProviderInterface):
    def __init__(self) -> None:
        self.server = Server()

    def handle_request(self, payload) -> str:
        print("Request received", payload)

        # Deserialize payload
        payload = json.loads(payload)

        if payload["method_name"] == "convertToUpperCase":
            string = payload["string"]
            res = self.server.convert_to_upper_case(string)

            response = {
                "status": "OK",
                "data": res
            }
            return json.dumps(response)
        elif payload["method_name"] == "getCharCount":
            string = payload["string"]
            res = self.server.get_char_count(string)

            response = {
                "status": "OK",
                "data": res
            }
            return json.dumps(response)
        else:
            response = {
                "status": "FAIL"
            }
            return json.dumps(response)
