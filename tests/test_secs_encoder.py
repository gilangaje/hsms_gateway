from hsms_gateway.secs.encoder import (
    encode_item,
)

from hsms_gateway.secs.items import (
    A,
)


def test_encode_ascii():

    encoded = encode_item(
        A("ABC")
    )

    assert encoded == bytes.fromhex(
        "40 03 41 42 43"
    )