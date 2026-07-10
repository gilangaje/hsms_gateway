from hsms_gateway.secs.messages.s1f2 import s1f2

from hsms_gateway.secs.items import (
    L,
    A,
)


def test_s1f2():

    msg = s1f2(
        "TEST-EQP",
        "1.0",
    )

    assert msg.stream == 1
    assert msg.function == 2
    assert msg.wbit is False

    assert isinstance(msg.body, L)

    assert msg.body[0].value == "TEST-EQP"
    assert msg.body[1].value == "1.0"