import time

from hsms_gateway.hsms.frame import HsmsFrame
from hsms_gateway.hsms.header import HsmsHeader
from hsms_gateway.hsms.socket import HsmsSocket

from tests.helpers.dummy_server import DummyTcpServer


def test_receive_frame():

    server = DummyTcpServer()

    server.start()

    time.sleep(0.1)

    client = HsmsSocket(
        "127.0.0.1",
        5001,
    )

    client.connect()

    frame = HsmsFrame(
        header=HsmsHeader(
            session_id=10,
            stream=1,
            function=14,
            p_type=0,
            s_type=0,
            system_bytes=99,
            w_bit=False,
        ),
        body=b"",
    )

    time.sleep(0.1)

    server.send_frame(frame)

    received = client.receive_frame()

    assert received == frame

    client.disconnect()

    server.stop()