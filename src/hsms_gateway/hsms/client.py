from .frame import HsmsFrame
from .socket import HsmsSocket
from .state import HsmsState
from .messages import select_req
from .constants import SType


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
        self.state = HsmsState.NOT_CONNECTED

    def send_frame(
        self,
        frame: HsmsFrame,
    ) -> None:
        self.socket.send_frame(frame)

    def receive_frame(self) -> HsmsFrame:
        return self.socket.receive_frame()
    
    def select(self) -> None:
        """
        Perform HSMS Select handshake.
        """

        if self.state != HsmsState.TCP_CONNECTED:
            raise RuntimeError(
                "TCP connection is not established."
            )

        # Kirim Select.req
        self.send_frame(
            select_req()
        )

        # Tunggu Select.rsp
        response = self.receive_frame()

        if response.header.s_type != SType.SELECT_RSP:
            raise RuntimeError(
                "Expected Select.rsp."
            )

        # Body Select.rsp harus 0x00 (Success)
        if response.body != b"\x00":
            raise RuntimeError(
                "Select rejected."
            )

        self.state = HsmsState.SELECTED