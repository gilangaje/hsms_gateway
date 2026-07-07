from hsms_gateway.hsms.socket import HsmsSocket
from tests.helpers.dummy_server import DummyTcpServer


def test_create_socket():

    sock = HsmsSocket(
        "127.0.0.1",
        5000,
    )

    assert sock.host == "127.0.0.1"

    assert sock.port == 5000

    assert sock.timeout == 5.0


def test_connect():

    server = DummyTcpServer()

    server.start()

    sock = HsmsSocket(
        "127.0.0.1",
        5001,
    )

    sock.connect()

    assert sock.connected

    server.stop()

def test_disconnect():

    server = DummyTcpServer()

    server.start()

    sock = HsmsSocket(
        "127.0.0.1",
        5001,
    )

    sock.connect()

    assert sock.connected

    sock.disconnect()

    assert not sock.connected

    server.stop()