from hsms_gateway.secs.messages.s1f1 import (
    s1f1,
)


def test_s1f1():

    msg = s1f1()

    assert msg.stream == 1
    assert msg.function == 1
    assert msg.wbit is True