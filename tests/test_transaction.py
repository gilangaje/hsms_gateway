from tests.helpers.dummy_server import DummyTcpServer

from hsms_gateway.hsms.client import HsmsClient

from hsms_gateway.secs.message import SecsMessage

from hsms_gateway.secs.message_codec import (
    encode_message,
)


def test_transaction():

    server = DummyTcpServer()

    reply = SecsMessage(
        stream=1,
        function=2,
        wbit=False,
    )

    server.queue_response(
        encode_message(reply).encode()
    )

    server.start()

    client = HsmsClient(
        "127.0.0.1",
        5001,
    )

    try:

        client.connect()

        response = client.transaction(

            SecsMessage(
                stream=1,
                function=1,
                wbit=True,
            )

        )

        assert response.stream == 1
        assert response.function == 2

    finally:

        client.disconnect()
        server.stop()