from hsms_gateway.hsms.messages import (
    select_rsp,
)

from hsms_gateway.hsms.client import (
    HsmsClient,
)

from hsms_gateway.hsms.state import (
    HsmsState,
)

from tests.helpers.dummy_server import (
    DummyTcpServer,
)


def test_select_handshake():

    server = DummyTcpServer()
    server.queue_response(select_rsp())
    server.start()

    client = HsmsClient("127.0.0.1", 5001)

    try:
        client.connect()

        client.select()

        assert client.state == HsmsState.SELECTED

    finally:
        client.disconnect()
        server.stop()