from hsms_gateway.secs.items import (
    A,
    B,
    U1,
    U2,
    U4,
    L,
)

from hsms_gateway.secs.formats import (
    SecsFormat,
)


def test_ascii():

    item = A("HOST")

    assert item.value == "HOST"

    assert item.format == SecsFormat.ASCII


def test_binary():

    item = B(b"\x01\x02")

    assert item.value == b"\x01\x02"

    assert item.format == SecsFormat.BINARY


def test_u1():

    item = U1(5)

    assert item.value == 5


def test_list():

    item = L([
        A("HOST"),
        U1(10),
    ])

    assert len(item) == 2

    assert item.value[0].value == "HOST"

    assert item.value[1].value == 10