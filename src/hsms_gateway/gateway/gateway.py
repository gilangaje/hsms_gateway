import time

class HsmsGateway:

    def __init__(self, gem, mqtt):

        self.gem = gem
        self.mqtt = mqtt

    def publish_status_variables(
        self,
        svids,
    ):

        values = self.gem.read_status_variables(
            svids
        )

        payload = {
            str(svid): value
            for svid, value in zip(
                svids,
                values,
            )
        }

        self.mqtt.publish(
            "factory/status",
            payload,
        )
    def run_once(self, svids):

        self.publish_status_variables(
            svids
        )

    def run(
        self,
        interval,
        svids,
        iterations,
    ):

        for _ in range(iterations):

            self.run_once(svids)

            time.sleep(interval)