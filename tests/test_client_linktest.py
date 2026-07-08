from hsms_gateway.hsms.client import HsmsClient
from hsms_gateway.hsms.messages import (
    select_rsp,
    linktest_rsp,
)
from hsms_gateway.hsms.state import HsmsState

from tests.helpers.dummy_server import DummyTcpServer


def test_client_linktest():

    server = DummyTcpServer()

    # Balasan pertama untuk Select
    server.queue_response(select_rsp())

    # Balasan kedua untuk Linktest
    server.queue_response(linktest_rsp())

    server.start()

    client = HsmsClient(
        "127.0.0.1",
        5001,
    )

    try:
        client.connect()

        client.select()

        assert client.state == HsmsState.SELECTED

        client.linktest()

    finally:
        client.disconnect()
        server.stop()