from .items import (
    A,
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

    raise NotImplementedError(
        type(item).__name__
    )