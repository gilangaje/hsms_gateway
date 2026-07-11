from hsms_gateway.gem.client import GemClient
from hsms_gateway.gateway import HsmsGateway
from hsms_gateway.mqtt.client import MqttClient

gem = GemClient(
    "192.168.0.10",
    5000,
)

mqtt = MqttClient(
    "localhost",
    1883,
)

gateway = HsmsGateway(
    gem,
    mqtt,
)

gateway.run(
    interval=1,
    svids=[
        1001,
        1002,
        1003,
    ],
)