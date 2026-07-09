from .formats import SecsFormat
from .items import (
    A,
    B,
    U1,
    U2,
    U4,
)


def decode_item(data: bytes):

    fmt, start, end = decode_header(data)

    payload = data[start:end]

    if fmt == SecsFormat.ASCII:
        return A(
            payload.decode("ascii")
        )

    if fmt == SecsFormat.BINARY:
        return B(payload)

    if fmt == SecsFormat.U1:
        return U1(
            int.from_bytes(
                payload,
                "big",
            )
        )

    if fmt == SecsFormat.U2:
        return U2(
            int.from_bytes(
                payload,
                "big",
            )
        )

    if fmt == SecsFormat.U4:
        return U4(
            int.from_bytes(
                payload,
                "big",
            )
        )

    raise NotImplementedError(
        fmt.name
    )

def decode_header(data: bytes):

    first = data[0]

    format_code = first >> 2

    length_bytes = (first & 0x03) + 1

    length = int.from_bytes(
        data[1:1 + length_bytes],
        "big",
    )

    payload_start = 1 + length_bytes

    payload_end = payload_start + length

    return (
        SecsFormat(format_code),
        payload_start,
        payload_end,
    )