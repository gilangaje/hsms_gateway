from hsms_gateway.secs.encoder import encode_item
from hsms_gateway.secs.items import L, A
from hsms_gateway.secs.items import (
    L,
    A,
)

def test_encode_empty_list():

    encoded = encode_item(
        L([])
    )

    assert encoded == bytes.fromhex(
        "00 00"
    )

def test_encode_list_one_item():

    encoded = encode_item(

        L([

            A("ABC")

        ])

    )

    assert encoded == bytes.fromhex(

        "00 01"

        "40 03 41 42 43"

    )