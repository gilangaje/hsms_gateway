from .items import (
    A,
    B,
    U1,
    U2,
    U4,
)

from .formats import (
    SecsFormat,
)

def encode_header(
    fmt: SecsFormat,
    length: int,
) -> bytes:

    if length <= 0xFF:

        n_length_bytes = 1

    elif length <= 0xFFFF:

        n_length_bytes = 2

    else:

        n_length_bytes = 3

    first = (
        (fmt << 2)
        | (n_length_bytes - 1)
    )

    return bytes([first]) + length.to_bytes(
        n_length_bytes,
        "big",
    )

def encode_item(item):

    if isinstance(item, A):

        data = item.value.encode("ascii")

        return (
            encode_header(
                SecsFormat.ASCII,
                len(data),
            )
            + data
        )
    if isinstance(item, B):

        data = item.value

        return (
            encode_header(
                SecsFormat.BINARY,
                len(data),
            )
            + data
        )
    if isinstance(item, U1):

        data = item.value.to_bytes(
            1,
            "big",
        )

        return (
            encode_header(
                SecsFormat.U1,
                len(data),
            )
            + data
        )
    if isinstance(item, U2):

        data = item.value.to_bytes(
            2,
            "big",
        )

        return (
            encode_header(
                SecsFormat.U2,
                len(data),
            )
            + data
        )
    if isinstance(item, U4):

        data = item.value.to_bytes(
            4,
            "big",
        )

        return (
            encode_header(
                SecsFormat.U4,
                len(data),
            )
            + data
        )

    raise NotImplementedError(
        type(item).__name__
    )

    