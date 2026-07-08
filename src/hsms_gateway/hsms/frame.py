import struct
from dataclasses import dataclass

from .header import HsmsHeader


@dataclass(slots=True)
class HsmsFrame:
    """
    Represents one complete HSMS frame.
    """

    header: HsmsHeader

    body: bytes = b""

    def encode(self) -> bytes:
        """
        Encode complete HSMS frame.
        """

        header = self.header.encode()

        length = len(header) + len(self.body)

        return (
            struct.pack(">I", length)
            + header
            + self.body
        )