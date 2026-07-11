from hsms_gateway.mqtt.client import MqttClient


def test_create_paho_client():

    client = MqttClient("localhost")

    assert client._client is not None