from hsms_gateway.gateway import HsmsGateway
from hsms_gateway.gem.client import GemClient
from hsms_gateway.mqtt.client import MqttClient


def test_gateway():

    gem = GemClient(
        "127.0.0.1",
        5000,
    )

    mqtt = MqttClient(
        "localhost",
    )

    gateway = HsmsGateway(
        gem,
        mqtt,
    )

    assert gateway.gem is gem
    assert gateway.mqtt is mqtt