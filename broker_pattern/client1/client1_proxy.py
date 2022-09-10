from broker_pattern.broker.get_broker import get_broker
import json


class Client1Proxy:

    def __init__(self):
        self._broker = get_broker()

    def add_two_integers(self, num1, num2):
        # Serialize Payload
        payload = {
            "method_name": "addTwoNumbers",
            "num1": num1,
            "num2": num2
        }
        payload = json.dumps(payload)
        response = self._broker.request("StatService", payload)

        try:
            response = self._deserialize_reponse(response)
        except:
            raise Exception()

        return response["data"]

    def find_maximum_element(self, numbers):
        # Serialize Payload
        payload = {
            "method_name": "findMaximumElement",
            "numbers": numbers
        }
        payload = json.dumps(payload)
        response = self._broker.request("StatService", payload)

        try:
            response = self._deserialize_reponse(response)
        except:
            raise Exception()

        return response["data"]


    def _deserialize_reponse(self, response) -> dict:
        response = json.loads(response)
        if response["status"] == "Fail":
            raise Exception()
        else:
            return response
