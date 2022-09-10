from broker_pattern.broker.broker import Broker
from broker_pattern.statServer.server_proxy import ServerAProxy
from broker_pattern.passwordServer.server_proxy import ServerCProxy
from broker_pattern.strServer.server_proxy import ServerBProxy

brokerObj = Broker()
# Register Services
brokerObj.register_service("StatService", ServerAProxy())
brokerObj.register_service("StringService", ServerBProxy())
brokerObj.register_service("PasswordService", ServerCProxy())


def get_broker():
    return brokerObj
