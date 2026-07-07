import socket

from tests.helpers.dummy_server import DummyTcpServer


def test_dummy_server():

    server = DummyTcpServer()

    server.start()

    client = socket.socket()

    client.connect(("127.0.0.1", 5001))

    client.close()

    server.stop()