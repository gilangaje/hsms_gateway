from hsms_gateway.secs.encoder import (
    encode_item,
)

from hsms_gateway.secs.items import (
    A,
)

from hsms_gateway.secs.items import (
    B,
    U1,
    U2,
    U4,
)


def test_encode_ascii():

    encoded = encode_item(
        A("ABC")
    )

    assert encoded == bytes.fromhex(
        "40 03 41 42 43"
    )

def test_encode_binary():

    encoded = encode_item(
        B(b"\xAA\xBB")
    )

    assert encoded == bytes.fromhex(
        "20 02 AA BB"
    )

def test_encode_u1():

    encoded = encode_item(
        U1(5)
    )

    assert encoded == bytes.fromhex(
        "A4 01 05"
    )

def test_encode_u2():

    encoded = encode_item(
        U2(300)
    )

    assert encoded == bytes.fromhex(
        "A8 02 01 2C"
    )

def test_encode_u4():

    encoded = encode_item(
        U4(1000)
    )

    assert encoded == bytes.fromhex(
        "B0 04 00 00 03 E8"
    )