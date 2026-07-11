from hsms_gateway.mqtt.client import MqttClient

client = MqttClient(
    "localhost",
    1883,
)

client.connect()

client.publish(
    "factory/status",
    "Hello HSMS Gateway"
)

client.disconnect()