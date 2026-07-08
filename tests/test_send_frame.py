import time

from hsms_gateway.hsms.frame import HsmsFrame
from hsms_gateway.hsms.header import HsmsHeader
from hsms_gateway.hsms.socket import HsmsSocket

from tests.helpers.dummy_server import DummyTcpServer


def test_send_frame():

    server = DummyTcpServer()

    server.start()

    time.sleep(0.1)

    sock = HsmsSocket(
        "127.0.0.1",
        5001,
    )

    sock.connect()

    frame = HsmsFrame(
        header=HsmsHeader(
            session_id=10,
            stream=1,
            function=13,
            p_type=0,
            s_type=0,
            system_bytes=1,
            w_bit=True,
        ),
        body=b"",
    )

    sock.send_frame(frame)

    time.sleep(0.1)

    assert server.last_data == frame.encode()

    sock.disconnect()

    server.stop()