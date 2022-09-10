from broker_pattern.broker.service_provider_interface import ServiceProviderInterface
from broker_pattern.statServer.server import Server
import json


class ServerAProxy(ServiceProviderInterface):

    def __init__(self) -> None:
        self._server = Server()

    def send_fail_response(self):
        response = {
            "status": "FAIL"
        }
        return json.dumps(response)

    def handle_request(self, payload) -> str:
        print("Request received", payload)

        # Deserialize payload
        payload = json.loads(payload)

        if payload["method_name"] is None:
            return "Error"
        elif payload["method_name"] == "addTwoNumbers":
            num1 = payload["num1"]
            num2 = payload["num2"]
            try:
                res = self._server.add_two_numbers(num1, num2)
                response = {
                    "status": "OK",
                    "data": res
                }
                return json.dumps(response)
            except Exception:
                self.send_fail_response()

        elif payload["method_name"] == "findMaximumElement":
            number_list = payload["numbers"]
            res = self._server.find_maximum_element(number_list)

            response = {
                "status": "OK",
                "data": res
            }
            return json.dumps(response)
        else:
            response = {
                "status": "FAIL"
            }
