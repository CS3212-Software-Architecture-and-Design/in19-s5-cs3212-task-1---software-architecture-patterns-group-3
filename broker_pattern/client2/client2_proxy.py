import json

from broker_pattern.broker.get_broker import get_broker


class Client2Proxy:
    def __init__(self) -> None:
        self.broker = get_broker()
    
    def get_char_count(self, string):
        # Serialize Payload
        payload = {
            "method_name": "getCharCount",
            "string": string
        }
        payload = json.dumps(payload)
        response = self.broker.request("StringService", payload)

        try:
            response = self._deserialize_reponse(response)
        except:
            raise Exception()

        return response["data"]

    def convert_to_upper_case(self, string):
        # Serialize Payload
        payload = {
            "method_name": "convertToUpperCase",
            "string": string
        }
        payload = json.dumps(payload)
        response = self.broker.request("StringService", payload)

        try:
            response = self._deserialize_reponse(response)
        except:
            raise Exception()

        return response["data"]

    def create_password(self, length):
        # Serialize Payload
        payload = {
            "method_name": "createPassword",
            "length": length
        }
        payload = json.dumps(payload)
        response = self.broker.request("PasswordService", payload)

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