from hsms_gateway.secs.decoder import decode_item
from hsms_gateway.secs.items import (
    A,
    B,
    U1,
    U2,
    U4,
)


def test_decode_ascii():

    item = decode_item(
        bytes.fromhex(
            "40 03 41 42 43"
        )
    )

    assert isinstance(item, A)
    assert item.value == "ABC"


def test_decode_binary():

    item = decode_item(
        bytes.fromhex(
            "20 02 AA BB"
        )
    )

    assert isinstance(item, B)
    assert item.value == b"\xAA\xBB"


def test_decode_u1():

    item = decode_item(
        bytes.fromhex(
            "A4 01 05"
        )
    )

    assert isinstance(item, U1)
    assert item.value == 5


def test_decode_u2():

    item = decode_item(
        bytes.fromhex(
            "A8 02 01 2C"
        )
    )

    assert isinstance(item, U2)
    assert item.value == 300


def test_decode_u4():

    item = decode_item(
        bytes.fromhex(
            "B0 04 00 00 03 E8"
        )
    )

    assert isinstance(item, U4)
    assert item.value == 1000