from dataclasses import dataclass
import struct

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
    
    @classmethod
    def decode(cls, data: bytes) -> "HsmsFrame":
        """
        Decode complete HSMS frame.
        """

        if len(data) < 14:
            raise ValueError(
                "HSMS frame is too short."
            )

        length = struct.unpack(">I", data[:4])[0]

        if length != len(data) - 4:
            raise ValueError(
                "Invalid HSMS frame length."
            )

        header = HsmsHeader.decode(
            data[4:14]
        )

        body = data[14:]

        return cls(
            header=header,
            body=body,
        )