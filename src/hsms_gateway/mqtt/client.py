import paho.mqtt.client as mqtt


class MqttClient:

    def __init__(
        self,
        host,
        port=1883,
    ):
        self.host = host
        self.port = port
        self._connected = False
        self._client = mqtt.Client()

    @property
    def connected(self):
        return self._connected

    def connect(self):

        self._client.connect(
            self.host,
            self.port,
        )

        self._client.loop_start()

        self._connected = True

    def disconnect(self):

        self._client.loop_stop()

        self._client.disconnect()

        self._connected = False

    def publish(
        self,
        topic,
        payload,
    ):

        if not self.connected:
            raise RuntimeError(
                "MQTT client is not connected"
            )

        self._client.publish(
            topic,
            payload,
        )