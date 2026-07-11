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

        self._client.on_connect = self._on_connect
        self._client.on_disconnect = self._on_disconnect

    def _on_connect(
        self,
        client,
        userdata,
        flags,
        rc,
    ):
        self._connected = True
        print("MQTT connected")


    def _on_disconnect(
        self,
        client,
        userdata,
        rc,
    ):
        self._connected = False
        print("MQTT disconnected")
        
    @property
    def connected(self):
        return self._connected

    def connect(self):
        result = self._client.connect(
            self.host,
            self.port,
        )

        if result != mqtt.MQTT_ERR_SUCCESS:
            raise RuntimeError(
                "Failed to connect to MQTT broker"
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
        
        self.last_topic = topic
        self.last_payload = payload

        self._client.publish(
            topic,
            payload,
        )