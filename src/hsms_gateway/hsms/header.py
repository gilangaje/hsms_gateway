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
    @classmethod
    def decode(cls, data: bytes) -> "HsmsHeader":
        """
        Decode a 10-byte HSMS header.
        """

        if len(data) != 10:
            raise ValueError(
                "HSMS header must be exactly 10 bytes."
            )

        (
            session_id,
            header_byte2,
            function,
            p_type,
            s_type,
            system_bytes,
        ) = struct.unpack(">HBBBBI", data)

        w_bit = bool(header_byte2 & 0x80)

        stream = header_byte2 & 0x7F

        return cls(
            session_id=session_id,
            stream=stream,
            function=function,
            p_type=p_type,
            s_type=s_type,
            system_bytes=system_bytes,
            w_bit=w_bit,
        )