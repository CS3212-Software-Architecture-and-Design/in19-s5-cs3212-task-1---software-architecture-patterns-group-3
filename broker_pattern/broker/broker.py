from broker_pattern.broker.service_provider_interface import ServiceProviderInterface


class Broker:

    def __init__(self):
        # Initialize Servers (service Providers)
        self._servers = {}

    def register_service(self, service_name, service_object: ServiceProviderInterface):
        if self._servers.get(service_name) is None:
            self._servers[service_name] = service_object
        else:
            print("Service already registered.")

    def request(self, service_name: str, payload: str):
        return self._on_request_receive(service_name, payload)

    def _on_request_receive(self, service_name, payload):
        # Get the Request from the Client

        if self._servers.get(service_name) is not None:
            # Service is available
            # Redirect the payload to server
            service_provider = self._servers.get(service_name)
            response = service_provider.handle_request(payload)
            return response
        else:
            # No such service is available
            print("No Such Service Available!")


