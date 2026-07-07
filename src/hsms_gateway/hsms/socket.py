import socket

from .exceptions import ConnectionTimeoutError
from .logger import logger
from .exceptions import (
    ConnectionClosedError,
    ReceiveTimeoutError,
)


class HsmsSocket:

    def __init__(
        self,
        host: str,
        port: int,
        timeout: float = 5.0,
    ):
        self.host = host
        self.port = port
        self.timeout = timeout

        self._socket = None

    @property
    def connected(self) -> bool:
        return self._socket is not None

    def connect(self):

        if self.connected:
            return

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            )

            sock.settimeout(self.timeout)

            sock.connect(
                (self.host, self.port)
            )

            self._socket = sock

            logger.info(
                f"Connected to {self.host}:{self.port}"
            )

        except socket.timeout as exc:

            raise ConnectionTimeoutError(
                "Connection timeout"
            ) from exc
        
    def disconnect(self) -> None:
        """
        Close TCP connection.
        """
        
        if not self.connected:
            return

        self._socket.close()
        self._socket = None

        logger.info(
            f"Disconnected from {self.host}:{self.port}"
        )

    def recv_exact(self, size: int) -> bytes:
        """
        Receive exactly 'size' bytes.
        """

        if not self.connected:
            raise ConnectionClosedError(
                "Socket is not connected."
            )

        data = bytearray()

        while len(data) < size:

            try:

                chunk = self._socket.recv(
                    size - len(data)
                )

            except socket.timeout as exc:

                raise ReceiveTimeoutError(
                    "Receive timeout."
                ) from exc

            if not chunk:

                raise ConnectionClosedError(
                    "Remote closed the connection."
                )

            data.extend(chunk)

        return bytes(data)