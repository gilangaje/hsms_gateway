from dataclasses import dataclass
import struct

@dataclass(slots=True)
class HsmsHeader:
    """
    Represents the 10-byte HSMS message header.
    """

    session_id: int

    stream: int

    function: int

    p_type: int

    s_type: int

    system_bytes: int

    w_bit: bool = False

    def encode(self) -> bytes:
        """
        Encode HSMS header into 10 bytes.
        """

        header_byte2 = self.stream & 0x7F

        if self.w_bit:
            header_byte2 |= 0x80

        return struct.pack(
            ">HBBBBI",
            self.session_id,
            header_byte2,
            self.function,
            self.p_type,
            self.s_type,
            self.system_bytes,
        )