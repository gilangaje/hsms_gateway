import socket
import threading


class DummyTcpServer:

    def __init__(
        self,
        host="127.0.0.1",
        port=5001,
    ):
        self.host = host
        self.port = port

        self.server = None
        self.client = None

        self.last_data = b""

    def start(self):

        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
        )

        self.server.bind(
            (self.host, self.port)
        )

        self.server.listen(1)

        threading.Thread(
            target=self._accept,
            daemon=True,
        ).start()

    def _accept(self):

        self.client, _ = self.server.accept()

        try:
            self.last_data = self.client.recv(4096)

        except (
            ConnectionResetError,
            ConnectionAbortedError,
            OSError,
        ):
            pass

    def stop(self):

        if self.client:
            self.client.close()

        if self.server:
            self.server.close()
            
    def send(self, data: bytes):

        if self.client is None:
            raise RuntimeError(
                "No client connected."
            )

        self.client.sendall(data)

    def send_frame(self, frame):

        self.send(
            frame.encode()
        )