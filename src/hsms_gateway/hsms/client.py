from .frame import HsmsFrame
from .socket import HsmsSocket
from .state import HsmsState


class HsmsClient:

    def __init__(
        self,
        host: str,
        port: int,
        timeout: float = 5.0,
    ):
        self.socket = HsmsSocket(
            host=host,
            port=port,
            timeout=timeout,
        )
        self.state = HsmsState.NOT_CONNECTED

    def connect(self) -> None:
        self.socket.connect()
        self.state = HsmsState.TCP_CONNECTED

    def disconnect(self) -> None:
        self.socket.disconnect()

    def send_frame(
        self,
        frame: HsmsFrame,
    ) -> None:
        self.socket.send_frame(frame)

    def receive_frame(self) -> HsmsFrame:
        return self.socket.receive_frame()