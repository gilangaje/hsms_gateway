from tests.helpers.dummy_server import DummyTcpServer
from hsms_gateway.gem.client import GemClient
from hsms_gateway.secs.messages.s1f2 import s1f2
from hsms_gateway.secs.message_codec import encode_message


def test_are_you_there():

    server = DummyTcpServer()

    server.queue_response(
        encode_message(
            s1f2(
                "TEST-EQP",
                "1.0"
            )
        ).encode()
    )

    server.start()

    client = GemClient(
        "127.0.0.1",
        5001,
    )

    try:

        client.connect()

        model, revision = client.are_you_there()

        assert model == "TEST-EQP"
        assert revision == "1.0"

    finally:

        client.disconnect()
        server.stop()