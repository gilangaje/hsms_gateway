from hsms_gateway.secs.encoder import encode_item
from hsms_gateway.secs.decoder import decode_item
from hsms_gateway.secs.items import (
    A,
    B,
    U1,
    U2,
    U4,
)


def check_roundtrip(item):

    encoded = encode_item(item)

    decoded = decode_item(encoded)

    assert type(decoded) is type(item)

    assert decoded.value == item.value


def test_roundtrip_ascii():
    check_roundtrip(A("HOST"))


def test_roundtrip_binary():
    check_roundtrip(B(b"\xAA\xBB"))


def test_roundtrip_u1():
    check_roundtrip(U1(5))


def test_roundtrip_u2():
    check_roundtrip(U2(300))


def test_roundtrip_u4():
    check_roundtrip(U4(1000))