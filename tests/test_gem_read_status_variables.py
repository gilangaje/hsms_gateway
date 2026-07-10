from tests.helpers.dummy_server import DummyTcpServer

from hsms_gateway.gem.client import GemClient

from hsms_gateway.secs.items import (
    U4,
    A,
)

from hsms_gateway.secs.messages.s1f4 import s1f4
from hsms_gateway.secs.message_codec import encode_message


def test_read_status_variables():

    server = DummyTcpServer()

    server.queue_response(
        encode_message(
            s1f4([
                A("RUN"),
                U4(25),
            ])
        ).encode()
    )

    server.start()

    client = GemClient(
        "127.0.0.1",
        5001,
    )

    try:

        client.connect()

        values = client.read_status_variables(
            [1001, 1002]
        )

        assert values[0] == A("RUN")
        assert values[1] == U4(25)

    finally:

        client.disconnect()
        server.stop()