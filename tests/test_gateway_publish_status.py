from hsms_gateway.gateway import HsmsGateway
from hsms_gateway.mqtt.client import MqttClient


class DummyGem:

    def read_status_variables(self, svids):

        return [
            "RUN",
            25,
        ]


def test_publish_status():

    gem = DummyGem()

    mqtt = MqttClient("localhost")
    mqtt.connect()

    gateway = HsmsGateway(
        gem,
        mqtt,
    )

    gateway.publish_status_variables(
        [1001, 1002],
    )

    assert mqtt.last_topic == "factory/status"
    assert mqtt.last_payload == {
        "1001": "RUN",
        "1002": 25,
    }