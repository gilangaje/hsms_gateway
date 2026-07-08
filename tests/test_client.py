from hsms_gateway.hsms.client import HsmsClient
from hsms_gateway.hsms.state import HsmsState
from tests.helpers.dummy_server import DummyTcpServer

def test_client_create():

    client = HsmsClient(
        "127.0.0.1",
        5000,
    )

    assert client.socket.host == "127.0.0.1"
    assert client.socket.port == 5000

def test_client_state_connect():

    server = DummyTcpServer()

    server.start()

    client = HsmsClient(
        "127.0.0.1",
        5001,
    )

    assert client.state == HsmsState.NOT_CONNECTED

    client.connect()

    assert client.state == HsmsState.TCP_CONNECTED

    client.disconnect()

    server.stop()