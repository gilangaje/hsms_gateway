from hsms_gateway.gateway import HsmsGateway


class DummyGem:

    def read_status_variables(self, svids):
        return ["RUN"]


class DummyMqtt:

    def __init__(self):
        self.topic = None
        self.payload = None

    def publish(self, topic, payload):
        self.topic = topic
        self.payload = payload


def test_run_once():

    gateway = HsmsGateway(
        DummyGem(),
        DummyMqtt(),
    )

    gateway.run_once([1001])

    assert gateway.mqtt.topic == "factory/status"

def run_once(self, svids):

    self.publish_status_variables(
        svids
    )