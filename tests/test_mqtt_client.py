from hsms_gateway.mqtt.client import MqttClient


def test_client():

    client = MqttClient(
        host="localhost",
        port=1883,
    )

    assert client.host == "localhost"
    assert client.port == 1883

def test_connect():

    client = MqttClient("localhost")

    assert client.connected is False

    client.connect()

    assert client.connected is True

    client.disconnect()

    assert client.connected is False

def test_publish():

    client = MqttClient("localhost")

    client.connect()

    client.publish(
        "factory/machine/state",
        "RUN",
    )

    assert client.last_topic == "factory/machine/state"
    assert client.last_payload == "RUN"