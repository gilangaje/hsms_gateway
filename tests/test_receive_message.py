import threading
import time

from tests.helpers.dummy_server import DummyTcpServer

from hsms_gateway.hsms.client import HsmsClient
from hsms_gateway.secs.message import SecsMessage
from hsms_gateway.secs.message_codec import encode_message


def test_receive_message():

    server = DummyTcpServer()
    server.start()

    msg = SecsMessage(
        stream=1,
        function=2,
        wbit=False,
    )

    frame = encode_message(msg)

    client = HsmsClient(
        "127.0.0.1",
        5001,
    )

    try:

        client.connect()

        def send():
            time.sleep(0.05)
            server.send_frame(frame)

        threading.Thread(
            target=send,
            daemon=True,
        ).start()

        received = client.receive_message()

        assert received.stream == 1
        assert received.function == 2
        assert received.wbit is False

    finally:

        client.disconnect()
        server.stop()