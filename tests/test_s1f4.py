from hsms_gateway.secs.messages.s1f4 import s1f4

from hsms_gateway.secs.items import (
    L,
    U4,
    A,
)


def test_s1f4():

    msg = s1f4([
        U4(123),
        A("AUTO"),
    ])

    assert msg.stream == 1
    assert msg.function == 4
    assert msg.wbit is False

    assert isinstance(msg.body, L)

    assert msg.body[0] == U4(123)
    assert msg.body[1] == A("AUTO")