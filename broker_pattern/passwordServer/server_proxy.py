from broker_pattern.passwordServer.server import Server
from broker_pattern.broker.service_provider_interface import ServiceProviderInterface
import json

class ServerCProxy(ServiceProviderInterface):
    def __init__(self) -> None:
        self.server = Server()
    
    def handle_request(self, payload) -> str:
        print("Request received", payload)
        
        # Deserialize payload
        payload = json.loads(payload)
        
        if payload["method_name"] == "createPassword":
            length = payload["length"]
            res = self.server.create_password(length)
            
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