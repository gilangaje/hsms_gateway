from tests.helpers.dummy_server import DummyTcpServer

from hsms_gateway.hsms.client import HsmsClient
from hsms_gateway.secs.message import SecsMessage


def test_send_message():

    server = DummyTcpServer()
    server.start()

    client = HsmsClient(
        "127.0.0.1",
        5001,
    )

    try:
        client.connect()

        client.send_message(

            SecsMessage(
                stream=1,
                function=1,
                wbit=True,
            )

        )

        assert server.last_data is not None

    finally:
        client.disconnect()
        server.stop()