class MqttClient:

    def __init__(
        self,
        host,
        port=1883,
    ):
        self.host = host
        self.port = port
        self._connected = False

    @property
    def connected(self):
        return self._connected

    def connect(self):
        self._connected = True

    def disconnect(self):
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

        self.last_topic = topic
        self.last_payload = payload