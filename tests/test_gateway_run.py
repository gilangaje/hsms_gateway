import time
from hsms_gateway.gateway import HsmsGateway


class DummyGem:

    def __init__(self):
        self.calls = 0

    def read_status_variables(self, svids):
        self.calls += 1
        return ["RUN"]


class DummyMqtt:

    def publish(self, topic, payload):
        pass


def test_run():

    gem = DummyGem()

    gateway = HsmsGateway(
        gem,
        DummyMqtt(),
    )

    gateway.run(
        interval=0,
        svids=[1001],
        iterations=3,
    )

    assert gem.calls == 3

def run(
    self,
    interval,
    svids,
    iterations,
):

    for _ in range(iterations):

        self.run_once(svids)

        time.sleep(interval)