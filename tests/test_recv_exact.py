import threading

from hsms_gateway.hsms.socket import HsmsSocket

from tests.helpers.dummy_server import DummyTcpServer


def test_recv_exact():

    server = DummyTcpServer()

    server.start()

    sock = HsmsSocket(
        "127.0.0.1",
        5001,
    )

    sock.connect()

    threading.Event().wait(0.1)

    server.send(b"Hello")

    data = sock.recv_exact(5)

    assert data == b"Hello"

    sock.disconnect()

    server.stop()